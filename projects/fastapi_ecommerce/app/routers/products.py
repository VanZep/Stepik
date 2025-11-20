from typing import List

from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy import select, and_, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.products import Product as ProductModel
from app.models.categories import Category as CategoryModel
from app.models.users import User as UserModel
from app.schemas import Product as ProductSchema, ProductCreate
from app.db_depends import get_async_db
from app.auth import get_current_seller

router = APIRouter(prefix='/products', tags=['products'])


@router.get(
    '/',
    response_model=List[ProductSchema],
    status_code=status.HTTP_200_OK
)
async def get_all_products(db: AsyncSession = Depends(get_async_db)):
    """
    Возвращает список всех товаров.
    """
    products = await db.scalars(
        select(
            ProductModel
        ).where(
            ProductModel.is_active == True
        )
    )

    return products.all()


@router.post(
    '/',
    response_model=ProductSchema,
    status_code=status.HTTP_201_CREATED
)
async def create_product(
        product: ProductCreate,
        db: AsyncSession = Depends(get_async_db),
        current_user: UserModel = Depends(get_current_seller)
):
    """
    Создаёт новый товар, привязанный к текущему продавцу (только для 'seller').
    """
    category = await db.scalars(
        select(
            CategoryModel
        ).where(
            and_(
                CategoryModel.id == product.category_id,
                CategoryModel.is_active == True
            )
        )
    )
    category = category.first()
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Category not found or not active'
        )

    product = ProductModel(
        **product.model_dump(),
        seller_id=current_user.id
    )
    db.add(product)
    await db.commit()
    await db.refresh(product)

    return product


@router.get(
    '/category/{category_id}',
    response_model=List[ProductSchema],
    status_code=status.HTTP_200_OK
)
async def get_products_by_category(
        category_id: int,
        db: AsyncSession = Depends(get_async_db)
):
    """
    Возвращает список товаров в указанной категории по её ID.
    """
    category = await db.scalars(
        select(
            CategoryModel
        ).where(
            and_(
                CategoryModel.id == category_id,
                CategoryModel.is_active == True
            )
        )
    )
    category = category.first()
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Category not found or not active'
        )

    products_by_category = await db.scalars(
        select(
            ProductModel
        ).where(
            and_(
                ProductModel.category_id == category_id,
                ProductModel.is_active == True
            )
        )
    )

    return products_by_category.all()


@router.get(
    '/{product_id}',
    response_model=ProductSchema,
    status_code=status.HTTP_200_OK
)
async def get_product(
        product_id: int,
        db: AsyncSession = Depends(get_async_db)
):
    """
    Возвращает детальную информацию о товаре по его ID.
    """
    product = await db.scalars(
        select(
            ProductModel
        ).where(
            and_(
                ProductModel.id == product_id,
                ProductModel.is_active == True
            )
        )
    )
    product = product.first()
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Product not found or not active'
        )

    category = await db.scalars(
        select(
            CategoryModel
        ).where(
            and_(
                CategoryModel.id == product.category_id,
                CategoryModel.is_active == True
            )
        )
    )
    category = category.first()
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Category not found or not active'
        )

    return product


@router.put(
    '/{product_id}',
    response_model=ProductSchema,
    status_code=status.HTTP_200_OK
)
async def update_product(
        product_id: int,
        product: ProductCreate,
        db: AsyncSession = Depends(get_async_db)
):
    """
    Обновляет товар по его ID.
    """
    db_product = await db.scalars(
        select(
            ProductModel
        ).where(
            and_(
                ProductModel.id == product_id,
                ProductModel.is_active == True
            )
        )
    )
    db_product = db_product.first()
    if db_product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Product not found or not active'
        )

    category = await db.scalars(
        select(
            CategoryModel
        ).where(
            and_(
                CategoryModel.id == product.category_id,
                CategoryModel.is_active == True
            )
        )
    )
    category = category.first()
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Category not found or not active'
        )

    await db.execute(
        update(
            ProductModel
        ).where(
            ProductModel.id == product_id
        ).values(
            **product.model_dump(exclude_unset=True)
        )
    )
    await db.commit()
    await db.refresh(db_product)

    return db_product


@router.delete(
    '/{product_id}',
    response_model=ProductSchema,
    status_code=status.HTTP_200_OK
)
async def delete_product(
        product_id: int,
        db: AsyncSession = Depends(get_async_db)
):
    """
    Удаляет товар по его ID (логическое удаление).
    """
    product = await db.scalars(
        select(
            ProductModel
        ).where(
            and_(
                ProductModel.id == product_id,
                ProductModel.is_active == True
            )
        )
    )
    product = product.first()
    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Product not found or not active'
        )

    product.is_active = False
    await db.commit()
    await db.refresh(product)

    return product
