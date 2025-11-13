"""
Создайте эндпоинт FastAPI для получения списка всех активных заказов
(is_active=True) из таблицы orders.

Используйте APIRouter для создания маршрута эндпоинта.

Эндпоинт должен принимать GET-запрос по корневому маршруту роутера (/).

Используйте зависимость get_async_db из модуля database для получения
асинхронной сессии базы данных.

Используйте SQLAlchemy модель OrderModel из модуля app.models.order.

Для ответа используйте для ответа Pydantic-модель OrderSchema из модуля
app.schemas.order, и верните список всех полученных объектов.


Код модели OrderModel из модуля app.models.order:

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



Код модели OrderSchema из модуля app.schemas.order:

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

from typing import List

from fastapi import APIRouter, status, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.order import OrderModel
from app.schemas.order import OrderSchema
from database import get_async_db

router = APIRouter(prefix='/orders', tags=['orders'])


@router.get(
    '/',
    response_model=List[OrderSchema],
    status_code=status.HTTP_200_OK
)
async def get_all_orders(db: AsyncSession = Depends(get_async_db)):
    orders = await db.scalars(
        select(
            OrderModel
        ).where(
            OrderModel.is_active == True
        )
    )

    return orders.all()
