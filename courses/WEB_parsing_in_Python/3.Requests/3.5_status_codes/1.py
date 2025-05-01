"""
Вашей задачей является написание кода, который будет выполнять сетевые запросы
к указанному диапазону веб-страниц и суммировать HTTP статус-коды всех
полученных ответов.
# От
https://parsinger.ru/3.3/2/1.html
# До
https://parsinger.ru/3.3/2/200.html
Примерно половина ссылок в этом диапазоне возвращает HTTP статус-код 200 (OK).
Оставшаяся половина возвращает HTTP статус-код 404 (Not Found).

Задание:
Сделайте HTTP запрос к каждой странице в указанном диапазоне.
Получите HTTP статус-код каждой страницы.
Суммируйте все полученные статус-коды.

Ожидаемый результат:
В качестве результата вы должны получить общую сумму всех HTTP статус-кодов,
полученных от всех страниц в указанном диапазоне.
"""

import time

import requests

PAGE_COUNT = 200
URL = 'https://parsinger.ru/3.3/2/'
status_codes_summ = 0
start_time = time.time()

with requests.Session() as session:
    for page_number in range(1, PAGE_COUNT + 1):
        try:
            status_codes_summ += session.get(
                url=f'{URL}{page_number}.html', timeout=0.1
            ).status_code
        except requests.Timeout:
            print(f'Слишком долгое ожидание страницы номер {page_number}')
        except requests.RequestException as e:
            print(f'Произошла ошибка: {e}')

print(f'Время - {time.time() - start_time}')
print(f'Сумма статус кодов - {status_codes_summ}')
