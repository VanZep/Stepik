"""add cart_items table

Revision ID: 7fef0b7eaf90
Revises: a2ee11401414
Create Date: 2025-12-01 19:26:38.803931

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '7fef0b7eaf90'
down_revision: Union[str, Sequence[str], None] = 'a2ee11401414'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'cart_items',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('product_id', sa.Integer(), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], name=op.f('fk_cart_items_product_id_products'), ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_cart_items_user_id_users'), ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_cart_items')),
        sa.UniqueConstraint('user_id', 'product_id', name='uq_cart_items_user_product')
    )
    op.create_index(op.f('ix_cart_items_id'), 'cart_items', ['id'], unique=True)
    op.create_index(op.f('ix_cart_items_product_id'), 'cart_items', ['product_id'], unique=False)
    op.create_index(op.f('ix_cart_items_user_id'), 'cart_items', ['user_id'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_cart_items_user_id'), table_name='cart_items')
    op.drop_index(op.f('ix_cart_items_product_id'), table_name='cart_items')
    op.drop_index(op.f('ix_cart_items_id'), table_name='cart_items')
    op.drop_table('cart_items')
