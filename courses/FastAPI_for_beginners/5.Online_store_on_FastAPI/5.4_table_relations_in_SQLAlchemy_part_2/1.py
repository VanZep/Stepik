"""
Создайте модели Student и Grade для системы учета успеваемости. Добавьте все
необходимые импорты, определите базовый класс Base и настройте двусторонний
доступ между моделями с использованием back_populates.

Модель Student:
Имя таблицы — students.
id — уникальный идентификатор студента (целое число, первичный ключ).
name — имя студента (строка, максимум 100 символов, не null).
student_id — номер студенческого билета (строка, максимум 20 символов,
уникальная, не null).

Модель Grade:
Имя таблицы — grades.
id — уникальный идентификатор оценки (целое число, первичный ключ).
value — значение оценки (целое число, не null).
subject — предмет (строка, максимум 50 символов, не null).
student_id — внешний ключ на студента (целое число, не null).

Связь: Один студент (Student) может иметь много оценок (Grade), связь
один-ко-многим через student_id. Настройте двусторонний доступ с
back_populates.
"""

from typing import List

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = 'students'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    student_id: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        unique=True
    )

    grades: Mapped[List['Grade']] = relationship(
        'Grade',
        uselist=True,
        back_populates='student',
        cascade='all, delete-orphan'
    )


class Grade(Base):
    __tablename__ = 'grades'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    value: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )
    subject: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )
    student_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('students.id'),
        nullable=False
    )

    student: Mapped['Student'] = relationship(
        'Student',
        back_populates='grades'
    )
