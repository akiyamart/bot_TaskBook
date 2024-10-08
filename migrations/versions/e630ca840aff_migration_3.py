"""Migration #3

Revision ID: e630ca840aff
Revises: 5daec160e383
Create Date: 2024-09-27 21:33:22.307200

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'e630ca840aff'
down_revision: Union[str, None] = '5daec160e383'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('start_time', sa.TIMESTAMP(), nullable=True))
    op.drop_column('tasks', 'time')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('tasks', 'start_time')
    # ### end Alembic commands ###
