"""Load District Teacher Salary Band Data

Revision ID: f9c8d7b6e5a4
Revises: e7f9d1c3b2a8
Create Date: 2024-08-28 13:00:00.000000

"""
from alembic import op
import logging
import sqlalchemy as sa

from app.etl import teacher_salary_band

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# Revision identifiers, used by Alembic
revision = 'f9c8d7b6e5a4'
down_revision = 'e7f9d1c3b2a8'
branch_labels = None
depends_on = None


def upgrade():
    """Load district teacher salary band data."""
    # Every year in app/alembic/config/district_teacher_salary_band_config.yaml
    teacher_salary_band.load(op.get_bind())

    # Create materialized view for state-level teacher salary band data
    # First, check if the materialized view already exists and drop it if it does
    op.execute(sa.text("""
        DROP MATERIALIZED VIEW IF EXISTS state_teacher_salary_band;
    """))

    # Create the materialized view
    op.execute(sa.text("""
        CREATE MATERIALIZED VIEW state_teacher_salary_band AS
        SELECT
            teacher_salary_band_type_id_fk, 
            year, 
            ROUND(AVG(min_salary)::numeric, 2) AS min_salary, 
            ROUND(AVG(max_salary)::numeric, 2) AS max_salary, 
            ROUND(AVG(steps)::numeric, 1) AS steps,
            CURRENT_TIMESTAMP AS date_created,
            CURRENT_TIMESTAMP AS date_updated
        FROM 
            district_teacher_salary_band dtsb
        GROUP BY teacher_salary_band_type_id_fk, year;
    """))

    # Create a unique index on the materialized view for faster refreshing
    op.execute(sa.text("""
        CREATE UNIQUE INDEX idx_state_teacher_salary_band_unique 
        ON state_teacher_salary_band (teacher_salary_band_type_id_fk, year);
    """))


def downgrade():
    """Remove district teacher salary band data."""
    logger.info("Starting District Teacher Salary Band Data migration downgrade")
    
    # Drop the materialized view first
    logger.info("Dropping materialized view for state_teacher_salary_band")
    op.execute("DROP MATERIALIZED VIEW IF EXISTS state_teacher_salary_band")
    
    # Remove all data from district_teacher_salary_band table
    logger.info("Removing data from district_teacher_salary_band table")
    op.execute("DELETE FROM district_teacher_salary_band")
    
    logger.info("Downgrade completed successfully") 