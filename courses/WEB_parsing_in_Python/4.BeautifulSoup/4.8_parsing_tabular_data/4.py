"""
Задача:
Открыть веб-сайт и найти целевую таблицу.
Провести анализ данных в таблице, фокусируясь на ячейках зелёного цвета.
Выделить и подсчитать сумму всех чисел из зелёных ячеек.
Внести полученную сумму в поле ответа.
Данные должны иметь следующий вид.
***.7659999999999
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://parsinger.ru/table/4/index.html'


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
    green_values = [float(tag.text) for tag in soup.find_all(class_='green')]

    print(sum(green_values))


if __name__ == '__main__':
    main()
