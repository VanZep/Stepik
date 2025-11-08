"""
Используя синхронный запрос, выберите email всех подписчиков из таблицы модели
Subscriber, у которых поле status равно 'active'.

Для выполнения запроса используйте сессию session, импортированную из модуля
db. Результат запроса сохраните в переменную result.


Код модели Subscriber из файла models.py:
class Subscriber(Base):

    __tablename__ = 'subscribers'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    status = Column(String)
"""

from db import session
from models import Subscriber
from sqlalchemy import select

result = session.scalars(
    select(
        Subscriber.email
    ).where(
        Subscriber.status == 'active'
    )
).all()
