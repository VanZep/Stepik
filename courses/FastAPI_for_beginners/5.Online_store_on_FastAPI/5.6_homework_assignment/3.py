"""
Используя синхронный запрос, выберите все транзакции клиента с client_id = 1
из таблицы модели Transaction.

Для выполнения запроса используйте сессию session, импортированную из модуля
db. Результат запроса сохраните в переменную result.

Код модели Transaction из файла models.py:
class Transaction(Base):

    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer)
    amount = Column(Float)
"""

from db import session
from models import Transaction
from sqlalchemy import select

result = session.scalars(
    select(
        Transaction
    ).where(
        Transaction.client_id == 1
    )
).all()
