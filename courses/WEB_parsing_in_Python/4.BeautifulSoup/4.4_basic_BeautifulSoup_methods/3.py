"""
Ваша задача — проанализировать страницу и понять как извлечь тег <img> целиком.
У тега <img> есть только родитель и название тега.
Найдите способ извлечь тег целиком.
"""

import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/4.1/1/index.html')
response.encoding = 'utf-8'
html = response.text


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    img = soup.find('img')
    print(img)


get_html(html)
