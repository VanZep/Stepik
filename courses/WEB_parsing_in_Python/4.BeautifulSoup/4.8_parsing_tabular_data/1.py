"""
Задача:
Перейти на сайт и найти таблицу.
Произвести парсинг данных из таблицы.
Отфильтровать и извлечь все уникальные числа, исключая числа в заголовке
таблицы.
Посчитать сумму этих чисел.
Вставить полученный результат в поле ответа.

Данные должны иметь следующий вид:
***.0959999999998
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://parsinger.ru/table/1/index.html'


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
    table_rows = soup.find('table').find_all('tr')
    unique_values = set()
    for row in table_rows[1:]:
        row_values = {float(tag.text) for tag in row.select('td')}
        unique_values.update(row_values)

    print(sum(unique_values))


if __name__ == '__main__':
    main()
