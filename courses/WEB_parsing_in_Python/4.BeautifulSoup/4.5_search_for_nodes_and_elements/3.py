"""
Открываем сайт
Получаем данные при помощи bs4 о старой цене и новой цене
По формуле высчитываем процент скидки
Формула (старая цена - новая цена) * 100 / старая цена)
Вставьте получившийся результат в поле ответа
Ответ должен быть числом с 1 знаком после запятой.
"""

import requests
from bs4 import BeautifulSoup

URL = 'https://parsinger.ru/html/hdd/4/4_1.html'

response = requests.get(url=URL)
response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'html.parser')
item = soup.find(class_='item_card')
old_price = float(item.select_one('#old_price').text.rstrip(' руб'))
price = float(item.select_one('#price').text.rstrip(' руб'))
discount = (old_price - price) * 100 / old_price

print(f'Процент скидки составляет: {discount:.1f}%')
