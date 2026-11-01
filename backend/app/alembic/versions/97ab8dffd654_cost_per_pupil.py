"""Cost Per Pupil Data Import

Revision ID: 97ab8dffd654
Revises: 65ab32afd32c
Create Date: 2025-04-05 01:33:00.000000

"""
from alembic import op
import sqlalchemy as sa
import logging

from app.etl import cost_per_pupil

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# Revision identifiers, used by Alembic
revision = '97ab8dffd654'
down_revision = '65ab32afd32c'
branch_labels = None
depends_on = None


def generate_table_creation_statements():
    """Generate SQL statements to create the necessary tables."""
    statements = []
    
    # District cost per pupil table
    statements.append("CREATE TABLE district_cost_per_pupil (id SERIAL PRIMARY KEY, district_id_fk INTEGER NOT NULL, year INTEGER NOT NULL, elementary INTEGER, middle INTEGER, high INTEGER, total INTEGER, date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, CONSTRAINT fk_district_cost_per_pupil FOREIGN KEY (district_id_fk) REFERENCES district(id) ON DELETE CASCADE, CONSTRAINT unique_district_cost_per_pupil_year UNIQUE (district_id_fk, year))")
    
    # State cost per pupil table
    statements.append("CREATE TABLE state_cost_per_pupil (id SERIAL PRIMARY KEY, year INTEGER NOT NULL, elementary INTEGER, middle INTEGER, high INTEGER, total INTEGER, date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, CONSTRAINT unique_state_cost_per_pupil_year UNIQUE (year))")
    
    # Triggers for timestamp updates
    statements.append("CREATE TRIGGER trigger_update_district_cost_per_pupil_timestamp BEFORE UPDATE ON district_cost_per_pupil FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()")
    
    statements.append("CREATE TRIGGER trigger_update_state_cost_per_pupil_timestamp BEFORE UPDATE ON state_cost_per_pupil FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()")
    
    # Indexes for performance
    statements.append("CREATE INDEX idx_district_cost_per_pupil_district ON district_cost_per_pupil(district_id_fk)")
    statements.append("CREATE INDEX idx_district_cost_per_pupil_year ON district_cost_per_pupil(year)")
    statements.append("CREATE INDEX idx_state_cost_per_pupil_year ON state_cost_per_pupil(year)")
    
    return statements


def upgrade():
    """Alembic upgrade function to create tables and import cost per pupil data."""
    for statement in generate_table_creation_statements():
        op.execute(sa.text(statement))

    # Every year in app/alembic/config/generate_cost_per_pupil_config.yaml
    cost_per_pupil.load(op.get_bind())


def downgrade():
    """Alembic downgrade function to remove cost per pupil tables."""
    try:
        sql_statements = [
            "DROP TABLE IF EXISTS district_cost_per_pupil CASCADE",
            "DROP TABLE IF EXISTS state_cost_per_pupil CASCADE"
        ]
        
        for statement in sql_statements:
            op.execute(sa.text(statement))
            
        logger.info("Successfully dropped cost per pupil tables")
    except Exception as e:
        logger.error(f"Error during downgrade: {e}")
        raise
