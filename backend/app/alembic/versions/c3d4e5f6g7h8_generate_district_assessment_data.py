"""Generate District Assessment Data (2009-2017)

Revision ID: c3d4e5f6g7h8
Revises: b2c3d4e5f6a7
Create Date: 2023-07-22 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
import logging

from app.etl import assessment

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# Revision identifiers, used by Alembic
revision = 'c3d4e5f6g7h8'
down_revision = 'b2c3d4e5f6a7'
branch_labels = None
depends_on = None


def upgrade():
    """Upgrade function that generates district assessment data from the school rows."""
    assessment.generate_district_rows(op.get_bind(), range(2009, 2018))  # 2009 to 2017


def downgrade():
    """Downgrade function to remove generated district assessment data."""
    try:
        conn = op.get_bind()
        
        # Delete generated district data for 2009-2017
        delete_sql = """
        DELETE FROM assessment_district
        WHERE year BETWEEN 2009 AND 2017
        """
        
        conn.execute(sa.text(delete_sql))
        logger.info("Successfully removed generated district assessment data for years 2009-2017")
        
    except Exception as e:
        logger.error(f"Error during downgrade: {e}")
        raise 