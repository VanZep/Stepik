from typing import List, Optional

from sqlalchemy import Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True,
        index=True
    )
    name: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )
    parent_id: Mapped[int | None] = mapped_column(
        Integer,
        ForeignKey('categories.id')
    )

    products: Mapped[List['Product']] = relationship(
        'Product',
        uselist=True,
        back_populates='category',
        cascade='all, delete-orphan'
    )

    parent: Mapped[Optional['Category']] = relationship(
        'Category',
        back_populates='children',
        remote_side='Category.id'
    )

    children: Mapped[List['Category']] = relationship(
        'Category',
        uselist=True,
        back_populates='parent',
        cascade='all, delete-orphan'
    )


if __name__ == "__main__":
    from sqlalchemy.schema import CreateTable
    from app.models.products import Product

    print(CreateTable(Category.__table__))
    print(CreateTable(Product.__table__))
