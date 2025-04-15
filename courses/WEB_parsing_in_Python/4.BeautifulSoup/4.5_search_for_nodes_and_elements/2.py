"""
Открываем страницу сайта.
Извлекаем при помощи bs4 данные о стоимости часов (всего 8 шт).
Складываем все полученные числа.
Вставляем результат в поле ответа.
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://parsinger.ru/html/index1_page_1.html'

response = requests.get(url=URL)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')
prices = soup.find_all(class_='price')
total_price = sum(int(price.text.rstrip(' руб')) for price in prices)

print(total_price)
