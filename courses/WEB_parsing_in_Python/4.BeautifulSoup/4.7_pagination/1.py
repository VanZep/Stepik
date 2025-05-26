"""
Цель:
Посетить указанный веб-сайт и извлечь названия товаров со всех четырех
страниц одной категории "МЫШИ". Необходимо организовать данные таким образом,
чтобы названия товаров с каждой страницы хранились в отдельном списке.
По завершении работы у вас должен быть главный список, содержащий четыре
вложенных списка с названиями товаров.

Условия выполнения:
Посещение и анализ четырех страниц веб-сайта с пагинацией.
Извлечение названий товаров с каждой страницы (8 шт на каждой странице).
Сохранение названий товаров с каждой страницы в отдельном списке.
Объединение всех четырех списков в один главный список.
Метод strip() для названий товаров использовать не требуется.
Отправьте полученый список списков в качестве ответа.
Пример ожидаемого результата:

[
    [' name1 ', 'name2', ' ... ', ' name_N'],
    [' name1 ', 'name2', ' ... ', ' name_N'],
    [' name1 ', 'name2', ' ... ', ' name_N'],
    [' name1 ', 'name2', ' ... ', ' name_N']
]
"""

from pprint import pprint

import requests
from bs4 import BeautifulSoup

URL = 'https://parsinger.ru/html/index3_page_1.html'
schema = 'https://parsinger.ru/html/'

response = requests.get(url=URL)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')
pagination_tags = soup.find(class_='pagen').find_all('a')
pagination_links = [link.get('href') for link in pagination_tags]
page_names_lists = []
for link in pagination_links:
    page_url = schema + link
    page_response = requests.get(url=page_url)
    page_response.encoding = 'utf-8'
    soup = BeautifulSoup(page_response.text, 'html.parser')
    name_tags = soup.find_all('a', class_='name_item')
    names = [tag.text for tag in name_tags]
    page_names_lists.append(names)

pprint(page_names_lists)
