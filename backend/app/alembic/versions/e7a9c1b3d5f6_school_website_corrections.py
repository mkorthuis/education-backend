"""School websites: working links for schools whose website in the state's list is broken

NH DOE's school list gives St. Joseph Regional School (Keene) an old Google Sites address that asks
for a sign-in, Our Lady of Mercy Academy an address that doesn't connect, and Granite Valley
Preparatory no website. The site shows each school's website on its school page. The loader now
applies website_corrections from generate_schools_config.yaml after every load; this applies them to
the schools already loaded.

Revision ID: e7a9c1b3d5f6
Revises: c3e5a7b9d1f2
Create Date: 2026-11-16 18:00:00.000000

"""
from alembic import op
import logging

from app.etl import location

logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = 'e7a9c1b3d5f6'
down_revision = 'c3e5a7b9d1f2'
branch_labels = None
depends_on = None


def upgrade():
    count = location.apply_website_corrections(op.get_bind())
    logger.info(f"Applied {count} school website corrections")


def downgrade():
    # Nothing to undo in the schema; the state's links stay in its school list files
    pass
