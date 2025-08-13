"""Create User model

Revision ID: 04c5ef986801
Revises: 8b4952a8c731
Create Date: 2025-08-06 16:29:46.260648

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '04c5ef986801'
down_revision: Union[str, Sequence[str], None] = '8b4952a8c731'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(), nullable=True),
        sa.Column('last_name', sa.String(), nullable=True),
        sa.Column('username', sa.String(), nullable=True),
        sa.Column('email', sa.String(), nullable=True),
        sa.Column('hashed_password', sa.String(), nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=True),
        sa.Column('is_admin', sa.Boolean(), nullable=True),
        sa.Column('is_supplier', sa.Boolean(), nullable=True),
        sa.Column('is_customer', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
        sa.UniqueConstraint('username')
    )
    op.create_index(
        op.f('ix_users_id'), 'users', ['id'], unique=False
    )
    op.add_column(
        'products',
        sa.Column('supplier_id', sa.Integer(), nullable=True)
    )
    op.create_foreign_key(None, 'products', 'users', ['supplier_id'], ['id'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.drop_column('products', 'supplier_id')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
