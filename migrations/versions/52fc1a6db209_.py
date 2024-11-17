"""empty message

Revision ID: 52fc1a6db209
Revises: d23018721c11
Create Date: 2024-11-15 18:33:06.482160

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '52fc1a6db209'
down_revision = 'd23018721c11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gfgfg',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mobile_no', sa.String(length=10), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('fname', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('mobile_no')
    )
    with op.batch_alter_table('pms_request_account', schema=None) as batch_op:
        batch_op.drop_index('email')
        batch_op.drop_index('mobile_no')

    op.drop_table('pms_request_account')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pms_request_account',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('mobile_no', mysql.VARCHAR(length=10), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('fname', mysql.VARCHAR(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='MyISAM'
    )
    with op.batch_alter_table('pms_request_account', schema=None) as batch_op:
        batch_op.create_index('mobile_no', ['mobile_no'], unique=True)
        batch_op.create_index('email', ['email'], unique=True)

    op.drop_table('gfgfg')
    # ### end Alembic commands ###
