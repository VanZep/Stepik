"""
Создайте эндпоинт FastAPI для обновления задачи по её ID в таблице tasks.

Используйте APIRouter для создания маршрута эндпоинта.

Эндпоинт должен принимать PUT-запрос по маршруту /{task_id}.

Используйте зависимость get_async_db из модуля database для получения
асинхронной сессии базы данных.

Используйте SQLAlchemy модели  TaskModel из модуля app.models.task и
ProjectModel из модуля app.models.project.

Используйте для входных данных Pydantic-модель TaskUpdate из модуля
app.schemas.task.

Если задача не найдена, либо неактивна (is_active == False), верните
HTTP-ответ с кодом 404 и сообщением об ошибке.

Если проект не найден, либо неактивен (is_active == False), верните
HTTP-ответ с кодом 404 и сообщением об ошибке.

Для ответа используйте TaskSchema из модуля app.schemas.task, и верните
созданный объект.


Код модели TaskModel из app.models.task:

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class TaskModel(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    status = Column(String)
    project_id = Column(Integer, index=True)
    is_active = Column(Boolean, default=True)



Код модели ProjectModel из app.models.project:

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



Код моделей TaskUpdate и TaskSchema из app.schemas.task:

from pydantic import BaseModel


class TaskUpdate(BaseModel):
    title: str | None = None
    status: str
    project_id: int


class TaskSchema(BaseModel):
    id: int
    title: str
    status: str
    project_id: int
    is_active: bool

    class Config:
        from_attributes = True
"""

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy import select, and_, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.task import TaskModel
from app.models.project import ProjectModel
from app.schemas.task import TaskSchema, TaskUpdate
from database import get_async_db

router = APIRouter(prefix='/tasks', tags=['tasks'])


@router.put(
    '/{task_id}',
    response_model=TaskSchema,
    status_code=status.HTTP_200_OK
)
async def update_task(
        task_id: int,
        task: TaskUpdate,
        db: AsyncSession = Depends(get_async_db)
):
    db_task = await db.scalars(
        select(
            TaskModel
        ).where(
            and_(
                TaskModel.id == task_id,
                TaskModel.is_active == True
            )
        )
    )
    db_task = db_task.first()
    if db_task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Task not found or not active'
        )

    project = await db.scalars(
        select(
            ProjectModel
        ).where(
            and_(
                ProjectModel.id == task.project_id,
                ProjectModel.is_active == True
            )
        )
    )
    project = project.first()
    if project is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Project not found or not active'
        )

    await db.execute(
        update(
            TaskModel
        ).where(
            TaskModel.id == task_id
        ).values(
            **task.model_dump(exclude_unset=True)
        )
    )
    await db.commit()
    await db.refresh(db_task)

    return db_task
