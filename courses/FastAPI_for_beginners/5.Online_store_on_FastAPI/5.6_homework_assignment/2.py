"""
Используя синхронный запрос, найдите первого пользователя из таблицы модели
User, зарегистрированного до 1 января 2023 года
(поле signup_date < '2023-01-01').

Для выполнения запроса используйте сессию session, импортированную из модуля
db. Результат запроса сохраните в переменную result.

Код модели User из файла models.py:
class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    signup_date = Column(DateTime)
"""

from db import session
from models import User
from sqlalchemy import select

result = session.scalars(
    select(
        User
    ).where(
        User.signup_date < '2023-01-01'
    )
).first()
