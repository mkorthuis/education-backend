"""Where every district's students go for the grades it doesn't run, statewide

places.yaml (assets/reference) had only SAU 9 and SAU 13; it now has every New Hampshire district that
sends students elsewhere for some grades, from each district's contracts, policies, minutes and reports
and the State Board of Education's approvals, with the Vermont, Maine and Massachusetts schools they
attend. Two arrangements the check didn't allow:

- interstate_district: a district formed with Vermont towns under the interstate school compact, such
  as Dresden (Hanover and Norwich, VT) and Rivendell (Orford and three Vermont towns)
- joint_maintenance: a school two districts run together under RSA 194:21, such as Prospect Mountain
  (Alton and Barnstead)

Revision ID: b7d9f1a3c5e8
Revises: 31a40d2bd2f9
Create Date: 2026-11-15 20:00:00.000000

"""
from alembic import op
import logging

from app.etl import reference
from app.etl.core import load_config

logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = 'b7d9f1a3c5e8'
down_revision = '31a40d2bd2f9'
branch_labels = None
depends_on = None

ARRANGEMENTS = ('tuition_contract', 'area_agreement', 'cooperative', 'choice', 'no_contract')
NEW_ARRANGEMENTS = ('interstate_district', 'joint_maintenance')


def _check(arrangements):
    values = ", ".join(f"'{a}'" for a in arrangements)
    op.execute("ALTER TABLE district_service DROP CONSTRAINT check_district_service_arrangement")
    op.execute(f"ALTER TABLE district_service ADD CONSTRAINT check_district_service_arrangement CHECK (arrangement IN ({values}))")


def upgrade():
    logger.info("Starting statewide district service migration upgrade")
    _check(ARRANGEMENTS + NEW_ARRANGEMENTS)
    counts = reference.load_places(op.get_bind(), load_config(reference.CONFIG))
    logger.info(f"Statewide district service migration upgrade completed successfully: {counts}")


def downgrade():
    values = ", ".join(f"'{a}'" for a in NEW_ARRANGEMENTS)
    op.execute(f"DELETE FROM district_service WHERE arrangement IN ({values})")
    _check(ARRANGEMENTS)
