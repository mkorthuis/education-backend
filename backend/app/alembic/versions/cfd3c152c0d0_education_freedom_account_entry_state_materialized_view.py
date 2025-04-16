"""Education Freedom Account Entry State Materialized View

Revision ID: cfd3c152c0d0
Revises: bfd3c152c0c9
Create Date: 2024-07-18 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes
import logging

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = 'cfd3c152c0d0'
down_revision = 'bfd3c152c0c9'
branch_labels = None
depends_on = None


def upgrade():
    """Create materialized view for Education Freedom Account Entry state-level data."""
    logger.info("Starting Education Freedom Account Entry State Materialized View migration upgrade")

    # Create education_freedom_account_entry_state materialized view
    logger.info("Creating education_freedom_account_entry_state materialized view")
    op.execute("""
        CREATE MATERIALIZED VIEW education_freedom_account_entry_state AS
        SELECT 
            year AS year, 
            education_freedom_account_entry_type_id_fk AS education_freedom_account_entry_type_id_fk, 
            SUM(value) AS value
        FROM
            education_freedom_account_entry
        GROUP BY 
            year, education_freedom_account_entry_type_id_fk
    """)

    # Add index for education_freedom_account_entry_state
    logger.info("Creating indices for education_freedom_account_entry_state")
    op.execute("""
        CREATE INDEX idx_efa_entry_state_year 
        ON education_freedom_account_entry_state (year)
    """)
    
    op.execute("""
        CREATE INDEX idx_efa_entry_state_type 
        ON education_freedom_account_entry_state (education_freedom_account_entry_type_id_fk)
    """)

    logger.info("Education Freedom Account Entry State Materialized View migration upgrade completed successfully")


def downgrade():
    """Drop the materialized view."""
    logger.info("Starting Education Freedom Account Entry State Materialized View migration downgrade")

    # Drop materialized view
    logger.info("Dropping materialized view education_freedom_account_entry_state")
    op.execute("DROP MATERIALIZED VIEW IF EXISTS education_freedom_account_entry_state")

    logger.info("Education Freedom Account Entry State Materialized View migration downgrade completed successfully") 