"""
Создайте эндпоинт FastAPI для получения списка всех активных проектов
(is_active=True) из таблицы projects.

Используйте APIRouter для создания маршрута эндпоинта.

Эндпоинт должен принимать GET-запрос по корневому маршруту роутера (/).

Используйте зависимость get_async_db из модуля database для получения
асинхронной сессии базы данных.

Используйте модель SQLAlchemy ProjectModel из модуля app.models.project.

Используйте для ответа Pydantic-модель ProjectSchema из модуля
app.schemas.project.


Код модели ProjectModel из модуля app.models.project:

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class ProjectModel(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)



Код модели ProjectSchema из модуля app.schemas.project:

from pydantic import BaseModel


class ProjectSchema(BaseModel):
    id: int
    name: str
    description: str | None
    is_active: bool

    class Config:
        from_attributes = True
"""

from typing import List

from fastapi import APIRouter, status, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.project import ProjectModel
from app.schemas.project import ProjectSchema
from database import get_async_db

router = APIRouter(prefix='/projects', tags=['projects'])


@router.get(
    '/',
    response_model=List[ProjectSchema],
    status_code=status.HTTP_200_OK
)
async def get_all_projects(db: AsyncSession = Depends(get_async_db)):
    projects = await db.scalars(
        select(
            ProjectModel
        ).where(
            ProjectModel.is_active == True
        )
    )

    return projects.all()
