from decimal import Decimal

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from watchfiles import awatch

from app.models.users import User as UserModel
from app.models.cart_items import CartItem as CartItemModel
from app.schemas.cart import (
    Cart as CartSchema,
    CartItem as CartItemSchema,
    CartItemCreate,
    CartItemUpdate
)
from app.db_depends import get_async_db
from app.auth import get_current_user
from app.utils import checking_product_availability, get_cart_item

router = APIRouter(prefix='/cart', tags=['cart'])


@router.get(
    '/',
    response_model=CartSchema,
    status_code=status.HTTP_200_OK
)
async def get_cart(
        db: AsyncSession = Depends(get_async_db),
        current_user: UserModel = Depends(get_current_user)
):
    """
    Возвращает корзину пользователя.
    """
    items = await db.scalars(
        select(
            CartItemModel
        ).options(
            selectinload(CartItemModel.product)
        ).where(
            CartItemModel.user_id == current_user.id
        ).order_by(
            CartItemModel.id
        )
    )
    items = items.all()

    total_quantity = sum(item.quantity for item in items)

    total_price = sum(
        (
            item.product.price if item.product.price is not None
            else Decimal('0') * Decimal(item.quantity)
            for item in items
        ),
        Decimal('0')
    )

    return CartSchema(
        user_id=current_user.id,
        items=items,
        total_quantity=total_quantity,
        total_price=total_price
    )


@router.post(
    '/items',
    response_model=CartItemSchema,
    status_code=status.HTTP_201_CREATED
)
async def add_item_to_cart(
        payload: CartItemCreate,
        db: AsyncSession = Depends(get_async_db),
        current_user: UserModel = Depends(get_current_user)
):
    """
    Добавляет товар в корзину пользователя.
    """
    await checking_product_availability(db, payload.product_id)

    cart_item = await get_cart_item(db, current_user.id, payload.product_id)
    if cart_item is not None:
        cart_item.quantity += payload.quantity
    else:
        cart_item = CartItemModel(
            **payload.model_dump(),
            user_id=current_user.id
        )
        db.add(cart_item)

    await db.commit()

    return await get_cart_item(db, current_user.id, payload.product_id)


@router.put(
    '/items/{product_id}',
    response_model=CartItemSchema,
    status_code=status.HTTP_200_OK
)
async def update_cart_item(
        product_id: int,
        payload: CartItemUpdate,
        db: AsyncSession = Depends(get_async_db),
        current_user: UserModel = Depends(get_current_user)
):
    """
    Обновляет количество товара в корзине пользователя.
    """
    await checking_product_availability(db, product_id)

    cart_item = await get_cart_item(db, current_user.id, product_id)
    if cart_item is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Cart item not found in cart'
        )

    cart_item.quantity = payload.quantity
    await db.commit()

    return await get_cart_item(db, current_user.id, product_id)
