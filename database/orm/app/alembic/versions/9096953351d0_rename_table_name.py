"""rename table name

Revision ID: 9096953351d0
Revises: 19a5d75837d9
Create Date: 2026-08-29 05:45:07.672025

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9096953351d0'
down_revision: Union[str, None] = '19a5d75837d9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.rename_table("scholars","students")


def downgrade() -> None:
    op.rename_table("scholars","students")
