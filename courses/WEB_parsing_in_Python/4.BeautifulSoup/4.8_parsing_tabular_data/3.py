"""
Задача:
Перейти на сайт и обнаружить требуемую таблицу.
Cобрать только числа, отформатированные жирным шрифтом.
.find('b')
или
.find_all('b')
Суммировать выделенные числа.
Вставить полученный результат в поле ответа.
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://parsinger.ru/table/3/index.html'


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
    b_values = [float(tag.text) for tag in soup.find_all('b')]

    print(sum(b_values))


if __name__ == '__main__':
    main()
