"""Add review model

Revision ID: a963e4209109
Revises: e7921bd08210
Create Date: 2025-11-23 21:53:32.986173

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = 'a963e4209109'
down_revision: Union[str, Sequence[str], None] = 'e7921bd08210'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'reviews',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('comment', sa.Text(), nullable=True),
        sa.Column(
            'comment_date',
            sa.DateTime(timezone=True),
            server_default=sa.text('now()'),
            nullable=False
        ),
        sa.Column('grade', sa.SmallInteger(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('product_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_reviews_id'), 'reviews', ['id'], unique=True)
    op.create_unique_constraint(None, 'users', ['id'])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_index(op.f('ix_reviews_id'), table_name='reviews')
    op.drop_table('reviews')
