"""
Создайте эндпоинт FastAPI для получения информации о заказе по его ID, если он
активен (is_active=True).

Используйте APIRouter для создания маршрута эндпоинта.

Эндпоинт должен принимать GET запрос по корневому маршруту роутера (/),
получая id заказа из параметра пути. Если заказ не найден или не активен,
верните ошибку с кодом 404.

Используйте зависимость get_db из модуля database,  для получения синхронной
сессии базы данных.

Используйте модель SQLAlchemy OrderModel из app.models.order

Для ответа используйте Pydantic модель OrderSchema из app.schemas.order.

Проверьте существование пользователя через модель UserModel из app.models.user,
если пользователь не найден или не активен, верните ошибку с кодом 404.


Код модели OrderModel:

from sqlalchemy import Column, Integer, Float, String, Boolean
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class OrderModel(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    total_amount = Column(Float)
    status = Column(String)
    is_active = Column(Boolean, default=True)



Код модели UserModel:

class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)



Код модели OrderSchema:

from pydantic import BaseModel


class OrderSchema(BaseModel):
    id: int
    user_id: int
    total_amount: float
    status: str
    is_active: bool

    class Config:
        from_attributes = True
"""

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy import select, and_
from sqlalchemy.orm import Session

from app.models.user import UserModel
from app.models.order import OrderModel
from app.schemas.order import OrderSchema
from database import get_db

router = APIRouter(prefix='/orders', tags=['orders'])


@router.get(
    '/{order_id}',
    response_model=OrderSchema,
    status_code=status.HTTP_200_OK
)
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.scalars(
        select(
            OrderModel
        ).where(
            and_(
                OrderModel.id == order_id,
                OrderModel.is_active == True
            )
        )
    ).first()
    if order is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Order not found or not active'
        )

    user = db.scalars(
        select(
            UserModel
        ).where(
            and_(
                UserModel.id == order.user_id,
                UserModel.is_active == True
            )
        )
    ).first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found or not active'
        )

    return order
