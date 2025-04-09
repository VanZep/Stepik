"""
Целью задания является закрепление навыков работы с методом response.json()

Условия:
Используйте API погодного сервиса, расположенный по адресу.
Данный API возвращает погодные данные для заданного города в формате JSON.

Задача:
Напишите код, который осуществляет GET-запрос к указанному API для получения
погодных данных заданного города.

Преобразовать полученный JSON-ответ в Python-объект с помощью метода
response.json().

Проанализировать данные и определить дату с самой минимальной температурой.

Результат:
В поле для ответа нужно вставить найденную дату с самой минимальной
температурой. Формат даты должен быть таковым, как представлен в данных
по ссылке API.

Пример вывода:
2023-10-01
"""

import requests

URL_API = 'https://parsinger.ru/3.4/1/json_weather.json'

try:
    response = requests.get(url=URL_API)
    response.raise_for_status()
except (requests.exceptions.HTTPError, requests.RequestException) as err:
    print(f"Произошла ошибка: {err}")

data = response.json()
min_temp = 100
date = None

for item in data:
    temp = int(item['Температура воздуха'].rstrip('°C'))
    if temp < min_temp:
        min_temp = temp
        date = item['Дата']

print(date)
