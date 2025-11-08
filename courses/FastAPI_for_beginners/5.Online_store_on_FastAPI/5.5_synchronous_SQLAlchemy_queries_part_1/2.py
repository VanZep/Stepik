"""
Используя синхронный запрос, найдите первого клиента из таблицы модели
Customer, отсортированного по полю registered_at в порядке убывания. Для этого
примените select(), order_by() и метод first().

Для выполнения запроса используйте сессию session, импортированную из модуля
db. Результат запроса сохраните в переменную result.

Код модели Customer из файла models.py:
class Customer(Base):

    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    registered_at = Column(DateTime)
"""

from db import session
from models import Customer
from sqlalchemy import select

result = session.scalars(
    select(
        Customer
    ).order_by(
        Customer.registered_at.desc()
    )
).first()
