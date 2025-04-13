"""
Задача:
Допишите код ниже, чтобы найти необходимый тег из встроенного в степ HTML.
Найдите тег <li> который имеет имя атрибута data-key
и значение атрибута cooling_system.
Извлеките текст из тега.
Ссылка на страницу c HTML.
"""

import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/4.1/1/index.html')
response.encoding = 'utf-8'
html = response.text


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    li_tag = soup.find('li', {'data-key': 'cooling_system'})
    print(li_tag.text)


get_html(html)
