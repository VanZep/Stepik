from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.ext.asyncio import (
    create_async_engine, async_sessionmaker, AsyncSession
)

# Строка подключения для SQLite
DATABASE_URL = "sqlite:///ecommerce.db"

# Создаём Engine
engine = create_engine(DATABASE_URL, echo=True)

# Настраиваем фабрику сеансов
SessionLocal = sessionmaker(bind=engine)


# Строка подключения для PostgreSQl
DATABASE_URL = "postgresql+asyncpg://ecommerce_user:795606@localhost:5432/ecommerce_db"

# Создаём Engine
async_engine = create_async_engine(DATABASE_URL, echo=True)

# Настраиваем фабрику сеансов
async_session_maker = async_sessionmaker(
    async_engine,
    expire_on_commit=False,
    class_=AsyncSession
)


class Base(DeclarativeBase):

    metadata = MetaData(
        naming_convention={
            'ix': 'ix_%(column_0_label)s',
            'uq': 'uq_%(table_name)s_%(column_0_N_name)s',
            'ck': 'ck_%(table_name)s_%(constraint_name)s',
            'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
            'pk': 'pk_%(table_name)s'
        }
    )
