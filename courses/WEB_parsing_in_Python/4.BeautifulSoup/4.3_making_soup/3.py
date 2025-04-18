"""
Цель:
Написать код, который будет обрабатывать HTML-структуру, содержащую
карточки товаров. Код должен находить все теги с классом card-articul,
извлекать из них числовые значения артикулов и суммировать их.

Задача:
Обработать все теги <p> с классом card-articul в предоставленной HTML-строке.
Для каждого тега <p>, извлечь числовое значение артикула, следующее после
текста "Артикул: ".
Суммировать все извлеченные числовые значения.
"""

from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
</head>
<body>
    <div class="cards">
        <!-- Карточка товара 1 -->
        <div class="card">
            <img src="parsing.png" alt="WEB Парсинг на Python">
            <h2 class="card-title">WEB Парсинг на Python</h2>
            <p class="card-articul">Артикул: 104774</p>
            <p class="card-stock">Наличие: 5 шт.</p>
            <p class="card-price">3500 руб.</p>
            <a href="https://stepik.org/a/104774" class="card-button">Купить</a>
        </div>
        <!-- Карточка товара 2 -->
        <div class="card">
            <img src="async.png" alt="Асинхронный Python">
            <h2 class="card-title">Асинхронный Python</h2>
            <p class="card-articul">Артикул: 170777</p>
            <p class="card-stock">Наличие: 10 шт.</p>
            <p class="card-price">3500 руб.</p>
            <a href="https://stepik.org/a/170777" class="card-button">Купить</a>
        </div>
        <!-- Карточка товара 3 -->
        <div class="card">
            <img src="selenium.PNG" alt="Selenium Python">
            <h2 class="card-title">Selenium Python</h2>
            <p class="card-articul">Артикул: 119495</p>
            <p class="card-stock">Наличие: 5 шт.</p>
            <p class="card-price">1250 руб.</p>
            <a href="https://stepik.org/a/119495" class="card-button">Купить</a>
        </div>
    </div>
</body>
</html>
"""


def main():
    soup = BeautifulSoup(html_doc, 'lxml')
    articuls = [item.text for item in soup.find_all(class_='card-articul')]
    sum_articuls = sum(int(art.lstrip('Артикул: ')) for art in articuls)
    print(f"Сумма артикулов: {sum_articuls}")


main()
