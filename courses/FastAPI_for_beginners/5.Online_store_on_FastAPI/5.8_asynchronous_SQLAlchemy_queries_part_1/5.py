"""
Используя асинхронный запрос, выберите все события из таблицы модели Event, у
которых дата (event_date) позже 2025-01-01.

Для выполнения запроса используйте асинхронную сессию async_session,
импортированную из модуля db. Результат запроса сохраните в переменную result.


Код модели Event из файла models.py:

from sqlalchemy import Column, Integer, Date
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    event_date = Column(Date)
"""

from datetime import date

from db import async_session
from models import Event
from sqlalchemy import select

result = await async_session.scalars(
    select(
        Event
    ).where(
        Event.event_date > date(2025, 1, 1)
    )
)
result = result.all()
