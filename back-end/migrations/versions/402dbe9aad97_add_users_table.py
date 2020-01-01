"""add users table

Revision ID: 402dbe9aad97
Revises: 
Create Date: 2019-12-12 17:34:25.119087

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '402dbe9aad97'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('create_time', sa.Integer(), nullable=True),
    sa.Column('status', sa.SmallInteger(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('phone', sa.String(length=24), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.Column('username', sa.String(length=12), nullable=True),
    sa.Column('姓名', sa.String(length=12), nullable=True),
    sa.Column('民族', sa.String(length=12), nullable=True),
    sa.Column('生日', sa.String(length=12), nullable=True),
    sa.Column('籍贯', sa.String(length=12), nullable=True),
    sa.Column('工作地点', sa.String(length=32), nullable=True),
    sa.Column('学历', sa.String(), nullable=True),
    sa.Column('身高', sa.String(), nullable=True),
    sa.Column('性别', sa.String(), nullable=True),
    sa.Column('月薪', sa.String(), nullable=True),
    sa.Column('职业', sa.String(), nullable=True),
    sa.Column('QQ', sa.String(length=24), nullable=True),
    sa.Column('微信', sa.String(length=48), nullable=True),
    sa.Column('婚姻状况', sa.String(), nullable=True),
    sa.Column('小孩', sa.String(), nullable=True),
    sa.Column('房', sa.String(), nullable=True),
    sa.Column('车', sa.String(), nullable=True),
    sa.Column('喝酒', sa.String(), nullable=True),
    sa.Column('吸烟', sa.String(), nullable=True),
    sa.Column('健康状况', sa.String(), nullable=True),
    sa.Column('宗教信仰', sa.String(), nullable=True),
    sa.Column('兴趣话题', sa.String(), nullable=True),
    sa.Column('体育运动', sa.String(), nullable=True),
    sa.Column('球类运动', sa.String(), nullable=True),
    sa.Column('休闲娱乐', sa.String(), nullable=True),
    sa.Column('饮食偏好', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('QQ'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('微信')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
