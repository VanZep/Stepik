"""
Напишите код приложения на FastAPI, в котором асинхронная функция
detail_view() будет принимать GET-запрос по маршруту /product, получая
числовой параметр item_id из параметра запроса.

Конечная точка должна возвращать словарь с ключом product и строковым
значением Stock number <item_id>.

P.S. На экран ничего не нужно выводить, пример запроса:
/product?item_id=57

ответ для него:
{'product': 'Stock number 57'}
"""

from fastapi import FastAPI

app = FastAPI()


@app.get('/product')
async def detail_view(item_id: int) -> dict:
    return {'product': f'Stock number {item_id}'}
