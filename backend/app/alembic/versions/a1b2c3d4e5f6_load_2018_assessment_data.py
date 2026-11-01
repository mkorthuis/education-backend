"""Load 2018 Assessment Data

Revision ID: a1b2c3d4e5f6
Revises: f9c8d7b6e5a4
Create Date: 2023-07-20 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
import logging

from app.etl import assessment

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# Revision identifiers, used by Alembic
revision = 'a1b2c3d4e5f6'
down_revision = 'f9c8d7b6e5a4'
branch_labels = None
depends_on = None


def upgrade():
    """Alembic upgrade function to load 2018 assessment data."""
    assessment.load_files(op.get_bind(), [assessment.YEAR_2018])


def downgrade():
    """Alembic downgrade function to remove 2018 assessment data."""
    try:
        # Delete 2018 assessment data
        sql_statements = [
            "DELETE FROM assessment_school WHERE year = 2018",
            "DELETE FROM assessment_district WHERE year = 2018",
            "DELETE FROM assessment_state WHERE year = 2018"
        ]
        
        for statement in sql_statements:
            op.execute(sa.text(statement))
            
        logger.info("Successfully deleted 2018 assessment data")
    except Exception as e:
        logger.error("Error during downgrade: {}".format(e))
        raise 