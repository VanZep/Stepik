from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.backend.db import Base

if TYPE_CHECKING:
    from app.models.review import Review


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )
    first_name = Column(String)
    last_name = Column(String)
    username = Column(
        String,
        unique=True
    )
    email = Column(
        String,
        unique=True
    )
    hashed_password = Column(String)
    is_active = Column(
        Boolean,
        default=True
    )
    is_admin = Column(
        Boolean,
        default=False
    )
    is_supplier = Column(
        Boolean,
        default=False
    )
    is_customer = Column(
        Boolean,
        default=True
    )

    reviews = relationship(
        'Review',
        back_populates='user',
        uselist=True,
        cascade='all, delete'
    )
