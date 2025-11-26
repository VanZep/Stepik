"""
Модернизируйте существующий эндпоинт /orders/ интернет-магазина, который
сейчас возвращает все заказы сразу. Требуется добавить пагинацию и подсчёт
общего количества, чтобы запрос:
GET /orders/?page=3&page_size=10

возвращал только 10 заказов со страницы 3 и мета-информацию о полном
количестве записей. Вернуть ответ необходимо в виде Pydantic модели OrderList,
которую вы тоже должны реализовать согласно данного условия задачи.

Требования к ответу (JSON):
{
  "items": [ ... ],
  "total": 145,
  "page": 3,
  "page_size": 10
}

items – список заказов текущей страницы (поля модели Order).
total – общее количество активных заказов (is_active == True).
page – номер запрошенной страницы (≥ 1).
page_size – количество элементов на странице (≥ 1, ≤ 100, по умолчанию 20).

Код модели OrderModel:
class _OrderModel(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    total_price = Column(Float)
    status = Column(String)
    is_active = Column(Boolean, default=True, index=True)


Исходный код (без пагинации):

# app/schemas.py
class Order(BaseModel):
    id: int
    user_id: int
    total_price: float
    status: str
    is_active: bool = True

    model_config = ConfigDict(from_attributes=True)


# app/routers/orders.py
from fastapi import APIRouter, Depends
from sqlalchemy import select
from app.db import AsyncSession, get_async_db
from app.models import Order as OrderModel
from app.schemas import Order as OrderSchema

router = APIRouter(prefix="/orders", tags=["orders"])


@router.get("/", response_model=list[OrderSchema])
async def get_all_orders(db: AsyncSession = Depends(get_async_db)):
    stmt = select(OrderModel).where(OrderModel.is_active == True)
    result = await db.scalars(stmt)
    orders = result.all()
    return orders
"""

# app/schemas.py
from pydantic import BaseModel, Field, ConfigDict
from typing import List


class Order(BaseModel):
    id: int
    user_id: int
    total_price: float
    status: str
    is_active: bool = True

    model_config = ConfigDict(from_attributes=True)


# Напишите в этот блок Pydantic модель OrderList в нужном для вывода формате.
class OrderList(BaseModel):
    items: List[Order] = Field(
        ...,
        description='Заказы для текущей страницы'
    )
    total: int = Field(
        ...,
        ge=0,
        description='Общее количество заказов'
    )
    page: int = Field(
        ...,
        gt=0,
        description='Номер текущей страницы'
    )
    page_size: int = Field(
        ...,
        gt=0,
        description='Количество элементов на странице'
    )


# app/routers/orders.py
# Модернизируйте в этом блоке эндпоинт /orders/, принимающий GET запросы с
# именем функции get_all_orders, добавив в него пагинацию.

from fastapi import APIRouter, Depends, status, Query
from sqlalchemy import select, func
from app.db import AsyncSession, get_async_db
from app.models import Order as OrderModel

router = APIRouter(prefix="/orders", tags=["orders"])


@router.get(
    "/",
    response_model=OrderList,
    status_code=status.HTTP_200_OK
)
async def get_all_orders(
        db: AsyncSession = Depends(get_async_db),
        page: int = Query(1, gt=0),
        page_size: int = Query(20, gt=0, le=100)
):
    total = await db.scalar(
        select(
            func.count()
        ).select_from(
            OrderModel
        ).where(
            OrderModel.is_active == True
        )
    ) or 0

    orders = await db.scalars(
        select(
            OrderModel
        ).where(
            OrderModel.is_active == True
        ).order_by(
            OrderModel.id.asc()
        ).offset(
            (page - 1) * page_size
        ).limit(
            page_size
        )
    )

    return {
        'items': orders.all(),
        'total': total,
        'page': page,
        'page_size': page_size
    }
