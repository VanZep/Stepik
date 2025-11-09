"""
Создайте эндпоинт FastAPI для логического удаления блог-поста по его ID
(установка is_active=False)

Используйте APIRouter для создания маршрута эндпоинта.

Эндпоинт должен принимать DELETE запрос по корневому маршруту роутера (/),
получая id поста из параметра маршрута. Если пост не найден или не активен,
верните ошибку с кодом 404.

Используйте зависимость get_db из модуля database,  для получения синхронной
сессии базы данных.

Используйте модель SQLAlchemy PostModel из app.models.post

Верните ответ в виде строки "Post marked as inactive"


Код модели PostModel:

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class PostModel(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    author_id = Column(Integer, index=True)
    is_active = Column(Boolean, default=True)



Код Pydantic-модели PostSchema:

from pydantic import BaseModel


class PostSchema(BaseModel):
    id: int
    title: str
    content: str
    author_id: int
    is_active: bool

    class Config:
        from_attributes = True
"""

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy import select, and_
from sqlalchemy.orm import Session

from app.models.post import PostModel
from database import get_db

router = APIRouter(prefix='/posts', tags=['posts'])


@router.delete(
    '/{post_id}',
    response_model=str,
    status_code=status.HTTP_200_OK
)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.scalars(
        select(
            PostModel
        ).where(
            and_(
                PostModel.id == post_id,
                PostModel.is_active == True
            )
        )
    ).first()
    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Post not found or not active'
        )

    post.is_active = False
    db.commit()

    return 'Post marked as inactive'
