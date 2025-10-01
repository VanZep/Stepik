"""
Напишите Pydantic модель для представления записей блога, со следующими полями:
title: Заголовок записи, строка. Ограничьте длину строки 255 символами.
description: Подробное описание записи, строка. Может иметь значение None.
created_at: Дата и время создания записи, устанавливает текущую дату и время
по умолчанию.
updated_at: Дата и время последнего обновления записи. По умолчанию имеет
значение None.
is_active: Флаг, указывающий, активна ли запись. Значение по умолчанию True.
tags: Список тегов, связанных с записью. Значение по умолчанию - пустой список.
"""

from datetime import datetime

from pydantic import BaseModel, Field


class Blog(BaseModel):
    title: str = Field(..., max_length=255)
    description: str | None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime | None = Field(default=None)
    is_active: bool = Field(default=True)
    tags: list[str] = Field(default=[])
