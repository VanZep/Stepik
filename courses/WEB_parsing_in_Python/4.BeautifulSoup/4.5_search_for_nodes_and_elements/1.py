"""
Цель:
Необходимо написать код, который будет обрабатывать HTML-структуру с
карточками товаров (в данном случае — книг). Код должен вычислять общую сумму,
которую можно получить при продаже всех книг на складе.

HTML-строка, содержащая структуру с карточками товаров. Каждая карточка товара
имеет следующий вид:
<div class="book-card">
    <p class="count price">Цена: $[цена]</p>
    <p class="count stock">Количество на складе: [количество]</p>
    <!-- ... остальные элементы карточки ... -->
</div>
 где [цена] — это стоимость одной единицы товара, а [количество] —
 это количество товара на складе.

Задача:
Извлечь из каждой карточки информацию о цене и количестве на складе.
Умножить цену на количество для каждого товара.
Подсчитать общую сумму для всех товаров.

Выходные данные:
Общая сумма, которую можно выручить при продаже всех книг.

<div class="book-card">
    <p class="count price">Цена: $19.50</p>
    <p class="count stock">Количество на складе: 63</p>
    <!-- ... -->
</div>
<div class="book-card">
    <p class="count price">Цена: $25.00</p>
    <p class="count stock">Количество на складе: 40</p>
    <!-- ... -->
</div>
Для данного примера общая сумма составит $2228.50 (19.50 * 63 + 25.00 * 40).

Требования к реализации:
Использовать библиотеку BeautifulSoup для обработки HTML.
Учесть возможное наличие двойных тегов.
Код должен быть написан так, чтобы легко масштабироваться для обработки любого
количества карточек товаров.
Функция calculate_total_price() принимает на вход документ html и должна
вернуть искомое значение.
Нужно вывести сообщение с итогом работы программы
print(
    'Общая стоимость в случае продажи всех товаров: '
    f'${calculate_total_price(html)}'
)
"""
import requests
from bs4 import BeautifulSoup

URL = 'https://parsinger.ru/4.3/5/index.html'
# html = '''<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Онлайн Магазин Книг</title>
# </head>
# <body>
#     <div class="book-card">
#         <img src="1.png" alt="Обложка книги 1" class="book-cover book-cover_hard">
#         <h2 class="book pages">Название Книги 1</h2>
#         <p class="book-author">Автор: Автор 1</p>
#         <p class="book-isbn">ISBN: 978-1234567890</p>
#         <p class="book-cover-type">Обложка: Твердая</p>
#         <p class="count price">Цена: $20.00</p>
#         <p class="book-format">Формат: Мягкая обложка</p>
#         <p class="count pages">Количество страниц: 300</p>
#         <p class="count stock">Количество на складе: 75</p>
#         <p class="book-publisher">Издательство: Издательство 1</p>
#         <p class="book-publication-date">Дата публикации: 01.01.2023</p>
#         <p class="count rating">Рейтинг: 4.5</p>
#         <p class="book-genre">Жанр: Роман</p>
#         <p class="book-language">Язык: Английский</p>
#         <p class="book-availability">Доступность: В наличии</p>
#         <p class="book-description">Описание: Краткое описание книги 1.</p>
#         <button class="book-purchase-btn">Добавить в корзину</button>
#     </div>
#     <div class="book-card">
#         <img src="2.png" alt="Обложка книги 2" class="book-cover book-cover_hard">
#         <h2 class="book pages">Название Книги 2</h2>
#         <p class="book-author">Автор: Автор 2</p>
#         <p class="book-isbn">ISBN: 978-9876543210</p>
#         <p class="book-cover-type">Обложка: Мягкая</p>
#         <p class="count price">Цена: $18.50</p>
#         <p class="book-format">Формат: Электронная версия (e-book)</p>
#         <p class="count pages">Количество страниц: 250</p>
#         <p class="count stock">Количество на складе: 119</p>
#         <p class="book-publisher">Издательство: Издательство 3</p>
#         <p class="book-publication-date">Дата публикации: 20.03.2023</p>
#         <p class="count rating">Рейтинг: 4.7</p>
#         <p class="book-genre">Жанр: Детская литература</p>
#         <p class="book-language">Язык: Французский</p>
#         <p class="book-availability">Доступность: В наличии</p>
#         <p class="book-description">Описание: Краткое описание книги 2.</p>
#          <button class="book-purchase-btn">Добавить в корзину</button>
#     </div>
#     <div class="book-card">
#         <img src="3.png" alt="Обложка книги 3" class="book-cover book-cover_hard">
#         <h2 class="book pages">Название Книги 3</h2>
#         <p class="book-author">Автор: Автор 3</p>
#         <p class="book-isbn">ISBN: 978-0987654321</p>
#         <p class="book-cover-type">Обложка: Твердая</p>
#         <p class="count price">Цена: $25.00</p>
#         <p class="book-format">Формат: Мягкая обложка</p>
#         <p class="count pages">Количество страниц: 400</p>
#         <p class="count stock">Количество на складе: 216</p>
#         <p class="book-publisher">Издательство: Издательство 2</p>
#         <p class="book-publication-date">Дата публикации: 15.02.2023</p>
#         <p class="count rating">Рейтинг: 4.8</p>
#         <p class="book-genre">Жанр: Фантастика</p>
#         <p class="book-language">Язык: Русский</p>
#         <p class="book-availability">Доступность: В наличии</p>
#         <p class="book-description">Описание: Краткое описание книги 3.</p>
#         <button class="book-purchase-btn">Добавить в корзину</button>
#     </div>
#     <div class="book-card">
#         <img src="4.png" alt="Обложка книги 4" class="book-cover book-cover_hard">
#         <h2 class="book pages">Название Книги 4</h2>
#         <p class="book-author">Автор: Автор 4</p>
#         <p class="book-isbn">ISBN: 978-5432109876</p>
#         <p class="book-cover-type">Обложка: Твердая</p>
#         <p class="count price">Цена: $22.00</p>
#         <p class="book-format">Формат: Мягкая обложка</p>
#         <p class="count pages">Количество страниц: 350</p>
#         <p class="count stock">Количество на складе: 17</p>
#         <p class="book-publisher">Издательство: Издательство 4</p>
#         <p class="book-publication-date">Дата публикации: 10.04.2023</p>
#         <p class="count rating">Рейтинг: 4.9</p>
#         <p class="book-genre">Жанр: Детектив</p>
#         <p class="book-language">Язык: Английский</p>
#         <p class="book-availability">Доступность: В наличии</p>
#         <p class="book-description">Описание: Краткое описание книги 4.</p>
#         <button class="book-purchase-btn">Добавить в корзину</button>
#     </div>
#     <div class="book-card">
#         <img src="5.png" alt="Обложка книги 5" class="book-cover book-cover_hard">
#         <h2 class="book pages">Название Книги 5</h2>
#         <p class="book-author">Автор: Автор 5</p>
#         <p class="book-isbn">ISBN: 978-8765432109</p>
#         <p class="book-cover-type">Обложка: Мягкая</p>
#         <p class="count price">Цена: $19.50</p>
#         <p class="book-format">Формат: Мягкая обложка</p>
#         <p class="count pages">Количество страниц: 280</p>
#         <p class="count stock">Количество на складе: 63</p>
#         <p class="book-publisher">Издательство: Издательство 5</p>
#         <p class="book-publication-date">Дата публикации: 05.05.2023</p>
#         <p class="count rating">Рейтинг: 4.6</p>
#         <p class="book-genre">Жанр: Фэнтези</p>
#         <p class="book-language">Язык: Испанский</p>
#         <p class="book-availability">Доступность: В наличии</p>
#         <p class="book-description">Описание: Краткое описание книги 5.</p>
#         <button class="book-purchase-btn">Добавить в корзину</button>
#     </div>
# </body>
# </html>
# '''

response = requests.get(url=URL)
response.encoding = 'utf-8'
html = response.text


def calculate_total_price(html: str) -> float:
    soup = BeautifulSoup(html, 'html.parser')
    book_cards = soup.find_all(class_='book-card')

    total_price = 0

    for card in book_cards:
        card_price = float(card.find(class_='price').text.split('$')[1])
        card_stock = int(card.find(class_='stock').text.split(': ')[1])
        total_price += card_price * card_stock

    return total_price


print(
    'Общая стоимость в случае продажи всех товаров: '
    f'${calculate_total_price(html):.2f}'
)
