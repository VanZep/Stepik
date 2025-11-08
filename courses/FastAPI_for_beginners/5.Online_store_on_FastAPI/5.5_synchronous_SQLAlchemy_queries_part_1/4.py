"""
Используя синхронный запрос, выберите все проекты из таблицы модели Project, у
которых поле priority равно 'high'. Примените select(), where() и метод all().

Для выполнения запроса используйте сессию session, импортированную из модуля
db. Результат запроса сохраните в переменную result.

Код модели Project из файла models.py:
class Project(Base):

    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    priority = Column(String)
"""

from db import session
from models import Project
from sqlalchemy import select

result = session.scalars(
    select(
        Project
    ).where(
        Project.priority == 'high'
    )
).all()
