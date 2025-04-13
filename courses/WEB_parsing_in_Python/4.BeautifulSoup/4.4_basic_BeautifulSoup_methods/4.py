"""
Проанализируйте страницу и найдите там тег с двойным классом
description detailz
Ваша задача — найти способ извлечь текст из этого тега.
"""

import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/4.1/1/index.html')
response.encoding = 'utf-8'
html = response.text


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    li_tag = soup.find(class_='description detailz')
    print(li_tag.text)


get_html(html)
