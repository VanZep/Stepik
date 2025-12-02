from decimal import Decimal

from fastapi import APIRouter, status, Depends
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.users import User as UserModel
from app.models.cart_items import CartItem as CartItemModel
from app.schemas.cart import Cart as CartSchema
from app.db_depends import get_async_db
from app.auth import get_current_user

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
    cart_items = await db.scalars(
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

    total_quantity = sum(item.quantity for item in cart_items)

    total_price = sum(
        (
            item.product.price if item.product.price is not None
            else Decimal('0') * Decimal(item.quantity)
            for item in cart_items
        ),
        Decimal('0')
    )

    return CartSchema(
        user_id=current_user.id,
        items=cart_items.all(),
        total_quantity=total_quantity,
        total_price=total_price
    )
