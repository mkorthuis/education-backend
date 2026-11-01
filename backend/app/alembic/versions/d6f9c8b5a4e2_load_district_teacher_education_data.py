"""Load District Teacher Education Data

Revision ID: d6f9c8b5a4e2
Revises: c5d7b9a8f2e3
Create Date: 2024-08-22 13:00:00.000000

"""
from alembic import op
import logging

from app.etl import teacher_education

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# Revision identifiers, used by Alembic
revision = 'd6f9c8b5a4e2'
down_revision = 'c5d7b9a8f2e3'
branch_labels = None
depends_on = None


def upgrade():
    """Load district teacher education data across multiple years."""
    # Every year in app/alembic/config/district_teacher_education_config.yaml
    teacher_education.load(op.get_bind())


def downgrade():
    """Remove district teacher education data and related objects."""
    logger.info("Starting District Teacher Education Data migration downgrade")
    
    # Remove all data from state_teacher_education table
    logger.info("Removing data from state_teacher_education table")
    op.execute("DELETE FROM state_teacher_education")
    
    # Remove all data from district_teacher_education table
    logger.info("Removing data from district_teacher_education table")
    op.execute("DELETE FROM district_teacher_education")
    
    logger.info("Downgrade completed successfully") 