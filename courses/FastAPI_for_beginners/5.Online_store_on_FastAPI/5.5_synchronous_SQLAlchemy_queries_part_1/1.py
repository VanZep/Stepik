"""
Используя синхронный запрос, получите всех сотрудников из таблицы модели
Employee с помощью select() и метода all().

Для выполнения запроса используйте сессию session, импортированную из модуля
db. Результат запроса сохраните в переменную result.

Код модели Employee из файла models.py:
class Employee(Base):

    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department = Column(String)
"""

from db import session
from models import Employee
from sqlalchemy import select

result = session.scalars(select(Employee)).all()
