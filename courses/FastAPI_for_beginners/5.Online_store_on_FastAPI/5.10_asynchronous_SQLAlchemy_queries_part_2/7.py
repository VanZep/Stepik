"""
Создайте эндпоинт FastAPI для создания новой категории в таблице categories.
При успешном создании категории верните созданный объект и код ответа 201.

Используйте APIRouter для создания маршрута эндпоинта.

Эндпоинт должен принимать POST-запрос по корневому маршруту роутера (/).

Используйте зависимость get_async_db из модуля database для получения
асинхронной сессии базы данных.

Используйте SQLAlchemy модель CategoryModel из модуля app.models.category.

Используйте для входных данных Pydantic-модель CategoryCreate из модуля
app.schemas.category.

Используйте для ответа Pydantic-модель CategorySchema из модуля
app.schemas.category.


Код модели CategoryModel из модуля app.models.category:

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



Код моделей CategoryCreate и CategorySchema из модуля app.schemas.category:

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

from fastapi import APIRouter, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.category import CategoryModel
from app.schemas.category import CategorySchema, CategoryCreate
from database import get_async_db

router = APIRouter(prefix='/categories', tags=['categories'])


@router.post(
    '/',
    response_model=CategorySchema,
    status_code=status.HTTP_201_CREATED
)
async def create_category(
        category: CategoryCreate,
        db: AsyncSession = Depends(get_async_db)
):
    category = CategoryModel(**category.model_dump())
    db.add(category)
    await db.commit()
    await db.refresh(category)

    return category
