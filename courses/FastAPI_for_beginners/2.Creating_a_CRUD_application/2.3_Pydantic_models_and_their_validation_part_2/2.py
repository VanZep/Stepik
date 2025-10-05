"""
Разработайте веб-приложение на фреймворке FastAPI, которое реализует эндпоинт
для создания нового пользователя с использованием Pydantic моделей для
валидации входных данных и формирования ответа. У вас есть глобальный
in-memory список users для хранения объектов. Эндпоинт должен принимать
данные пользователя, добавлять его в список users и возвращать созданную
модель в ответе.

Вам необходимо:
Определить Pydantic модель UserCreate с полями name: str, age: int
(с валидацией age >= 18) для валидации входных данных.

Определить Pydantic модель User с полями id: int (автоматически присваивается),
name: str, age: int (с валидацией age >= 18) для возврата созданного
пользователя.

Реализовать эндпоинт, который принимает POST запрос по пути /users. Он будет
принимать тело запроса в формате модели UserCreate, добавлять объект в список
users с присвоением id (например, длина списка + 1) и возвращать ответ в виде
модели User.
То есть ответ эндпоинта должен быть следующий: JSON с данными созданного
пользователя в формате модели User.

Убедитесь, что вы импортировали все необходимые библиотеки, чтобы избежать
ошибок при запуске приложения.
"""

from typing import Annotated

from fastapi import FastAPI, status, Body
from pydantic import BaseModel, Field

app = FastAPI()

users = []


class UserCreate(BaseModel):
    name: str
    age: Annotated[
        int,
        Field(..., gt=17)
    ]


class User(UserCreate):
    id: int


@app.post('/users', status_code=status.HTTP_201_CREATED, response_model=User)
async def create_user(user_create: UserCreate = Body(...)) -> User:
    new_id = max(user.id for user in users) + 1 if users else 1
    new_user = User(id=new_id, **user_create.model_dump())
    users.append(new_user)
    return new_user
