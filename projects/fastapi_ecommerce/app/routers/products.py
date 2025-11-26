from typing import List

from fastapi import APIRouter, status, Depends, HTTPException, Query
from sqlalchemy import select, and_, update, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.products import Product as ProductModel
from app.models.categories import Category as CategoryModel
from app.models.users import User as UserModel
from app.schemas import Product as ProductSchema, ProductCreate, ProductList
from app.db_depends import get_async_db
from app.auth import get_current_seller

router = APIRouter(prefix='/products', tags=['products'])


@router.get(
    '/',
    response_model=ProductList,
    status_code=status.HTTP_200_OK
)
async def get_all_products(
        page: int = Query(1, ge=1),
        page_size: int = Query(20, ge=1, le=100),
        db: AsyncSession = Depends(get_async_db)
):
    """
    Возвращает список всех активных товаров.
    """
    total = await db.scalar(
        select(
            func.count()
        ).select_from(
            ProductModel
        ).where(
            ProductModel.is_active == True
        )
    ) or 0

    products = await db.scalars(
        select(
            ProductModel
        ).where(
            ProductModel.is_active == True
        ).order_by(
            ProductModel.id.asc()
        ).offset(
            (page - 1) * page_size
        ).limit(
            page_size
        )
    )

    return {
        'items': products.all(),
        'total': total,
        'page': page,
        'page_size': page_size
    }


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

    product_db = ProductModel(
        **product.model_dump(),
        seller_id=current_user.id
    )
    db.add(product_db)
    await db.commit()
    await db.refresh(product_db)

    return product_db


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
        db: AsyncSession = Depends(get_async_db),
        current_user: UserModel = Depends(get_current_seller)
):
    """
    Обновляет товар, если он принадлежит текущему продавцу
    (только для 'seller').
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

    if db_product.seller_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You can only update your own products'
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
        db: AsyncSession = Depends(get_async_db),
        current_user: UserModel = Depends(get_current_seller)
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

    if product.seller_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail='You can only delete your own products'
        )

    product.is_active = False
    await db.commit()
    await db.refresh(product)

    return product
