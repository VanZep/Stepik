from sqlalchemy import select, and_, func
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Product as ProductModel
from app.models import Review as ReviewModel


async def update_product_rating(
        product: ProductModel,
        db: AsyncSession
) -> None:
    product.rating = await db.scalar(
        select(
            func.avg(ReviewModel.grade)
        ).where(
            and_(
                ReviewModel.product_id == product.id,
                ReviewModel.is_active == True
            )
        )
    )
    await db.commit()
    await db.refresh(product)
