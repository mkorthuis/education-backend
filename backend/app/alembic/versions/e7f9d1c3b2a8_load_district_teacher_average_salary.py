"""Load District Teacher Average Salary Data

Revision ID: e7f9d1c3b2a8
Revises: d6f9c8b5a4e2
Create Date: 2024-08-25 13:00:00.000000

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
revision = 'e7f9d1c3b2a8'
down_revision = 'd6f9c8b5a4e2'
branch_labels = None
depends_on = None


def load_config():
    """Load configuration from YAML file."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.abspath(os.path.join(current_dir, '../config/district_teacher_salary_config.yaml'))
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


def clean_district_name(name):
    """Clean and standardize district name for matching.
    
    Args:
        name: The district name to clean
        
    Returns:
        Cleaned district name
    """
    if pd.isna(name):
        return None
        
    if not isinstance(name, str):
        return None
        
    # Convert to lowercase
    name = name.lower()
    
    # Remove "school district", "schools", etc.
    name = re.sub(r'\s+school\s+district\s*$', '', name)
    name = re.sub(r'\s+schools\s*$', '', name)
    name = re.sub(r'\s+sd\s*$', '', name)
    
    # Remove leading/trailing whitespace
    name = name.strip()
    
    # Replace multiple spaces with a single space
    name = re.sub(r'\s+', ' ', name)
    
    return name


def process_district_teacher_salary_data(df, year, config):
    """Process district teacher average salary data from Excel file for years 2023-2025.
    
    Args:
        df: DataFrame containing district teacher salary data
        year: The year for this data
        config: Configuration dictionary with column mappings
        
    Returns:
        Tuple of (district entries, state entries list) to be inserted
    """
    district_entries = []
    state_entries = []
    district_count = 0
    processed_districts = set()  # Track districts we've already processed for this year
    
    # Get column indices for easier access
    district_id_col = config['column_mappings']['district_id']
    salary_col = config['column_mappings']['salary']
    
    # Get state identifier settings from config
    state_column_index = config.get('state_data_settings', {}).get('modern_state_column_index', 3)
    state_identifier_text = config.get('state_data_settings', {}).get('modern_state_identifier_text', 'State Average Salary')
    
    logger.info(f"Looking for modern state data in column {state_column_index} with identifier text starting with '{state_identifier_text}'")
    
    # Process each row in the DataFrame
    for index, row in df.iterrows():
        try:
            # Check if this is a state average row
            is_state_row = False
            
            # Check for state identifier text in the specified column
            if len(row) > state_column_index:
                state_value = row.iloc[state_column_index] if isinstance(state_column_index, int) else row[state_column_index]
                logger.info(f"State value: '{state_value}'")
                if isinstance(state_value, str) and state_value.strip().lower().startswith(state_identifier_text.lower()):
                    is_state_row = True
                    logger.info(f"Found state average row at index {index} for year {year}")
            
            if is_state_row:
                # Process state-level data
                # Get salary - use iloc for integer-based positional indexing
                raw_salary = row.iloc[salary_col] if isinstance(salary_col, int) else row[salary_col]
                
                # Parse salary, handling text formats
                salary = try_parse_salary(raw_salary)
                
                # Skip rows with invalid salary
                if pd.isna(salary) or salary <= 0:
                    logger.warning(f"Line {index+1}: Invalid state average salary: {raw_salary}")
                    continue
                
                # Round to two decimal places
                salary = round_to_two_decimal(salary)
                
                # Store state entry
                state_entry = {
                    'year': year,
                    'salary': salary
                }
                state_entries.append(state_entry)
                logger.info(f"Added state average salary entry for year {year}: {salary}")
            else:
                # Process district-level data
                # Use iloc for integer-based positional indexing
                raw_district_id = row.iloc[district_id_col] if isinstance(district_id_col, int) else row[district_id_col]
                
                # Try to parse district ID, handling text values
                district_id = try_parse_int(raw_district_id)
                
                # Skip if district ID couldn't be parsed
                if district_id is None:
                    logger.warning(f"Line {index+1}: Could not parse district ID from value: {raw_district_id}")
                    continue
                    
                # Skip if we've already processed this district for this year
                if district_id in processed_districts:
                    continue
                    
                # Verify district exists in database
                exists_check = sa.text("""
                    SELECT EXISTS (SELECT 1 FROM district WHERE id = :district_id)
                """)
                district_exists = op.get_bind().execute(exists_check, {"district_id": district_id}).scalar()
                
                if not district_exists:
                    logger.warning(f"Line {index+1}: District ID {district_id} not found in database")
                    continue
                
                # Check if this district already has salary data for this year
                existing_check = sa.text("""
                    SELECT EXISTS (
                        SELECT 1 FROM district_teacher_average_salary 
                        WHERE district_id_fk = :district_id AND year = :year
                    )
                """)
                has_existing_data = op.get_bind().execute(
                    existing_check, 
                    {"district_id": district_id, "year": year}
                ).scalar()
                
                if has_existing_data:
                    continue
                
                # Get salary - use iloc for integer-based positional indexing
                raw_salary = row.iloc[salary_col] if isinstance(salary_col, int) else row[salary_col]
                
                # Parse salary, handling text formats
                salary = try_parse_salary(raw_salary)
                
                # Skip rows with invalid salary
                if pd.isna(salary) or salary <= 0:
                    logger.warning(f"Line {index+1}: Invalid salary for district {district_id}: {raw_salary}")
                    continue
                
                # Round to two decimal places
                salary = round_to_two_decimal(salary)
                
                # Add entry
                district_entries.append({
                    'district_id': district_id,
                    'year': year,
                    'salary': salary
                })
                
                # Mark this district as processed
                processed_districts.add(district_id)
                district_count += 1
                
        except Exception as e:
            # Get detailed stack trace
            stack_trace = traceback.format_exc()
            
            # Log error information
            logger.error(f"Error processing Line {index+1} for year {year}: {str(e)}")
            logger.debug(f"Stack trace: {stack_trace}")
            
            continue
    
    logger.info(f"Processed {district_count} districts with average teacher salary for year {year}")
    if state_entries:
        logger.info(f"Found state average salary for year {year}: {state_entries[0]['salary']}")
    return district_entries, state_entries


def process_legacy_teacher_salary_data(df, year, config):
    """Process district teacher average salary data from Excel file for years 2008-2022.
    This function checks for district names in column 0 or 1, with salary always at district_col + 2.
    
    Args:
        df: DataFrame containing district teacher salary data
        year: The year for this data
        config: Configuration dictionary with column mappings
        
    Returns:
        Tuple of (district entries, state entries list) to be inserted
    """
    district_entries = []
    state_entries = []
    district_count = 0
    processed_districts = set()  # Track districts we've already processed for this year
    
    # Get state identifier settings from config
    state_identifier_text = config.get('state_data_settings', {}).get('legacy_state_identifier_text', 'State Average Salary')
    
    logger.info(f"Looking for legacy state data with district name starting with '{state_identifier_text}'")
    
    # Define both possible column positions
    district_positions = [
        # Position 0 configuration
        {
            'district_col': config['column_mappings']['legacy_district_name_col0'],
            'salary_col': config['column_mappings']['legacy_salary_col0']
        },
        # Position 1 configuration
        {
            'district_col': config['column_mappings']['legacy_district_name_col1'],
            'salary_col': config['column_mappings']['legacy_salary_col1']
        }
    ]
    
    # Process each row in the DataFrame
    for index, row in df.iterrows():
        # Try both district column positions
        district_found = False
        
        for position in district_positions:
            try:
                district_col = position['district_col']
                salary_col = position['salary_col']
                
                # Use iloc for integer-based positional indexing
                raw_district_name = row.iloc[district_col] if isinstance(district_col, int) else row[district_col]
                
                # Skip to the next position if district name is missing or not a string
                if pd.isna(raw_district_name) or not isinstance(raw_district_name, str):
                    continue
                
                # Check if this is a state average row
                is_state_row = raw_district_name.strip().lower().startswith(state_identifier_text.lower())
                
                if is_state_row:
                    # Process state-level data
                    # Get salary - use iloc for integer-based positional indexing
                    raw_salary = row.iloc[salary_col] if isinstance(salary_col, int) else row[salary_col]
                    
                    # Parse salary, handling text formats
                    salary = try_parse_salary(raw_salary)
                    
                    # Skip rows with invalid salary
                    if pd.isna(salary) or salary <= 0:
                        logger.warning(f"Line {index+1}: Invalid state average salary: {raw_salary}")
                        continue
                    
                    # Round to two decimal places
                    salary = round_to_two_decimal(salary)
                    
                    # Store state entry
                    state_entry = {
                        'year': year,
                        'salary': salary
                    }
                    state_entries.append(state_entry)
                    logger.info(f"Added state average salary entry for year {year}: {salary}")
                    district_found = True
                    break
                else:
                    # Clean and standardize the district name
                    district_name = clean_district_name(raw_district_name)
                    
                    if not district_name:
                        continue
                    
                    # Look up district ID by name
                    district_query = sa.text("""
                        SELECT id FROM district 
                        WHERE LOWER(name) LIKE :district_name
                        OR LOWER(name) LIKE :district_name_alt
                        OR LOWER(name) LIKE :district_name_sd
                        LIMIT 1
                    """)
                    
                    result = op.get_bind().execute(
                        district_query, 
                        {
                            "district_name": f"%{district_name}%",
                            "district_name_alt": f"%{district_name} school%",
                            "district_name_sd": f"%{district_name} sd%"
                        }
                    ).fetchone()
                    
                    if not result:
                        logger.warning(f"Line {index+1}: Could not find district ID for name: {raw_district_name}")
                        continue
                        
                    district_id = result[0]
                    
                    # Skip if we've already processed this district for this year
                    if district_id in processed_districts:
                        district_found = True
                        break
                        
                    # Check if this district already has salary data for this year
                    existing_check = sa.text("""
                        SELECT EXISTS (
                            SELECT 1 FROM district_teacher_average_salary 
                            WHERE district_id_fk = :district_id AND year = :year
                        )
                    """)
                    has_existing_data = op.get_bind().execute(
                        existing_check, 
                        {"district_id": district_id, "year": year}
                    ).scalar()
                    
                    if has_existing_data:
                        district_found = True
                        break
                    
                    # Get salary - use iloc for integer-based positional indexing
                    raw_salary = row.iloc[salary_col] if isinstance(salary_col, int) else row[salary_col]
                    
                    # Parse salary, handling text formats
                    salary = try_parse_salary(raw_salary)
                    
                    # Skip rows with invalid salary
                    if pd.isna(salary) or salary <= 0:
                        logger.warning(f"Line {index+1}: Invalid salary for district '{raw_district_name}': {raw_salary}")
                        continue
                    
                    # Round to two decimal places
                    salary = round_to_two_decimal(salary)
                    
                    # Add entry
                    district_entries.append({
                        'district_id': district_id,
                        'year': year,
                        'salary': salary
                    })
                    
                    # Mark this district as processed
                    processed_districts.add(district_id)
                    district_count += 1
                    district_found = True
                    # We found a valid district, break out of the position loop
                    break
                    
            except Exception as e:
                # Log the error but continue trying the other position
                logger.debug(f"Error processing Line {index+1} position {district_col}: {str(e)}")
                continue
        
        # If we tried all positions and encountered an error each time, log the final error
        if not district_found:
            logger.debug(f"Line {index+1}: No valid district found in any position")
    
    logger.info(f"Processed {district_count} districts with average teacher salary for year {year} (legacy format)")
    if state_entries:
        logger.info(f"Found state average salary for year {year} (legacy format): {state_entries[0]['salary']}")
    return district_entries, state_entries


def generate_sql(district_entries, state_entries):
    """Generate SQL INSERT statements for district and state teacher average salary data.
    
    Args:
        district_entries: List of district salary entries to be inserted
        state_entries: List of state salary entries to be inserted
        
    Returns:
        String containing SQL statements
    """
    sql_statements = []
    
    # Add header for district data
    if district_entries:
        sql_statements.append("-- District Teacher Average Salary data INSERT statements")
        
        # Generate district INSERT statements
        for entry in district_entries:
            sql_statements.append(
                f"INSERT INTO district_teacher_average_salary (district_id_fk, year, salary, "
                f"date_created, date_updated) VALUES ("
                f"{entry['district_id']}, "
                f"{entry['year']}, "
                f"{entry['salary']}, "
                f"CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);"
            )
    
    # Add state data if present
    if state_entries:
        sql_statements.append("\n-- State Teacher Average Salary data INSERT statements")
        
        # Generate state INSERT statements for all entries
        for entry in state_entries:
            sql_statements.append(
                f"INSERT INTO state_teacher_average_salary (year, salary, "
                f"date_created, date_updated) VALUES ("
                f"{entry['year']}, "
                f"{entry['salary']}, "
                f"CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);"
            )
    
    return "\n".join(sql_statements)


def upgrade():
    """Load district teacher average salary data across multiple years."""
    logger.info("Starting District Teacher Average Salary Data migration")
    
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
            all_state_entries = []
            
            # Get the base pattern for input files
            input_pattern = config['file_settings']['teacher_salary_file']
            # Get the base pattern without extension
            base_pattern_parts = os.path.splitext(input_pattern)
            base_pattern_without_ext = base_pattern_parts[0]
            
            base_dir = os.path.abspath(os.path.join(current_dir, os.path.dirname(input_pattern)))
            base_pattern = os.path.basename(base_pattern_without_ext)
            
            # Remove asterisks and get the pattern parts
            pattern_parts = base_pattern.split('****')
            
            # Get years from config
            years = config['file_settings'].get('years', [])
            legacy_years = config['file_settings'].get('legacy_years', [])
            modern_years = config['file_settings'].get('modern_years', [])
            
            logger.info(f"Processing data for years: {years}")
            logger.info(f"Using legacy format for years: {legacy_years}")
            logger.info(f"Using modern format for years: {modern_years}")
            
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
                        
                        # Process teacher salary entries for this file
                        # Use the appropriate processing function based on the year
                        if year in legacy_years:
                            district_year_entries, state_year_entries = process_legacy_teacher_salary_data(df, year, config)
                        else:
                            district_year_entries, state_year_entries = process_district_teacher_salary_data(df, year, config)
                            
                        logger.info(f"Found {len(district_year_entries)} district teacher salary entries for year {year}")
                        all_district_entries.extend(district_year_entries)
                        
                        # Add state entries if found
                        if state_year_entries:
                            all_state_entries.extend(state_year_entries)
                            logger.info(f"Added state average salary for year {year}")
                    except Exception as e:
                        logger.error(f"Error processing data for year {year}: {e}")
                        # Continue to next file rather than failing completely
                else:
                    logger.warning(f"No file found for year {year} with extensions {extensions}")
            
            logger.info(f"Processed {found_files} files, found {len(all_district_entries)} total district entries")
            logger.info(f"Found {len(all_state_entries)} total state entries")
            
            if len(all_district_entries) == 0 and len(all_state_entries) == 0:
                logger.error("No teacher salary entries were found! Check file paths and Excel structure.")
                raise Exception("No teacher salary entries found")
            
            # Generate SQL with combined data
            logger.info("Generating SQL statements")
            sql_statements = generate_sql(all_district_entries, all_state_entries)
            
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
        district_executed = 0
        state_executed = 0
        skipped = 0
        
        for statement in sql_statements.split(';'):
            statement = statement.strip()
            if not statement:  # Skip empty statements
                continue
                
            try:
                # Execute the SQL statement
                op.execute(sa.text(statement))
                executed += 1
                
                # Determine the type of statement for logging
                if "district_teacher_average_salary" in statement:
                    district_executed += 1
                elif "state_teacher_average_salary" in statement:
                    state_executed += 1
                
                if executed % 500 == 0:
                    logger.info(f"Executed {executed} statements so far")
            except Exception as e:
                if "duplicate key" in str(e).lower():
                    skipped += 1
                else:
                    logger.error(f"Error executing SQL: {str(e)[:100]}")
                    skipped += 1
                
        logger.info(f"SQL execution complete: {executed} statements executed ({district_executed} district, {state_executed} state), {skipped} skipped")
            
    except Exception as e:
        logger.error(f"Critical error during migration: {e}")
        raise Exception(f"Error during migration: {e}")
    
    logger.info("Migration completed successfully")


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