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


def get_soup(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = 'utf-8'

        return BeautifulSoup(response.text, 'lxml')

    except requests.RequestException as error:
        print(f"Произошла ошибка: {error}")


def get_pagination_links(url):
    soup = get_soup(url)
    return [tag.get('href') for tag in soup.find(class_='pagen').find_all('a')]


# def get_data(links):
#     names = []
#     prices = []
#     descriptions = []
#
#     for link in links:
#         url = URL + link
#         soup = get_soup(url)
#         names += [x.text.strip() for x in soup.find_all(class_='name_item')]
#         prices += [x.text for x in soup.find_all(class_='price')]
#         descriptions += [
#             x.text.strip().split('\n') for x in
#             soup.find_all(class_='description')
#         ]
#
#     z = [[x.split(':')[-1].strip() for x in desc] for desc in descriptions]
#
#     return zip(names, *zip(*z), prices)


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
    with open('hdd.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(CSV_HEADERS)
        writer.writerows(data)


def main():
    pagination_links = get_pagination_links(START_URL)
    data = get_data(pagination_links)
    write_csv(data)


if __name__ == '__main__':
    main()
