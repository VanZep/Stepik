"""
Создайте эндпоинт FastAPI для обновления статуса подписки по её ID в таблице
subscriptions. Проверьте существование пользователя.

Используйте APIRouter для создания маршрута эндпоинта.

Эндпоинт должен принимать PUT-запрос по маршруту /{subscription_id}.

Используйте зависимость get_async_db из модуля database для получения
асинхронной сессии базы данных.

Используйте модели SQLAlchemy SubscriptionModel из модуля
app.models.subscription и UserModel из модуля app.models.user.

Используйте для входных данных Pydantic-модель SubscriptionUpdate из модуля
app.schemas.subscription.

Если пользователь не найден, либо неактивен (is_active == False), верните
HTTP-ответ с кодом 404 и сообщением об ошибке.

Если подписка не найдена, либо неактивна (is_active == False), верните
HTTP-ответ с кодом 404 и сообщением об ошибке.

Используйте для ответа Pydantic-модель SubscriptionSchema из модуля
app.schemas.subscription.


Код модели SubscriptionModel из модуля app.models.subscription:

from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class SubscriptionModel(Base):
    __tablename__ = "subscriptions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    plan = Column(String)
    start_date = Column(Date)
    end_date = Column(Date, nullable=True)
    is_active = Column(Boolean, default=True)



Код модели UserModel из модуля app.models.user:

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class UserModel(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)



Код моделей SubscriptionUpdate и SubscriptionSchema из модуля app.schemas.subscription:

from pydantic import BaseModel
from datetime import date


class SubscriptionUpdate(BaseModel):
    plan: str
    end_date: date | None = None


class SubscriptionSchema(BaseModel):
    id: int
    user_id: int
    plan: str
    start_date: date
    end_date: date | None
    is_active: bool

    class Config:
        from_attributes = True
"""

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy import select, and_, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.subscription import SubscriptionModel
from app.models.user import UserModel
from app.schemas.subscription import SubscriptionSchema, SubscriptionUpdate
from database import get_async_db

router = APIRouter(prefix='/subscriptions', tags=['subscriptions'])


@router.put(
    '/{subscription_id}',
    response_model=SubscriptionSchema,
    status_code=status.HTTP_200_OK
)
async def update_subscription(
        subscription_id: int,
        subscription: SubscriptionUpdate,
        db: AsyncSession = Depends(get_async_db)
):
    db_subscription = await db.scalars(
        select(
            SubscriptionModel
        ).where(
            and_(
                SubscriptionModel.id == subscription_id,
                SubscriptionModel.is_active == True
            )
        )
    )
    db_subscription = db_subscription.first()
    if db_subscription is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Subscription not found or not active'
        )

    user = await db.scalars(
        select(
            UserModel
        ).where(
            and_(
                UserModel.id == db_subscription.user_id,
                UserModel.is_active == True
            )
        )
    )
    user = user.first()
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User not found or not active'
        )

    await db.execute(
        update(
            SubscriptionModel
        ).where(
            SubscriptionModel.id == subscription_id
        ).values(
            **subscription.model_dump(exclude_unset=True)
        )
    )
    await db.commit()
    await db.refresh(db_subscription)

    return db_subscription
