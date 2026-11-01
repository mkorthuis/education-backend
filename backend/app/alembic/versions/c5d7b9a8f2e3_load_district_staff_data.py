"""Load District Staff Data

Revision ID: c5d7b9a8f2e3
Revises: b5c8d9e7f3a1
Create Date: 2024-08-20 13:00:00.000000

"""
from alembic import op
import logging

from app.etl import staff

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# Revision identifiers, used by Alembic
revision = 'c5d7b9a8f2e3'
down_revision = 'b5c8d9e7f3a1'
branch_labels = None
depends_on = None


def upgrade():
    """Load district staff data across multiple years."""
    # Every year in app/alembic/config/district_staff_config.yaml
    staff.load(op.get_bind())


def downgrade():
    """Remove district staff data and related objects."""
    logger.info("Starting District Staff Data migration downgrade")
    
    # Remove all data from state_staff table
    logger.info("Removing data from state_staff table")
    op.execute("DELETE FROM state_staff")
    
    # Remove all data from district_staff table
    logger.info("Removing data from district_staff table")
    op.execute("DELETE FROM district_staff")
    
    logger.info("Downgrade completed successfully") 