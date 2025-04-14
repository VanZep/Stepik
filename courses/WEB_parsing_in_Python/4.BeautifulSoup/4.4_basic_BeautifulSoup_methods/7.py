"""
Проанализируйте структуру сайта, найдите способ получить все цены с помощью
.find_all(), затем суммируйте их.
"""

import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/4.1/1/index4.html')
response.encoding = 'utf-8'
html = response.text


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    prices = soup.find_all('p', class_='price product_price')

    count = 0
    for price in prices:
        count += int(price.text.replace(' ', '').rstrip('руб'))

    return count


print(get_html(html))
