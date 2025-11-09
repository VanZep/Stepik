"""
Напишите эндпоинт FastAPI для создания новой категории.

Используйте APIRouter для создания маршрута эндпоинта.

Эндпоинт должен принимать POST запрос по корневому маршруту роутера (/).

Используйте зависимость get_db из модуля database,  для получения синхронной
сессии базы данных.

Используйте модель SQLAlchemy CategoryModel из модуля app.models.category

Для создания используйте Pydantic-модель CategoryCreate из модуля
app.schemas.category.

Используйте для ответа Pydantic-модель CategorySchema из модуля
app.schemas.category.

В случае успеха верните созданную категорию с кодом ответа 201.


Код модели CategoryModel:

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class CategoryModel(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)


Код Pydantic моделей CategoryCreate и CategorySchema:

from pydantic import BaseModel


class CategoryCreate(BaseModel):
    name: str
    description: str | None = None


class CategorySchema(BaseModel):
    id: int
    name: str
    description: str | None
    is_active: bool

    class Config:
        from_attributes = True
"""

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.models.category import CategoryModel
from app.schemas.category import CategorySchema, CategoryCreate
from database import get_db

router = APIRouter(prefix='/categories', tags=['categories'])


@router.post(
    '/',
    response_model=CategorySchema,
    status_code=status.HTTP_201_CREATED
)
def create_category(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = CategoryModel(**category.model_dump())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)

    return db_category
