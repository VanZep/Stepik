"""
Создайте модели Project, Employee и промежуточную таблицу Participation для
системы управления проектами. Добавьте все необходимые импорты, определите
базовый класс Base и настройте двусторонний доступ между моделями с
использованием back_populates.

Модель Project:
Имя таблицы — projects.
id — уникальный идентификатор проекта (целое число, первичный ключ).
name — название проекта (строка, максимум 150 символов, не null).
start_date — дата начала проекта (дата, не null).

Модель Employee:
Имя таблицы — employees.
id — уникальный идентификатор сотрудника (целое число, первичный ключ).
name — имя сотрудника (строка, максимум 100 символов, не null).
email — электронная почта (строка, максимум 120 символов, уникальная, не null).

Модель Participation (промежуточная):
Имя таблицы — participations.
project_id — внешний ключ на проект (целое число, первичный ключ).
employee_id — внешний ключ на сотрудника (целое число, первичный ключ).
role — роль сотрудника в проекте (строка, максимум 50 символов, не null).

Связь: Один проект (Project) может включать много сотрудников (Employee), и
один сотрудник может участвовать в нескольких проектах, связь многие-ко-многим
через модель Participation. Настройте двусторонний доступ с back_populates.
"""

from typing import List
from datetime import date

from sqlalchemy import Integer, String, Date, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Project(Base):
    __tablename__ = 'projects'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True,
        index=True
    )
    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )
    start_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    employees: Mapped[List['Employee']] = relationship(
        'Employee',
        uselist=True,
        secondary='participations',
        back_populates='projects'
    )
    participations: Mapped[List['Participation']] = relationship(
        'Participation',
        uselist=True,
        back_populates='project',
        single_parent=True,
        cascade='all, delete-orphan'
    )


class Employee(Base):
    __tablename__ = 'employees'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True,
        index=True
    )
    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    email: Mapped[str] = mapped_column(
        String(120),
        nullable=False,
        unique=True
    )

    projects: Mapped[List['Project']] = relationship(
        'Project',
        uselist=True,
        secondary='participations',
        back_populates='employees'
    )
    participations: Mapped[List['Participation']] = relationship(
        'Participation',
        uselist=True,
        back_populates='employee',
        single_parent=True,
        cascade='all, delete-orphan'
    )


class Participation(Base):
    __tablename__ = 'participations'

    project_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('projects.id'),
        primary_key=True,
        index=True
    )
    employee_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('employees.id'),
        primary_key=True,
        index=True
    )
    role: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    project: Mapped['Project'] = relationship(
        'Project',
        back_populates='participations'
    )
    employee: Mapped['Employee'] = relationship(
        'Employee',
        back_populates='participations'
    )
