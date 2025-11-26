"""add rating column in product table

Revision ID: d723c8853f3c
Revises: de8bb6a90e52
Create Date: 2025-11-26 12:53:47.496828

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'd723c8853f3c'
down_revision: Union[str, Sequence[str], None] = 'de8bb6a90e52'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('products', sa.Column('rating', sa.Float(), server_default=sa.text('0'), nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('products', 'rating')
