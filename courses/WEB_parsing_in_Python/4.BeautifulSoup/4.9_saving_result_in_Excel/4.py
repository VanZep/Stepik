"""
Напишите код, который соберёт данные в каждой категории c каждой карточки,
всего 160шт.

Перед отправкой кода на рецензирование убедитесь что код соблюдает условия.

Функциональность:
Все ли необходимые данные успешно извлекаются с сайта и записываются в
CSV-файл?
Проверьте, все ли обязательные заголовки присутствуют?
Перечисленные заголовки являются общими для всех карточек.

# Обязательные заголовки:
Наименование;Артикул;Бренд;Модель;Наличие;Цена;Старая цена;Ссылка;

Читаемость:
Являются ли имена переменных и функций понятными?
Есть ли комментарии, объясняющие ключевые части кода?
Соблюдается ли отступ и форматирование кода?

Оптимальность:
Могут ли какие-либо участки кода быть оптимизированы или упрощены?
Есть ли избыточные повторения, например, открытие и закрытие файла для каждой
записи?

Обработка ошибок:
Как код реагирует на возможные ошибки? Например, если сайт недоступен или
структура веб-страницы изменяется?
Предусмотрены ли исключения для обработки ошибок?

Стандарты кодирования:
Соблюдаются ли общепринятые стандарты кодирования для Python?
Есть ли лишние пробелы или неиспользуемые переменные?
"""

import csv

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

BASE_URL = 'https://parsinger.ru/html/'
START_URL = BASE_URL + 'index1_page_1.html'
CSV_HEADERS = (
    'Наименование', 'Артикул', 'Бренд', 'Модель',
    'Наличие', 'Цена', 'Старая цена', 'Ссылка'
)

user_agent = UserAgent()


def get_headers():
    """Возвращает заголовки со случайным агентом пользователя."""
    return {'User-Agent': user_agent.random}


def get_soup(url):
    """Делает запрос к странице и возвращает объект BeautifulSoup."""
    try:
        response = requests.get(url, get_headers())
        response.raise_for_status()
        response.encoding = 'utf-8'

        return BeautifulSoup(response.text, 'lxml')

    except requests.ConnectionError:
        print("Проблема с соединением! Проверьте интернет.")
    except requests.HTTPError as error:
        print(f"Ошибка HTTP: {error} Проверьте URL или доступ.")
    except requests.RequestException as error:
        print(f'Произошла ошибка: {error}')


def get_urls(class_1, class_2, *args):
    """Получение ссылок."""
    urls = []

    for url in args:
        soup = get_soup(url)
        urls.extend(
            [
                BASE_URL + x.get('href') for x in
                soup.find(class_=class_1).find_all('a', class_=class_2)
            ]
        )

    return urls


def get_data(urls):
    """Получение данных."""
    data = []

    for url in urls:
        soup = get_soup(url)
        name = soup.find(id='p_header').text.strip()
        article = soup.find(class_='article').text.split(':')[1].strip()
        brand = soup.find(id='brand').text.split(':')[1].strip()
        model = soup.find(id='model').text.split(':')[1].strip()
        stock = soup.find(id='in_stock').text.split(':')[1].strip()
        price = soup.find(id='price').text.strip()
        old_price = soup.find(id='old_price').text.strip()

        data.append(
            [name, article, brand, model, stock, price, old_price, url]
        )

    return data


def write_csv(data):
    """Запись данных в файл."""
    with open(
            'total_items.csv', 'w', encoding='utf-8-sig', newline=''
    ) as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(CSV_HEADERS)
        writer.writerows(data)


def main():
    """Главная функция."""
    try:
        navigation_urls = get_urls('nav_menu', None, START_URL)
        pagination_urls = get_urls('pagen', None, *navigation_urls)
        item_urls = get_urls('item_card', 'name_item', *pagination_urls)
        data = get_data(item_urls)
        write_csv(data)
    except AttributeError:
        print('Элемент не найден. Возможно структура сайта изменилась.')
    except Exception as error:
        print(f'Произошла ошибка - {error}!')


if __name__ == '__main__':
    main()
