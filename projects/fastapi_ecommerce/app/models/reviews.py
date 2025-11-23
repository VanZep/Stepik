from datetime import datetime, timezone

from sqlalchemy import (
    Integer, SmallInteger, Text, DateTime, Boolean, func, ForeignKey
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Review(Base):
    __tablename__ = 'reviews'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True,
        index=True
    )
    comment: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )
    comment_date: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(timezone.utc),
        server_default=func.now(),
        nullable=False
    )
    grade: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )
    user_id: Mapped[int | None] = mapped_column(
        Integer,
        ForeignKey('users.id'),
        nullable=True
    )
    product_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('products.id'),
        nullable=False
    )

    buyer: Mapped['User'] = relationship(
        'User',
        back_populates='reviews'
    )
    product: Mapped['Product'] = relationship(
        'Product',
        back_populates='reviews'
    )
