"""
Создайте эндпоинт FastAPI для получения информации о сообщении по его ID из
таблицы messages, если оно активно (is_active=True). Если сообщения нет или
оно не активно (is_active=False), верните код ответа 404 с соответствующим
текстом.

Используйте APIRouter для создания маршрута эндпоинта.

Эндпоинт должен принимать GET-запрос по маршруту /{message_id}.

Используйте зависимость get_async_db из модуля database для получения
асинхронной сессии базы данных.

Используйте модель SQLAlchemy MessageModel из модуля app.models.message.

Используйте для ответа Pydantic-модель MessageSchema из модуля
app.schemas.message и верните полученный объект.


Код модели MessageModel:

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class MessageModel(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    sender_id = Column(Integer, index=True)
    is_active = Column(Boolean, default=True)



Код модели MessageSchema:

from pydantic import BaseModel


class MessageSchema(BaseModel):
    id: int
    content: str
    sender_id: int
    is_active: bool

    class Config:
        from_attributes = True
"""

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.message import MessageModel
from app.schemas.message import MessageSchema
from database import get_async_db

router = APIRouter(prefix='/messages', tags=['messages'])


@router.get(
    '/message_id',
    response_model=MessageSchema,
    status_code=status.HTTP_200_OK
)
async def get_message(
        message_id: int,
        db: AsyncSession = Depends(get_async_db)
):
    message = await db.scalars(
        select(
            MessageModel
        ).where(
            and_(
                MessageModel.id == message_id,
                MessageModel.is_active == True
            )
        )
    )
    message = message.first()
    if message is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Message not found or not active'
        )

    return message
