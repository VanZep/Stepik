"""
Проанализируйте предоставленный HTML-код страницы. Ваша задача - обнаружить и
извлечь все email-адреса, которые находятся вне стандартных тегов.

Вам предстоит модифицировать функцию ниже таким образом, чтобы она возвращала
список всех найденных email-адресов, очищенных от лишних пробелов с помощью
метода strip().

Ваша функция должна возвращать список email-адресов в чистом виде, готовых к
дальнейшему использованию.
Пример:
['keep2036@duck.com', 'andrea1837@example.org', и т.д.,]
"""

import requests
from bs4 import BeautifulSoup

response = requests.get('https://parsinger.ru/4.1/1/index5.html')
response.encoding = 'utf-8'
html = response.text


def get_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    emails = [
        tag.next_sibling.strip() for tag in
        soup.select('div.email_field > strong')
    ]

    return emails


print(get_html(html))
