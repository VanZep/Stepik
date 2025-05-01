"""
Вашей задачей является создание скрипта, который делает сетевые запросы к
указанному диапазону ссылок для выявления единственной рабочей страницы и
поиска кода на ней. Для этого необходимо считывать HTTP статус-код каждой
страницы.

Диапазон ссылок:
# От
https://parsinger.ru/3.3/1/1.html
# До
https://parsinger.ru/3.3/1/200.html

Детали:
В указанном диапазоне существует только одна рабочая страница с HTTP
статус-кодом 200 (OK).
Все остальные страницы возвращают HTTP статус-код 404 (Not Found).

Задание:
Выполните HTTP запрос к каждой ссылке в заданном диапазоне.
Считывайте HTTP статус-код каждой страницы.
Определите, какая именно ссылка является рабочей, то есть возвращает HTTP
статус-код 200 (OK).
Перейдите по рабочей ссылке вручную, или получите данные с помощью
response.text для извлечения числа на этой странице.
Вставьте число в поле ответа Cтепик.
"""

from http import HTTPStatus

import requests
from bs4 import BeautifulSoup

PAGE_COUNT = 200
URL = 'https://parsinger.ru/3.3/1/'

with requests.Session() as session:
    for page_number in range(1, PAGE_COUNT + 1):
        try:
            response = session.get(url=f'{URL}{page_number}.html', timeout=0.1)
        except requests.Timeout:
            print(f'Слишком долгое ожидание страницы номер {page_number}')
        except requests.RequestException as e:
            print(f'Произошла ошибка: {e}')
        if response.status_code == HTTPStatus.OK:
            page_html = response.text

soup = BeautifulSoup(page_html, 'html.parser')
page_code = soup.select_one('body').text.strip()
print(page_code)
