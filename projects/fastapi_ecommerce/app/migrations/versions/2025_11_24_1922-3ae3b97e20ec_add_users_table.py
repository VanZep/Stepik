"""add users table

Revision ID: 3ae3b97e20ec
Revises: a4b76e4748bb
Create Date: 2025-11-24 19:22:52.096381

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '3ae3b97e20ec'
down_revision: Union[str, Sequence[str], None] = 'a4b76e4748bb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('role', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_users'))
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=True)
    op.add_column('products', sa.Column('seller_id', sa.Integer(), nullable=False))
    op.create_foreign_key(op.f('fk_products_seller_id_users'), 'products', 'users', ['seller_id'], ['id'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(op.f('fk_products_seller_id_users'), 'products', type_='foreignkey')
    op.drop_column('products', 'seller_id')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
