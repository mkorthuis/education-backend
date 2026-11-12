"""When each school's record starts

The school list gives each school's open date: when it opened, or when the state renumbered or
reorganized it (blank for most long-standing schools). It's kept in school.open_date, so a page
can say a new school opened after the latest figures, instead of showing nothing.

The lists are loaded again to fill it in.

Revision ID: c6e8a0b2d4f7
Revises: b3d5f7a9c1e4
Create Date: 2026-11-12 10:00:00.000000

"""
from alembic import op

from app.etl import location


# revision identifiers, used by Alembic.
revision = 'c6e8a0b2d4f7'
down_revision = 'b3d5f7a9c1e4'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("ALTER TABLE school ADD COLUMN open_date DATE")
    location.load(op.get_bind())


def downgrade():
    op.execute("ALTER TABLE school DROP COLUMN open_date")
