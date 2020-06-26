"""empty message

Revision ID: 7cf26e31f299
Revises: 65ca667a0f9b
Create Date: 2020-06-26 16:32:59.580953

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7cf26e31f299'
down_revision = '65ca667a0f9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('schedules', sa.Column('ended_at', sa.DateTime(), nullable=False))
    op.add_column('schedules', sa.Column('started_at', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('schedules', 'started_at')
    op.drop_column('schedules', 'ended_at')
    # ### end Alembic commands ###
