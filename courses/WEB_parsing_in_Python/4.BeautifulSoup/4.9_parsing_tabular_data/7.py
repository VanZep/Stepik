"""
Задача:
Загрузить страницу с шестью таблицами.
Пройтись по каждой ячейке каждой таблицы и проверить значение на кратность
трём.
Если число кратно трем, добавить его к общей сумме.
Вставить результат в поле ответа.
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://parsinger.ru/4.8/7/index.html'


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

    total_summ = sum(
        int(tag.text) for tag in soup.find_all('td') if int(tag.text) % 3 == 0
    )

    print(total_summ)


if __name__ == '__main__':
    main()
