"""
Используя асинхронный запрос, выберите все книги из таблицы модели Book, у
которых длина названия (title) меньше 10 символов.

Для выполнения запроса используйте асинхронную сессию async_session,
импортированную из модуля db. Результат запроса сохраните в переменную result.


Код модели Book из файла models.py:

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
"""

from db import async_session
from models import Book
from sqlalchemy import select, func

result = await async_session.scalars(
    select(
        Book
    ).where(
        func.length(Book.title) < 10
    )
)
result = result.all()
