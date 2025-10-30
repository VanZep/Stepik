"""
Создайте модели Customer и Order для системы заказов. Добавьте все необходимые
импорты, определите базовый класс Base и настройте двусторонний доступ между
моделями с использованием back_populates.

Модель Customer:
Имя таблицы — customers.
id — уникальный идентификатор клиента (целое число, первичный ключ).
name — имя клиента (строка, максимум 100 символов, не null).
email — электронная почта (строка, максимум 120 символов, уникальная, не null).

Модель Order:
Имя таблицы — orders.
id — уникальный идентификатор заказа (целое число, первичный ключ).
order_number — номер заказа (строка, максимум 20 символов, уникальная,
не null).
total_amount — сумма заказа (десятичное число, максимум 10 цифр, 2 после
запятой, не null).
customer_id — внешний ключ на клиента (целое число, не null).

Связь: Один клиент (Customer) может иметь много заказов (Order), связь
один-ко-многим через customer_id. Настройте двусторонний доступ с
back_populates.
"""
from typing import List
from decimal import Decimal

from sqlalchemy import Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Customer(Base):
    __tablename__ = 'customers'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
        unique=True
    )

    orders: Mapped[List['Order']] = relationship(
        'Order',
        uselist=True,
        back_populates='customer',
        cascade='all, delete-orphan'
    )


class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    order_number: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        unique=True
    )
    total_amount: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )
    customer_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('customers.id'),
        nullable=False
    )

    customer: Mapped['Customer'] = relationship(
        'Customer',
        back_populates='orders'
    )
