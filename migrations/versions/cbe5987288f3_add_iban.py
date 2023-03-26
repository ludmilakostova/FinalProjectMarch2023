"""Add iban

Revision ID: cbe5987288f3
Revises: e622a4d81576
Create Date: 2023-03-22 20:55:17.992964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cbe5987288f3'
down_revision = 'e622a4d81576'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('iban', sa.String(length=22), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('iban')

    # ### end Alembic commands ###
