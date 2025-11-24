"""Add rating column to Product model

Revision ID: fbf1b74f755b
Revises: a963e4209109
Create Date: 2025-11-24 12:53:00.475803

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fbf1b74f755b'
down_revision: Union[str, Sequence[str], None] = 'a963e4209109'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        'products',
        sa.Column(
            'rating',
            sa.Numeric(precision=2, scale=1),
            server_default=sa.text('0'),
            nullable=False
        )
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('products', 'rating')
