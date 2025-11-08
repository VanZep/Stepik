"""
Используя синхронный запрос, выберите все задачи из таблицы модели Task для
проекта с project_id = 3.

Для выполнения запроса используйте сессию session, импортированную из модуля
db. Результат запроса сохраните в переменную result.

Код модели Task из файла models.py:

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    project_id = Column(Integer)
    description = Column(String)
"""

from db import session
from models import Task
from sqlalchemy import select

result = session.scalars(
    select(
        Task
    ).where(
        Task.project_id == 3
    )
).all()
