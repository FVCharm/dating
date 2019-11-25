"""users jwt

Revision ID: 5be47687c5f5
Revises: 
Create Date: 2019-11-26 00:23:35.213450

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5be47687c5f5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index('ix_user_token')
        batch_op.drop_column('token')
        batch_op.drop_column('token_expiration')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('token_expiration', sa.DATETIME(), nullable=True))
        batch_op.add_column(sa.Column('token', sa.VARCHAR(length=32), nullable=True))
        batch_op.create_index('ix_user_token', ['token'], unique=1)

    # ### end Alembic commands ###
