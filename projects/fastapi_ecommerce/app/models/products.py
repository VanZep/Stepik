from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship

from backend.db import Base


class Product(Base):
    __tablename__ = 'products'

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
    category_id = Column(
        Integer,
        ForeignKey('categories.id')
    )

    category = relationship(
        'Category',
        back_populates='products',
        uselist=False
    )

# from sqlalchemy.schema import CreateTable
#
# print(CreateTable(Product.__table__))
