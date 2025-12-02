from typing import List
from decimal import Decimal
from datetime import datetime, timezone

from sqlalchemy import Integer, ForeignKey, String, Numeric, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base


class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True,
        index=True
    )
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey('users.id', ondelete='CASCADE'),
        nullable=False,
        index=True
    )
    status: Mapped[str] = mapped_column(
        String(20),
        default='pending',
        nullable=False
    )
    total_amount: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        default=0,
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(timezone.utc),
        server_default=func.now(),
        nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.now(timezone.utc),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    user: Mapped['User'] = relationship(
        'User',
        back_populates='orders'
    )
