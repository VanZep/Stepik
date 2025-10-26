"""
Создайте модель Event для календаря событий с именем таблицы events. Добавьте
все необходимые импорты и определите базовый класс Base.

Поля модели:
id — уникальный идентификатор события (целое число, первичный ключ)
title — название события (строка, максимум 100 символов, не null)
start_time — дата и время начала события (дата и время, не null)
end_time — дата и время окончания события (дата и время, nullable)
description — описание события (текст, nullable)
"""

from datetime import datetime

from sqlalchemy import Integer, String, DateTime, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Event(Base):
    __tablename__ = 'events'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    title: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    start_time: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )
    end_time: Mapped[datetime | None] = mapped_column(DateTime)
    description: Mapped[str | None] = mapped_column(Text)
