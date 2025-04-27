"""
Соберите указанные на изображении ниже данные с сайта тренажёра.
Заходить в каждую карточку с товаром не требуется, собирать необходимо только
с превью карточки.

Сохраните данные в формате CSV с разделителем:
delimiter=';'

Отправьте ваш csv-файл на указанный валидатор. Обратите внимание на сохранение
порядка строк и столбцов, так чтобы они соответствовали эталонному файлу.
Заголовки указывать не нужно.
Если ваш файл совпадает с эталоном, вы получите код. Этот код нужно будет
вставить в соответствующее поле.
Для сравнения строк воспользуйтесь рекомендованным сервисом.
"""

import csv

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

URL = 'https://parsinger.ru/html/'
START_URL = 'https://parsinger.ru/html/index1_page_1.html'

user_agent = UserAgent()


def get_headers():
    return {'User-Agent': user_agent.random}


def get_soup(url):
    try:
        response = requests.get(url, get_headers())
        response.raise_for_status()
        response.encoding = 'utf-8'

        return BeautifulSoup(response.text, 'lxml')

    except requests.RequestException as error:
        print(f"Произошла ошибка: {error}")


def get_navigation_links(url):
    soup = get_soup(url)
    return [
        x.get('href') for x in soup.find(class_='nav_menu').find_all('a')
    ]


def get_pagination_links(links):
    pagination_links = []

    for link in links:
        url = URL + link
        soup = get_soup(url)
        pagination_links.extend(
            [x.get('href') for x in soup.find(class_='pagen').find_all('a')]
        )

    return pagination_links


def get_data(links):
    data = []

    for link in links:
        url = URL + link
        soup = get_soup(url)
        names = [x.text.strip() for x in soup.find_all(class_='name_item')]
        prices = [x.text for x in soup.find_all(class_='price')]
        descriptions = [
            x.text.strip().split('\n') for x in
            soup.find_all(class_='description')
        ]
        descr_info = zip(*(
            [x.split(':')[-1].strip() for x in desc] for desc in descriptions
        ))
        data.extend(zip(*[names, *descr_info, prices]))

    return data


def write_csv(data):
    with open('total.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(data)


def main():
    category_links = get_navigation_links(START_URL)
    pagination_links = get_pagination_links(category_links)
    data = get_data(pagination_links)
    write_csv(data)


if __name__ == '__main__':
    main()
