"""
Используя синхронный запрос, выберите все товары из таблицы модели Product,
у которых значение поля price больше 50. Примените select(), where() и метод
all().

Для выполнения запроса используйте сессию session, импортированную из модуля
db. Результат запроса сохраните в переменную result.

Код модели Product из файла models.py:
class Product(Base):

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
"""

from db import session
from models import Product
from sqlalchemy import select

result = session.scalars(select(Product).where(Product.price > 50)).all()
