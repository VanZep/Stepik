"""
Создайте модель Task для списка задач с именем таблицы tasks. Добавьте все
необходимые импорты и определите базовый класс Base.

Поля модели:
id — уникальный идентификатор задачи (целое число, первичный ключ)
title — название задачи (строка, максимум 100 символов, не null)
is_completed — статус завершения (булево, не null, по умолчанию False)
"""

from sqlalchemy import String, Boolean, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Task(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    title: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    is_completed: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False
    )
