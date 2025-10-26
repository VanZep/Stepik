"""
Создайте модель Movie для каталога фильмов с именем таблицы movies. Добавьте
все необходимые импорты и определите базовый класс Base.

Поля модели:
id — уникальный идентификатор фильма (целое число, первичный ключ)
title — название фильма (строка, максимум 200 символов, не null)
duration — длительность фильма в минутах (целое число, не null)
release_date — дата выхода фильма (дата, nullable)
"""

from datetime import date

from sqlalchemy import Integer, String, Date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Movie(Base):
    __tablename__ = 'movies'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )
    duration: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )
    release_date: Mapped[date | None] = mapped_column(Date)
