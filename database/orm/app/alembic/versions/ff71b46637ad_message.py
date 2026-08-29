"""message

Revision ID: ff71b46637ad
Revises: 9096953351d0
Create Date: 2026-08-29 07:00:19.388075

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ff71b46637ad'
down_revision: Union[str, None] = '9096953351d0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
