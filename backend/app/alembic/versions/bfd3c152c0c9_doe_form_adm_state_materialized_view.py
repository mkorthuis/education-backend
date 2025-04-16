"""DOE Form ADM State Materialized View

Revision ID: bfd3c152c0c9
Revises: afd3c152c0c8
Create Date: 2024-07-17 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes
import logging

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = 'bfd3c152c0c9'
down_revision = 'afd3c152c0c8'
branch_labels = None
depends_on = None


def upgrade():
    """Create materialized view for DOE Form ADM state-level data."""
    logger.info("Starting DOE Form ADM State Materialized View migration upgrade")

    # Create doe_form_adm_state materialized view
    logger.info("Creating doe_form_adm_state materialized view")
    op.execute("""
        CREATE MATERIALIZED VIEW doe_form_adm_state AS
        SELECT
            df.year AS year,
            SUM(dfa.elementary) AS elementary,
            SUM(dfa.middle) AS middle,
            SUM(dfa.high) AS high,
            SUM(dfa.total) AS total
        FROM
            doe_form_adm dfa
        JOIN 
            doe_form df ON dfa.doe_form_id_fk = df.id
        GROUP BY 
            df.year
    """)

    # Add index for doe_form_adm_state
    logger.info("Creating index for doe_form_adm_state")
    op.execute("""
        CREATE INDEX idx_doe_form_adm_state_year 
        ON doe_form_adm_state (year)
    """)

    logger.info("DOE Form ADM State Materialized View migration upgrade completed successfully")


def downgrade():
    """Drop the materialized view."""
    logger.info("Starting DOE Form ADM State Materialized View migration downgrade")

    # Drop materialized view
    logger.info("Dropping materialized view doe_form_adm_state")
    op.execute("DROP MATERIALIZED VIEW IF EXISTS doe_form_adm_state")

    logger.info("DOE Form ADM State Materialized View migration downgrade completed successfully") 