"""
Напишите код приложения, в котором создайте экземпляр класса FastAPI и функцию
welcome(), которая будет будет принимать GET-запрос по маршруту /  и возвращать
словарь с ключом message и строковым значением My first project in FastAPI.
"""

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def welcome():
    return {'message': 'My first project in FastAPI'}
