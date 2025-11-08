"""
Используя синхронный запрос, найдите первую статью из таблицы модели Article,
опубликованную после 1 января 2024 года (поле published_at > '2024-01-01').

Для выполнения запроса используйте сессию session, импортированную из модуля
db. Результат запроса сохраните в переменную result.

Код модели Article из файла models.py:
class Article(Base):

    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    published_at = Column(DateTime)
"""

from db import session
from models import Article
from sqlalchemy import select

result = session.scalars(
    select(
        Article
    ).where(
        Article.published_at > '2024-01-01'
    )
).first()
