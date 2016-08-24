"""empty message

Revision ID: 1915e596bdc9
Revises: e30068c1a278
Create Date: 2016-08-24 08:40:25.160000

"""

# revision identifiers, used by Alembic.
revision = '1915e596bdc9'
down_revision = 'e30068c1a278'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    ### end Alembic commands ###