"""empty message

Revision ID: e34690e72e81
Revises: 951493dc22a2
Create Date: 2022-11-12 16:46:28.264840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e34690e72e81'
down_revision = '951493dc22a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('characters', sa.Column('stats', sa.INTEGER(), nullable=True))
    op.add_column('characters', sa.Column('dojo', sa.SMALLINT(), nullable=True))
    op.add_column('characters', sa.Column('ba', sa.SMALLINT(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('characters', 'ba')
    op.drop_column('characters', 'dojo')
    op.drop_column('characters', 'stats')
    # ### end Alembic commands ###
