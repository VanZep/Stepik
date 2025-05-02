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
        print(f'Произошла ошибка: {error}')


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
    data = []

    for link in links:
        url = URL + link
        soup = get_soup(url)
        name = soup.find(id='p_header').text.strip()
        price = soup.find(id='price').text.strip()
        old_price = soup.find(id='old_price').text.strip()
        description = [
            desc.split(':')[-1].strip() for desc in
            soup.find(class_='description').text.strip().split('\n')
            if ':' in desc
        ]
        data.append([name, *description, price, old_price, url])

    return data


def write_csv(data):
    with open('watch.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(CSV_HEADERS)
        writer.writerows(data)


def main():
    pagination_links = get_pagination_links(START_URL)
    item_links = get_item_links(pagination_links)
    data = get_data(item_links)
    write_csv(data)


if __name__ == '__main__':
    main()
