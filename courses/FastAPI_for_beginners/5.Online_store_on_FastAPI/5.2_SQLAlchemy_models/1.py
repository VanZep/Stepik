"""
Создайте модель Category для категорий товаров с именем таблицы categories.
Добавьте все необходимые импорты и определите базовый класс Base.

Поля модели:
id — уникальный идентификатор категории (целое число, первичный ключ)
name — название категории (строка, максимум 50 символов, не null)
"""

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
