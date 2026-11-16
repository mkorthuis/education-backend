"""Teacher salary bands: skip NH DOE's impossible values and apply sourced corrections

NH DOE's Teacher Salary Schedule files for 2023-24 to 2025-26 have 13 impossible bands: minimums of
$14 to $5,680, a $440,367 minimum above its maximum, a maximum below its minimum, and 464 or 1,300
steps. They showed on district pages and pulled the state averages (the 2023-24 average bachelor's
minimum was $44,874 with Newmarket's row). The loader now replaces NH DOE's values with those from
a district's published schedule or teachers' agreement where the config has one (Conway, Fall
Mountain, Jackson, Lebanon, Newmarket, Northumberland, Portsmouth and Tamworth), skips rows whose
salaries are still impossible, and drops step counts over 60 (Lincoln-Woodstock's 2024-25 1,300).
This reloads every configured year, which replaces that year's rows.

Revision ID: d2f4a6c8e0b1
Revises: b7d9f1a3c5e8
Create Date: 2026-11-15 22:00:00.000000

"""
from alembic import op
import logging

from app.etl import teacher_salary_band

logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = 'd2f4a6c8e0b1'
down_revision = 'b7d9f1a3c5e8'
branch_labels = None
depends_on = None


def upgrade():
    counts = teacher_salary_band.load(op.get_bind())
    logger.info(f"Reloaded teacher salary bands with the limits and corrections: {counts}")


def downgrade():
    # Nothing to undo in the schema; NH DOE's original values stay in its files in assets/staff
    pass
