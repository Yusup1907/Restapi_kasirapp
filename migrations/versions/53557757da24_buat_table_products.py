"""buat table products

Revision ID: 53557757da24
Revises: d78bd4d024fb
Create Date: 2022-01-10 15:34:35.843844

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '53557757da24'
down_revision = 'd78bd4d024fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('kode', sa.String(length=5), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('harga', sa.Integer(), nullable=True),
    sa.Column('category', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['category'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    # ### end Alembic commands ###
