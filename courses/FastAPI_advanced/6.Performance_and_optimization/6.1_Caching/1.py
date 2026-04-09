import json
import time
from contextlib import asynccontextmanager
from typing import Dict, Optional

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
import redis.asyncio as redis

redis_client: Optional[redis.Redis] = None


class Item(BaseModel):
    id: str
    name: str
    value: int


fake_database: Dict[str, Item] = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Запуск приложения: Инициализация ресурсов...")
    global redis_client
    global fake_database  # Инициализируем нашу фейковую базу данных

    # Инициализация клиента Redis
    # decode_responses=True гарантирует, что операции GET возвращают строки вместо байтов
    redis_client = redis.Redis(host='localhost', port=6379, db=0,
                               decode_responses=True)
    try:
        await redis_client.ping()
        print("Успешное подключение к Redis!")
    except redis.ConnectionError as e:
        print(f"Не удалось подключиться к Redis: {e}")
        # В продакшене можно было бы вызвать исключение или реализовать запасной вариант
        redis_client = None  # Установливаем None, чтобы запросы могли продолжаться без кэширования

    # Заполняем фейковую базу данных некоторыми начальными данными для тестирования
    fake_database["item:1"] = Item(id="1", name="Продукт A", value=10)
    fake_database["item:2"] = Item(id="2", name="Продукт B", value=20)
    print("Фейковая база данных инициализирована данными.")

    yield

    # Закрытие соединения Redis при завершении работы приложения
    print("Завершение работы приложения")
    if redis_client:
        await redis_client.close()
        print("Отключено от Redis.")


app = FastAPI(lifespan=lifespan)


# Зависимость для получения клиента Redis в маршрутах
async def get_redis_client_dependency():
    if redis_client is None:
        raise HTTPException(
            status_code=500,
            detail="Клиент Redis не инициализирован или не подключен."
        )
    return redis_client


# Тест подключения к Redis
@app.get('/redis_connect')
async def redis_connect_test(
        r: redis.Redis = Depends(get_redis_client_dependency)):
    await r.ping()
    return {'message': 'Успешное подключение к Redis'}
