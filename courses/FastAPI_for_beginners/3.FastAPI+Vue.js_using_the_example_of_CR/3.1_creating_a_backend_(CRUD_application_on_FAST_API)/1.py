"""
Создадим приложение FastAPI.
Настроим CORS для взаимодействия с фронтендом.
Определим модели Pydantic для валидации данных.
Создадим простую базу данных в памяти.
"""

# Импортируем необходимые библиотеки
from typing import List, Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, field_validator

# Создаём приложение FastAPI
app = FastAPI(title="Messages CRUD")

# Настраиваем CORS для взаимодействия с фронтендом
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Модель Pydantic для создания нового сообщения
class MessageCreate(BaseModel):
    content: str


# Модель Pydantic для частичного обновления сообщения
class MessageUpdate(BaseModel):
    content: Optional[str] = None


# Модель Pydantic для представления сообщения в ответах API
class Message(BaseModel):
    id: int
    content: str


# Простая "база данных" в памяти для хранения сообщений
messages_db: List[Message] = [Message(id=0, content="First post in FastAPI")]
