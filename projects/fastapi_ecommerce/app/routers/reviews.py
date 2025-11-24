from typing import List

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Review as ReviewModel
from app.models import Product as ProductModel
from app.schemas import Review as ReviewSchema, ReviewCreate
from app.routers.products import router as products_router
from app.db_depends import get_async_db

router = APIRouter(prefix='/reviews', tags=['reviews'])


@router.get(
    '/',
    response_model=List[ReviewSchema],
    status_code=status.HTTP_200_OK
)
async def get_all_reviews(
        db: AsyncSession = Depends(get_async_db)
):
    """
    Возвращает список всех отзывов.
    """
    reviews = await db.scalars(
        select(
            ReviewModel
        ).where(
            ReviewModel.is_active == True
        )
    )

    return reviews.all()


@router.get(
    '/products/{product_id}/reviews',
    response_model=List[ReviewSchema],
    status_code=status.HTTP_200_OK
)
async def get_reviews_by_product(
        product_id: int,
        db: AsyncSession = Depends(get_async_db)
):
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
    product = product.first()
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Product not found or not active'
        )

    reviews = await db.scalars(
        select(
            ReviewModel
        ).where(
            and_(
                ReviewModel.product_id == product_id,
                ReviewModel.is_active == True
            )
        )
    )

    return reviews.all()
