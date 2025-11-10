"""
Используя асинхронный запрос, выберите все категории из таблицы модели
Category, у которых название (name) заканчивается на "ing".

Для выполнения запроса используйте асинхронную сессию async_session,
импортированную из модуля db. Результат запроса сохраните в переменную result.


Код модели Category из файла models.py:

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)
"""

from db import async_session
from models import Category
from sqlalchemy import select

result = await async_session.scalars(
    select(
        Category
    ).where(
        Category.name.endswith('ing')
    )
)
result = result.all()
