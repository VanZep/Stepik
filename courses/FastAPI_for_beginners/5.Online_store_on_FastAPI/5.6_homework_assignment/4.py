"""
Используя синхронный запрос, выберите все категории из таблицы модели Category,
у которых название (поле name) начинается с буквы A(англ. буква).

Для выполнения запроса используйте сессию session, импортированную из модуля
db. Результат запроса сохраните в переменную result.


Код модели Category из файла models.py:
class Category(Base):

    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String)
"""

from db import session
from models import Category
from sqlalchemy import select

result = session.scalars(
    select(
        Category
    ).where(
        Category.name.startswith('A')
    )
).all()

result = session.scalars(
    select(
        Category
    ).where(
        Category.name.like('A%')
    )
).all()
