"""
Создайте модели User и Profile для системы авторизации. Добавьте все
необходимые импорты, определите базовый класс Base и настройте двусторонний
доступ между моделями с использованием back_populates.

Модель User:
Имя таблицы — users.
id — уникальный идентификатор пользователя (целое число, первичный ключ).
username — имя пользователя (строка, максимум 50 символов, уникальная,
не null).

Модель Profile:
Имя таблицы — profiles.
id — уникальный идентификатор профиля (целое число, первичный ключ).
user_id — внешний ключ на пользователя (целое число, уникальный, не null).
bio — биография (текст, nullable).

Связь: Один пользователь (User) имеет один профиль (Profile), связь
один-к-одному через user_id. Настройте двусторонний доступ с back_populates.
"""

from sqlalchemy import Integer, String, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )

    profile: Mapped['Profile'] = relationship(
        'Profile',
        uselist=False,
        back_populates='user',
        cascade='all, delete-orphan'
    )


class Profile(Base):
    __tablename__ = 'profiles'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('users.id'),
        unique=True,
        nullable=False
    )
    bio: Mapped[str | None] = mapped_column(Text)

    user: Mapped['User'] = relationship(
        'User',
        back_populates='profile'
    )
