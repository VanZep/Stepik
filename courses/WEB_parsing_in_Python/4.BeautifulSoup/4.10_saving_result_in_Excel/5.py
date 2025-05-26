"""
Парсер нацелен показать то, как бы я его писал для себя, а не как короткий скрипт.

Для работы нужны следующие библиотеки:

1. requests
2. bs4
3. fake_useragent

Обзор работы парсера:

1. URL Generation: Генератор создает URL для парсинга по шаблонам из PARSING_ORDER
2. Session Management: Контекстный менеджер управляет жизненным циклом сессии
3. Page Fetching: PageFetcher обрабатывает запросы с индивидуальными заголовками
4. Error Handling: Критические ошибки приводят к выходу с кодом 1 и сообщением в stderr
5. Страницы обрабатываются последовательно через process_page

Компоненты взаимодействуют по схеме:
main() → generate_urls() → PageFetcher → process_page() → parse_product_card()
           ↑
managed_session()
"""
import csv
import logging
import re
import sys
import time
from collections.abc import Iterator
from contextlib import contextmanager
from typing import ContextManager, Protocol

import requests
from bs4 import BeautifulSoup, Tag
from fake_useragent import UserAgent

# type NamedField = str
# type StringValue = str

# Настройка логирования для отслеживания работы парсера
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('../Theory/parser.log'),  # Логи в файл
        logging.StreamHandler()  # Логи в консоль
    ]
)

DEFAULT_CONFIG = {

    "base_urls": {  # Шаблоны URL для различных категорий товаров
        "watch": "https://parsinger.ru/html/watch/1/1_{}.html",
        "mobile": "https://parsinger.ru/html/mobile/2/2_{}.html",
        "mouse": "https://parsinger.ru/html/mouse/3/3_{}.html",
        "hdd": "https://parsinger.ru/html/hdd/4/4_{}.html",
        "headphones": "https://parsinger.ru/html/headphones/5/5_{}.html",
    },
    "product_per_category": 32,  # Количество товаров для каждой категории
    "request_delay": 0.1,  # Задержка между запросами (в секундах)
    "max_retries": 3,  # Максимальное количество попыток запроса
    "output_columns": [
        'Наименование',
        'Артикул',
        'Бренд',
        'Модель',
        'Наличие',
        'Цена',
        'Старая цена',
        'Ссылка'
    ]
}


class CSVWriter(Protocol):
    """Протокол для объектов записи CSV."""

    def writerow(self, row: list[str]) -> None: ...


class Selectors:
    """CSS селекторы для извлечения данных со страниц."""
    CARD = '.item_card > .description'  # Информация с карточки
    NAME = '#p_header'  # Название продукта в карточке
    ARTICLE = '#p_header + p.article'  # Артикул с карточки
    BRAND = '#brand'  # Бренд товара
    MODEL = '#model'  # Модель товара
    IN_STOCK = '#in_stock'  # Наличие
    PRICE = '#price'  # Цена в карточке
    OLD_PRICE = '#old_price'  # Старая цена


@contextmanager
def managed_csv_writer(file_path: str) -> ContextManager[csv.writer]:
    """Контекстный менеджер для управления записью в CSV файл.

    Args:
        file_path: Путь к файлу для сохранения данных

    Yields:
        Объект csv.writer для записи данных
    """
    with open(file_path, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(DEFAULT_CONFIG["output_columns"])
        yield writer


@contextmanager
def managed_session() -> ContextManager[requests.Session]:
    """Контекстный менеджер для управления HTTP-сессией.

    Обеспечивает корректное создание и закрытие сессии.

    Yields:
        Активная HTTP-сессия для выполнения запросов
    """
    session = requests.Session()
    try:
        yield session
    finally:
        session.close()


class PageFetcher:
    """Класс для загрузки и обработки веб-страниц.

    Обеспечивает:
    - Загрузку страниц с настраиваемой задержкой
    - Обработку ошибок с повторными попытками
    - Логирование процесса загрузки

    Attributes:
        session: Объект HTTP-сессии для выполнения запросов
        config: Конфигурация парсера (задержки, кол-во попыток)
        logger: Логер для записи событий
    """

    def __init__(self, session: requests.Session, config: dict):
        self.session = session
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)

    def _handle_request_error(self, error: Exception, url: str,
                              attempt: int) -> None:
        """Обрабатывает ошибки при выполнении запросов.

        Args:
            error: Исключение, вызвавшее ошибку
            url: URL, на котором произошла ошибка
            attempt: Номер текущей попытки
        """
        self.logger.warning(
            f"Attempt {attempt}/{self.config['max_retries']} failed for {url}: {error}"
        )
        time.sleep(2 ** attempt)  # Экспоненциальная задержка

    def get_page(self, url: str) -> BeautifulSoup:
        """Загружает и парсит веб-страницу.

        Args:
            url: URL страницы для загрузки

        Returns:
            Объект BeautifulSoup с распарсенной страницей

        Raises:
            SystemExit: Если страницу не удалось загрузить после всех попыток
        """
        for attempt in range(1, self.config["max_retries"] + 1):
            try:
                time.sleep(self.config["request_delay"])
                response = self.session.get(url, headers={
                    'UserAgent': UserAgent().random}, timeout=10)
                response.encoding = "utf-8"
                response.raise_for_status()
                self.logger.info(f'Successfully fetched {url}')
                return BeautifulSoup(response.text, "lxml")
            except requests.RequestException as e:
                self._handle_request_error(e, url, attempt)
        self.logger.error(
            f"Failed to fetch {url} after {self.config['max_retries']} attempts")
        sys.exit(1)


def parse_product_card(card: Tag) -> dict[str, str]:
    """Парсит данные товара из HTML-карточки.

    Извлекает и обрабатывает следующие данные:
    - Название товара
    - Текущую и старую цену
    - Артикул, бренд, модель
    - Количество на складе

    Args:
        card: BeautifulSoup Tag объект карточки товара

    Returns:
        Словарь с распарсенными данными товара в формате:
        {
            'name': str,        # Название товара
            'price': str,       # Текущая цена
            'old_price': str,   # Старая цена
            'article': str,     # Артикул товара
            'brand': str,       # Производитель
            'model': str,       # Модель
            'in_stock': str     # Количество на складе
        }

    Raises:
        AttributeError: Если не удалось извлечь числовые значения из строк
    """

    def safe_get_text(element: Tag, selector: str, default: str = '',
                      strip: bool = True) -> str:
        """Безопасно извлекает текст из элемента по CSS-селектору.

        Args:
            element: Родительский HTML-элемент
            selector: CSS-селектор для поиска
            default: Значение по умолчанию при отсутствии элемента
            strip: Удалять ли пробелы по краям текста

        Returns:
            Текст элемента или значение по умолчанию
        """
        if (elem := element.select_one(selector)) is not None:
            return elem.get_text(strip=strip).strip()
        return default

    def extract_number(text: str) -> str:
        """Извлекает числовое значение из строки.

        Args:
            text: Строка, содержащая число

        Returns:
            Строка с найденным числом или '0' если не найдено

        Raises:
            AttributeError: Если число не найдено и нет значения по умолчанию
        """
        if (match := re.search(r'\d+', text)) is not None:
            return match.group(0)
        return '0'

    def extract_after_colon(text: str) -> str:
        """Извлекает часть строки после двоеточия.

        Args:
            text: Строка в формате "ключ: значение"

        Returns:
            Часть строки после двоеточия или исходную строку
        """
        return text.split(': ')[1] if ': ' in text else text

    # Извлечение сырых данных из карточки
    raw_data = {
        'article': safe_get_text(card, Selectors.ARTICLE),
        'brand': safe_get_text(card, Selectors.BRAND),
        'model': safe_get_text(card, Selectors.MODEL),
        'in_stock': safe_get_text(card, Selectors.IN_STOCK),
        'name': safe_get_text(card, Selectors.NAME),
        'price': safe_get_text(card, Selectors.PRICE),
        'old_price': safe_get_text(card, Selectors.OLD_PRICE)
    }

    # Обработка и валидация данных
    return {
        'name': raw_data['name'] or 'N/A',
        'price': raw_data['price'] or 'N/A',
        'old_price': raw_data['old_price'] or 'N/A',
        'article': extract_number(raw_data['article']),
        'brand': extract_after_colon(raw_data['brand']),
        'model': extract_after_colon(raw_data['model']),
        'in_stock': extract_number(raw_data['in_stock'])
    }


def process_page(fetcher: PageFetcher, url: str, writer: CSVWriter) -> None:
    """Обрабатывает страницу товара и сохраняет данные в CSV.

    Args:
        fetcher: Объект для загрузки страниц
        url: URL обрабатываемой страницы
        writer: Объект для записи данных в CSV

    Процесс работы:
    1. Загружает страницу через PageFetcher
    2. Находит карточку товара
    3. Парсит данные из карточки
    4. Записывает данные в CSV в строгом порядке:
       - Название, артикул, бренд, модель
       - Наличие, цена, старая цена
       - URL страницы

    Raises:
        Exception: Логирует любые ошибки парсинга без прерывания работы
    """
    try:
        soup = fetcher.get_page(url)
        if (card := soup.select_one(Selectors.CARD)) is None:
            logging.warning(f"No product card found on page: {url}")
            return

        product_data = parse_product_card(card)
        writer.writerow([
            product_data['name'],
            product_data['article'],
            product_data['brand'],
            product_data['model'],
            product_data['in_stock'],
            product_data['price'],
            product_data['old_price'],
            url  # Сохраняем URL для отслеживания источника данных
        ])
    except Exception as e:
        logging.error(f"Error processing page {url}: {str(e)}", exc_info=True)


def generate_urls(config: dict) -> Iterator[str]:
    """Генерирует URL страниц для парсинга на основе конфигурации.

    Args:
        config: Словарь с настройками парсера

    Yields:
        URL очередной страницы для обработки
    """
    for url_template in config["base_urls"].values():
        for page in range(1, config["product_per_category"] + 1):
            yield url_template.format(page)


def main(cvs_file_name: str) -> None:
    """Основная функция для запуска процесса парсинга.

    Args:
        cvs_file_name: Имя файла для сохранения результатов
    """
    with managed_session() as session, managed_csv_writer(
            cvs_file_name) as writer:
        fetcher = PageFetcher(session, DEFAULT_CONFIG)
        for url in generate_urls(DEFAULT_CONFIG):
            process_page(fetcher, url, writer)


if __name__ == '__main__':
    main('products_all.csv')
