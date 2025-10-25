from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.backend.db_depends import get_db
from app.models.review import Review
from app.models.product import Product
from app.schemas import CreateReview
from .auth import get_current_user

router = APIRouter(prefix='/reviews', tags=['reviews'])


@router.get('/')
async def all_reviews(db: Annotated[AsyncSession, Depends(get_db)]):
    reviews = await db.scalars(
        select(
            Review
        ).where(
            Review.is_active == True
        )
    )
    reviews_all = reviews.all()

    if not reviews_all:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There are no reviews'
        )

    return reviews_all


@router.get('/{product_slug}')
async def products_reviews(
        db: Annotated[AsyncSession, Depends(get_db)],
        product_slug: str
):
    product = await db.scalar(
        select(
            Product
        ).where(
            Product.slug == product_slug,
            Product.is_active == True,
            Product.stock > 0
        )
    )

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no product found'
        )

    product_reviews = await db.scalars(
        select(
            Review
        ).where(
            Review.product_id == product.id,
            Review.is_active == True
        )
    )
    product_reviews_all = product_reviews.all()

    if not product_reviews_all:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There are no reviews for this product'
        )

    return product_reviews_all


@router.post('/')
async def add_review(
        db: Annotated[AsyncSession, Depends(get_db)],
        create_review: CreateReview,
        get_user: Annotated[dict, Depends(get_current_user)]
):
    if get_user.get('is_customer'):
        product = await db.scalar(
            select(
                Product
            ).where(
                Product.id == create_review.product_id
            )
        )

        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='There is no product found'
            )

        await db.execute(
            insert(
                Review
            ).values(
                user_id=get_user.get('id'),
                product_id=create_review.product_id,
                comment=create_review.comment,
                grade=create_review.grade
            )
        )

        product_reviews = await db.scalars(
            select(
                Review
            ).where(
                Review.product_id == create_review.product_id
            )
        )
        product_reviews_all = product_reviews.all()

        product.rating = round(
            sum(
                review.grade for review in product_reviews_all
            ) / len(
                product_reviews_all
            ),
            1
        )

        await db.commit()

        return {
            'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'
        }

    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have customer permission"
        )


@router.delete('/{review_id}')
async def delete_reviews(
        db: Annotated[AsyncSession, Depends(get_db)],
        review_id: int,
        get_user: Annotated[dict, get_current_user]
):
    if get_user.get('is_admin'):
        review_delete = await db.scalar(
            select(
                Review
            ).where(
                Review.id == review_id,
                Review.is_active == True
            )
        )

        if not review_delete:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='There is no review found'
            )

        review_delete.is_active = False
        await db.commit()

        return {
            'status_code': status.HTTP_200_OK,
            'transaction': 'Review delete is successful'
        }

    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You don't have admin permission"
        )
