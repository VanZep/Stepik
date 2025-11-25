from os.path import exists
from typing import List

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Review as ReviewModel
from app.models import Product as ProductModel
from app.models import User as UserModel
from app.schemas import Review as ReviewSchema, ReviewCreate
from app.db_depends import get_async_db
from app.auth import get_current_buyer
from app.utils import update_product_rating

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

    reviews_by_product = await db.scalars(
        select(
            ReviewModel
        ).where(
            and_(
                ReviewModel.product_id == product_id,
                ReviewModel.is_active == True
            )
        )
    )

    return reviews_by_product.all()


@router.post(
    '/',
    response_model=ReviewSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_review(
        review: ReviewCreate,
        db: AsyncSession = Depends(get_async_db),
        current_user: UserModel = Depends(get_current_buyer)
):
    product = await db.scalars(
        select(
            ProductModel
        ).where(
            and_(
                ProductModel.id == review.product_id,
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

    review_db = await db.scalars(
        select(
            ReviewModel
        ).where(
            and_(
                ReviewModel.user_id == current_user.id,
                ReviewModel.product_id == product.id
            )
        )
    )
    review_db = review_db.first()
    if review_db is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='This user has already left a review for this product'
        )

    review_db = ReviewModel(**review.model_dump(), user_id=current_user.id)
    db.add(review_db)
    await db.commit()
    await db.refresh(review_db)

    await update_product_rating(product, db)

    return review_db

