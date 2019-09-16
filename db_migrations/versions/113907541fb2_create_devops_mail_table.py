"""create devops_mail table

Revision ID: 113907541fb2
Revises: 
Create Date: 2019-09-15 15:52:25.550432

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '113907541fb2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('devops_mail',
        sa.Column('id', sa.Integer(), primary_key=True,autoincrement=True),
        sa.Column('subject', sa.String(250), nullable=False),
        sa.Column('sender', sa.String(250), nullable=False),
        sa.Column('date', sa.Date)
    )
def downgrade():
    op.drop_table('devops_mail')
