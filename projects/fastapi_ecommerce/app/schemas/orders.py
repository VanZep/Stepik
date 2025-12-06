from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field

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
        description='Цена за единицу на момент покупки'
    )
    total_price: Decimal = Field(
        ...,
        ge=0,
        description='Сумма по позиции'
    )
    product: Optional[Product] = Field(
        None,
        description='Полная информация о товаре'
    )
