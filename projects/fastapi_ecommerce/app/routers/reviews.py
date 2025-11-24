from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Review as ReviewModel
from app.schemas import Review as ReviewSchema, ReviewCreate
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