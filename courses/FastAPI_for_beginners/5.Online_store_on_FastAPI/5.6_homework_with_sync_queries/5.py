"""
Используя синхронный запрос, найдите товар с минимальной ценой (поле price) из
таблицы модели Item.

Для выполнения запроса используйте сессию session, импортированную из модуля
db. Результат запроса сохраните в переменную result.

Код модели Item из файла models.py:
class Item(Base):

    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
"""

from db import session
from models import Item
from sqlalchemy import select, func

result = session.scalars(select(func.min(Item.price))).first()
