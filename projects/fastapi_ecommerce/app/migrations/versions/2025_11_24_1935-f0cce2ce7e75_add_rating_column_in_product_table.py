"""add rating column in product table

Revision ID: f0cce2ce7e75
Revises: de8bb6a90e52
Create Date: 2025-11-24 19:35:50.014820

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'f0cce2ce7e75'
down_revision: Union[str, Sequence[str], None] = 'de8bb6a90e52'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('products', sa.Column('rating', sa.Numeric(precision=2, scale=1), server_default=sa.text('0'), nullable=False))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('products', 'rating')
