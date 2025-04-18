"""
Задача:
Перейти на сайт и найти таблицу.
Произвести парсинг данных из первого столбца таблицы.
Суммировать все числа, найденные в первом столбце.
Вставить полученный результат в поле ответа.
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://parsinger.ru/table/2/index.html'


def get_response(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = 'utf-8'

        return response.text
    except requests.RequestException as error:
        print(f"Произошла ошибка: {error}")


def main():
    html = get_response(URL)
    soup = BeautifulSoup(html, 'html.parser')
    first_col_tags = soup.select('td:first-child')
    first_col_values = [float(tag.text) for tag in first_col_tags]

    print(sum(first_col_values))


if __name__ == '__main__':
    main()
