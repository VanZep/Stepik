"""
Создайте модель Product для интернет-магазина с именем таблицы products.
Добавьте все необходимые импорты и определите базовый класс Base.

Поля модели:
id — уникальный идентификатор продукта (целое число, первичный ключ)
name — название продукта (строка, максимум 150 символов, не null)
price — цена продукта (десятичное число, максимум 10 цифр, 2 после запятой,
не null)
stock_quantity — количество на складе (целое число, не null, по умолчанию 0)
"""

from decimal import Decimal

from sqlalchemy import Integer, String, Numeric
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )
    price: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )
    stock_quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0
    )
