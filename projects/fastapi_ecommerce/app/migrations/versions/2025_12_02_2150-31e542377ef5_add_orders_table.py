"""add orders table

Revision ID: 31e542377ef5
Revises: 7fef0b7eaf90
Create Date: 2025-12-02 21:50:15.185497

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '31e542377ef5'
down_revision: Union[str, Sequence[str], None] = '7fef0b7eaf90'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'orders',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('status', sa.String(length=20), nullable=False),
        sa.Column('total_amount', sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_orders_user_id_users'), ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_orders'))
    )
    op.create_index(op.f('ix_orders_id'), 'orders', ['id'], unique=True)
    op.create_index(op.f('ix_orders_user_id'), 'orders', ['user_id'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_orders_user_id'), table_name='orders')
    op.drop_index(op.f('ix_orders_id'), table_name='orders')
    op.drop_table('orders')
