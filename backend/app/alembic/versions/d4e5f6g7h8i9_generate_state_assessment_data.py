"""Generate State Assessment Data (2009-2017)

Revision ID: d4e5f6g7h8i9
Revises: c3d4e5f6g7h8
Create Date: 2023-07-23 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
import logging

from app.etl import assessment

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# Revision identifiers, used by Alembic
revision = 'd4e5f6g7h8i9'
down_revision = 'c3d4e5f6g7h8'
branch_labels = None
depends_on = None


def upgrade():
    """Upgrade function to generate state assessment data from the district rows."""
    assessment.generate_state_rows(op.get_bind(), range(2009, 2018))  # 2009 to 2017


def downgrade():
    """Downgrade function to remove generated state assessment data."""
    try:
        conn = op.get_bind()
        
        # Delete generated state data for 2009-2017
        delete_sql = """
        DELETE FROM assessment_state
        WHERE year BETWEEN 2009 AND 2017
        """
        
        conn.execute(sa.text(delete_sql))
        logger.info("Successfully removed generated state assessment data for years 2009-2017")
        
    except Exception as e:
        logger.error(f"Error during downgrade: {e}")
        raise 