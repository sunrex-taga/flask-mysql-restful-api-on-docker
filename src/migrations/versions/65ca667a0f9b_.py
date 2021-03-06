"""empty message

Revision ID: 65ca667a0f9b
Revises: 2e85eaaaf8e7
Create Date: 2020-06-19 00:18:46.465377

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '65ca667a0f9b'
down_revision = '2e85eaaaf8e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('schedules', sa.Column('rooms_name', sa.String(length=20), nullable=False))
    op.drop_column('schedules', 'room_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('schedules', sa.Column('room_name', mysql.VARCHAR(length=20), nullable=False))
    op.drop_column('schedules', 'rooms_name')
    # ### end Alembic commands ###
