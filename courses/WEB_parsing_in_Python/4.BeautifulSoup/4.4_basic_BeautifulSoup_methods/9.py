"""
Проанализируйте HTML на странице и извлеките из него текст находящийся после
третьего раздела.
"""

import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/4.1/1/index6.html')
response.encoding = 'utf-8'
html = response.text


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    sibling = soup.select_one('#section3 .section-text').next_sibling

    return sibling.strip()


print(get_html(html))
