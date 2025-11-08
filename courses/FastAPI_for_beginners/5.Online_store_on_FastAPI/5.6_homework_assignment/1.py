"""
Используя синхронный запрос, выберите названия всех курсов из таблицы модели
Course, отсортированные по алфавиту (поле title).

Для выполнения запроса используйте сессию session, импортированную из модуля
db. Результат запроса сохраните в переменную result.

Код модели Course из файла models.py:
class Course(Base):

    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    duration = Column(Integer)
"""

from db import session
from models import Course
from sqlalchemy import select

result = session.scalars(select(Course.title).order_by(Course.title)).all()
