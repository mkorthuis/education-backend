"""Load Historical Assessment Data (2009-2017)

Revision ID: b2c3d4e5f6a7
Revises: a1b2c3d4e5f6
Create Date: 2023-07-21 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
import logging

from app.etl import assessment
from app.etl.core import load_config

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# Revision identifiers, used by Alembic
revision = 'b2c3d4e5f6a7'
down_revision = 'a1b2c3d4e5f6'
branch_labels = None
depends_on = None


def upgrade():
    """Alembic upgrade function to load historical assessment data."""
    # Every year in app/alembic/config/assessment_historical_data_config.yaml (school rows only)
    assessment.load_files(op.get_bind(), assessment.historical_years())


def downgrade():
    """Alembic downgrade function to remove historical assessment data."""
    try:
        # Load configuration to get year range
        config = load_config(assessment.HISTORICAL_CONFIG)
        year_start = int(config['file_settings']['year_start'])
        year_end = int(config['file_settings']['year_end'])
        
        # Build delete statements for each year
        delete_statements = []
        for year in range(year_start, year_end + 1):
            delete_statements.extend([
                "DELETE FROM assessment_school WHERE year = {}".format(year),
                "DELETE FROM assessment_district WHERE year = {}".format(year),
                "DELETE FROM assessment_state WHERE year = {}".format(year)
            ])
        
        # Execute delete statements
        for statement in delete_statements:
            op.execute(sa.text(statement))
            
        logger.info("Successfully deleted historical assessment data for years {}-{}".format(
            year_start, year_end))
    except Exception as e:
        logger.error("Error during downgrade: {}".format(e))
        raise 