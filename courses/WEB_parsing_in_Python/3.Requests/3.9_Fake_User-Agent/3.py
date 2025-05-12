"""
Разведотдел «Ω-Net» взломал консоль управления корпорации "NexuSphere".
Главный пароль к их облачной сети фрагментирован и разбросан по
«узлам-зеркалам». Каждый узел раскрывает свой осколок только перед тем, кто
умеет идеально имитировать правдоподобную связку «браузер + операционная
система».

Не все браузеры работают на всех ОС (например, Safari в основном доступен
только на Mac OS X, не путать с "Mobile Safari").

Что нужно сделать:
Напишите скрипт, который отправит GET-запросы к API с User-Agent заголовками
разных комбинаций браузер + ОС.
Для каждой пары сгенерируйте агент browser=browser, os=os.
combinations = {
    "valid_combinations": [
        {
            "browser": "Chrome",
            "os": "Windows",
        },
        {
            "browser": "Chrome",
            "os": "Mac OS X",
        },
        {
            "browser": "Chrome",
            "os": "Linux",
        },
        {
            "browser": "Safari",
            "os": "Mac OS X",
        },
        {
            "browser": "Firefox",
            "os": "Windows",
        },
        {
            "browser": "Firefox",
            "os": "Linux",
        },
        {
            "browser": "Firefox",
            "os": "Mac OS X",
        },
        {
            "browser": "Edge",
            "os": "Windows",
        },
    ],
}
При каждой комбинации из списка сервер вернёт в ответ словарь.
{
"browser": "Chrome",
"os": "Windows",
"part_of_password": ****,
"is_valid": true
}
Неверных комбинаций в списке нет.
Итоговый пароль = сумма всех чисел из полей "part_of_password".
Введите полученный пароль в поле ответа на Stepik.
"""

import requests
from fake_useragent import UserAgent

URL = 'http://31.130.149.237/browser-compatibility/browser-os-check'
combinations = {
    'valid_combinations': [
        {'browser': 'Chrome', 'os': 'Windows'},
        {'browser': 'Chrome', 'os': 'Mac OS X'},
        {'browser': 'Chrome', 'os': 'Linux'},
        {'browser': 'Safari', 'os': 'Mac OS X'},
        {'browser': 'Firefox', 'os': 'Windows'},
        {'browser': 'Firefox', 'os': 'Linux'},
        {'browser': 'Firefox', 'os': 'Mac OS X'},
        {'browser': 'Edge', 'os': 'Windows'}
    ]
}
password = 0

for combination in combinations['valid_combinations']:
    user_agent = UserAgent(
        os=combination['os'], browsers=combination['browser']
    )
    part_of_password = requests.get(
        URL, headers={'User-Agent': user_agent.random}
    ).json()['part_of_password']
    password += part_of_password

print(password)
