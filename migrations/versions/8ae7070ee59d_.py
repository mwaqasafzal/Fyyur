"""empty message

Revision ID: 8ae7070ee59d
Revises: ab84d1e9aa9b
Create Date: 2020-07-27 17:47:43.028585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ae7070ee59d'
down_revision = 'ab84d1e9aa9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('ArtistGenre_artist_id_fkey', 'ArtistGenre', type_='foreignkey')
    op.drop_constraint('ArtistGenre_genre_id_fkey', 'ArtistGenre', type_='foreignkey')
    op.create_foreign_key(None, 'ArtistGenre', 'Artist', ['artist_id'], ['id'], ondelete='cascade')
    op.create_foreign_key(None, 'ArtistGenre', 'Genre', ['genre_id'], ['id'], ondelete='cascade')
    op.drop_constraint('Show_venue_id_fkey', 'Show', type_='foreignkey')
    op.drop_constraint('Show_artist_id_fkey', 'Show', type_='foreignkey')
    op.create_foreign_key(None, 'Show', 'Venue', ['venue_id'], ['id'], ondelete='cascade')
    op.create_foreign_key(None, 'Show', 'Artist', ['artist_id'], ['id'], ondelete='cascade')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.create_foreign_key('Show_artist_id_fkey', 'Show', 'Artist', ['artist_id'], ['id'])
    op.create_foreign_key('Show_venue_id_fkey', 'Show', 'Venue', ['venue_id'], ['id'])
    op.drop_constraint(None, 'ArtistGenre', type_='foreignkey')
    op.drop_constraint(None, 'ArtistGenre', type_='foreignkey')
    op.create_foreign_key('ArtistGenre_genre_id_fkey', 'ArtistGenre', 'Genre', ['genre_id'], ['id'])
    op.create_foreign_key('ArtistGenre_artist_id_fkey', 'ArtistGenre', 'Artist', ['artist_id'], ['id'])
    # ### end Alembic commands ###
