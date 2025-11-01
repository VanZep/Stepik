"""
Создайте модели Post и Comment для блога. Добавьте все необходимые импорты,
определите базовый класс Base и настройте двусторонний доступ между моделями с
использованием back_populates.

Модель Post:
Имя таблицы — posts.
id — уникальный идентификатор поста (целое число, первичный ключ).
title — заголовок поста (строка, максимум 200 символов, не null).
content — содержимое поста (текст, не null).
created_at — дата создания (дата и время, не null, по умолчанию текущая дата).

Модель Comment:
Имя таблицы — comments.
id — уникальный идентификатор комментария (целое число, первичный ключ).
content — текст комментария (текст, не null).
created_at — дата создания комментария (дата и время, не null, по умолчанию
текущая дата).
post_id — внешний ключ на пост (целое число, не null).

Связь: Один пост (Post) может иметь много комментариев (Comment), связь
один-ко-многим через post_id. Настройте двусторонний доступ с back_populates.
"""

from typing import List
from datetime import datetime

from sqlalchemy import Integer, String, Text, DateTime, func, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Post(Base):
    __tablename__ = 'posts'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )
    content: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=func.now
    )

    comments: Mapped[List['Comment']] = relationship(
        'Comment',
        uselist=True,
        back_populates='post',
        cascade='all, delete-orphan',
        single_parent=True
    )


class Comment(Base):
    __tablename__ = 'comments'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    content: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=func.now
    )
    post_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('posts.id'),
        nullable=False
    )

    post: Mapped['Post'] = relationship(
        'Post',
        back_populates='comments'
    )
