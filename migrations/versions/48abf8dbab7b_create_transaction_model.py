"""Create transaction model

Revision ID: 48abf8dbab7b
Revises: f7bfb130c047
Create Date: 2023-04-02 15:37:18.454294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48abf8dbab7b'
down_revision = 'f7bfb130c047'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quote_id', sa.String(length=100), nullable=False),
    sa.Column('transfer_id', sa.String(length=100), nullable=False),
    sa.Column('custom_transfer_id', sa.String(length=200), nullable=False),
    sa.Column('target_account_id', sa.String(length=100), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('create_on', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('complaint_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['complaint_id'], ['complaints.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transactions')
    # ### end Alembic commands ###