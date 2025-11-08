"""
Используя синхронный запрос, найдите заказ с наибольшей суммой (amount) из
таблицы модели Order. Примените select(), order_by() и метод first().

Для выполнения запроса используйте сессию session, импортированную из модуля
db. Результат запроса сохраните в переменную result.

Код модели Order из файла models.py:
class Order(Base):

    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    order_date = Column(DateTime)
"""

from db import session
from models import Order
from sqlalchemy import select, func

result = session.scalars(select(Order).order_by(Order.amount.desc())).first()
