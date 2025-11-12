"""
Создайте эндпоинт FastAPI для логического удаления отзыва по его ID
(установка is_active=False) в таблице reviews. Проверьте существование
продукта и отзыва.

Используйте APIRouter для создания маршрута эндпоинта.

Эндпоинт должен принимать DELETE-запрос по маршруту /{review_id}.

Используйте зависимость get_async_db из модуля database для получения
асинхронной сессии базы данных.

Используйте SQLAlchemy модели  ReviewModel из модуля app.models.review и
ProductModel из модуля app.models.product.

Проверьте существование продукта и его активность, в случае если он не активен
или не найден, верните 404 ошибку с соответствующим текстом.

Проверьте существование отзыва и его активность, в случае если он не активен
или не найден, верните 404 ошибку с соответствующим текстом.

В случае успешного удаления (установка is_active=False), верните
JSON-сообщение {"status": "success", "message": "Review marked as inactive"}.


Код модели ReviewModel из модуля app.models.review:

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class ReviewModel(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, index=True)
    user_id = Column(Integer, index=True)
    comment = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)



Код модели ProductModel из модуля app.models.product:

from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class ProductModel(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    is_active = Column(Boolean, default=True)
"""

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.review import ReviewModel
from app.models.product import ProductModel
from database import get_async_db

router = APIRouter(prefix='/reviews', tags=['reviews'])


@router.delete(
    '/{review_id}',
    response_model=dict,
    status_code=status.HTTP_200_OK
)
async def delete_review(
        review_id: int,
        db: AsyncSession = Depends(get_async_db)
):
    review = await db.scalars(
        select(
            ReviewModel
        ).where(
            and_(
                ReviewModel.id == review_id,
                ReviewModel.is_active == True
            )
        )
    )
    review = review.first()
    if review is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Review not found or not active'
        )

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

    review.is_active = False
    await db.commit()
    await db.refresh(review)

    return {'status': 'success', 'message': 'Review marked as inactive'}
