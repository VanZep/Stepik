"""
Создайте эндпоинт FastAPI для получения списка всех активных пользователей
(is_active=True) из таблицы users.

Используйте APIRouter для создания маршрута эндпоинта.

Эндпоинт должен принимать GET запрос по корневому маршруту роутера (/).

Используйте зависимость get_db из модуля database,  для получения синхронной
сессии базы данных.

Используйте модель SQLAlchemy UserModel из модуля app.models.user

Используйте для ответа Pydantic-модель UserSchema из модуля app.schemas.user.


Код модели UserModel:

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



Код модели UserSchema:

from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool

    class Config:
        from_attributes = True
"""

from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import UserModel
from app.schemas.user import UserSchema
from database import get_db

router = APIRouter(prefix='/users', tags=['users'])


@router.get(
    '/',
    response_model=List[UserSchema],
    status_code=status.HTTP_200_OK
)
def get_all_active_users(db: Session = Depends(get_db)):
    users = db.scalars(
        select(
            UserModel
        ).where(
            UserModel.is_active == True
        )
    ).all()

    return users
