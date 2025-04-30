"""District Materialized Views

Revision ID: e2a3d4c5b6a7
Revises: c9d8e7f6b5a4
Create Date: 2024-10-02 00:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
import logging

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = 'e2a3d4c5b6a7'
down_revision = 'c9d8e7f6b5a4'
branch_labels = None
depends_on = None


def upgrade():
    """Create district-level materialized views for early exit and post-graduation data."""
    logger.info("Starting District Materialized Views migration upgrade")

    # ------------------------------------------------------------------
    # district_early_exit
    # ------------------------------------------------------------------
    logger.info("Creating district_early_exit materialized view")
    op.execute(
        """
        CREATE MATERIALIZED VIEW district_early_exit AS
        SELECT
            d.id AS district_id_fk,
            see.year AS year,
            SUM(see.adjusted_fall_enrollment) AS adjusted_fall_enrollment,
            SUM(see.earned_hiset) AS earned_hiset,
            SUM(see.enrolled_in_college) AS enrolled_in_college,
            SUM(see.dropped_out) AS dropped_out,
            SUM(see.missing) AS missing,
            SUM(see.annual_early_exit_percentage) AS annual_early_exit_percentage,
            SUM(see.four_year_early_exit_percentage) AS four_year_early_exit_percentage,
            SUM(see.annual_dropout_percentage) AS annual_dropout_percentage,
            SUM(see.four_year_dropout_percentage) AS four_year_dropout_percentage
        FROM
            school_early_exit see
            JOIN school s ON see.school_id_fk = s.id
            JOIN district d ON s.district_id_fk = d.id
        GROUP BY d.id, see.year
        """
    )

    logger.info("Creating index for district_early_exit")
    op.execute(
        """
        CREATE INDEX idx_district_early_exit_district_year
        ON district_early_exit (district_id_fk, year)
        """
    )

    # ------------------------------------------------------------------
    # district_post_graduation
    # ------------------------------------------------------------------
    logger.info("Creating district_post_graduation materialized view")
    op.execute(
        """
        CREATE MATERIALIZED VIEW district_post_graduation AS
        SELECT
            d.id AS district_id_fk,
            spg.year AS year,
            spg.post_graduation_type_id_fk AS post_graduation_type_id_fk,
            SUM(spg.value) AS value
        FROM
            school_post_graduation spg
            JOIN school s ON spg.school_id_fk = s.id
            JOIN district d ON s.district_id_fk = d.id
        GROUP BY d.id, spg.post_graduation_type_id_fk, spg.year
        """
    )

    logger.info("Creating index for district_post_graduation")
    op.execute(
        """
        CREATE INDEX idx_district_post_graduation_district_type_year
        ON district_post_graduation (district_id_fk, post_graduation_type_id_fk, year)
        """
    )

    logger.info("District Materialized Views migration upgrade completed successfully")


def downgrade():
    """Drop the materialized views created in the upgrade."""
    logger.info("Starting District Materialized Views migration downgrade")

    views_to_drop = [
        'district_post_graduation',
        'district_early_exit'
    ]

    for view in views_to_drop:
        logger.info(f"Dropping materialized view {view}")
        op.execute(f"DROP MATERIALIZED VIEW IF EXISTS {view}")

    logger.info("District Materialized Views migration downgrade completed successfully") 