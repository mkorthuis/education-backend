"""School types by the state's code, and the kind of each district

The location loader matched a school's type on the state's description, which the 2026 list
renamed, so the 2026 load left most schools without a type. Types are now matched on the
state's code, stored in school_type.code. district.kind tells a school district from a
charter school's board and a private school's operator (all of which the school list has).

The lists are loaded again, so every school gets its type and every district its kind.

Revision ID: b3d5f7a9c1e4
Revises: a7c9e1b3d5f2
Create Date: 2026-11-11 16:00:00.000000

"""
from alembic import op

from app.etl import location


# revision identifiers, used by Alembic.
revision = 'b3d5f7a9c1e4'
down_revision = 'a7c9e1b3d5f2'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("ALTER TABLE school_type ADD COLUMN code VARCHAR(10)")
    op.execute("ALTER TABLE district ADD COLUMN kind VARCHAR(20) NOT NULL DEFAULT 'district'")
    location.load(op.get_bind())


def downgrade():
    op.execute("ALTER TABLE district DROP COLUMN kind")
    op.execute("ALTER TABLE school_type DROP COLUMN code")
