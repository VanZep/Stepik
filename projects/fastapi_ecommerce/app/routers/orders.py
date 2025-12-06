from decimal import Decimal

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy import select, delete
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import User as UserModel
from app.models import CartItem as CartItemModel
from app.models import Order, OrderItem as OrderItemModel
from app.schemas.orders import Order as OrderSchema
from app.db_depends import get_async_db
from app.auth import get_current_user
from app.utils import load_order_with_items

router = APIRouter(prefix='/orders', tags=['orders'])


@router.post(
    '/checkout',
    response_model=OrderSchema,
    status_code=status.HTTP_201_CREATED
)
async def checkout_order(
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
    cart_items = cart_items.all()
    if not cart_items:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Cart items not found in cart'
        )

    order = Order(user_id=current_user.id)

    total_amount = Decimal('0')

    for item in cart_items:
        product = item.product

        if not product or product.is_active == False:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Product {item.product_id} is unavailable'
            )

        if product.stock < item.quantity:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Not enough stock for product {product.name}'
            )

        unit_price = product.price
        if unit_price is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Product {product.name} has no price set'
            )

        total_price = unit_price * Decimal(item.quantity)
        total_amount += total_price

        order.items.append(
            OrderItemModel(
                product_id=product.id,
                quantity=item.quantity,
                unit_price=unit_price,
                total_price=total_price
            )
        )

        product.stock -= item.quantity

    order.total_amount = total_amount

    db.add(order)
    await db.execute(
        delete(
            CartItemModel
        ).where(
            CartItemModel.user_id == current_user.id
        )
    )
    await db.commit()

    created_order = await load_order_with_items(db, order.id)
    if not created_order:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Failed to load created order'
        )

    return created_order
