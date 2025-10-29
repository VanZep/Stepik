"""
Создайте модели Author и Book для библиотеки. Добавьте все необходимые
импорты, определите базовый класс Base и настройте двусторонний доступ между
моделями с использованием back_populates.

Модель Author:
Имя таблицы — authors.
id — уникальный идентификатор автора (целое число, первичный ключ).
name — имя автора (строка, максимум 100 символов, не null).

Модель Book:
Имя таблицы — books.
id — уникальный идентификатор книги (целое число, первичный ключ).
title — название книги (строка, максимум 200 символов, не null).
author_id — внешний ключ на автора (целое число, не null).

Связь: Один автор (Author) может иметь много книг (Book), связь один-ко-многим
через author_id. Настройте двусторонний доступ с back_populates.
"""

from typing import List

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = 'authors'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    books: Mapped[List['Book']] = relationship(
        'Book',
        uselist=True,
        back_populates='author',
        cascade='all, delete-orphan'
    )


class Book(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )
    author_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('authors.id'),
        nullable=False
    )

    author: Mapped['Author'] = relationship(
        'Author',
        back_populates='books'
    )
