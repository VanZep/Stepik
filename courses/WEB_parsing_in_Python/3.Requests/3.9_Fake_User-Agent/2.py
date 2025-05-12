"""
Секретная лаборатория корпорации "CipherCore" хранит мастер-пароль к
глобальной сети спутниковых ретрансляторов.

Пароль расщеплён на пять фрагментов и распределён по «серверам-маякам», каждый
из которых откликается только на запросы, замаскированные под конкретную
операционную систему.

Тайные аналитики «Ω-Net» выяснили, что вам понадобятся следующие
маски-оболочки:
os_list = ["Mac OS X", "Windows", "Android", "Linux", "iOS"]
Задача:

Целевой сайт.
Используйте библиотеку fake-useragent, создавая для каждой ОС новый экземпляр
UserAgent(os=...). Каждый двойник ― ваш поддельный браузер.
Для каждой ОС сервер вернет часть пароля в виде числа

Успешный отклик выглядит так:
#### Пример ответа при успешном определении ОС:
{
    "part_of_password": 123....
}

Когда получите все числа, найдите их сумму ⟶ это и будет целевой пароль.
Вставьте полученный секретный код в поле ниже на платформе Stepik.
"""

import requests
from fake_useragent import UserAgent

TARGET_URL = 'http://31.130.149.237/os-challenge/os'
os_list = ["Mac OS X", "Windows", "Android", "Linux", "iOS"]
password = 0

for os in os_list:
    user_agent = UserAgent(os=os)
    part_of_password = requests.get(
        TARGET_URL, headers={'User-Agent': user_agent.random}
    ).json()['part_of_password']
    password += part_of_password

print(password)
