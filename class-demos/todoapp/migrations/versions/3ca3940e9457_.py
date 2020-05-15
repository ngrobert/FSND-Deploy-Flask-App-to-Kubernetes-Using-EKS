"""empty message

Revision ID: 3ca3940e9457
Revises: 5cb2417e1c1e
Create Date: 2020-05-12 21:51:41.830395

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ca3940e9457'
down_revision = '5cb2417e1c1e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todolists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('todos', sa.Column('list_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'todos', 'todolists', ['list_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'todos', type_='foreignkey')
    op.drop_column('todos', 'list_id')
    op.drop_table('todolists')
    # ### end Alembic commands ###
