"""rename grade column to marks

Revision ID: b842a68849c7
Revises: d81777a45bf7
Create Date: 2026-08-29 07:08:14.041119

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b842a68849c7'
down_revision: Union[str, None] = 'd81777a45bf7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "students",
        "grade",
        new_column_name="marks"
    )


def downgrade() -> None:
    pass
