"""
Задача:
Открыть веб-сайт и обнаружить необходимую таблицу.
Для каждой строки таблицы найти числа в оранжевой и голубой ячейках, после
чего умножить их друг на друга.
Сложить все получившиеся произведения, чтобы получить общую сумму.
Ввести итоговый результат в поле ответа.

Данные должны иметь следующий вид:
*******.6860000016
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://parsinger.ru/table/5/index.html'


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
    product_cells = [
        float(tag.select_one('.orange').text) *
        float(tag.select_one('td:last-child').text)
        for tag in soup.find_all('tr')[1:]
    ]

    print(sum(product_cells))


if __name__ == '__main__':
    main()
