"""add reviews table

Revision ID: de8bb6a90e52
Revises: 3ae3b97e20ec
Create Date: 2025-11-24 19:33:28.689267

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'de8bb6a90e52'
down_revision: Union[str, Sequence[str], None] = '3ae3b97e20ec'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'reviews',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('comment', sa.Text(), nullable=True),
        sa.Column('comment_date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('grade', sa.SmallInteger(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('product_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], name=op.f('fk_reviews_product_id_products')),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_reviews_user_id_users')),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_reviews'))
    )
    op.create_index(op.f('ix_reviews_id'), 'reviews', ['id'], unique=True)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_reviews_id'), table_name='reviews')
    op.drop_table('reviews')
