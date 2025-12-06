from typing import Optional
from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict


class ReviewCreate(BaseModel):
    """
    Модель для создания и обновления отзыва.
    Используется в POST и PUT запросах.
    """

    product_id: int = Field(
        ...,
        description="ID товара, к которому относится отзыв"
    )
    comment: Optional[str] = Field(
        None,
        description="Текст отзыва"
    )
    grade: int = Field(
        ...,
        ge=1,
        le=5,
        description="Оценка товара"
    )


class Review(BaseModel):
    """
    Модель для ответа с данными отзыва.
    Используется в GET-запросах.
    """

    id: int = Field(
        ...,
        description="Уникальный идентификатор отзыва"
    )
    user_id: int = Field(
        ...,
        description="ID пользователя, который оставил отзыв"
    )
    product_id: int = Field(
        ...,
        description="ID товара, к которому относится отзыв"
    )
    comment: Optional[str] = Field(
        None,
        description="Текст отзыва"
    )
    comment_date: datetime = Field(
        ...,
        description="Дата и время создания отзыва"
    )
    grade: int = Field(
        ...,
        ge=1,
        le=5,
        description="Оценка товара"
    )
    is_active: bool = Field(
        ...,
        description="Активность отзыва"
    )

    model_config = ConfigDict(from_attributes=True)
