"""add categories table

Revision ID: e54f1116575b
Revises: 
Create Date: 2025-11-24 18:49:14.590157

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = 'e54f1116575b'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'categories',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('parent_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['parent_id'], ['categories.id'], name=op.f('fk_categories_parent_id_categories')),
        sa.PrimaryKeyConstraint('id', name=op.f('pk_categories'))
    )
    op.create_index(op.f('ix_categories_id'), 'categories', ['id'], unique=True)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_categories_id'), table_name='categories')
    op.drop_table('categories')
