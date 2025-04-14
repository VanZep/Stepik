"""
Проанализируйте страницу и найдите способ извлечь все ID из каждого тега <li>
(используйте select() или find_all()).
"""

import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/4.1/1/index4.html')
response.encoding = 'utf-8'
html = response.text


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    tags_li = soup.select('li')
    for tag in tags_li:
        print(tag.get('id'))


get_html(html)
