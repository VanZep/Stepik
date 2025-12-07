from decimal import Decimal
from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel, Field, ConfigDict

from app.schemas.products import Product


class OrderItem(BaseModel):
    """
    Модель позиции в заказе.
    """

    id: int = Field(
        ...,
        description='Уникальный идентификатор позиции в заказе'
    )
    product_id: int = Field(
        ...,
        description='Уникальный идентификатор товара в заказе'
    )
    quantity: int = Field(
        ...,
        gt=0,
        description='Количество'
    )
    unit_price: Decimal = Field(
        ...,
        ge=0,
        description='Цена за единицу на момент покупки',
        decimal_places=2
    )
    total_price: Decimal = Field(
        ...,
        ge=0,
        description='Сумма по позиции',
        decimal_places=2
    )
    product: Optional[Product] = Field(
        None,
        description='Полная информация о товаре'
    )

    model_config = ConfigDict(from_attributes=True)


class Order(BaseModel):
    """
    Модель заказа.
    """

    id: int = Field(
        ...,
        description='Уникальный идентификатор заказа'
    )
    user_id: int = Field(
        ...,
        description='Уникальный идентификатор пользователя'
    )
    status: str = Field(
        ...,
        description='Текущий статус заказа'
    )
    total_amount: Decimal = Field(
        ...,
        ge=0,
        description='Общая стоимость заказа',
        decimal_places=2
    )
    created_at: datetime = Field(
        ...,
        description='Когда заказ был создан'
    )
    updated_at: datetime = Field(
        ...,
        description='Когда заказ последний раз обновлялся'
    )
    items: List[OrderItem] = Field(
        default_factory=List,
        description='Список позиций заказа'
    )

    model_config = ConfigDict(from_attributes=True)


class OrderList(BaseModel):
    """
    Модель списка заказов с пагинацией.
    """

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
        ge=1,
        description='Номер текущей страницы'
    )
    page_size: int = Field(
        ...,
        ge=1,
        description='Количество элементов на странице'
    )

    model_config = ConfigDict(from_attributes=True)
