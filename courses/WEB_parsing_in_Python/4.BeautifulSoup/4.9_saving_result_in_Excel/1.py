"""
Используйте страницу, чтобы собрать данные с четырёх страниц в категории hdd.
"Проваливаться" в каждую карточку не нужно, соберите информацию с превью
карточки.

При создании CSV используйте разделитель:
delimiter=';'

Отправьте готовый csv файл в валидатор, для успешной валидации файла,
необходимо сохранить тот же порядок строк и столбцов, что и в эталонном файле.
Если файл совпадает с эталонным на сервере, вы получите код который необходимо
вставить в поле ответа.

Информация которую необходимо собрать с каждой карточки:
Заголовки:
Наименование;Бренд;Форм-фактор;Ёмкость;Объем буферной памяти;Цена
"""

import csv

import requests
from bs4 import BeautifulSoup

URL = 'https://parsinger.ru/html/'
START_URL = 'https://parsinger.ru/html/index4_page_1.html'
CSV_HEADERS = (
    'Наименование', 'Бренд', 'Форм-фактор', 'Ёмкость',
    'Объем буферной памяти', 'Цена'
)


def get_response(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = 'utf-8'

        return response.text
    except requests.RequestException as error:
        print(f"Произошла ошибка: {error}")


def create_csv_with_headers(headers):
    with open('hdd.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(headers)


def get_pagination_links(url):
    html = get_response(url)
    soup = BeautifulSoup(html, 'html.parser')
    return [tag.get('href') for tag in soup.find(class_='pagen').find_all('a')]


def get_data(links):
    names = []
    prices = []
    descriptions = []

    for link in links:
        url = URL + link
        html = get_response(url)
        soup = BeautifulSoup(html, 'html.parser')
        names += [x.text.strip() for x in soup.find_all(class_='name_item')]
        prices += [x.text for x in soup.find_all(class_='price')]
        descriptions += [
            x.text.strip().split('\n') for x in
            soup.find_all(class_='description')
        ]

    brands = []
    form_factors = []
    containers = []
    buffer_memory_sizes = []

    for row in descriptions:
        brands.append(row[0].split(':')[1].strip())
        form_factors.append(row[1].split(':')[1].strip())
        containers.append(row[2].split(':')[1].strip())
        buffer_memory_sizes.append(row[3].split(':')[1].strip())

    return zip(
        names, brands, form_factors, containers, buffer_memory_sizes, prices
    )


def write_csv(data):
    with open('hdd.csv', 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        for row in data:
            writer.writerow(row)


def main():
    create_csv_with_headers(CSV_HEADERS)
    pagination_links = get_pagination_links(START_URL)
    data = get_data(pagination_links)
    write_csv(data)


if __name__ == '__main__':
    main()
