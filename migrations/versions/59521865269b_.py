"""empty message

Revision ID: 59521865269b
Revises: 8ae7070ee59d
Create Date: 2020-07-27 18:18:44.914872

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59521865269b'
down_revision = '8ae7070ee59d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('genres', sa.String(length=120), nullable=True))
    op.add_column('Venue', sa.Column('genres', sa.String(length=120), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'genres')
    op.drop_column('Artist', 'genres')
    # ### end Alembic commands ###
