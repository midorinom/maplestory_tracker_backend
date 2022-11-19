"""empty message

Revision ID: caf62baf3b5b
Revises: 557a94c823ca
Create Date: 2022-11-19 15:43:27.232995

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'caf62baf3b5b'
down_revision = '557a94c823ca'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ursus_tour',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('username', sa.VARCHAR(length=20), nullable=True),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.Column('first_day_of_bossing_week', sa.DATE(), nullable=True),
    sa.Column('ursus', sa.INTEGER(), nullable=True),
    sa.Column('tour', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['username'], ['users.username'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('dailies',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('character', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('date', sa.DATE(), nullable=True),
    sa.Column('is_current_day', sa.BOOLEAN(), nullable=True),
    sa.Column('dailies_list', sa.TEXT(), nullable=True),
    sa.Column('dailies_done', sa.TEXT(), nullable=True),
    sa.ForeignKeyConstraint(['character'], ['characters.uuid'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('weeklies',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('character', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('first_day_of_week', sa.DATE(), nullable=True),
    sa.Column('is_current_week', sa.BOOLEAN(), nullable=True),
    sa.Column('weeklies_list', sa.TEXT(), nullable=True),
    sa.Column('weeklies_done', sa.TEXT(), nullable=True),
    sa.ForeignKeyConstraint(['character'], ['characters.uuid'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('weeklies')
    op.drop_table('dailies')
    op.drop_table('ursus_tour')
    # ### end Alembic commands ###
