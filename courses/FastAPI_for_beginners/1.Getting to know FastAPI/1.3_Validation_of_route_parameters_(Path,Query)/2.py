"""
Напишите код приложения на FastAPI, в котором асинхронная функция category()
будет принимать GET-запрос по маршруту /category/<category_id>/products,
получая числовой параметр пути category_id и числовой параметр запроса page.

Для параметра category_id используется валидатор Path со следующими
параметрами:
Значение должно быть больше 0
Описание поля Category ID

Для параметра page валидатор не нужен.

Конечная точка должна возвращать словарь с ключом 'category_id' и значением
параметра category_id, и ключом 'page' и значением параметра page.

P.S. На экран ничего не нужно выводить, пример запроса:
/category/3/products?page=7

ответ для него:
{'category_id': 3, 'page': 7}
"""

from typing import Annotated

from fastapi import FastAPI, Path

app = FastAPI()


@app.get('/category/{category_id}/products')
async def category(
        category_id: Annotated[int, Path(gt=0, description='Category ID')],
        page: int
) -> dict:
    return {'category_id': category_id, 'page': page}
