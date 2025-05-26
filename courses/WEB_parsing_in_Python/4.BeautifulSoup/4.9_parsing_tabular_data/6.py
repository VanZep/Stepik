"""
Задача:
Открыть веб-сайт и обнаружить интересующую таблицу.
Для каждого столбца вычислить сумму всех чисел в этом столбце.
Округлить каждое получившееся значение до трех знаков после запятой.
row: round(sum(column), 3)
Формировать словарь, где ключами будут названия столбцов, а значениями -
рассчитанные суммы.
Вставить полученный словарь в поле ответа на веб-сайте.


Пример ожидаемого валидатором словаря, в одну строку и без переносов на новую
строку:

{
    '1 column': 000.000, '2 column': 000.000, '3 column': 000.000,
    '4 column': 000.000, '5 column': 000.00, '6 column': 000.000,
    '7 column': 000.000, '8 column': 000.000, '9 column': 000.000,
    '10 column': 000.000, '11 column': 000.000, '12 column': 000.000,
    '13 column': 000.000, '14 column': 000.000, '15 column': 000000.0
}
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
    column_names = [tag.text for tag in soup.find_all('th')]
    rows = soup.find_all('tr')
    row_values = [
        [float(tag.text) for tag in row.find_all('td')] for row in rows[1:]
    ]
    column_values = zip(*row_values)
    column_sum_values = [round(sum(values), 3) for values in column_values]
    column_sums = dict(zip(column_names, column_sum_values))
    print(column_sums)


if __name__ == '__main__':
    main()
