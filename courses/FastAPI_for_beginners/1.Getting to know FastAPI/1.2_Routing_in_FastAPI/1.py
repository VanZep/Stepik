"""
Напишите код приложения на FastAPI, в котором асинхронная функция
detail_view() будет принимать GET-запрос по маршруту /product/<product_id>,
получая числовой параметр product_id из параметра пути.

Конечная точка должна возвращать словарь с ключом product и строковым
значением Stock number <product_id>.

P.S. На экран ничего не нужно выводить, пример запроса:
/product/15

ответ для него:
{'product': 'Stock number 15'}
"""

from fastapi import FastAPI

app = FastAPI()


@app.get('/product/{product_id}')
async def detail_view(product_id):
    return {'product': f'Stock number {product_id}'}
