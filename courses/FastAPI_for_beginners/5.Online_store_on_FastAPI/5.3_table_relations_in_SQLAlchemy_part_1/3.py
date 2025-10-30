"""
Создайте модели Category и Product для интернет-магазина. Добавьте все
необходимые импорты, определите базовый класс Base и настройте двусторонний
доступ между моделями с использованием back_populates.

Модель Category:
Имя таблицы — categories.
id — уникальный идентификатор категории (целое число, первичный ключ).
name — название категории (строка, максимум 50 символов, не null).

Модель Product:
Имя таблицы — products.
id — уникальный идентификатор продукта (целое число, первичный ключ).
name — название продукта (строка, максимум 150 символов, не null).
price — цена продукта (десятичное число, максимум 10 цифр, 2 после запятой,
не null).
category_id — внешний ключ на категорию (целое число, не null).

Связь: Одна категория (Category) может иметь много продуктов (Product), связь
один-ко-многим через category_id. Настройте двусторонний доступ с
back_populates.
"""

from typing import List
from decimal import Decimal

from sqlalchemy import Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    name: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    products: Mapped[List['Product']] = relationship(
        'Product',
        uselist=True,
        back_populates='category',
        cascade='all, delete-orphan'
    )


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
    category_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('categories.id'),
        nullable=False
    )

    category: Mapped['Category'] = relationship(
        'Category',
        back_populates='products'
    )
