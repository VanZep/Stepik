"""
Соберите данные всех карточек товара всех категорий и со всех страниц тренажера
(всего 160шт).
Не "проваливайтесь" внутрь каждой карточки. Соберите только информацию из
превью.
Сохраните данные в JSON файл с использованием указанных параметров:
json.dump(res, file, indent=4, ensure_ascii=False)
Отправьте готовый JSON файл в валидатор, для успешной валидации файла,
необходимо сохранить порядок объектов JSON:
Порядок сбора категорий:
Часы
Телефоны
Мыши
HDD
Наушники
Имя файла произвольное.
Удалите все лишние пробелы из данных методом strip().
Если файл совпадает с эталоном на сервере, вы получите код. Этот код необходимо
будет вставить в поле ответа.
Используйте этот сервис для проверки разности строк.

# Порядок ключей объекта JSON
{
        "Наименование": "Crown CMGH-3100",
        "Бренд": "Crown",
        "Тип подключения": "Проводной",
        "Цвет": "черный, красный",
        "Тип наушников": "Мониторные",
        "Цена": "3110 руб"
}
"""

import json

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
        print(f'Произошла ошибка: {error}')


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


def get_data_for_json(links):
    data_json = []

    for link in links:
        url = URL + link
        soup = get_soup(url)
        for item in soup.find_all(class_='item'):
            name = {'Наименование': item.find(class_='name_item').text.strip()}
            price = {'Цена': item.find(class_='price').text}
            description = {
                x.text.split(':')[0].strip(): x.text.split(':')[1].strip()
                for x in item.find(class_='description').find_all('li')
            }
            data_json.append(name | description | price)

    return data_json


def write_json(data):
    with open('total.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    category_links = get_navigation_links(START_URL)
    pagination_links = get_pagination_links(category_links)
    data = get_data_for_json(pagination_links)
    write_json(data)


if __name__ == '__main__':
    main()
