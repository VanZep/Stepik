"""
Используя асинхронный запрос, выберите все продукты из таблицы модели Product,
у которых цена (price) находится в диапазоне от 50 до 200
(включительно, 50 <= price <= 200).

Для выполнения запроса используйте асинхронную сессию async_session,
импортированную из модуля db. Результат запроса сохраните в переменную result.


Код модели Product из файла models.py:

from sqlalchemy import Column, Integer, Float
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    price = Column(Float)
"""

from db import async_session
from models import Product
from sqlalchemy import select

result = await async_session.scalars(
    select(
        Product
    ).where(
        Product.price.between(50, 200)
    )
)
result = result.all()
