"""
Создайте модели Article и Tag для блога с тегами. Добавьте все необходимые
импорты, определите базовый класс Base и настройте двусторонний доступ между
моделями с использованием back_populates.

Модель Article:
Имя таблицы — articles.
id — уникальный идентификатор статьи (целое число, первичный ключ).
title — заголовок статьи (строка, максимум 200 символов, не null).
content — содержимое статьи (текст, не null).

Модель Tag:
Имя таблицы — tags.
id — уникальный идентификатор тега (целое число, первичный ключ).
name — название тега (строка, максимум 50 символов, уникальная, не null).

Связь: Одна статья (Article) может иметь много тегов (Tag), и один тег может
быть связан с множеством статей, связь многие-ко-многим через промежуточную
таблицу article_tags. Настройте двусторонний доступ с back_populates.
"""

from typing import List

from sqlalchemy import Integer, String, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Article(Base):
    __tablename__ = 'articles'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True,
        index=True
    )
    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )
    content: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    tags: Mapped[List['Tag']] = relationship(
        'Tag',
        uselist=True,
        secondary='article_tags',
        back_populates='articles'
    )
    article_tags: Mapped[List['ArticleTag']] = relationship(
        'ArticleTag',
        uselist=True,
        back_populates='article',
        single_parent=True,
        cascade='all, delete-orphan'
    )


class Tag(Base):
    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True,
        index=True
    )
    name: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        unique=True
    )

    articles: Mapped[List['Article']] = relationship(
        'Article',
        uselist=True,
        secondary='article_tags',
        back_populates='tags'
    )
    article_tags: Mapped[List['ArticleTag']] = relationship(
        'ArticleTag',
        uselist=True,
        back_populates='tag',
        single_parent=True,
        cascade='all, delete-orphan'
    )


class ArticleTag(Base):
    __tablename__ = 'article_tags'

    article_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('articles.id'),
        primary_key=True,
        index=True
    )
    tag_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('tags.id'),
        primary_key=True,
        index=True
    )

    article: Mapped['Article'] = relationship(
        'Article',
        back_populates='article_tags'
    )
    tag: Mapped['Tag'] = relationship(
        'Tag',
        back_populates='article_tags'
    )
