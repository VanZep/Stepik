"""
Секретное хранилище корпорации “GraniteCore” заперто сложным замком. Ключ
разбит на фрагменты и спрятан за щитами, распознающими точные пары browser+os.
Всего у вас на руках 17 юзер агентов — одни открывают ячейки с частью кода,
другие безжалостно отвечают 403 Forbidden.

Не все браузеры работают на всех ОС (например, Safari в основном доступен
только на Mac OS X, не путать с "Mobile Safari").

browser_os_combinations = [
    {"browser": ["Chrome"], "os": "Windows"},
    {"browser": ["Chrome"], "os": "Mac OS X"},
    {"browser": ["Chrome"], "os": "Linux"},
    {"browser": ["Chrome"], "os": "Android"},
    {"browser": ["Firefox"], "os": "Windows"},
    {"browser": ["Firefox"], "os": "Mac OS X"},
    {"browser": ["Firefox"], "os": "Linux"},
    {"browser": ["Firefox"], "os": "Android"},
    {"browser": ["Safari"], "os": "Mac OS X"},
    {"browser": ["Edge"], "os": "Windows"},
    {"browser": ["Opera"], "os": "Windows"},
    {"browser": ["Opera"], "os": "Mac OS X"},
    {"browser": ["Opera"], "os": "Linux"},
    {"browser": ["Opera"], "os": "Android"},
    {"browser": ["Mobile Safari"], "os": "iOS"},
    {"browser": ["Opera"], "os": "iOS"},
    {"browser": ["Chrome"], "os": "iOS"},
]

Твоя задача: проверить каждую комбинацию из списка, найти все рабочие варианты
и сложить полученные числовые части пароля для получения итогового значения.

Проверить все комбинации из списка отправив GET запрос на API.
Собрать числовые части пароля из поля  "part_of_password".
Суммировать все части для получения итогового пароля.
Вставить итоговый пароль в поле на Stepik.
Пример возвращаемого ответа:
{
    "browser":"***",
    "os":"***",
    "success":true,
    "message":"Поздравляем! Вы успешно обошли блокировку, используя комбинацию *** на ***.",
    "part_of_password":****
}
"""

import requests
from fake_useragent import UserAgent

URL = 'http://31.130.149.237/right_combination/check'
browser_os_combinations = [
    {'browser': ['Chrome'], 'os': 'Windows'},
    {'browser': ['Chrome'], 'os': 'Mac OS X'},
    {'browser': ['Chrome'], 'os': 'Linux'},
    {'browser': ['Chrome'], 'os': 'Android'},
    {'browser': ['Firefox'], 'os': 'Windows'},
    {'browser': ['Firefox'], 'os': 'Mac OS X'},
    {'browser': ['Firefox'], 'os': 'Linux'},
    {'browser': ['Firefox'], 'os': 'Android'},
    {'browser': ['Safari'], 'os': 'Mac OS X'},
    {'browser': ['Edge'], 'os': 'Windows'},
    {'browser': ['Opera'], 'os': 'Windows'},
    {'browser': ['Opera'], 'os': 'Mac OS X'},
    {'browser': ['Opera'], 'os': 'Linux'},
    {'browser': ['Opera'], 'os': 'Android'},
    {'browser': ['Mobile Safari'], 'os': 'iOS'},
    {'browser': ['Opera'], 'os': 'iOS'},
    {'browser': ['Chrome'], 'os': 'iOS'},
]
password = 0

for combination in browser_os_combinations:
    user_agent = UserAgent(
        os=combination['os'], browsers=combination['browser']
    )
    response = requests.get(URL, headers={'User-Agent': user_agent.random})
    if response.ok:
        password += response.json()['part_of_password']

print(password)
