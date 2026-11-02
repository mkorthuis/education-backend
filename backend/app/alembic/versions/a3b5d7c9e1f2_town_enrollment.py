"""Town Enrollment

Revision ID: a3b5d7c9e1f2
Revises: cfd3c152c0d0
Create Date: 2024-06-24 12:00:00.000000

"""
from alembic import op
import logging

from app.etl import town_enrollment

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# Revision identifiers, used by Alembic
revision = 'a3b5d7c9e1f2'
down_revision = 'cfd3c152c0d0'
branch_labels = None
depends_on = None


def upgrade():
    """Create town enrollment tables and load data."""
    logger.info("Starting Town Enrollment migration upgrade")
    
    # Create new town_enrollment table
    logger.info("Creating town_enrollment table")
    op.execute("""
        CREATE TABLE town_enrollment (
            id SERIAL PRIMARY KEY,
            town_id_fk INTEGER NOT NULL,
            grade_id_fk INTEGER NOT NULL,
            year INTEGER NOT NULL,
            enrollment INTEGER NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_town_enrollment_town
                FOREIGN KEY (town_id_fk)
                REFERENCES town(id)
                ON DELETE CASCADE,
            CONSTRAINT fk_town_enrollment_grade
                FOREIGN KEY (grade_id_fk)
                REFERENCES grades(id)
                ON DELETE CASCADE,
            CONSTRAINT unique_town_grade_year
                UNIQUE (town_id_fk, grade_id_fk, year)
        )
    """)
    
    # Create indexes
    logger.info("Creating indexes for town_enrollment table")
    op.execute("CREATE INDEX idx_town_enrollment_town ON town_enrollment(town_id_fk)")
    op.execute("CREATE INDEX idx_town_enrollment_grade ON town_enrollment(grade_id_fk)")
    op.execute("CREATE INDEX idx_town_enrollment_year ON town_enrollment(year)")
    
    # Create trigger
    logger.info("Creating trigger for town_enrollment table")
    op.execute("""
        CREATE TRIGGER trigger_update_town_enrollment_timestamp
        BEFORE UPDATE ON town_enrollment
        FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
    """)
    
    # Every year in app/alembic/config/generate_town_enrollments.yaml
    logger.info("Loading town enrollment data")
    town_enrollment.load(op.get_bind())

    # Create materialized view after data is loaded
    logger.info("Creating town_enrollment_state materialized view")
    op.execute("""
        CREATE MATERIALIZED VIEW town_enrollment_state AS
        SELECT
            year, 
            grade_id_fk, 
            SUM(enrollment) as total_enrollment
        FROM 
            town_enrollment
        GROUP BY 
            year, grade_id_fk
        ORDER BY
            year DESC, grade_id_fk
    """)
    logger.info("Successfully created town_enrollment_state materialized view")
    
    # Create an index on the materialized view for better query performance
    logger.info("Creating indexes on town_enrollment_state materialized view")
    op.execute("CREATE INDEX idx_town_enrollment_state_year ON town_enrollment_state(year)")
    op.execute("CREATE INDEX idx_town_enrollment_state_grade ON town_enrollment_state(grade_id_fk)")
    # One row per year and grade; unique, so the ETL can refresh the view CONCURRENTLY (without blocking reads)
    op.execute("CREATE UNIQUE INDEX idx_town_enrollment_state_year_grade ON town_enrollment_state(year, grade_id_fk)")
    logger.info("Successfully created indexes on town_enrollment_state materialized view")
    
    logger.info("Migration completed successfully")


def downgrade():
    """Drop town enrollment tables and related objects."""
    logger.info("Starting Town Enrollment migration downgrade")
    
    # Drop the materialized view first
    logger.info("Dropping town_enrollment_state materialized view")
    op.execute("DROP MATERIALIZED VIEW IF EXISTS town_enrollment_state CASCADE")
    
    # Drop town_enrollment table
    logger.info("Dropping town_enrollment table")
    op.execute("DROP TABLE IF EXISTS town_enrollment CASCADE")
    
    logger.info("Downgrade completed successfully") 