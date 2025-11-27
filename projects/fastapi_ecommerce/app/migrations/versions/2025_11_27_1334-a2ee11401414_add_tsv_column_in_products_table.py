"""add tsv column in products table

Revision ID: a2ee11401414
Revises: d723c8853f3c
Create Date: 2025-11-27 13:34:47.480653

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision: str = 'a2ee11401414'
down_revision: Union[str, Sequence[str], None] = 'd723c8853f3c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('products', sa.Column('tsv', postgresql.TSVECTOR(), sa.Computed("\n            setweight(to_tsvector('english', coalesce(name, '')), 'A')\n            || \n            setweight(to_tsvector('english', coalesce(description, '')), 'B')\n            ", persisted=True), nullable=False))
    op.create_index('ix_products_tsv_gin', 'products', ['tsv'], unique=False, postgresql_using='gin')


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index('ix_products_tsv_gin', table_name='products', postgresql_using='gin')
    op.drop_column('products', 'tsv')
