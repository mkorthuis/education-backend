"""School Safety Data Migration

Revision ID: 6ed3c152c0c2
Revises: 99baf2d34ef7
Create Date: 2025-04-10 19:19:30.724964

"""
from alembic import op
import sqlalchemy as sa
import logging

from app.etl import safety

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = '6ed3c152c0c2'
down_revision = '99baf2d34ef7'
branch_labels = None
depends_on = None


def upgrade():
    """Import school safety data from Excel files."""
    # Every year in app/alembic/config/generate_school_safety_data.yaml. The type tables still
    # have their school_* names here (bed3c152c0c7 renames them to safety_*), and the state and
    # district totals are created and filled by later migrations.
    safety.load(op.get_bind(), type_table_prefix="school_", rebuild_state_district=False)


def downgrade():
    """
    Remove all school safety data.
    """
    logger.info("Removing all school safety data")
    
    # List of tables in reverse order (to handle foreign keys)
    tables = [
        "school_seclusion",
        "school_restraint",
        "school_harassment",
        "school_bullying_impact",
        "school_bullying_classification",
        "school_bullying",
        "school_discipline_count",
        "school_discipline_incident",
        "school_safety",
        "school_truancy"
    ]
    
    # Truncate each table
    for table in tables:
        try:
            logger.info(f"Truncating table {table}")
            op.execute(sa.text(f"DELETE FROM {table};"))
        except Exception as e:
            logger.error(f"Error truncating table {table}: {e}")
            
    logger.info("School safety data removal completed successfully")
