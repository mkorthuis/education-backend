"""State average class size

NH DOE's statewide average class size for all grades, from iExplore's Compare view (2016 on),
as state_class_size.all_grades. The table's grade band averages are unchanged.

Revision ID: f5a7c9e2b4d8
Revises: e4b7c1d9a2f6
Create Date: 2026-11-06 00:10:00.000000

"""
from alembic import op
import logging

from app.etl import state_class_size

logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = 'f5a7c9e2b4d8'
down_revision = 'e4b7c1d9a2f6'
branch_labels = None
depends_on = None


def upgrade():
    logger.info("Starting state average class size migration upgrade")

    op.execute("ALTER TABLE state_class_size ADD COLUMN all_grades NUMERIC(15,2)")

    # Load every year in app/alembic/config/state_average_class_size_config.yaml
    state_class_size.load(op.get_bind())

    logger.info("State average class size migration upgrade completed successfully")


def downgrade():
    op.execute("ALTER TABLE state_class_size DROP COLUMN IF EXISTS all_grades")
