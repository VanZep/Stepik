"""
Используя синхронный запрос, получите названия всех книг из таблицы модели
Book с помощью select(), scalars() и метода all().

Для выполнения запроса используйте сессию session, импортированную из модуля
db. Результат запроса сохраните в переменную result.

Код модели Book из файла models.py:
class Book(Base):

    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    price = Column(Float)
"""

from db import session
from models import Book
from sqlalchemy import select

result = session.scalars(select(Book.title)).all()
