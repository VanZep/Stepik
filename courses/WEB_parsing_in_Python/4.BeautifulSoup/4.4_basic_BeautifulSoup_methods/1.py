"""
Задача:
Ваша задача — найти тег, который имеет имя и значение атрибута
data-gpu="nVidia GeForce RTX 4060".
Извлеките текст из тега после его нахождения.
Ссылка на страницу c HTML.
"""

import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/4.1/1/index3.html')
response.encoding = 'utf-8'
html = response.text


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup.find(attrs={'data-gpu': 'nVidia GeForce RTX 4060'})
    print(tag.text)


get_html(html)
