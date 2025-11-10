"""
Используя асинхронный запрос, выберите все заказы из таблицы модели Order, у
которых количество (quantity) больше 5.

Для выполнения запроса используйте асинхронную сессию async_session,
импортированную из модуля db. Результат запроса сохраните в переменную result.


Код модели Order из файла models.py:

from sqlalchemy import Column, Integer
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    quantity = Column(Integer)
"""

from db import async_session
from models import Order
from sqlalchemy import select

result = await async_session.scalars(
    select(
        Order
    ).where(
        Order.quantity > 5
    )
)
result = result.all()
