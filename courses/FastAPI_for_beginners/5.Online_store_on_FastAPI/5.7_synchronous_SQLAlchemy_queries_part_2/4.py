"""
Создайте эндпоинт FastAPI для обновления отзыва по его ID.

Используйте APIRouter для создания маршрута эндпоинта.

Эндпоинт должен принимать PUT запрос по корневому маршруту роутера (/),
получая id отзыва из параметра маршрута. Если отзыв не найден или не активен,
верните ошибку с кодом 404.

Используйте зависимость get_db из модуля database, для получения синхронной
сессии базы данных.

Используйте модель SQLAlchemy ReviewModel из app.models.review

Используйте для создания Pydantic-модель ReviewCreate из модуля
app.schemas.review.

Используйте для ответа Pydantic-модель ReviewSchema из модуля
app.schemas.review.

Проверьте существование продукта через модель ProductModel из модуля
app.models.product перед обновлением отзыва. Если продукт не найден или не
активен, верните ошибку с кодом 404.


Код модели ReviewModel:

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class ReviewModel(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, index=True)
    user_id = Column(Integer, index=True)
    rating = Column(Integer)
    comment = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)



Код модели ProductModel:

from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class ProductModel(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    category_id = Column(Integer, index=True)
    is_active = Column(Boolean, default=True)



Код Pydantic-моделей ReviewCreate и ReviewSchema:

from pydantic import BaseModel


class ReviewCreate(BaseModel):
    user_id: int
    rating: int
    comment: str | None = None


class ReviewSchema(BaseModel):
    id: int
    product_id: int
    user_id: int
    rating: int
    comment: str | None
    is_active: bool

    class Config:
        from_attributes = True
"""

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy import select, update, and_
from sqlalchemy.orm import Session

from app.models.review import ReviewModel
from app.models.product import ProductModel
from app.schemas.review import ReviewSchema, ReviewCreate
from database import get_db

router = APIRouter(prefix='/reviews', tags=['reviews'])


@router.put(
    '/{review_id}',
    response_model=ReviewSchema,
    status_code=status.HTTP_200_OK
)
def update_review(
        review_id: int,
        review: ReviewCreate,
        db: Session = Depends(get_db)
):
    db_review = db.scalars(
        select(
            ReviewModel
        ).where(
            and_(
                ReviewModel.id == review_id,
                ReviewModel.is_active == True
            )
        )
    ).first()
    if db_review is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Review not found or not active'
        )

    product = db.scalars(
        select(
            ProductModel
        ).where(
            and_(
                ProductModel.id == db_review.product_id,
                ProductModel.is_active == True
            )
        )
    ).first()
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Product not found or not active'
        )

    db.execute(
        update(
            ReviewModel
        ).where(
            ReviewModel.id == review_id
        ).values(
            **review.model_dump()
        )
    )
    db.commit()
    db.refresh(db_review)

    return db_review
