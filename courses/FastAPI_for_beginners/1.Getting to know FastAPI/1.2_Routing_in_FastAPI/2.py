"""
Напишите код приложения на FastAPI, в котором асинхронная функция users()
будет принимать GET-запрос по маршруту /users/<name>/<age>, получая
строковой параметр name и числовой параметр age из параметров пути.

Конечная точка должна возвращать словарь с ключом user_name и значением
параметра name, и ключом user_age и значением параметра age.

P.S. На экран ничего не нужно выводить, пример запроса:
/users/Alex/34

ответ для него:
{'user_name': 'Alex', 'user_age': 34}
"""

from fastapi import FastAPI

app = FastAPI()


@app.get('/users/{name}/{age}')
async def users(name: str, age: int) -> dict:
    return {'user_name': name, 'user_age': age}
