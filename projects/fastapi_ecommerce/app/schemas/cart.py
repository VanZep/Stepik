from typing import List
from decimal import Decimal

from pydantic import BaseModel, Field, ConfigDict

from .products import Product


class CartItem(BaseModel):
    """Товар в корзине с данными продукта."""

    id: int = Field(
        ...,
        description='ID позиции корзины'
    )
    quantity: int = Field(
        ...,
        gt=0,
        description='Количество товара'
    )
    product: Product = Field(
        ...,
        description='Информация о товаре'
    )

    model_config = ConfigDict(from_attributes=True)


class Cart(BaseModel):
    """ Модель для получения полной информации о корзине пользователя."""

    user_id: int = Field(
        ...,
        description='ID пользователя, обладающего корзиной'
    )
    items: List[CartItem] = Field(
        default_factory=List,
        description='Содержимое корзины'
    )
    total_quantity: int = Field(
        ...,
        ge=0,
        description='Общее количество товаров'
    )
    total_price: Decimal = Field(
        ...,
        ge=0,
        description='Общая стоимость товаров'
    )

    model_config = ConfigDict(from_attributes=True)


class CartItemCreate(BaseModel):
    """Модель для добавления нового товара в корзину."""

    product_id: int = Field(
        ...,
        description='ID товара'
    )
    quantity: int = Field(
        ...,
        gt=0,
        description='Количество товара'
    )
