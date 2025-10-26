"""
Создайте модель Car для автосалона с именем таблицы cars. Добавьте все
необходимые импорты и определите базовый класс Base.

Поля модели:
id — уникальный идентификатор автомобиля (целое число, первичный ключ)
brand — марка автомобиля (строка, максимум 50 символов, не null)
model — модель автомобиля (строка, максимум 50 символов, не null)
year — год выпуска (целое число, не null)
price — цена автомобиля (десятичное число, максимум 10 цифр, 2 после запятой,
nullable)
is_available — доступность автомобиля (булево, не null, по умолчанию True)
"""

from decimal import Decimal

from sqlalchemy import Integer, String, Numeric, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Car(Base):
    __tablename__ = 'cars'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    brand: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )
    model: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )
    year: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )
    price: Mapped[Decimal | None] = mapped_column(
        Numeric(10, 2)
    )
    is_available: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=True
    )
