"""Assessment Data Import

Revision ID:234adb12cac2
Revises: 97ab8dffd654
Create Date: 2025-04-05 01:33:00.000000

"""
from alembic import op
import sqlalchemy as sa
import logging

from app.etl import assessment

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# Revision identifiers, used by Alembic
revision = '234adb12cac2'
down_revision = '97ab8dffd654'
branch_labels = None
depends_on = None


def generate_table_creation_statements():
    """Generate SQL statements to create the necessary tables."""
    statements = []
    
    # Create enum for assessment exceptions
    enum_sql = "CREATE TYPE assessment_exception AS ENUM ('TOO_FEW_SAMPLES', 'SCORE_UNDER_10', 'SCORE_OVER_90')"
    statements.append(enum_sql)
    
    # Define common columns for assessment tables
    common_assessment_columns = {
        'assessment_subject_id_fk': 'INTEGER NOT NULL',
        'year': 'INTEGER NOT NULL',
        'grade_id_fk': 'INTEGER',
        'assessment_subgroup_id_fk': 'INTEGER NOT NULL',
        'total_fay_students_low': 'INTEGER',
        'total_fay_students_high': 'INTEGER',
        'level_1_percentage': 'DECIMAL(5,2)',
        'level_1_percentage_exception': 'assessment_exception',
        'level_2_percentage': 'DECIMAL(5,2)',
        'level_2_percentage_exception': 'assessment_exception',
        'level_3_percentage': 'DECIMAL(5,2)',
        'level_3_percentage_exception': 'assessment_exception',
        'level_4_percentage': 'DECIMAL(5,2)',
        'level_4_percentage_exception': 'assessment_exception',
        'above_proficient_percentage': 'DECIMAL(5,2)',
        'above_proficient_percentage_exception': 'assessment_exception',
        'participate_percentage': 'DECIMAL(5,2)',
        'mean_sgp': 'DECIMAL(5,2)',
        'average_score': 'DECIMAL(7,2)',
        'date_created': 'TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP',
        'date_updated': 'TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP'
    }
    
    # Common constraints template for foreign key references
    common_fk_constraints = [
        'CONSTRAINT fk_{table}_subject FOREIGN KEY (assessment_subject_id_fk) REFERENCES assessment_subject(id) ON DELETE CASCADE',
        'CONSTRAINT fk_{table}_grade FOREIGN KEY (grade_id_fk) REFERENCES grades(id) ON DELETE CASCADE',
        'CONSTRAINT fk_{table}_subgroup FOREIGN KEY (assessment_subgroup_id_fk) REFERENCES assessment_subgroup(id) ON DELETE CASCADE'
    ]
    
    # Define table structures
    tables = {
        'assessment_subject': {
            'id': 'SERIAL PRIMARY KEY',
            'name': 'VARCHAR(100) NOT NULL',
            'description': 'VARCHAR(255)',
            'date_created': 'TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP',
            'date_updated': 'TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP'
        },
        'assessment_subgroup': {
            'id': 'SERIAL PRIMARY KEY',
            'name': 'VARCHAR(100) NOT NULL',
            'description': 'VARCHAR(255)',
            'date_created': 'TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP',
            'date_updated': 'TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP'
        },
        'assessment_district': {
            'id': 'SERIAL PRIMARY KEY',
            'district_id_fk': 'INTEGER NOT NULL',
            **common_assessment_columns,
            'constraints': [
                'CONSTRAINT fk_assessment_district_district FOREIGN KEY (district_id_fk) REFERENCES district(id) ON DELETE CASCADE',
                *[c.format(table='assessment_district') for c in common_fk_constraints],
                'CONSTRAINT unique_district_assessment UNIQUE (district_id_fk, assessment_subject_id_fk, year, grade_id_fk, assessment_subgroup_id_fk)'
            ]
        },
        'assessment_school': {
            'id': 'SERIAL PRIMARY KEY',
            'school_id_fk': 'INTEGER NOT NULL',
            **common_assessment_columns,
            'constraints': [
                'CONSTRAINT fk_assessment_school_school FOREIGN KEY (school_id_fk) REFERENCES school(id) ON DELETE CASCADE',
                *[c.format(table='assessment_school') for c in common_fk_constraints],
                'CONSTRAINT unique_school_assessment UNIQUE (school_id_fk, assessment_subject_id_fk, year, grade_id_fk, assessment_subgroup_id_fk)'
            ]
        },
        'assessment_state': {
            'id': 'SERIAL PRIMARY KEY',
            **common_assessment_columns,
            'constraints': [
                *[c.format(table='assessment_state') for c in common_fk_constraints],
                'CONSTRAINT unique_state_assessment UNIQUE (assessment_subject_id_fk, year, grade_id_fk, assessment_subgroup_id_fk)'
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
    
    # Create initial assessment_subject entries
    subject_entries_sql = """
    INSERT INTO assessment_subject (id, name, description) VALUES 
    (1, 'mat', 'Math'),
    (2, 'rea', 'Reading'),
    (3, 'sci', 'Science')
    """
    statements.append(' '.join(line.strip() for line in subject_entries_sql.strip().split('\n')))
    
    # Create triggers for all tables
    tables = [
        'assessment_subject', 
        'assessment_subgroup', 
        'assessment_district', 
        'assessment_school', 
        'assessment_state'
    ]
    
    for table in tables:
        trigger_sql = f"""
        CREATE TRIGGER trigger_update_{table}_timestamp
        BEFORE UPDATE ON {table}
        FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
        """
        statements.append(' '.join(line.strip() for line in trigger_sql.strip().split('\n')))
    
    # Define index patterns
    index_patterns = {
        'assessment_district': [
            ('district', 'district_id_fk'),
            ('subject', 'assessment_subject_id_fk'),
            ('year', 'year'),
            ('grade', 'grade_id_fk'),
            ('subgroup', 'assessment_subgroup_id_fk')
        ],
        'assessment_school': [
            ('school', 'school_id_fk'),
            ('subject', 'assessment_subject_id_fk'),
            ('year', 'year'),
            ('grade', 'grade_id_fk'),
            ('subgroup', 'assessment_subgroup_id_fk')
        ],
        'assessment_state': [
            ('subject', 'assessment_subject_id_fk'),
            ('year', 'year'),
            ('grade', 'grade_id_fk'),
            ('subgroup', 'assessment_subgroup_id_fk')
        ]
    }
    
    # Create indexes for all foreign keys and commonly queried columns
    indexes = []
    for table, patterns in index_patterns.items():
        for name_suffix, column in patterns:
            indexes.append(f"CREATE INDEX idx_{table}_{name_suffix} ON {table}({column})")
    
    statements.extend(indexes)
    
    return statements


def upgrade():
    """Alembic upgrade function to create tables and import assessment data."""
    for statement in generate_table_creation_statements():
        op.execute(sa.text(statement))

    # Every year in app/alembic/config/assessment_data_config.yaml (2019 on)
    assessment.load_files(op.get_bind(), assessment.current_years())


def downgrade():
    """Alembic downgrade function to remove assessment tables."""
    try:
        sql_statements = [
            "DROP TABLE IF EXISTS assessment_district CASCADE",
            "DROP TABLE IF EXISTS assessment_school CASCADE",
            "DROP TABLE IF EXISTS assessment_state CASCADE",
            "DROP TABLE IF EXISTS assessment_subgroup CASCADE",
            "DROP TABLE IF EXISTS assessment_subject CASCADE",
            "DROP TYPE IF EXISTS assessment_exception CASCADE"
        ]
        
        for statement in sql_statements:
            op.execute(sa.text(statement))
            
        logger.info("Successfully dropped assessment tables")
    except Exception as e:
        logger.error(f"Error during downgrade: {e}")
        raise