"""
Цель данного задания — научиться работе с сетевыми запросами для скачивания
файлов.

Условия:
Перейдите на заданный сайт, где размещено 160 картинок.
На одной из картинок написан секретный код.
Код спрятан в углу картинки.

Задачи:
Напишите код, который скачает все 160 картинок с указанного сайта на ваш
локальный компьютер.

После скачивания, просмотрите картинки вручную и найдите на одной из них
секретный код.
"""

import requests

IMG_COUNTS = 160
URL = 'https://parsinger.ru/img_download/img/ready/'

with requests.Session() as session:
    for i in range(1, IMG_COUNTS + 1):
        url = f'{URL}{i}.png'
        try:
            response = session.get(url=url, timeout=0.1)
        except requests.exceptions.HTTPError as err:
            print(f"Произошла ошибка: {err}")
        except requests.Timeout:
            print(f'Слишком долгое ожидание! Изображение {i}.png')
        except requests.RequestException as e:
            print(f'Произошла ошибка: {e}')

        with open(f'images/img{i}.png', 'wb') as file:
            file.write(response.content)
