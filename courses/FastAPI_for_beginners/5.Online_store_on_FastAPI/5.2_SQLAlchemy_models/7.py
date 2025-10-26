"""
Создайте модель Recipe для кулинарного приложения с именем таблицы recipes.
Добавьте все необходимые импорты и определите базовый класс Base.

Поля модели:
id — уникальный идентификатор рецепта (целое число, первичный ключ)
name — название рецепта (строка, максимум 150 символов, не null)
cooking_time — время приготовления в минутах (целое число, не null)
ingredients — список ингредиентов (текст, не null)
calories — калорийность (целое число, nullable)
created_at — дата создания рецепта (дата и время, не null, по умолчанию текущая
дата)
"""

from datetime import datetime

from sqlalchemy import Integer, String, Text, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Recipe(Base):
    __tablename__ = 'recipes'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )
    cooking_time: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )
    ingredients: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )
    calories: Mapped[int | None] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False,
        default=datetime.now
    )
