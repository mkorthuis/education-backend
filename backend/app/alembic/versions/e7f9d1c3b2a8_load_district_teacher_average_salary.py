"""Load District Teacher Average Salary Data

Revision ID: e7f9d1c3b2a8
Revises: d6f9c8b5a4e2
Create Date: 2024-08-25 13:00:00.000000

"""
from alembic import op
import logging

from app.etl import teacher_salary

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# Revision identifiers, used by Alembic
revision = 'e7f9d1c3b2a8'
down_revision = 'd6f9c8b5a4e2'
branch_labels = None
depends_on = None


def upgrade():
    """Load district teacher average salary data across multiple years."""
    # Every year in app/alembic/config/district_teacher_salary_config.yaml
    teacher_salary.load(op.get_bind())


def downgrade():
    """Remove district teacher average salary data and related objects."""
    logger.info("Starting District Teacher Average Salary Data migration downgrade")
    
    # Remove all data from state_teacher_average_salary table
    logger.info("Removing data from state_teacher_average_salary table")
    op.execute("DELETE FROM state_teacher_average_salary")
    
    # Remove all data from district_teacher_average_salary table
    logger.info("Removing data from district_teacher_average_salary table")
    op.execute("DELETE FROM district_teacher_average_salary")
    
    logger.info("Downgrade completed successfully") 