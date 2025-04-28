"""Load District Staff Data

Revision ID: c5d7b9a8f2e3
Revises: b5c8d9e7f3a1
Create Date: 2024-08-20 13:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
import pandas as pd
import os
import yaml
import logging
import re
from datetime import datetime
import traceback

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# Revision identifiers, used by Alembic
revision = 'c5d7b9a8f2e3'
down_revision = 'b5c8d9e7f3a1'
branch_labels = None
depends_on = None


def load_config():
    """Load configuration from YAML file."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.abspath(os.path.join(current_dir, '../config/district_staff_config.yaml'))
    logger.info(f"Attempting to load configuration from: {config_path}")
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
            logger.info(f"Successfully loaded configuration: {config}")
            return config
    except Exception as e:
        logger.error(f"Error loading configuration: {e}")
        raise Exception(f"Error loading configuration: {e}")


def try_parse_int(value):
    """Attempt to parse a value as an integer, handling various formats.
    
    Args:
        value: The value to parse, which could be an int, float, string, or other type
        
    Returns:
        An integer if parsing succeeds, None otherwise
    """
    if pd.isna(value):
        return None
        
    # If it's already an integer, return it
    if isinstance(value, int):
        return value
        
    # If it's a float, check if it's a whole number
    if isinstance(value, float):
        if value.is_integer():
            return int(value)
        return None
        
    # If it's a string, try to extract an integer
    if isinstance(value, str):
        # Try to extract digits from the string
        digits = re.sub(r'\D', '', value)
        if digits:
            try:
                return int(digits)
            except ValueError:
                pass
    
    # Log the type and value that couldn't be parsed
    logger.debug(f"Unable to parse as integer: {value} (type: {type(value)})")
    return None


def process_district_staff_data(df, year, config):
    """Process district staff data from Excel file for a specific year.
    
    Args:
        df: DataFrame containing district staff data
        year: The year for this data
        config: Configuration dictionary with column mappings
        
    Returns:
        Tuple of (district staff entries, state staff entries) to be inserted
    """
    # Map staff types to their IDs
    staff_type_map = {
        'teacher_count': 1,              # Teacher
        'instruction_support_count': 2,  # Instruction Support
        'librarian_count': 3,            # Librarian
        'specialist_count': 4,           # Specialist
        'admin_support_count': 5,        # Admin Support
        'other_support_count': 6,        # All Other Support
    }
    
    district_entries = []
    state_entries = []
    district_count = 0
    entry_count = 0
    
    # Get state total column index and identifier text from config
    state_total_col = config.get('state_data_settings', {}).get('state_column_index', 3)
    state_identifier_text = config.get('state_data_settings', {}).get('state_identifier_text', 'state total')
    
    logger.info(f"Looking for state data in column {state_total_col} with identifier text '{state_identifier_text}'")
    
    # Log column mappings for debugging
    logger.info(f"Column mappings: {config['column_mappings']}")
    
    # Process each row in the DataFrame
    for index, row in df.iterrows():
        try:
            # Check if this is a state total row
            is_state_total = False
            
            # Check for state identifier text in the specified column
            if len(row) > state_total_col:
                state_value = row.iloc[state_total_col] if isinstance(state_total_col, int) else row[state_total_col]
                if isinstance(state_value, str) and state_identifier_text.lower() in state_value.lower():
                    is_state_total = True
                    logger.info(f"Found state total row at index {index} for year {year}")
            
            if is_state_total:
                # Process state-level data
                for staff_col, staff_id in staff_type_map.items():
                    col_idx = config['column_mappings'].get(staff_col)
                    if col_idx is None:
                        continue
                        
                    staff_count = row[col_idx]
                    
                    # Skip if count is invalid or zero
                    if pd.isna(staff_count) or staff_count == 0:
                        continue
                    
                    # Try to convert to float
                    try:
                        staff_count_float = float(staff_count)
                    except (ValueError, TypeError):
                        logger.warning(f"Invalid state staff count '{staff_count}' for staff type {staff_col}, year {year}")
                        continue
                    
                    # Add state entry
                    state_entries.append({
                        'staff_type_id': staff_id,
                        'year': year,
                        'value': staff_count_float
                    })
                    logger.info(f"Added state staff entry for year {year}, type {staff_id}: {staff_count_float}")
            else:
                # Process district-level data
                district_id_raw = row[config['column_mappings']['district_id']]
                district_id = try_parse_int(district_id_raw)
                
                # Skip if district ID parsing failed
                if district_id is None:
                    logger.warning(f"Invalid district ID format at row {index+1} for year {year}: {district_id_raw} (type: {type(district_id_raw)})")
                    continue
                    
                district_count += 1
                logger.debug(f"Processing district ID {district_id} at row {index+1} for year {year}")
                
                # Verify district exists in database
                exists_check = sa.text("""
                    SELECT EXISTS (SELECT 1 FROM district WHERE id = :district_id)
                """)
                district_exists = op.get_bind().execute(exists_check, {"district_id": district_id}).scalar()
                
                if not district_exists:
                    logger.warning(f"District ID {district_id} for year {year} not found in database, skipping row {index+1}")
                    continue
                
                # Process each staff type
                for staff_col, staff_id in staff_type_map.items():
                    col_idx = config['column_mappings'].get(staff_col)
                    if col_idx is None:
                        continue
                        
                    staff_count = row[col_idx]
                    
                    # Skip if count is invalid or zero
                    if pd.isna(staff_count) or staff_count == 0:
                        continue
                    
                    # Try to convert to float
                    try:
                        staff_count_float = float(staff_count)
                    except (ValueError, TypeError):
                        logger.warning(f"Invalid staff count '{staff_count}' for district {district_id}, staff type {staff_col}, year {year}, row {index+1}")
                        continue
                    
                    district_entries.append({
                        'district_id': district_id,
                        'staff_type_id': staff_id,
                        'year': year,
                        'value': staff_count_float
                    })
                    entry_count += 1
                
        except Exception as e:
            logger.warning(f"Error processing row {index+1} for year {year}: {e}")
            logger.debug(f"Exception details: {traceback.format_exc()}")
            continue
    
    logger.info(f"Processed {district_count} districts with {entry_count} staff entries for year {year}")
    logger.info(f"Found {len(state_entries)} state staff entries for year {year}")
    return district_entries, state_entries


def generate_district_sql(entries):
    """Generate SQL INSERT statements for district staff data.
    
    Args:
        entries: List of district staff data entries to be inserted
        
    Returns:
        String containing SQL statements
    """
    sql_statements = []
    
    # Add header
    sql_statements.append("-- District Staff data INSERT statements")
    
    # Generate INSERT statements
    for entry in entries:
        sql_statements.append(
            f"INSERT INTO district_staff (school_staff_type_id_fk, district_id_fk, year, value, "
            f"date_created, date_updated) VALUES ("
            f"{entry['staff_type_id']}, "
            f"{entry['district_id']}, "
            f"{entry['year']}, "
            f"{entry['value']}, "
            f"CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);"
        )
    
    return "\n".join(sql_statements)


def generate_state_sql(entries):
    """Generate SQL INSERT statements for state staff data.
    
    Args:
        entries: List of state staff data entries to be inserted
        
    Returns:
        String containing SQL statements
    """
    sql_statements = []
    
    # Add header
    sql_statements.append("-- State Staff data INSERT statements")
    
    # Generate INSERT statements
    for entry in entries:
        sql_statements.append(
            f"INSERT INTO state_staff (school_staff_type_id_fk, year, value, "
            f"date_created, date_updated) VALUES ("
            f"{entry['staff_type_id']}, "
            f"{entry['year']}, "
            f"{entry['value']}, "
            f"CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);"
        )
    
    return "\n".join(sql_statements)


def upgrade():
    """Load district staff data across multiple years."""
    logger.info("Starting District Staff Data migration upgrade")
    
    # Load configuration
    config = load_config()
    
    try:
        # Check for existing cache file first
        current_dir = os.path.dirname(os.path.abspath(__file__))
        cache_dir = os.path.abspath(os.path.join(current_dir, config['file_settings']['sql_cache_dir']))
        district_cache_file = os.path.join(cache_dir, f'{revision}_district_cache.sql')
        state_cache_file = os.path.join(cache_dir, f'{revision}_state_cache.sql')
        logger.info(f"Cache directory path: {cache_dir}")
        logger.info(f"District cache file path: {district_cache_file}")
        logger.info(f"State cache file path: {state_cache_file}")
        
        if os.path.exists(district_cache_file) and os.path.exists(state_cache_file):
            logger.info(f"Found existing SQL cache files")
            with open(district_cache_file, 'r') as f:
                district_sql_statements = f.read()
            with open(state_cache_file, 'r') as f:
                state_sql_statements = f.read()
            logger.info(f"Loaded cached SQL statements")
        else:
            logger.info("No cache files found, processing input files")
            
            # Process input files
            all_district_entries = []
            all_state_entries = []
            
            # Get the base pattern for input files
            input_pattern = config['file_settings']['district_staff_file']
            base_dir = os.path.abspath(os.path.join(current_dir, os.path.dirname(input_pattern)))
            base_pattern = os.path.basename(input_pattern)
            
            logger.info(f"Input pattern: {input_pattern}")
            logger.info(f"Base directory: {base_dir}")
            logger.info(f"Base pattern: {base_pattern}")
            
            # Remove asterisks and get the pattern parts
            pattern_parts = base_pattern.split('****')
            logger.info(f"Pattern parts: {pattern_parts}")
            
            # Get years from config
            years = config['file_settings'].get('years', [])
            logger.info(f"Processing years: {years}")
            
            found_files = 0
            
            for year in years:
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
                        df = pd.read_excel(
                            file_path,
                            sheet_name=config['file_settings']['sheet_name'],
                            skiprows=config['file_settings']['start_row'] - 1
                        )
                        logger.info(f"Successfully loaded Excel file with shape: {df.shape}")
                        
                        # Process district and state staff entries for this file
                        logger.info(f"Processing staff data for year {year}")
                        district_year_entries, state_year_entries = process_district_staff_data(df, year, config)
                        logger.info(f"Found {len(district_year_entries)} district staff entries for year {year}")
                        logger.info(f"Found {len(state_year_entries)} state staff entries for year {year}")
                        all_district_entries.extend(district_year_entries)
                        all_state_entries.extend(state_year_entries)
                    except Exception as e:
                        logger.error(f"Error processing Excel file {file_path}: {e}")
                        # Continue to next file rather than failing completely
                        continue
                else:
                    logger.warning(f"File not found for year {year}: {file_path}")
            
            logger.info(f"Processed {found_files} files")
            logger.info(f"Total district staff entries found: {len(all_district_entries)}")
            logger.info(f"Total state staff entries found: {len(all_state_entries)}")
            
            if len(all_district_entries) == 0 and len(all_state_entries) == 0:
                logger.error("No staff entries were found! Check file paths and Excel structure.")
                raise Exception("No staff entries found")
            
            # Generate SQL with combined data
            logger.info("Generating SQL statements")
            district_sql_statements = generate_district_sql(all_district_entries)
            state_sql_statements = generate_state_sql(all_state_entries)
            
            # Save to cache
            logger.info(f"Creating cache directory: {cache_dir}")
            os.makedirs(cache_dir, exist_ok=True)
            
            if len(all_district_entries) > 0:
                logger.info(f"Writing district SQL cache to: {district_cache_file}")
                with open(district_cache_file, 'w') as f:
                    f.write(district_sql_statements)
                logger.info(f"Successfully created district SQL cache file")
            
            if len(all_state_entries) > 0:
                logger.info(f"Writing state SQL cache to: {state_cache_file}")
                with open(state_cache_file, 'w') as f:
                    f.write(state_sql_statements)
                logger.info(f"Successfully created state SQL cache file")
        
        # Execute SQL statements for district staff
        if district_sql_statements:
            logger.info("Starting district SQL execution")
            district_statement_count = district_sql_statements.count(';')
            logger.info(f"Found approximately {district_statement_count} district SQL statements to execute")
            
            district_executed = 0
            district_skipped = 0
            
            for statement in district_sql_statements.split(';'):
                statement = statement.strip()
                if not statement:  # Skip empty statements
                    continue
                    
                try:
                    # Execute the SQL statement
                    op.execute(sa.text(statement))
                    district_executed += 1
                    if district_executed % 100 == 0:
                        logger.info(f"Executed {district_executed} district statements so far")
                except Exception as e:
                    if "duplicate key" in str(e).lower():
                        logger.warning(f"Skipped duplicate key: {str(e)[:100]}")
                        district_skipped += 1
                    else:
                        logger.error(f"Error executing district SQL statement: {e}")
                        logger.error(f"Statement: {statement[:300]}...")
                        # Continue execution despite errors
                        district_skipped += 1
                
            logger.info(f"District SQL execution complete: {district_executed} statements executed, {district_skipped} skipped")
        
        # Execute SQL statements for state staff
        if state_sql_statements:
            logger.info("Starting state SQL execution")
            state_statement_count = state_sql_statements.count(';')
            logger.info(f"Found approximately {state_statement_count} state SQL statements to execute")
            
            state_executed = 0
            state_skipped = 0
            
            for statement in state_sql_statements.split(';'):
                statement = statement.strip()
                if not statement:  # Skip empty statements
                    continue
                    
                try:
                    # Execute the SQL statement
                    op.execute(sa.text(statement))
                    state_executed += 1
                    if state_executed % 100 == 0:
                        logger.info(f"Executed {state_executed} state statements so far")
                except Exception as e:
                    if "duplicate key" in str(e).lower():
                        logger.warning(f"Skipped duplicate key: {str(e)[:100]}")
                        state_skipped += 1
                    else:
                        logger.error(f"Error executing state SQL statement: {e}")
                        logger.error(f"Statement: {statement[:300]}...")
                        # Continue execution despite errors
                        state_skipped += 1
                
            logger.info(f"State SQL execution complete: {state_executed} statements executed, {state_skipped} skipped")
        
    except Exception as e:
        logger.error(f"Critical error during migration: {e}")
        raise Exception(f"Error during migration: {e}")
    
    logger.info("Migration completed successfully")


def downgrade():
    """Remove district staff data and related objects."""
    logger.info("Starting District Staff Data migration downgrade")
    
    # Remove all data from state_staff table
    logger.info("Removing data from state_staff table")
    op.execute("DELETE FROM state_staff")
    
    # Remove all data from district_staff table
    logger.info("Removing data from district_staff table")
    op.execute("DELETE FROM district_staff")
    
    logger.info("Downgrade completed successfully") 