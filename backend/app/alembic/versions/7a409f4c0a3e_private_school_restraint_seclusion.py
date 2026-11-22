"""Private schools' restraints and seclusions, 2018-19 to 2023-24

NHED publishes restraint and seclusion counts for each private (nonpublic) school in its yearly
restraint and seclusion reports; the School Safety Data Collection that loads school_restraint and
school_seclusion lists no private school. These get a table of their own, so the public schools'
state and district totals, safety enrollment views and rates never include them. See
app/etl/private_safety.py.

Revision ID: 7a409f4c0a3e
Revises: e7a9c1b3d5f6
Create Date: 2026-11-21 12:00:00.000000

"""
from alembic import op
import logging

from app.etl import private_safety

logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = '7a409f4c0a3e'
down_revision = 'e7a9c1b3d5f6'
branch_labels = None
depends_on = None


def upgrade():
    logger.info("Creating private_school_restraint_seclusion")
    op.execute("""
        CREATE TABLE private_school_restraint_seclusion (
            id SERIAL PRIMARY KEY,
            school_id_fk INTEGER NOT NULL,
            year INTEGER NOT NULL,
            enrollment INTEGER,
            restraint_reports INTEGER,
            restraints_bodily_harm INTEGER,
            restraints_serious_injury_or_death INTEGER,
            restraint_investigations_active INTEGER,
            restraint_investigations_closed INTEGER,
            seclusion_reports INTEGER,
            seclusion_investigations_active INTEGER,
            seclusion_investigations_closed INTEGER,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_private_school_restraint_seclusion_school FOREIGN KEY (school_id_fk) REFERENCES school(id) ON DELETE CASCADE,
            CONSTRAINT unique_private_school_restraint_seclusion_year UNIQUE (school_id_fk, year)
        )
    """)
    op.execute("CREATE INDEX idx_private_school_restraint_seclusion_year ON private_school_restraint_seclusion(year)")
    op.execute("""
        CREATE TRIGGER trigger_update_private_school_restraint_seclusion_timestamp
        BEFORE UPDATE ON private_school_restraint_seclusion
        FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
    """)

    # Every year in app/alembic/config/private_school_restraint_seclusion_config.yaml
    counts = private_safety.load(op.get_bind())
    logger.info(f"Loaded private school restraints and seclusions: {counts}")


def downgrade():
    op.execute("DROP TABLE IF EXISTS private_school_restraint_seclusion CASCADE")
