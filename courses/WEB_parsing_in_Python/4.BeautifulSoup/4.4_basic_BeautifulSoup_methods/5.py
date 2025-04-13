"""
Ваша задача заключается в поиске тега который содержит сразу все перечисленные
ниже атрибуты и значения.

class="description_detail class1 class2 class3"
data-fdg45="value13"
data-54dfg60="value14"
data-d6f50hg="value15"

После того как тег будет найден, извлеките из него текст.
Ссылка на страницу с необходимым HTML.
"""

import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/4.1/1/index2.html')
response.encoding = 'utf-8'
html = response.text


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    tag = soup.find(
        class_='description_detail class1 class2 class3',
        attrs={
            'data-fdg45': 'value13',
            'data-54dfg60': 'value14',
            'data-d6f50hg': 'value15'
        }
    )
    print(tag.text)


get_html(html)
