"""
Модернизируйте эндпоинт из прошлой задачи, который сейчас возвращает все
активные заказы с пагинацией.

Возьмите код эндпоинта get_all_orders из решения прошлой задачи и к имеющимся
параметрам запроса добавьте параметры для фильтрации:
status: str | None — фильтр по статусу заказа (например "paid", "canceled").
min_price — минимальная сумма заказа, число с плавающей точкой.
max_price — максимальная сумма заказа, число с плавающей точкой.

Требования к ответу (JSON):
{
  "items": [ ... ],
  "total": 145, // общее число записей, удовлетворяющих фильтрам (и is_active=True)
  "page": 3,
  "page_size": 10
}

Пример запроса:
GET /orders/?page=3&page_size=10&status=paid&min_price=1.5&max_price=150

Код модели OrderModel:
class OrderModel(Base):
    __tablename__ = "orders"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    user_id: Mapped[int] = mapped_column(Integer, index=True)
    total_price: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    status: Mapped[str] = mapped_column(String(20))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, index=True)
"""

from pydantic import BaseModel, Field, ConfigDict
from typing import List


class Order(BaseModel):
    id: int
    user_id: int
    total_price: float
    status: str
    is_active: bool = True

    model_config = ConfigDict(from_attributes=True)


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


from decimal import Decimal
from typing import Optional

from fastapi import APIRouter, Depends, status as st, Query, HTTPException
from sqlalchemy import select, func
from app.db import AsyncSession, get_async_db
from app.models import Order as OrderModel

router = APIRouter(prefix="/orders", tags=["orders"])


@router.get(
    "/",
    response_model=OrderList,
    status_code=st.HTTP_200_OK
)
async def get_all_orders(
        db: AsyncSession = Depends(get_async_db),
        page: int = Query(1, gt=0),
        page_size: int = Query(20, gt=0, le=100),
        status: Optional[str] = Query(
            None,
            pattern='^(paid|canceled)$',
            description='Статус заказа'
        ),
        min_price: Optional[Decimal] = Query(
            None,
            gt=0,
            description='Минимальная цена заказа'
        ),
        max_price: Optional[Decimal] = Query(
            None,
            gt=0,
            description='Максимальная цена заказа'
        )
):
    if min_price and max_price and min_price > max_price:
        raise HTTPException(
            status_code=st.HTTP_400_BAD_REQUEST,
            detail='min_price не может быть больше max_price'
        )

    filters = [OrderModel.is_active == True]

    if status is not None:
        filters.append(OrderModel.status == status)
    if min_price is not None:
        filters.append(OrderModel.total_price >= min_price)
    if max_price is not None:
        filters.append(OrderModel.total_price <= max_price)

    total = await db.scalar(
        select(
            func.count()
        ).select_from(
            OrderModel
        ).where(
            *filters
        )
    ) or 0

    orders = await db.scalars(
        select(
            OrderModel
        ).where(
            *filters
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
