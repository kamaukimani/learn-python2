"""initial migration

Revision ID: 392b588e83f2
Revises: 4baf80234d68
Create Date: 2026-08-29 05:11:27.203510

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '392b588e83f2'
down_revision: Union[str, None] = '4baf80234d68'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
