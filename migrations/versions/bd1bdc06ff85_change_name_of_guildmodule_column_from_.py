"""change name of GuildModule column from active to enabled

Revision ID: bd1bdc06ff85
Revises: 2023b1841f34
Create Date: 2021-07-21 18:58:25.390444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd1bdc06ff85'
down_revision = '2023b1841f34'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('guildmodules', sa.Column('enabled', sa.Boolean(), nullable=False))
    op.drop_column('guildmodules', 'active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('guildmodules', sa.Column('active', sa.BOOLEAN(), nullable=False))
    op.drop_column('guildmodules', 'enabled')
    # ### end Alembic commands ###
