import uuid
from pathlib import Path

from fastapi import status, HTTPException, UploadFile
from sqlalchemy import select, and_, func
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Product as ProductModel
from app.models import Review as ReviewModel
from app.models import CartItem as CartItemModel
from app.models import Order as OrderModel, OrderItem as OrderItemModel
from app.config import ALLOWED_IMAGE_TYPES, MAX_IMAGE_SIZE, MEDIA_ROOT


async def update_product_rating(
        product: ProductModel,
        db: AsyncSession
) -> None:
    """
    Пересчитывает и обновляет рейтинг товара.
    """
    product.rating = await db.scalar(
        select(
            func.avg(ReviewModel.grade)
        ).where(
            and_(
                ReviewModel.product_id == product.id,
                ReviewModel.is_active == True
            )
        )
    ) or 0.0
    await db.commit()
    await db.refresh(product)


async def checking_product_availability(
        db: AsyncSession,
        product_id: int
) -> None:
    """
    Проверяет доступность активного продукта.
    """
    product = await db.scalars(
        select(
            ProductModel
        ).where(
            and_(
                ProductModel.id == product_id,
                ProductModel.is_active == True
            )
        )
    )
    if product.first() is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Product not found or not active'
        )


async def get_cart_item(
        db: AsyncSession,
        user_id: int,
        product_id: int
) -> CartItemModel:
    """
    Возвращает позицию из корзины пользователя.
    """
    item = await db.scalars(
        select(
            CartItemModel
        ).options(
            selectinload(CartItemModel.product)
        ).where(
            and_(
                CartItemModel.user_id == user_id,
                CartItemModel.product_id == product_id
            )
        )
    )

    return item.first()


async def load_order_with_items(db: AsyncSession, order_id: int) -> OrderModel:
    """Возвращает заказ со всеми позициями."""
    order = await db.scalars(
        select(
            OrderModel
        ).options(
            selectinload(OrderModel.items).selectinload(OrderItemModel.product)
        ).where(
            OrderModel.id == order_id
        )
    )

    return order.first()


async def save_product_image(file: UploadFile) -> str:
    """
    Сохраняет изображение товара и возвращает относительный URL.
    """
    if file.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only JPG, PNG or WebP images are allowed"
        )

    content = await file.read()
    if len(content) > MAX_IMAGE_SIZE:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Image is too large"
        )

    extension = Path(file.filename or "").suffix.lower() or ".jpg"
    file_name = f"{uuid.uuid4()}{extension}"
    file_path = MEDIA_ROOT / file_name
    file_path.write_bytes(content)

    return f"/media/products/{file_name}"