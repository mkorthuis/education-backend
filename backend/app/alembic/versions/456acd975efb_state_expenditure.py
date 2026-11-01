"""State Expenditure Import

Revision ID:456acd975efb
Revises: 234adb12cac2
Create Date: 2025-04-05 01:33:00.000000

"""
from alembic import op
import sqlalchemy as sa
import logging

from app.etl import state_expenditure

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# Revision identifiers, used by Alembic
revision = '456acd975efb'
down_revision = '234adb12cac2'
branch_labels = None
depends_on = None


def generate_table_creation_statements():
    """Generate SQL statements to create the necessary tables."""
    statements = []
    
    # Define tables
    tables = {
        'expenditure_state_total': {
            'id': 'SERIAL PRIMARY KEY',
            'year': 'INTEGER NOT NULL',
            'operating_elementary': 'NUMERIC(15,2)',
            'operating_middle': 'NUMERIC(15,2)',
            'operating_high': 'NUMERIC(15,2)',
            'operating_total': 'NUMERIC(15,2)',
            'current_elementary': 'NUMERIC(15,2)',
            'current_middle': 'NUMERIC(15,2)',
            'current_high': 'NUMERIC(15,2)',
            'current_total': 'NUMERIC(15,2)',
            'total': 'NUMERIC(15,2)',
            'date_created': 'TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP',
            'date_updated': 'TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP',
            'constraints': [
                'CONSTRAINT unique_expenditure_state_total_year UNIQUE (year)'
            ]
        },
        'state_enrollment': {
            'id': 'SERIAL PRIMARY KEY',
            'year': 'INTEGER NOT NULL',
            'elementary': 'NUMERIC(15,2)',
            'middle': 'NUMERIC(15,2)',
            'high': 'NUMERIC(15,2)',
            'total': 'NUMERIC(15,2)',
            'date_created': 'TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP',
            'date_updated': 'TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP',
            'constraints': [
                'CONSTRAINT unique_state_enrollment_year UNIQUE (year)'
            ]
        }
    }
    
    # Generate create table statements
    for table_name, columns in tables.items():
        column_defs = []
        constraints = columns.pop('constraints', [])
        
        for col_name, col_def in columns.items():
            column_defs.append(f"{col_name} {col_def}")
        
        # Add constraints
        column_defs.extend(constraints)
        
        # Create table statement
        create_table = f"CREATE TABLE {table_name} (\n    "
        create_table += ",\n    ".join(column_defs)
        create_table += "\n)"
        
        # Add to statements as single line
        statements.append(' '.join(line.strip() for line in create_table.split('\n')))
    
    # Create triggers for all tables
    for table in tables.keys():
        trigger_sql = f"""
        CREATE TRIGGER trigger_update_{table}_timestamp
        BEFORE UPDATE ON {table}
        FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
        """
        statements.append(' '.join(line.strip() for line in trigger_sql.strip().split('\n')))
    
    # Create indexes
    indexes = [
        "CREATE INDEX idx_expenditure_state_total_year ON expenditure_state_total(year)",
        "CREATE INDEX idx_state_enrollment_year ON state_enrollment(year)"
    ]
    
    statements.extend(indexes)
    
    return statements


def upgrade():
    """Alembic upgrade function to create tables and import state expenditure data."""
    for statement in generate_table_creation_statements():
        op.execute(sa.text(statement))

    # Every year in app/alembic/config/state_expenditure_config.yaml. The table is created here as
    # expenditure_state_total; 49358ad1275f renames it to expenditure_state_rollup.
    state_expenditure.load(op.get_bind(), expenditure_table='expenditure_state_total')


def downgrade():
    """Alembic downgrade function to remove state expenditure tables."""
    try:
        sql_statements = [
            "DROP TABLE IF EXISTS expenditure_state_total CASCADE",
            "DROP TABLE IF EXISTS state_enrollment CASCADE"
        ]
        
        for statement in sql_statements:
            op.execute(sa.text(statement))
            
        logger.info("Successfully dropped state expenditure tables")
    except Exception as e:
        logger.error(f"Error during downgrade: {e}")
        raise
