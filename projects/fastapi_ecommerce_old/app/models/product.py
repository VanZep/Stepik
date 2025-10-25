from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship

from app.backend.db import Base

if TYPE_CHECKING:
    from app.models.review import Review


class Product(Base):
    __tablename__ = 'products'
    __table_args__ = {'extend_existing': True}

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )
    name = Column(String)
    slug = Column(
        String,
        unique=True,
        index=True
    )
    description = Column(String)
    price = Column(Integer)
    image_url = Column(String)
    stock = Column(Integer)
    rating = Column(Float)
    is_active = Column(
        Boolean,
        default=True
    )
    supplier_id = Column(
        Integer,
        ForeignKey('users.id'),
        nullable=True
    )
    category_id = Column(
        Integer,
        ForeignKey('categories.id')
    )

    category = relationship(
        'Category',
        back_populates='products',
        uselist=False
    )
    reviews = relationship(
        'Review',
        back_populates='product',
        uselist=True,
        cascade='all, delete'
    )
