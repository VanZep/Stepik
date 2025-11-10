from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.categories import Category as CategoryModel
from app.schemas import Category as CategorySchema, CategoryCreate
from app.db_depends import get_async_db

router = APIRouter(prefix="/categories", tags=["categories"])


@router.post(
    "/",
    response_model=CategorySchema,
    status_code=status.HTTP_201_CREATED
)
async def create_category(
        category: CategoryCreate,
        db: AsyncSession = Depends(get_async_db)
):
    """
    Создаёт новую категорию.
    """
    if category.parent_id:
        result = await db.scalars(
            select(
                CategoryModel
            ).where(
                and_(
                    CategoryModel.id == category.parent_id,
                    CategoryModel.is_active == True
                )
            )
        )
        parent = result.first()
        if parent is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Parent category not found"
            )

    db_category = CategoryModel(**category.model_dump())
    db.add(db_category)
    await db.commit()
    await db.refresh(db_category)

    return db_category
