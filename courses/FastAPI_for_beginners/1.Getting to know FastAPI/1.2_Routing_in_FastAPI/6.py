"""
Напишите код приложения на FastAPI, в котором асинхронная функция users()
будет принимать GET-запрос по маршруту /users, получая строковой параметр name,
и числовой параметр age из параметров запроса.

Конечная точка должна возвращать словарь с ключом user_name и значением
параметра name, и с ключом user_age и значением параметра age.

Если параметр name не передан, то его значение должно быть 'Undefined'.
Если параметр age не передан, то его значение должно быть 18.

P.S. На экран ничего не нужно выводить, первый пример запроса:
/users?name=Pavel&age=25

ответ для него:
{'user_name': 'Pavel', 'user_age': 25}

Второй пример запроса:
/users?name=Pavel

ответ для него:
{'user_name': 'Pavel', 'user_age': 18}

Третий пример запроса:
/users

ответ для него:
{'user_name': 'Undefined', 'user_age': 18}
"""

from fastapi import FastAPI

app = FastAPI()


@app.get('/users')
async def users(name: str = 'Undefined', age: int = 18) -> dict:
    return {'user_name': name, 'user_age': age}
