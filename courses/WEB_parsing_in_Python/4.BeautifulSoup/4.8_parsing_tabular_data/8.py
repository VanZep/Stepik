"""
Задача:
Загрузить страницу на которой расположена таблица с объединёнными ячейками.
Извлечь данные из каждой объединённой ячейки(всего 16 ячеек), объединённую
ячейку можно определить по атрибуту colspan.
Суммировать все числовые значения, полученные из объединённых ячеек.
Ввести полученную сумму в поле ответа.
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://parsinger.ru/4.8/8/index.html'


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
        int(tag.text) for tag in soup.find_all(attrs={'colspan': True})
        if tag.string
    )

    print(total_summ)


if __name__ == '__main__':
    main()
