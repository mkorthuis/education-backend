"""Load District Teacher Salary Band Data

Revision ID: f9c8d7b6e5a4
Revises: e7f9d1c3b2a8
Create Date: 2024-08-28 13:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
import pandas as pd
import os
import yaml
import logging
import re
import traceback
from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# Revision identifiers, used by Alembic
revision = 'f9c8d7b6e5a4'
down_revision = 'e7f9d1c3b2a8'
branch_labels = None
depends_on = None


def load_config():
    """Load configuration from YAML file."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.abspath(os.path.join(current_dir, '../config/district_teacher_salary_band_config.yaml'))
    logger.info(f"Loading configuration from: {config_path}")
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
            return config
    except Exception as e:
        logger.error(f"Error loading configuration: {e}")
        raise Exception(f"Error loading configuration: {e}")


def round_to_two_decimal(value):
    """Round a value to two decimal places."""
    if value is None:
        return None
    return float(Decimal(str(value)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))


def try_parse_int(value):
    """Try to parse a value as integer, handling various formats.
    
    Args:
        value: The value to parse
        
    Returns:
        Integer value if successful, None otherwise
    """
    if pd.isna(value):
        return None
        
    # Try direct conversion for numeric types
    if isinstance(value, (int, float)):
        return int(value) if value == int(value) else None
    
    # Handle string values
    if isinstance(value, str):
        # Remove non-numeric characters
        clean_value = re.sub(r'[^0-9]', '', value)
        try:
            if clean_value:
                return int(clean_value)
        except ValueError:
            pass
            
    return None


def try_parse_salary(value):
    """Parse a salary value, handling various text and numeric formats.
    
    Args:
        value: The raw salary value (could be text, float, etc.)
        
    Returns:
        Float value representing the salary, or None if parsing fails
    """
    if pd.isna(value):
        return None
    
    # Already a number, return as is
    if isinstance(value, (int, float)):
        return float(value)
    
    # Handle string values
    if isinstance(value, str):
        # Remove currency symbols and other non-numeric chars except decimal point
        clean_value = re.sub(r'[^0-9\.]', '', value.replace(',', ''))
        try:
            if clean_value:
                # Convert to float
                return float(clean_value)
        except ValueError:
            pass
    
    return None


def normalize_salary_band_name(name):
    """Normalize the salary band name to match with entries in the mapping.
    
    Args:
        name: The salary band name to normalize
        
    Returns:
        Normalized salary band name
    """
    if pd.isna(name):
        return None
        
    if not isinstance(name, str):
        return None
        
    # Convert to uppercase
    name = name.upper()
    
    # Replace periods with nothing
    name = name.replace('.', '')
    
    # Replace "PLUS" with "+"
    name = name.replace(' PLUS ', '+')
    name = name.replace('PLUS', '+')
    
    # Replace spaces
    name = name.replace(' ', '')
    
    # Replace "BACHELOR" or "BACHELORS" with "BA"
    name = re.sub(r'^BACHELOR(S)?(\+|$)', 'BA\\2', name)
    
    # Replace "MASTER" or "MASTERS" with "MA"
    name = re.sub(r'^MASTER(S)?(\+|$)', 'MA\\2', name)
    
    return name


def map_salary_band_to_id(normalized_name, config):
    """Map a normalized salary band name to an ID from the configuration.
    
    Args:
        normalized_name: The normalized salary band name
        config: Configuration dictionary with salary band mappings
        
    Returns:
        The ID of the salary band type, or None if not found
    """
    if not normalized_name:
        return None
        
    # Create a normalized mapping from the configuration
    normalized_mapping = {}
    for name, id_value in config['salary_band_mapping'].items():
        normalized_key = normalize_salary_band_name(name)
        normalized_mapping[normalized_key] = id_value
    
    # Look up the normalized name in the mapping
    return normalized_mapping.get(normalized_name)


def process_district_teacher_salary_band_data(df, year, config):
    """Process district teacher salary band data from Excel file for a specific year.
    
    Args:
        df: DataFrame containing district teacher salary band data
        year: The year for this data
        config: Configuration dictionary with column mappings
        
    Returns:
        List of district teacher salary band entries to be inserted
    """
    district_entries = []
    district_count = 0
    entry_count = 0
    processed_districts = set()  # Track unique district-band combinations
    
    # Get column indices for easier access
    district_id_col = config['column_mappings']['district_id']
    salary_band_type_col = config['column_mappings']['salary_band_type']
    min_salary_col = config['column_mappings']['min_salary']
    max_salary_col = config['column_mappings']['max_salary']
    steps_col = config['column_mappings']['steps']
    
    logger.info(f"Processing district teacher salary band data for year {year}")
    logger.info(f"Column mappings: {config['column_mappings']}")
    
    # Process each row in the DataFrame
    for index, row in df.iterrows():
        try:
            # Use iloc for integer-based positional indexing
            raw_district_id = row.iloc[district_id_col] if isinstance(district_id_col, int) else row[district_id_col]
            
            # Try to parse district ID, handling text values
            district_id = try_parse_int(raw_district_id)
            
            # Skip if district ID couldn't be parsed
            if district_id is None:
                logger.warning(f"Line {index+1}: Could not parse district ID from value: {raw_district_id}")
                continue
                
            # Verify district exists in database
            exists_check = sa.text("""
                SELECT EXISTS (SELECT 1 FROM district WHERE id = :district_id)
            """)
            district_exists = op.get_bind().execute(exists_check, {"district_id": district_id}).scalar()
            
            if not district_exists:
                logger.warning(f"Line {index+1}: District ID {district_id} not found in database")
                continue
            
            # Get the salary band type - use iloc for integer-based positional indexing
            raw_salary_band_type = row.iloc[salary_band_type_col] if isinstance(salary_band_type_col, int) else row[salary_band_type_col]
            
            # Skip if the salary band type is missing
            if pd.isna(raw_salary_band_type):
                logger.warning(f"Line {index+1}: Missing salary band type for district {district_id}")
                continue
            
            # Normalize and map the salary band type to an ID
            normalized_band_type = normalize_salary_band_name(str(raw_salary_band_type))
            salary_band_type_id = map_salary_band_to_id(normalized_band_type, config)
            
            if salary_band_type_id is None:
                logger.warning(f"Line {index+1}: Could not map salary band type '{raw_salary_band_type}' (normalized: '{normalized_band_type}') to an ID for district {district_id}")
                continue
                
            # Generate a unique key for this district-band combination
            district_band_key = f"{district_id}:{salary_band_type_id}"
            
            # Skip if we've already processed this district-band combination for this year
            if district_band_key in processed_districts:
                logger.debug(f"Line {index+1}: Skipping duplicate district-band combination {district_band_key}")
                continue
            
            # Check if this district-band combination already exists in the database
            existing_check = sa.text("""
                SELECT EXISTS (
                    SELECT 1 FROM district_teacher_salary_band 
                    WHERE district_id_fk = :district_id 
                    AND teacher_salary_band_type_id_fk = :band_type_id
                    AND year = :year
                )
            """)
            has_existing_data = op.get_bind().execute(
                existing_check, 
                {
                    "district_id": district_id, 
                    "band_type_id": salary_band_type_id,
                    "year": year
                }
            ).scalar()
            
            if has_existing_data:
                logger.debug(f"Line {index+1}: Skipping existing district-band combination {district_band_key} for year {year}")
                continue
            
            # Get minimum salary - use iloc for integer-based positional indexing
            raw_min_salary = row.iloc[min_salary_col] if isinstance(min_salary_col, int) else row[min_salary_col]
            
            # Parse minimum salary, handling text formats
            min_salary = try_parse_salary(raw_min_salary)
            
            # Skip rows with invalid minimum salary
            if pd.isna(min_salary) or min_salary <= 0:
                logger.warning(f"Line {index+1}: Invalid minimum salary for district {district_id}, band {raw_salary_band_type}: {raw_min_salary}")
                continue
            
            # Round to two decimal places
            min_salary = round_to_two_decimal(min_salary)
            
            # Get maximum salary - use iloc for integer-based positional indexing
            raw_max_salary = row.iloc[max_salary_col] if isinstance(max_salary_col, int) else row[max_salary_col]
            
            # Parse maximum salary, handling text formats
            max_salary = try_parse_salary(raw_max_salary)
            
            # Skip rows with invalid maximum salary
            if pd.isna(max_salary) or max_salary <= 0:
                logger.warning(f"Line {index+1}: Invalid maximum salary for district {district_id}, band {raw_salary_band_type}: {raw_max_salary}")
                continue
            
            # Round to two decimal places
            max_salary = round_to_two_decimal(max_salary)
            
            # Get number of steps - use iloc for integer-based positional indexing
            raw_steps = row.iloc[steps_col] if isinstance(steps_col, int) else row[steps_col]
            
            # Parse steps, handling text formats
            steps = try_parse_int(raw_steps)
            
            # If steps is missing or invalid, calculate based on min and max salaries
            if pd.isna(steps) or steps <= 0:
                logger.warning(f"Line {index+1}: Invalid steps for district {district_id}, band {raw_salary_band_type}: {raw_steps}, using NULL")
                steps = None
            
            # Add entry
            district_entries.append({
                'district_id': district_id,
                'salary_band_type_id': salary_band_type_id,
                'year': year,
                'min_salary': min_salary,
                'max_salary': max_salary,
                'steps': steps
            })
            
            # Mark this district-band combination as processed
            processed_districts.add(district_band_key)
            entry_count += 1
            
            # Count unique districts
            if district_id not in processed_districts:
                district_count += 1
            
        except Exception as e:
            # Get detailed stack trace
            stack_trace = traceback.format_exc()
            
            # Log error information
            logger.error(f"Error processing Line {index+1} for year {year}: {str(e)}")
            logger.debug(f"Stack trace: {stack_trace}")
            
            continue
    
    logger.info(f"Processed {len(processed_districts)} distinct district-band combinations with salary band data for year {year}")
    return district_entries


def generate_sql(district_entries):
    """Generate SQL INSERT statements for district teacher salary band data.
    
    Args:
        district_entries: List of district salary band entries to be inserted
        
    Returns:
        String containing SQL statements
    """
    sql_statements = []
    
    # Add header for district data
    if district_entries:
        sql_statements.append("-- District Teacher Salary Band data INSERT statements")
        
        # Generate district INSERT statements
        for entry in district_entries:
            # Handle NULL steps value
            steps_value = "NULL" if entry['steps'] is None else entry['steps']
            
            sql_statements.append(
                f"INSERT INTO district_teacher_salary_band (district_id_fk, teacher_salary_band_type_id_fk, year, min_salary, max_salary, steps, "
                f"date_created, date_updated) VALUES ("
                f"{entry['district_id']}, "
                f"{entry['salary_band_type_id']}, "
                f"{entry['year']}, "
                f"{entry['min_salary']}, "
                f"{entry['max_salary']}, "
                f"{steps_value}, "
                f"CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);"
            )
    
    return "\n".join(sql_statements)


def upgrade():
    """Load district teacher salary band data."""
    logger.info("Starting District Teacher Salary Band Data migration")
    
    # Load configuration
    config = load_config()
    
    try:
        # Check for existing cache file first
        current_dir = os.path.dirname(os.path.abspath(__file__))
        cache_dir = os.path.abspath(os.path.join(current_dir, config['file_settings']['sql_cache_dir']))
        cache_file = os.path.join(cache_dir, f'{revision}_cache.sql')
        
        if os.path.exists(cache_file):
            logger.info(f"Using existing SQL cache file")
            with open(cache_file, 'r') as f:
                sql_statements = f.read()
            logger.info(f"Loaded cached SQL statements")
        else:
            logger.info("Processing input files")
            
            # Process input files
            all_district_entries = []
            
            # Get the base pattern for input files
            input_pattern = config['file_settings']['teacher_salary_band_file']
            # Get the base pattern without extension
            base_pattern_parts = os.path.splitext(input_pattern)
            base_pattern_without_ext = base_pattern_parts[0]
            
            base_dir = os.path.abspath(os.path.join(current_dir, os.path.dirname(input_pattern)))
            base_pattern = os.path.basename(base_pattern_without_ext)
            
            # Remove asterisks and get the pattern parts
            pattern_parts = base_pattern.split('****')
            
            # Get years from config
            years = config['file_settings'].get('years', [])
            
            logger.info(f"Processing data for years: {years}")
            
            found_files = 0
            
            for year in years:
                # Try both file extensions
                file_found = False
                df = None
                
                extensions = ['.xlsx', '.xls']
                for ext in extensions:
                    file_pattern = f"{pattern_parts[0]}{year}{pattern_parts[1] if len(pattern_parts) > 1 else ''}{ext}"
                    file_path = os.path.join(base_dir, file_pattern)
                    
                    # Check if the file exists
                    if os.path.exists(file_path):
                        try:
                            # Load the Excel file using the first sheet (0-indexed)
                            # No need to check sheet names, just use the first available sheet
                            df = pd.read_excel(
                                file_path,
                                skiprows=config['file_settings']['start_row'] - 1
                            )
                            
                            file_found = True
                            found_files += 1
                            logger.info(f"Loaded Excel file for year {year}: {file_path}")
                            # Break the loop if we successfully loaded the file
                            break
                        except Exception as e:
                            logger.error(f"Error reading Excel file {file_path}: {e}")
                            # Continue to try the next extension
                            df = None
                            continue
                
                # If we found and loaded a file, process it
                if file_found and df is not None:
                    try:
                        logger.info(f"Processing data for year {year}")
                        
                        # Process teacher salary band entries for this file
                        district_year_entries = process_district_teacher_salary_band_data(df, year, config)
                            
                        logger.info(f"Found {len(district_year_entries)} district teacher salary band entries for year {year}")
                        all_district_entries.extend(district_year_entries)
                    except Exception as e:
                        logger.error(f"Error processing data for year {year}: {e}")
                        # Continue to next file rather than failing completely
                else:
                    logger.warning(f"No file found for year {year} with extensions {extensions}")
            
            logger.info(f"Processed {found_files} files, found {len(all_district_entries)} total district entries")
            
            if len(all_district_entries) == 0:
                logger.error("No teacher salary band entries were found! Check file paths and Excel structure.")
                raise Exception("No teacher salary band entries found")
            
            # Generate SQL with combined data
            logger.info("Generating SQL statements")
            sql_statements = generate_sql(all_district_entries)
            
            # Save to cache
            os.makedirs(cache_dir, exist_ok=True)
            with open(cache_file, 'w') as f:
                f.write(sql_statements)
            logger.info(f"Created SQL cache file")
        
        # Execute SQL statements
        logger.info("Executing SQL statements")
        statement_count = sql_statements.count(';')
        logger.info(f"Executing {statement_count} SQL statements")
        
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
                
                if executed % 500 == 0:
                    logger.info(f"Executed {executed} statements so far")
            except Exception as e:
                if "duplicate key" in str(e).lower():
                    skipped += 1
                else:
                    logger.error(f"Error executing SQL: {str(e)[:100]}")
                    skipped += 1
                
        logger.info(f"SQL execution complete: {executed} statements executed, {skipped} skipped")
        
        # Create materialized view for state-level teacher salary band data
        logger.info("Creating materialized view for state_teacher_salary_band")
        
        try:
            # First, check if the materialized view already exists and drop it if it does
            op.execute(sa.text("""
                DROP MATERIALIZED VIEW IF EXISTS state_teacher_salary_band;
            """))
            
            # Create the materialized view
            op.execute(sa.text("""
                CREATE MATERIALIZED VIEW state_teacher_salary_band AS
                SELECT
                    teacher_salary_band_type_id_fk, 
                    year, 
                    ROUND(AVG(min_salary)::numeric, 2) AS min_salary, 
                    ROUND(AVG(max_salary)::numeric, 2) AS max_salary, 
                    ROUND(AVG(steps)::numeric, 1) AS steps,
                    CURRENT_TIMESTAMP AS date_created,
                    CURRENT_TIMESTAMP AS date_updated
                FROM 
                    district_teacher_salary_band dtsb
                GROUP BY teacher_salary_band_type_id_fk, year;
            """))
            
            # Create a unique index on the materialized view for faster refreshing
            op.execute(sa.text("""
                CREATE UNIQUE INDEX idx_state_teacher_salary_band_unique 
                ON state_teacher_salary_band (teacher_salary_band_type_id_fk, year);
            """))
            
            logger.info("Successfully created materialized view for state_teacher_salary_band")
        except Exception as e:
            logger.error(f"Error creating materialized view: {str(e)}")
            raise Exception(f"Error creating materialized view: {str(e)}")
            
    except Exception as e:
        logger.error(f"Critical error during migration: {e}")
        raise Exception(f"Error during migration: {e}")
    
    logger.info("Migration completed successfully")


def downgrade():
    """Remove district teacher salary band data."""
    logger.info("Starting District Teacher Salary Band Data migration downgrade")
    
    # Drop the materialized view first
    logger.info("Dropping materialized view for state_teacher_salary_band")
    op.execute("DROP MATERIALIZED VIEW IF EXISTS state_teacher_salary_band")
    
    # Remove all data from district_teacher_salary_band table
    logger.info("Removing data from district_teacher_salary_band table")
    op.execute("DELETE FROM district_teacher_salary_band")
    
    logger.info("Downgrade completed successfully") 