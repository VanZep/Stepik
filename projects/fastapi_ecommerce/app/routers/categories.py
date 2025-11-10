from typing import List

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy import select, update, and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.categories import Category as CategoryModel
from app.schemas import Category as CategorySchema, CategoryCreate
from app.db_depends import get_async_db

router = APIRouter(prefix="/categories", tags=["categories"])


@router.get(
    "/",
    response_model=List[CategorySchema],
    status_code=status.HTTP_200_OK
)
async def get_all_categories(db: AsyncSession = Depends(get_async_db)):
    categories = await db.scalars(
        select(
            CategoryModel
        ).where(
            CategoryModel.is_active == True
        )
    )

    return categories.all()


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


@router.put(
    "/{category_id}",
    response_model=CategorySchema,
    status_code=status.HTTP_200_OK
)
async def update_category(
        category_id: int,
        category: CategoryCreate,
        db: AsyncSession = Depends(get_async_db)
):
    """
    Обновляет категорию по её ID.
    """
    db_category = await db.scalars(
        select(
            CategoryModel
        ).where(
            and_(
                CategoryModel.id == category_id,
                CategoryModel.is_active == True
            )
        )
    )
    db_category = db_category.first()
    if db_category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Category not found or not active"
        )

    if category.parent_id:
        parent = await db.scalars(
            select(
                CategoryModel
            ).where(
                and_(
                    CategoryModel.id == category.parent_id,
                    CategoryModel.is_active == True
                )
            )
        )
        parent = parent.first()
        if parent is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Category parent not found or not active"
            )
        if category_id == parent.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Category cannot be its own parent"
            )

    await db.execute(
        update(
            CategoryModel
        ).where(
            CategoryModel.id == category_id
        ).values(**category.model_dump(exclude_unset=True))
    )
    await db.commit()
    await db.refresh(db_category)

    return db_category