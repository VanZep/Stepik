"""
Напишите код приложения на FastAPI, в котором:

Асинхронная функция users() будет принимать GET-запрос по маршруту
/users/<name>, получая строковой параметр name  и выводя словарь с ключом
user_name и значением параметра name.
Асинхронная функция admin() будет принимать GET-запрос по маршруту
/users/admin, и будет выводить словарь с ключом message и строковым значением
Hello admin.

P.S. На экран ничего не нужно выводить, первый пример запроса:
/users/Alex

ответ для него:
{'user_name': 'Alex'}

Второй пример запроса:
/users/admin

ответ для него:
{'message': 'Hello admin'}

Внимание: важно чтобы запрос /users/admin обрабатывала функция admin(),
а не функция users()
"""

from fastapi import FastAPI

app = FastAPI()


@app.get('/users/admin')
async def admin() -> dict:
    return {'message': 'Hello admin'}


@app.get('/users/{name}')
async def users(name: str) -> dict:
    return {'user_name': name}
