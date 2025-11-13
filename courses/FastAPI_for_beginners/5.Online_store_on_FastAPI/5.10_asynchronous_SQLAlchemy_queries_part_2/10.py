"""
Создайте эндпоинт FastAPI для логического удаления промокода по его ID
(установка значения is_active=False) в таблице promocodes.

Используйте APIRouter для создания маршрута эндпоинта.

Эндпоинт должен принимать DELETE-запрос по маршруту /{promocode_id}.

Используйте зависимость get_async_db из модуля database для получения
асинхронной сессии базы данных.

Используйте модель SQLAlchemy PromoCodeModel из модуля app.models.promocode.

Если промокод не найден, либо неактивен (is_active == False), верните
HTTP-ответ с кодом 404 и сообщением об ошибке.

В случае успешного удаления (установка значения is_active=False), верните
JSON-сообщение {"status": "success", "message": "Promocode marked as inactive"}.


Код модели PromoCodeModel из модуля app.models.promocode:

from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class PromoCodeModel(Base):
    __tablename__ = "promocodes"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    discount_percentage = Column(Float)
    is_active = Column(Boolean, default=True)



Код модели PromoCodeSchema из модуля app.schemas.promocode:

from pydantic import BaseModel


class PromoCodeSchema(BaseModel):
    id: int
    code: str
    discount_percentage: float
    is_active: bool

    class Config:
        from_attributes = True
"""

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.promocode import PromoCodeModel
from database import get_async_db

router = APIRouter(prefix='/promocodes', tags=['promocodes'])


@router.delete(
    '/{promocode_id}',
    response_model=dict,
    status_code=status.HTTP_200_OK
)
async def delete_promocode(
        promocode_id: int,
        db: AsyncSession = Depends(get_async_db)
):
    promocode = await db.scalars(
        select(
            PromoCodeModel
        ).where(
            and_(
                PromoCodeModel.id == promocode_id,
                PromoCodeModel.is_active == True
            )
        )
    )
    promocode = promocode.first()
    if promocode is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Promocode not found or not active'
        )

    promocode.is_active = False
    await db.commit()
    await db.refresh(promocode)

    return {'status': 'success', 'message': 'Promocode marked as inactive'}
