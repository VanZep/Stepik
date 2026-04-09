import json
import time
import logging
from contextlib import asynccontextmanager
from typing import Dict, Optional

from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
import redis.asyncio as redis

logger = logging.getLogger()

redis_client: Optional[redis.Redis] = None


class Item(BaseModel):
    id: str
    name: str
    value: int


fake_database: Dict[str, Item] = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.warning("Запуск приложения: Инициализация ресурсов...")
    global redis_client
    global fake_database  # Инициализируем нашу фейковую базу данных

    # Инициализация клиента Redis
    # decode_responses=True гарантирует, что операции GET возвращают строки вместо байтов
    redis_client = redis.Redis(
        host='localhost',
        port=6379,
        db=0,
        decode_responses=True
    )
    try:
        await redis_client.ping()
        logger.warning("Успешное подключение к Redis!")
    except redis.ConnectionError as e:
        logger.warning(f"Не удалось подключиться к Redis: {e}")
        # В продакшене можно было бы вызвать исключение или реализовать запасной вариант
        redis_client = None  # Установливаем None, чтобы запросы могли продолжаться без кэширования

    # Заполняем фейковую базу данных некоторыми начальными данными для тестирования
    fake_database["1"] = Item(id="1", name="Продукт A", value=10)
    fake_database["2"] = Item(id="2", name="Продукт B", value=20)
    logger.warning("Фейковая база данных инициализирована данными.")

    yield

    # Закрытие соединения Redis при завершении работы приложения
    logger.warning("Завершение работы приложения")
    if redis_client:
        await redis_client.close()
        logger.warning("Отключено от Redis.")


app = FastAPI(lifespan=lifespan)


# Зависимость для получения клиента Redis в маршрутах
async def get_redis_client_dependency():
    if redis_client is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Клиент Redis не инициализирован или не подключен."
        )

    return redis_client


# Тест подключения к Redis
@app.get('/redis_connect')
async def redis_connect_test(
        r: redis.Redis = Depends(get_redis_client_dependency)):
    await r.ping()

    return {'message': 'Успешное подключение к Redis'}


@app.get("/item/{item_id}", response_model=Item)
async def get_item(
        item_id: str,
        r: redis.Redis = Depends(get_redis_client_dependency)
):
    cache_key = f"item:{item_id}"
    cached = await r.get(cache_key)
    if cached:
        data = json.loads(cached)
        item = Item.model_validate(data)
        return item

    item = fake_database.get(item_id)
    time.sleep(2)  # Имитируем задержку получения из фейковой БД
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Item not found"
        )
    await r.set(cache_key, json.dumps(item.model_dump()), ex=60)

    return item


@app.post("/item", response_model=Item)
async def create_item(
        item: Item,
        r: redis.Redis = Depends(get_redis_client_dependency)
):
    fake_database[item.id] = item
    cache_key = f"item:{item.id}"
    await r.delete(cache_key)

    return item
