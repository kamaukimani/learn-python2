"""recreate

Revision ID: 766cf2b9859b
Revises: e524fda7f93f
Create Date: 2026-08-30 05:16:05.529666

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '766cf2b9859b'
down_revision: Union[str, None] = 'e524fda7f93f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    with op.batch_alter_table("games", schema=None) as batch_op:
        batch_op.alter_column(
            "updated_at",
            existing_type=sa.DateTime(),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            existing_nullable=False,
        )


def downgrade() -> None:
    with op.batch_alter_table("games", schema=None) as batch_op:
        batch_op.alter_column(
            "updated_at",
            existing_type=sa.DateTime(),
            server_default=None,
            existing_nullable=False,
        )