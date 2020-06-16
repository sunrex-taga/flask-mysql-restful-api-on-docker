"""empty message

Revision ID: 929f333a6731
Revises: 2d6bc48d3b7e
Create Date: 2020-06-16 10:49:45.201394

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '929f333a6731'
down_revision = '2d6bc48d3b7e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rooms',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('createTime', sa.DateTime(), nullable=False),
    sa.Column('updateTime', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rooms')
    # ### end Alembic commands ###
