"""
Напишите программу которая делает GET-запрос к указанной веб-странице для
получения её HTML-кода.
Выведите полученный HTML-код на экран с помощью response.text.
Используйте response.encoding = 'utf-8' чтобы починить кодировку.
"""

import requests

URL = 'https://parsinger.ru/3.4/2/index.html'

try:
    response = requests.get(url=URL)
    response.raise_for_status()
    print("Запрос успешно выполнен")
except requests.exceptions.HTTPError as err:
    print(f"Произошла ошибка: {err}")

response.encoding = 'utf-8'
print(response.text)
