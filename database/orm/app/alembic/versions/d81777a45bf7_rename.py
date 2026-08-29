"""rename

Revision ID: d81777a45bf7
Revises: ff71b46637ad
Create Date: 2026-08-29 07:03:05.020942

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd81777a45bf7'
down_revision: Union[str, None] = 'ff71b46637ad'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table("scholars","students")


def downgrade() -> None:
    op.rename_table("students","scholars")
