from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from backend.db import SessionLocal, async_session_maker


# async def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
