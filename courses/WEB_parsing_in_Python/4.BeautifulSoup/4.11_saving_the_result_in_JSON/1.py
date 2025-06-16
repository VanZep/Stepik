"""
Соберите данные о HDD с четырёх страниц в категории HDD.
Не "проваливайтесь" внутрь каждой карточки. Соберите только информацию из
превью.
Сохраните данные в JSON файл с использованием указанных параметров.
json.dump(res, file, indent=4, ensure_ascii=False)
Отправьте готовый JSON файл в валидатор, для успешной валидации файла,
необходимо сохранить тот же порядок объектов JSON (для этого необходимо
собирать данные в том же порядке, в котором они находятся на сайте).
Имя файла произвольное.
Удалите все лишние пробелы из данных методом strip().
Если файл совпадает с эталоном на сервере, вы получите код. Этот код
необходимо будет вставить в поле ответа.
Используйте этот сервис для проверки разности строк.


# Порядок ключей в объекте JSON
{
    "Наименование": "Toshiba S300 Surveillance",
    "Бренд": "Toshiba",
    "Форм-фактор": "3.5",
    "Ёмкость": "4 Tb",
    "Объем буферной памяти": "128 Mb",
    "Цена": "10710 руб"
}
"""

import json

import requests
from bs4 import BeautifulSoup

URL = 'https://parsinger.ru/html/'
START_URL = 'https://parsinger.ru/html/index4_page_1.html'
JSON_HEADERS = (
    'Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость',
    'Объем буферной памяти', 'Цена'
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


def get_data_for_json(links):
    data_json = []

    for link in links:
        url = URL + link
        soup = get_soup(url)
        for item in soup.find_all(class_='item'):
            name = item.find(class_='name_item').text.strip()
            price = item.find(class_='price').text
            description = [
                x.text.split(':')[1].strip() for x in
                item.find(class_='description').find_all('li')
            ]
            data_json.append(
                dict(zip(JSON_HEADERS, (name, *description, price)))
            )

    return data_json


def write_json(data):
    with open('hdd.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    pagination_links = get_pagination_links(START_URL)
    data = get_data_for_json(pagination_links)
    write_json(data)


if __name__ == '__main__':
    main()
