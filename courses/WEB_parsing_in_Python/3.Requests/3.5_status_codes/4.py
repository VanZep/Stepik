"""
Целью этой задачи является определение первой и последней доступных страниц в
заданном диапазоне URL-адресов.

Условия
# От
https://parsinger.ru/3.3/4/1.html
# До
https://parsinger.ru/3.3/4/100.html

Ваша задача сосредоточена на определении страниц с HTTP статус-кодом 200,
который означает успешный ответ от сервера.

Задачи
Написать скрипт, который будет делать GET запросы к каждой странице в
диапазоне.
Определить, какая страница в диапазоне является первой доступной
(статус-код 200).
Определить, какая страница в диапазоне является последней доступной
(также статус-код 200).

Результат
Программа должна вывести номера первой и последней доступных страниц в
заданном диапазоне.

Первая доступная страница: 3.html
Последняя доступная страница: 98.html
"""

from http import HTTPStatus

import requests

PAGES_COUNT = 100
URL = 'https://parsinger.ru/3.3/4/'
first_available_page = None
last_available_page = None

with requests.Session() as session:
    for page_number in range(1, PAGES_COUNT + 1):
        url = f'{URL}{page_number}.html'
        try:
            response = session.get(url=url, timeout=0.1)
            if response.status_code == HTTPStatus.OK:
                first_available_page = (
                    page_number if first_available_page is None
                    else first_available_page
                )
                last_available_page = page_number
        except requests.Timeout:
            print(f'Слишком долгое ожидание страницы номер {page_number}')
        except requests.RequestException as e:
            print(f'Произошла ошибка: {e}')

print(
    f'Первая доступная страница: {first_available_page}.html',
    f'Последняя доступная страница: {last_available_page}.html',
    sep='\n'
)
