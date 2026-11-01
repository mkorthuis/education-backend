"""Cohort Graduation

Revision ID: 8f7e6d5c4b3a
Revises: b3c5d7e9fa12
Create Date: 2024-03-19 12:00:00.000000

"""
from alembic import op
import logging

from app.etl import graduation_cohort

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# Revision identifiers, used by Alembic.
revision = '8f7e6d5c4b3a'
down_revision = 'e2a3d4c5b6a7'
branch_labels = None
depends_on = None

# ----------------------------
# Alembic upgrade / downgrade
# ----------------------------

def upgrade():
    logger.info("Starting Cohort Graduation migration upgrade")

    # 1. Create tables
    op.execute(
        """
        CREATE TABLE school_graduation_cohort (
            id SERIAL PRIMARY KEY,
            school_id_fk INTEGER NOT NULL,
            year INTEGER NOT NULL,
            cohort_size INTEGER,
            graduate INTEGER,
            earned_hiset INTEGER,
            dropped_out INTEGER,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_school_graduation_cohort_school FOREIGN KEY (school_id_fk) REFERENCES school(id) ON DELETE CASCADE,
            CONSTRAINT unique_school_graduation_cohort_year UNIQUE (school_id_fk, year)
        )
        """
    )

    # Indexes
    op.execute("CREATE INDEX idx_school_graduation_cohort_school ON school_graduation_cohort(school_id_fk)")
    op.execute("CREATE INDEX idx_school_graduation_cohort_year ON school_graduation_cohort(year)")

    # Trigger
    op.execute(
        """
        CREATE TRIGGER trigger_update_school_graduation_cohort_timestamp
        BEFORE UPDATE ON school_graduation_cohort
        FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
        """
    )

    # State table
    op.execute(
        """
        CREATE TABLE state_graduation_cohort (
            id SERIAL PRIMARY KEY,
            year INTEGER NOT NULL,
            cohort_size INTEGER,
            graduate INTEGER,
            earned_hiset INTEGER,
            dropped_out INTEGER,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT unique_state_graduation_cohort_year UNIQUE (year)
        )
        """
    )

    # Index on year for state table
    op.execute("CREATE INDEX idx_state_graduation_cohort_year ON state_graduation_cohort(year)")

    # 2. Load data: every year in app/alembic/config/cohort_graduation_config.yaml
    graduation_cohort.load(op.get_bind())

    # 3. Create district materialized view
    op.execute(
        """
        CREATE MATERIALIZED VIEW district_graduation_cohort AS
        SELECT
            d.id AS district_id_fk,
            sgc.year AS year,
            SUM(sgc.cohort_size) AS cohort_size,
            SUM(sgc.graduate) AS graduate,
            SUM(sgc.earned_hiset) AS earned_hiset,
            SUM(sgc.dropped_out) AS dropped_out
        FROM
            school_graduation_cohort sgc
            JOIN school s ON sgc.school_id_fk = s.id
            JOIN district d ON s.district_id_fk = d.id
        GROUP BY d.id, sgc.year
        """
    )

    logger.info("Cohort Graduation migration upgrade completed successfully")


def downgrade():
    logger.info("Downgrading Cohort Graduation migration")
    op.execute("DROP MATERIALIZED VIEW IF EXISTS district_graduation_cohort")
    op.execute("DROP TABLE IF EXISTS school_graduation_cohort CASCADE")
    op.execute("DROP TABLE IF EXISTS state_graduation_cohort CASCADE")
    logger.info("Downgrade completed successfully") 