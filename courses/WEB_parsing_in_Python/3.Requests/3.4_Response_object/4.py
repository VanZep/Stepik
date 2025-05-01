"""
Вам предоставлен доступ к API, который возвращает данные в формате JSON.
Данные представляют собой древовидную структуру переписки между участниками.

Анализ данных:
Пройдитесь по древовидной структуре переписки.
Подсчитайте, сколько сообщений отправил каждый участник.
Участника необходимо определить по полю "username", поле  "user_id" не имеет
отношения к решению данной задачи.

Задача:
Написать скрипт на Python, который выполнит GET-запрос к данному API для
получения JSON-данных.
Преобразовать полученный JSON-ответ в Python-объект с использованием метода
response.json().
Проанализировать древовидную структуру переписки и подсчитать количество
сообщений, отправленных каждым участником.
Вставить полученный словарь в поле для ответа.

{
    'Anastasia': *, 'Vladimir': *, 'Yulia': *, 'Maria': *, 'Kirill': *,
    'Anton': *, 'Petr': *, 'Dmitry': *, 'Olga': *, 'Maxim': *, 'Elena': *,
    'Alex': *, 'Natalia': *, 'Tatiana': *, 'Svetlana': *, 'Andrey': *,
    'Sergey': *, 'Oksana': *, 'Ivan': *, 'Irina': *
}
Сортировка:
Необходимо упорядочить данный словарь сначала по убыванию числа сообщений.
То есть участник с наибольшим количеством сообщений должен идти первым,
а с наименьшим — последним.
В случае равенства числа сообщений между участниками, необходимо применить
дополнительный критерий сортировки. Этот критерий основан на лексикографическом
порядке имен участников. Лексикографическая сортировка схожа с алфавитной:
если, например, имена 'Алексей' и 'Анна' имеют одинаковое количество сообщений,
то 'Алексей' будет расположен перед 'Анной', так как лексикографически он идет
раньше. Таким образом, участники с одинаковым числом сообщений будут
упорядочены в словаре в зависимости от их имён, начиная с самого раннего и
заканчивая самым поздним.
"""

import requests

API_ENDPOINT = 'https://parsinger.ru/3.4/3/dialog.json'

try:
    response = requests.get(url=API_ENDPOINT)
    response.raise_for_status()
except (requests.exceptions.HTTPError, requests.RequestException) as err:
    print(f"Произошла ошибка: {err}")

chat = response.json()


def get_count_of_user_messages(chat):
    comments = chat['comments']
    for comment in comments:
        comments = comment['comments']
        if comments:
            get_count_of_user_messages(comment)
        username = comment['username']
        count_of_user_messages[username] = count_of_user_messages.get(
            username, 0
        ) + 1

    return count_of_user_messages


count_of_user_messages = {chat['username']: 1}
count_of_user_messages.update(get_count_of_user_messages(chat))
sorted_count_of_user_messages = dict(sorted(
    count_of_user_messages.items(),
    key=lambda x: (-x[1], x[0])
))
print(sorted_count_of_user_messages)
