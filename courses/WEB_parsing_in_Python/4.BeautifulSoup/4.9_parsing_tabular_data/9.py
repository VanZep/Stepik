"""
Ваш друг обратился к вам с просьбой помочь найти автомобиль, который
соответствует определенным требованиям. Вы решили использовать ваши навыки
программирования для написания кода, который может автоматически отфильтровать
и сортировать автомобили по заданным критериям.

Основные этапы выполнения задачи:

Запрашивайте данные с веб-сайта, который содержит таблицу автомобилей.
Фильтруйте автомобили по заданным критериям:
Cтоимость не выше 4 000 000 (Стоимость авто <= 4000000),
Год выпуска начиная с 2005 года (Год выпуска >= 2005),
Тип двигателя - Бензиновый (Тип двигателя == "Бензиновый").
Выводите результат в формате JSON, при отправке данных в валидатор, важен
каждый пробел и перенос строки.

Используйте эти параметры для формирования JSON:
json.dumps(sorted_cars, indent=4, ensure_ascii=False)

Пример ожидаемого валидатором JSON:

[
    {
        "Марка Авто": "***",     # str
        "Год выпуска": ***,      # int
        "Тип двигателя": "***",  # str
        "Стоимость авто": ***    # int
    },
...
...
...
    {
        "Марка Авто": "***",     # str
        "Год выпуска": ***,      # int
        "Тип двигателя": "***",  # str
        "Стоимость авто": ***    # int
    }
]

Обратите внимание на тип данных.
        "Марка Авто": str("Nissan"),
        "Год выпуска": int(2009),
        "Тип двигателя": str("Бензиновый"),
        "Стоимость авто": int(891048)

Сортируйте отфильтрованный JSON автомобилей по стоимости от меньшего к
большему:
sorted(filtered_cars, key=lambda x: x["Стоимость авто"])
"""

import json

import requests
from bs4 import BeautifulSoup

URL = 'https://parsinger.ru/4.8/6/index.html'
BRAND = 'Марка Авто'
YEAR = 'Год выпуска'
ENGINE = 'Тип двигателя'
PRICE = 'Стоимость авто'


def get_response(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = 'utf-8'

        return response.text
    except requests.RequestException as error:
        print(f"Произошла ошибка: {error}")


def get_col_numbers(headers_row):
    headers = [tag.text for tag in headers_row.find_all('th')]

    return {name: headers.index(name) for name in (BRAND, YEAR, ENGINE, PRICE)}


def get_filtered_cars(car_rows, col_numbers):
    filtered_cars = []

    for row in car_rows:
        car = [tag.text for tag in row.find_all('td')]
        if (
                int(car[col_numbers[YEAR]]) >= 2005 and
                car[col_numbers[ENGINE]] == 'Бензиновый' and
                int(car[col_numbers[PRICE]]) <= 4_000_000
        ):
            filtered_cars.append({
                BRAND: car[col_numbers[BRAND]],
                YEAR: int(car[col_numbers[YEAR]]),
                ENGINE: car[col_numbers[ENGINE]],
                PRICE: int(car[col_numbers[PRICE]])
            })

    return filtered_cars


def main():
    html = get_response(URL)
    soup = BeautifulSoup(html, 'html.parser')
    table_rows = soup.find_all('tr')
    col_numbers = get_col_numbers(table_rows[0])
    filtered_cars = get_filtered_cars(table_rows[1:], col_numbers)
    sorted_cars = sorted(filtered_cars, key=lambda car: car[PRICE])
    json_cars = json.dumps(sorted_cars, indent=4, ensure_ascii=False)
    print(json_cars)


if __name__ == '__main__':
    main()
