from decimal import Decimal
from typing import List, Optional

from fastapi import(
    APIRouter, status, Depends, HTTPException, Query, UploadFile, File
)
from sqlalchemy import select, and_, update, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.products import Product as ProductModel
from app.models.categories import Category as CategoryModel
from app.models.users import User as UserModel
from app.schemas.products import (
    Product as ProductSchema, ProductCreate, ProductList
)
from app.db_depends import get_async_db
from app.auth import get_current_seller
from app.utils import save_product_image, remove_product_image

router = APIRouter(prefix='/products', tags=['products'])


@router.get(
    '/',
    response_model=ProductList,
    status_code=status.HTTP_200_OK
)
async def get_all_products(
        db: AsyncSession = Depends(get_async_db),
        page: int = Query(1, ge=1),
        page_size: int = Query(20, ge=1, le=100),
        category_id: Optional[int] = Query(
            None,
            description='ID категории для фильтрации'
        ),
        min_price: Optional[Decimal] = Query(
            None,
            ge=0,
            description='Минимальная цена товара'
        ),
        max_price: Optional[Decimal] = Query(
            None,
            ge=0,
            description='Максимальная цена товара'
        ),
        in_stock: Optional[bool] = Query(
            None,
            description='true — товары в наличии, false — товары без остатка'
        ),
        seller_id: Optional[int] = Query(
            None,
            description='ID продавца для фильтрации'
        ),
        search: Optional[str] = Query(
            None,
            min_length=1,
            description='Поиск по названию товара'
        )
):
    """
    Возвращает список всех активных товаров по фильтру.
    """
    if min_price and max_price and min_price > max_price:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='min_price не может быть больше max_price'
        )

    filters = [ProductModel.is_active == True]

    if category_id is not None:
        filters.append(ProductModel.category_id == category_id)
    if min_price is not None:
        filters.append(ProductModel.price >= min_price)
    if max_price is not None:
        filters.append(ProductModel.price <= max_price)
    if in_stock is not None:
        filters.append(
            ProductModel.stock > 0 if in_stock else ProductModel.stock == 0
        )
    if seller_id is not None:
        filters.append(ProductModel.seller_id == seller_id)

    rank_col = None
    if search is not None:
        search = search.strip()
        if search:
            ts_query = func.websearch_to_tsquery('english', search)
            filters.append(ProductModel.tsv.op('@@')(ts_query))
            rank_col = func.ts_rank_cd(
                ProductModel.tsv, ts_query
            ).label('rank')

    total = await db.scalar(
        select(
            func.count()
        ).select_from(
            ProductModel
        ).where(
            *filters
        )
    ) or 0

    if rank_col is not None:
        products = (await db.scalars(
            select(
                ProductModel
            ).where(
                *filters
            ).order_by(
                rank_col.desc(), ProductModel.id.asc()
            ).offset(
                (page - 1) * page_size
            ).limit(
                page_size
            )
        )).all()
    else:
        products = (await db.scalars(
            select(
                ProductModel
            ).where(
                *filters
            ).order_by(
                ProductModel.id.asc()
            ).offset(
                (page - 1) * page_size
            ).limit(
                page_size
            )
        )).all()

    return {
        'items': products,
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
        product: ProductCreate = Depends(ProductCreate.as_form),
        image: Optional[UploadFile] = File(None),
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

    image_url = await save_product_image(image) if image else None

    product_db = ProductModel(
        **product.model_dump(),
        seller_id=current_user.id,
        image_url=image_url
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
        product: ProductCreate = Depends(ProductCreate.as_form),
        image: Optional[UploadFile] = File(
            None,
            description='Изображение товара'
        ),
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
            **product.model_dump()
        )
    )

    if image:
        remove_product_image(db_product.image_url)
        db_product.image_url = await save_product_image(image)

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
