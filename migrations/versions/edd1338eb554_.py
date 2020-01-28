"""empty message

Revision ID: edd1338eb554
Revises: 1b5621cfb665
Create Date: 2020-01-28 08:31:39.056188

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'edd1338eb554'
down_revision = '1b5621cfb665'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=80), nullable=False),
                    sa.Column('price', sa.Float(), nullable=False),
                    sa.Column('isbn', sa.Integer(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.drop_table('book')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
                    sa.Column('id', sa.INTEGER(),
                              autoincrement=True, nullable=False),
                    sa.Column('name', sa.VARCHAR(length=80),
                              autoincrement=False, nullable=False),
                    sa.Column('price', postgresql.DOUBLE_PRECISION(
                        precision=53), autoincrement=False, nullable=False),
                    sa.Column('isbn', sa.INTEGER(),
                              autoincrement=False, nullable=True),
                    sa.PrimaryKeyConstraint('id', name='book_pkey')
                    )
    op.drop_table('users')
    # ### end Alembic commands ###