from datetime import datetime, timezone
from typing import TYPE_CHECKING

from sqlalchemy import (
    Column, Integer, ForeignKey, Text, DateTime, func, Boolean
)
from sqlalchemy.orm import relationship

from app.backend.db import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.product import Product


class Review(Base):
    __tablename__ = 'reviews'

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )
    user_id = Column(
        Integer,
        ForeignKey('users.id'),
        nullable=False
    )
    product_id = Column(
        Integer,
        ForeignKey('products.id'),
        nullable=False
    )
    comment = Column(
        Text,
        nullable=True
    )
    comment_date = Column(
        DateTime(timezone=True),
        default=datetime.now(timezone.utc),
        server_default=func.now()
    )
    grade = Column(
        Integer,
        nullable=False
    )
    is_active = Column(
        Boolean,
        default=True
    )

    user = relationship(
        'User',
        back_populates='reviews',
        uselist=False
    )
    product = relationship(
        'Product',
        back_populates='reviews',
        uselist=False
    )
