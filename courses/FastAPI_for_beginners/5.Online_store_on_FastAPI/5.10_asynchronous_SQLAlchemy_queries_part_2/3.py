"""
Создайте эндпоинт FastAPI для создания нового тикета в таблице tickets, при
создании которого обязательно проверьте существование пользователя, в случае
если он не существует или он не активен (is_active == False), верните код
ответа 400 с соответствующим текстом.

Используйте APIRouter для создания маршрута эндпоинта.

Эндпоинт должен принимать POST-запрос по корневому маршруту роутера (/), и в
случае успешного добавления тикета, необходимо вернуть код ответа 201 с телом
ответа в виде созданного тикета.

Используйте зависимость get_async_db из модуля database для получения
асинхронной сессии базы данных.

Используйте модель SQLAlchemy TicketModel из модуля app.models.ticket и
UserModel из модуля app.models.user.

Используйте для входных данных Pydantic-модель TicketCreate из модуля
app.schemas.ticket.

Используйте для ответа Pydantic-модель  TicketSchema из модуля
app.schemas.ticket, и верните созданный объект.


Код модели TicketModel из модуля app.models.ticket:

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class TicketModel(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    user_id = Column(Integer, index=True)
    is_active = Column(Boolean, default=True)



Код модели UserModel из модуля app.models.user:

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)



Код моделей TicketCreate и TicketSchema из модуля app.schemas.ticket:

from pydantic import BaseModel


class TicketCreate(BaseModel):
    title: str
    description: str | None = None
    user_id: int


class TicketSchema(BaseModel):
    id: int
    title: str
    description: str | None
    user_id: int
    is_active: bool

    class Config:
        from_attributes = True
"""

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.ticket import TicketModel
from app.models.user import UserModel
from app.schemas.ticket import TicketSchema, TicketCreate
from database import get_async_db

router = APIRouter(prefix='/tickets', tags=['tickets'])


@router.post(
    '/',
    response_model=TicketSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_ticket(
        ticket: TicketCreate,
        db: AsyncSession = Depends(get_async_db)
):
    user = await db.scalars(
        select(
            UserModel
        ).where(
            and_(
                UserModel.id == ticket.user_id,
                UserModel.is_active == True
            )
        )
    )
    user = user.first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='User not found or not active'
        )

    ticket = TicketModel(**ticket.model_dump())
    db.add(ticket)
    await db.commit()
    await db.refresh(ticket)

    return ticket
