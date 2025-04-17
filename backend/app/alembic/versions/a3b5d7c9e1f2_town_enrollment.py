"""Town Enrollment

Revision ID: a3b5d7c9e1f2
Revises: cfd3c152c0d0
Create Date: 2024-06-24 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
import logging
import pandas as pd
import yaml
import re
import os
from datetime import datetime

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# Revision identifiers, used by Alembic
revision = 'a3b5d7c9e1f2'
down_revision = 'cfd3c152c0d0'
branch_labels = None
depends_on = None


def load_config():
    """Load configuration from YAML file."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.abspath(os.path.join(current_dir, '../config/generate_town_enrollments.yaml'))
    logger.info(f"Attempting to load configuration from: {config_path}")
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
            logger.info(f"Successfully loaded configuration: {config}")
            return config
    except Exception as e:
        logger.error(f"Error loading configuration: {e}")
        logger.error(f"Does the file exist? {os.path.exists(config_path)}")
        
        # If config file doesn't exist, create default config
        default_config = {
            'file_settings': {
                'default_input': '../assets/town-enrollments/****-Town Level Enrollment By Grade.xlsx',
                'year_start': 2012,
                'year_end': 2025,
                'sql_cache_dir': '../sql_cache'
            }
        }
        
        # Create the config directory if it doesn't exist
        config_dir = os.path.dirname(config_path)
        os.makedirs(config_dir, exist_ok=True)
        
        # Write the default config
        try:
            with open(config_path, 'w') as f:
                yaml.dump(default_config, f)
            logger.info(f"Created default configuration file at: {config_path}")
            return default_config
        except Exception as write_error:
            logger.error(f"Error creating default configuration: {write_error}")
            raise
        
        raise Exception(f"Error loading configuration: {e}")


def clean_value(value):
    """Clean numeric values by removing $, commas, etc."""
    if pd.isna(value) or value == "":
        return None
    
    value_str = str(value)
    
    # Remove non-numeric characters except decimal point
    cleaned = re.sub(r'[^0-9.-]', '', value_str)
    
    return cleaned if cleaned != "" else None


def process_town_enrollments(df, year):
    """Process town enrollment data from Excel file."""
    logger.info(f"Processing town enrollments for year {year} with DataFrame shape: {df.shape}")
    enrollments = []
    
    # Map columns to grade IDs (grade_id_fk values)
    # Column C = grade_id_fk 2, Column D = grade_id_fk 3, etc.
    # We'll programmatically create this mapping from column index to grade ID
    grade_column_map = {}
    for col_idx in range(2, 15):  # Column C (index 2) to Column O (index 14)
        grade_id = col_idx  # This follows the pattern you specified
        grade_column_map[col_idx] = grade_id
    
    logger.info(f"Grade column mapping: {grade_column_map}")
    
    # Find rows where column A has an integer value
    town_count = 0
    enrollment_count = 0
    
    # Log all column names to help debug
    logger.info(f"Available columns in DataFrame: {df.columns.tolist()}")
    
    for index, row in df.iterrows():
        town_id = row.iloc[0]  # Column A (0-indexed is 0)
        
        if pd.notna(town_id) and isinstance(town_id, (int, float)) and town_id == int(town_id):
            town_id = int(town_id)
            town_count += 1
            logger.debug(f"Processing town ID {town_id} at row {index}")
            
            # Process enrollment data for each grade
            for col_idx, grade_id in grade_column_map.items():
                if col_idx < len(row):
                    enrollment_value = row.iloc[col_idx]
                    
                    # Check if enrollment value is valid
                    if pd.notna(enrollment_value) and enrollment_value != "" and enrollment_value != 0:
                        try:
                            enrollment_int = int(float(enrollment_value))
                            
                            enrollment = {
                                'town_id': town_id,
                                'grade_id': grade_id,
                                'year': year,
                                'enrollment': enrollment_int
                            }
                            
                            enrollments.append(enrollment)
                            enrollment_count += 1
                        except (ValueError, TypeError) as e:
                            logger.warning(f"Invalid enrollment value '{enrollment_value}' for town {town_id}, grade {grade_id}, year {year}: {e}")
    
    logger.info(f"Processed {town_count} towns with a total of {enrollment_count} enrollments for year {year}")
    return enrollments


def generate_sql(town_enrollments):
    """Generate SQL INSERT statements for town enrollments."""
    logger.info(f"Generating SQL statements for {len(town_enrollments)} town enrollments")
    sql_statements = []
    
    # Town enrollment inserts
    sql_statements.append("-- Insert town enrollments")
    
    valid_enrollments = 0
    skipped_enrollments = 0
    towns_with_data = set()
    
    for enrollment in town_enrollments:
        # Check if town exists
        exists_check = sa.text("""
            SELECT EXISTS (
                SELECT 1 FROM town WHERE id = :town_id
            )
        """)
        town_exists = op.get_bind().execute(exists_check, {"town_id": enrollment['town_id']}).scalar()
        
        # Check if grade exists
        grade_check = sa.text("""
            SELECT EXISTS (
                SELECT 1 FROM grades WHERE id = :grade_id
            )
        """)
        grade_exists = op.get_bind().execute(grade_check, {"grade_id": enrollment['grade_id']}).scalar()
        
        if town_exists and grade_exists:
            sql_statements.append(f"""INSERT INTO town_enrollment (town_id_fk, grade_id_fk, year, enrollment, date_created, date_updated) VALUES ({enrollment['town_id']}, {enrollment['grade_id']}, {enrollment['year']}, {enrollment['enrollment']}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);""")
            towns_with_data.add(enrollment['town_id'])
            valid_enrollments += 1
        else:
            if not town_exists:
                logger.warning(f"Town ID {enrollment['town_id']} for year {enrollment['year']} not found in database, skipping enrollment")
            if not grade_exists:
                logger.warning(f"Grade ID {enrollment['grade_id']} for year {enrollment['year']} not found in database, skipping enrollment")
            skipped_enrollments += 1
    
    logger.info(f"Generated {valid_enrollments} valid town enrollment statements for {len(towns_with_data)} unique towns")
    logger.info(f"Skipped {skipped_enrollments} enrollments due to missing town IDs or grade IDs")
    
    return "\n".join(sql_statements)


def upgrade():
    """Create town enrollment tables and load data."""
    logger.info("Starting Town Enrollment migration upgrade")
    
    # Create new town_enrollment table
    logger.info("Creating town_enrollment table")
    op.execute("""
        CREATE TABLE town_enrollment (
            id SERIAL PRIMARY KEY,
            town_id_fk INTEGER NOT NULL,
            grade_id_fk INTEGER NOT NULL,
            year INTEGER NOT NULL,
            enrollment INTEGER NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_town_enrollment_town
                FOREIGN KEY (town_id_fk)
                REFERENCES town(id)
                ON DELETE CASCADE,
            CONSTRAINT fk_town_enrollment_grade
                FOREIGN KEY (grade_id_fk)
                REFERENCES grades(id)
                ON DELETE CASCADE,
            CONSTRAINT unique_town_grade_year
                UNIQUE (town_id_fk, grade_id_fk, year)
        )
    """)
    
    # Create indexes
    logger.info("Creating indexes for town_enrollment table")
    op.execute("CREATE INDEX idx_town_enrollment_town ON town_enrollment(town_id_fk)")
    op.execute("CREATE INDEX idx_town_enrollment_grade ON town_enrollment(grade_id_fk)")
    op.execute("CREATE INDEX idx_town_enrollment_year ON town_enrollment(year)")
    
    # Create trigger
    logger.info("Creating trigger for town_enrollment table")
    op.execute("""
        CREATE TRIGGER trigger_update_town_enrollment_timestamp
        BEFORE UPDATE ON town_enrollment
        FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
    """)
    
    # Load and process data from Excel files
    logger.info("Starting data loading process")
    
    try:
        logger.info("Loading configuration")
        config = load_config()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Check for existing cache file first
        cache_dir = os.path.abspath(os.path.join(current_dir, config['file_settings']['sql_cache_dir']))
        cache_file = os.path.join(cache_dir, f'{revision}_cache.sql')
        logger.info(f"Cache directory path: {cache_dir}")
        logger.info(f"Cache file path: {cache_file}")
        
        if os.path.exists(cache_file):
            logger.info(f"Found existing SQL cache file at: {cache_file}")
            with open(cache_file, 'r') as f:
                sql_statements = f.read()
            logger.info(f"Loaded cached SQL statements ({os.path.getsize(cache_file)} bytes)")
        else:
            logger.info("No cache file found, processing input files")
            # Process input files
            all_town_enrollments = []
            
            # Get the base pattern for input files
            input_pattern = config['file_settings']['default_input']
            base_dir = os.path.abspath(os.path.join(current_dir, os.path.dirname(input_pattern)))
            base_pattern = os.path.basename(input_pattern)
            
            logger.info(f"Input pattern: {input_pattern}")
            logger.info(f"Base directory: {base_dir}")
            logger.info(f"Base pattern: {base_pattern}")
            
            # Remove asterisks and get the pattern parts
            pattern_parts = base_pattern.split('****')
            logger.info(f"Pattern parts: {pattern_parts}")
            
            # Generate file paths for each year
            year_start = config['file_settings']['year_start']
            year_end = config['file_settings']['year_end']
            logger.info(f"Processing years from {year_start} to {year_end}")
            
            found_files = 0
            
            for year in range(year_start, year_end+1):
                file_pattern = f"{pattern_parts[0]}{year}{pattern_parts[1] if len(pattern_parts) > 1 else ''}"
                file_path = os.path.join(base_dir, file_pattern)
                
                logger.info(f"Looking for year {year} file at: {file_path}")
                
                # Check if the file exists
                if os.path.exists(file_path):
                    found_files += 1
                    logger.info(f"Found input file for year {year}: {file_path}")
                    
                    # Load the Excel file
                    try:
                        logger.info(f"Loading Excel file: {file_path}")
                        df = pd.read_excel(file_path)
                        logger.info(f"Successfully loaded Excel file with shape: {df.shape}")
                        
                        # Process town enrollments for this file
                        logger.info(f"Processing town enrollments for year {year}")
                        town_enrollments = process_town_enrollments(df, year)
                        logger.info(f"Found {len(town_enrollments)} town enrollments for year {year}")
                        all_town_enrollments.extend(town_enrollments)
                    except Exception as e:
                        logger.error(f"Error processing Excel file {file_path}: {e}")
                        raise
                else:
                    logger.warning(f"File not found for year {year}: {file_path}")
            
            logger.info(f"Processed {found_files} files out of {year_end - year_start + 1} possible years")
            logger.info(f"Total town enrollments found: {len(all_town_enrollments)}")
            
            if len(all_town_enrollments) == 0:
                logger.error("No town enrollments were found! Check file paths and Excel structure.")
            
            # Generate SQL with combined data
            logger.info("Generating SQL statements")
            sql_statements = generate_sql(all_town_enrollments)
            
            # Save to cache
            logger.info(f"Creating cache directory: {cache_dir}")
            os.makedirs(cache_dir, exist_ok=True)
            logger.info(f"Writing SQL cache to: {cache_file}")
            with open(cache_file, 'w') as f:
                f.write(sql_statements)
            logger.info(f"Successfully created SQL cache file ({os.path.getsize(cache_file)} bytes)")
        
        # Execute SQL statements
        logger.info("Starting SQL execution")
        statement_count = sql_statements.count(';')
        logger.info(f"Found approximately {statement_count} SQL statements to execute")
        
        executed = 0
        skipped = 0
        
        for statement in sql_statements.split(';'):
            statement = statement.strip()
            if not statement:  # Skip empty statements
                continue
                
            try:
                # Execute the SQL statement
                op.execute(sa.text(statement))
                executed += 1
                if executed % 100 == 0:
                    logger.info(f"Executed {executed} statements so far")
            except Exception as e:
                if "duplicate key" in str(e).lower():
                    logger.warning(f"Skipped duplicate key: {str(e)[:100]}")
                    skipped += 1
                else:
                    logger.error(f"Error executing SQL statement: {e}")
                    logger.error(f"Statement: {statement[:300]}...")
                    raise
            
        logger.info(f"SQL execution complete: {executed} statements executed, {skipped} skipped")
        
        # Create materialized view after data is loaded
        logger.info("Creating town_enrollment_state materialized view")
        op.execute("""
            CREATE MATERIALIZED VIEW town_enrollment_state AS
            SELECT
                year, 
                grade_id_fk, 
                SUM(enrollment) as total_enrollment
            FROM 
                town_enrollment
            GROUP BY 
                year, grade_id_fk
            ORDER BY
                year DESC, grade_id_fk
        """)
        logger.info("Successfully created town_enrollment_state materialized view")
        
        # Create an index on the materialized view for better query performance
        logger.info("Creating indexes on town_enrollment_state materialized view")
        op.execute("CREATE INDEX idx_town_enrollment_state_year ON town_enrollment_state(year)")
        op.execute("CREATE INDEX idx_town_enrollment_state_grade ON town_enrollment_state(grade_id_fk)")
        logger.info("Successfully created indexes on town_enrollment_state materialized view")
        
    except Exception as e:
        logger.error(f"Critical error during migration: {e}")
        raise Exception(f"Error during migration: {e}")
    
    logger.info("Migration completed successfully")


def downgrade():
    """Drop town enrollment tables and related objects."""
    logger.info("Starting Town Enrollment migration downgrade")
    
    # Drop the materialized view first
    logger.info("Dropping town_enrollment_state materialized view")
    op.execute("DROP MATERIALIZED VIEW IF EXISTS town_enrollment_state CASCADE")
    
    # Drop town_enrollment table
    logger.info("Dropping town_enrollment table")
    op.execute("DROP TABLE IF EXISTS town_enrollment CASCADE")
    
    logger.info("Downgrade completed successfully") 