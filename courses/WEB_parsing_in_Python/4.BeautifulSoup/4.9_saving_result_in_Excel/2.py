"""
Изучите указанную страницу для получения информации о часах с четырёх страниц
в разделе "ЧАСЫ".
Вам потребуется заходить в каждую товарную карточку и собирать данные,
отмеченные на предоставленном изображении.

Сохраните данные в формате CSV с разделителем:
delimiter=';'

Отправьте ваш csv-файл на указанный валидатор. Обратите внимание на сохранение
порядка строк и столбцов, так чтобы они соответствовали эталонному файлу.
Если ваш файл совпадает с эталоном, вы получите код. Этот код нужно будет
вставить в соответствующее поле.
Для сравнения строк воспользуйтесь рекомендованным сервисом.

Информация которую необходимо собрать с каждой карточки:
Заголовки:
Наименование;Артикул;Бренд;Модель;Тип;Технология экрана;Материал корпуса;
Материал браслета;Размер;Сайт производителя;Наличие;Цена;Старая цена;
Ссылка на карточку с товаром
"""

import csv

import requests
from bs4 import BeautifulSoup

URL = 'https://parsinger.ru/html/'
START_URL = 'https://parsinger.ru/html/index1_page_1.html'
CSV_HEADERS = (
    'Наименование', 'Артикул', 'Бренд', 'Модель', 'Тип', 'Технология экрана',
    'Материал корпуса', 'Материал браслета', 'Размер', 'Сайт производителя',
    'Наличие', 'Цена', 'Старая цена', 'Ссылка на карточку с товаром'
)


def get_soup(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = 'utf-8'

        return BeautifulSoup(response.text, 'lxml')

    except requests.RequestException as error:
        print(f"Произошла ошибка: {error}")


def create_csv_with_headers(headers):
    with open('watch.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(headers)


def get_pagination_links(url):
    soup = get_soup(url)
    return [tag.get('href') for tag in soup.find(class_='pagen').find_all('a')]


def get_item_links(links):
    item_links = []

    for link in links:
        url = URL + link
        soup = get_soup(url)
        item_links.extend(
            [tag.get('href') for tag in soup.find_all(class_='name_item')]
        )

    return item_links


def get_data(links):
    names = []
    articles = []
    brands = []
    models = []
    types = []
    displays = []
    bodies = []
    bracelets = []
    sizes = []
    sites = []
    stocks = []
    prices = []
    old_prices = []
    item_urls = []

    for link in links:
        url = URL + link
        soup = get_soup(url)
        names.append(soup.find(id='p_header').text.strip())
        articles.append(
            soup.find(class_='article').text.split(':')[-1].strip()
        )
        brands.append(soup.find(id='brand').text.split(':')[-1].strip())
        models.append(soup.find(id='model').text.split(':')[-1].strip())
        types.append(soup.find(id='type').text.split(':')[-1].strip())
        displays.append(soup.find(id='display').text.split(':')[-1].strip())
        bodies.append(
            soup.find(id='material_frame').text.split(':')[-1].strip()
        )
        bracelets.append(
            soup.find(id='material_bracer').text.split(':')[-1].strip()
        )
        sizes.append(soup.find(id='size').text.split(':')[-1].strip())
        sites.append(soup.find(id='site').text.split(':')[-1].strip())
        stocks.append(soup.find(id='in_stock').text.split(':')[-1].strip())
        prices.append(soup.find(id='price').text.strip())
        old_prices.append(soup.find(id='old_price').text.strip())
        item_urls.append(url)

    return zip(
        names, articles, brands, models, types, displays, bodies, bracelets,
        sizes, sites, stocks, prices, old_prices, item_urls
    )


def write_csv(data):
    with open('watch.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in data:
            writer.writerow(row)


def main():
    create_csv_with_headers(CSV_HEADERS)
    pagination_links = get_pagination_links(START_URL)
    item_links = get_item_links(pagination_links)
    data = get_data(item_links)
    write_csv(data)


if __name__ == '__main__':
    main()
