"""create new tables for managing org

Revision ID: 1d424e3b86ce
Revises: f76427c595a1
Create Date: 2025-02-17 22:50:50.173137

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1d424e3b86ce'
down_revision: Union[str, None] = 'f76427c595a1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('organization_careers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('is_closed', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('organization_centers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('center_name', sa.String(), nullable=False),
    sa.Column('location', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('organization_contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('is_closed', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('organization_partners',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('socials', sa.JSON(), nullable=False),
    sa.Column('logo_url', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('profiles', sa.Column('name', sa.String(), nullable=False))
    op.add_column('profiles', sa.Column('org_role', sa.String(), nullable=False))
    op.add_column('publications', sa.Column('paper_summary', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('publications', 'paper_summary')
    op.drop_column('profiles', 'org_role')
    op.drop_column('profiles', 'name')
    op.drop_table('organization_partners')
    op.drop_table('organization_contacts')
    op.drop_table('organization_centers')
    op.drop_table('organization_careers')
    # ### end Alembic commands ###
