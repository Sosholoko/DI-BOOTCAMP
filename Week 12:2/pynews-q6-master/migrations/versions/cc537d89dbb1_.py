"""empty message

Revision ID: cc537d89dbb1
Revises: f26a81b66219
Create Date: 2021-04-22 19:15:35.462343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc537d89dbb1'
down_revision = 'f26a81b66219'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('boolean', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'boolean')
    # ### end Alembic commands ###
