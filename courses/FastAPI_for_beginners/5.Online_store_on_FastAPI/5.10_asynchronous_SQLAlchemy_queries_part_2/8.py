"""
Создайте эндпоинт FastAPI для получения информации о событии по его ID из
таблицы events, если оно активно (is_active=True), в ином случае верните код
ответа 404 с соответствующим сообщением.

Используйте APIRouter для создания маршрута эндпоинта.

Эндпоинт должен принимать GET-запрос по маршруту /{event_id}.

Используйте зависимость get_async_db из модуля database для получения
асинхронной сессии базы данных.

Используйте SQLAlchemy модель  EventModel из модуля app.models.event.

Используйте для ответа Pydantic-модель EventSchema из модуля app.schemas.event.


Код модели EventModel из модуля app.models.event:

from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class EventModel(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    date = Column(DateTime)
    location = Column(String)
    is_active = Column(Boolean, default=True)



Код модели EventSchema из модуля app.schemas.event:

from pydantic import BaseModel
from datetime import datetime


class EventSchema(BaseModel):
    id: int
    name: str
    date: datetime
    location: str
    is_active: bool

    class Config:
        from_attributes = True
"""

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.event import EventModel
from app.schemas.event import EventSchema
from database import get_async_db

router = APIRouter(prefix='/events', tags=['events'])


@router.get(
    '/{event_id}',
    response_model=EventSchema,
    status_code=status.HTTP_200_OK
)
async def get_event(
        event_id: int,
        db: AsyncSession = Depends(get_async_db)
):
    event = await db.scalars(
        select(
            EventModel
        ).where(
            and_(
                EventModel.id == event_id,
                EventModel.is_active == True
            )
        )
    )
    event = event.first()
    if event is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Event no found or not active'
        )

    return event
