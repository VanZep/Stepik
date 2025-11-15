from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.users import User as UserModel
from app.schemas import User as UserSchema, UserCreate
from app.db_depends import get_async_db
from app.auth import hash_password

router = APIRouter(prefix='/users', tags=['users'])


@router.post(
    '/',
    response_model=UserSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_user(
        user: UserCreate,
        db: AsyncSession = Depends(get_async_db)
):
    """
    Регистрирует нового пользователя с ролью 'buyer' или 'seller'.
    """
    db_user = await db.scalars(
        select(
            UserModel
        ).where(
            UserModel.email == user.email
        )
    )
    if db_user.first():
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Email already registered'
        )

    user = UserModel(
        email=user.email,
        hashed_password=hash_password(user.password),
        role=user.role
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)

    return user
