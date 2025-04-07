"""
Задача:
Перейдите на сайт
Скачайте видео с сайта  при помощи requests
Определите его размер вручную
Напишите размер файла в поле для ответа. Написать нужно только число в
мегабайтах
"""

import requests

URL = 'https://parsinger.ru/video_downloads/videoplayback.mp4'
response = requests.get(url=URL, stream=True)

with open('file.mp4', 'wb') as video:
    video.write(response.content)
