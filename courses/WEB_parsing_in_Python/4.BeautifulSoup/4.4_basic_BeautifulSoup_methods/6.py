"""
Проанализируйте страницу, определите тег и его атрибуты, затем примените метод
.find_all(), извлеките из каждого соответствующего тега текст и уберите лишние
пробелы.



Ваша программа должна выводить список всех найденных на странице имен
следующим образом.

Видеокарта MSI Radeon RX 6650 XT MECH 2X OC PCI-E 8192Mb GDDR6 128 Bit Retail
Видеокарта GigaByte nVidia GeForce RTX 3050 WINDFORCE OC 8G PCI-E 8192Mb GDDR6 128 Bit Retail GV-N3050WF2OC-8GD
***
***
***
Видеокарта Palit nVidia GeForce RTX 3060 Dual OC PCI-E 12288Mb GDDR6 192 Bit Retail (NE63060T19K9-190AD)
Видеокарта Palit GeForce GTX 1650 GP PCI-E 4096Mb GDDR6 128 Bit Bulk (NE6165001BG1-1175A)
"""

import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/4.1/1/index4.html')
response.encoding = 'utf-8'
html = response.text


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup.find_all('a', class_=['name_item product_name'])
    for tag in tags:
        print(tag.text.strip())


get_html(html)
