"""
Напишите код приложения на FastAPI, в котором асинхронная функция users()
будет принимать GET-запрос по маршруту /users, получая строковой параметр name,
и числовой параметр age из параметров запроса.

Конечная точка должна возвращать словарь с ключом user_name и значением
параметра name, и с ключом user_age и значением параметра age.

P.S. На экран ничего не нужно выводить, пример запроса:
/users?name=Max&age=39

ответ для него:
{'user_name': 'Max', 'user_age': 39}
"""

from fastapi import FastAPI

app = FastAPI()


@app.get('/users')
async def users(name: str, age: int) -> dict:
    return {'user_name': name, 'user_age': age}
