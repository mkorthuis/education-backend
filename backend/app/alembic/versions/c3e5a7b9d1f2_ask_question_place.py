"""Ask question log: the page a question came from

A question can now be asked from a district's or school's page, and is about that place when it
names none. ask_question records which: place_kind (district or school) and place_id, both empty
for a question asked from the Ask page or the home page. Still nothing about who asked.

Revision ID: c3e5a7b9d1f2
Revises: d2f4a6c8e0b1
Create Date: 2026-11-16 12:00:00.000000

"""
from alembic import op
import logging

logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = 'c3e5a7b9d1f2'
down_revision = 'd2f4a6c8e0b1'
branch_labels = None
depends_on = None


def upgrade():
    logger.info("Starting ask question place migration upgrade")
    op.execute("ALTER TABLE ask_question ADD COLUMN place_kind VARCHAR(10), ADD COLUMN place_id INTEGER")
    logger.info("Completed ask question place migration upgrade")


def downgrade():
    logger.info("Starting ask question place migration downgrade")
    op.execute("ALTER TABLE ask_question DROP COLUMN IF EXISTS place_kind, DROP COLUMN IF EXISTS place_id")
    logger.info("Completed ask question place migration downgrade")
