from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.users import User as UserModel
from app.schemas import User as UserSchema, UserCreate
from app.db_depends import get_async_db
from app.auth import hash_password, verify_password, create_access_token

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


@router.post(
    '/token',
    response_model=dict,
    status_code=status.HTTP_200_OK
)
async def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: AsyncSession = Depends(get_async_db)
):
    """
    Аутентифицирует пользователя и возвращает JWT с email, role и id.
    """
    user = await db.scalars(
        select(
            UserModel
        ).where(
            and_(
                UserModel.email == form_data.username,
                UserModel.is_active == True
            )
        )
    )
    user = user.first()
    if user is None or not verify_password(
            form_data.password, user.hashed_password
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect email or password',
            headers={'WWW-Authenticate': 'Bearer'}
        )

    access_token = create_access_token(
        data={'sub': user.email, 'role': user.role, 'id': user.id}
    )

    return {'access_token': access_token, 'token_type': 'bearer'}
