"""
Используя асинхронный запрос, выберите всех пользователей из таблицы модели
User, у которых имя (name) начинается с буквы "J".

Для выполнения запроса используйте асинхронную сессию async_session,
импортированную из модуля db. Результат запроса сохраните в переменную result.


Код модели User из файла models.py:

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
"""

from db import async_session
from models import User
from sqlalchemy import select

result = await async_session.scalars(
    select(
        User
    ).where(
        User.name.startswith('J')
    )
)
result = result.all()
