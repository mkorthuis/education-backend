"""Load District Teacher Education Data

Revision ID: d6f9c8b5a4e2
Revises: c5d7b9a8f2e3
Create Date: 2024-08-22 13:00:00.000000

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
revision = 'd6f9c8b5a4e2'
down_revision = 'c5d7b9a8f2e3'
branch_labels = None
depends_on = None


def load_config():
    """Load configuration from YAML file."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.abspath(os.path.join(current_dir, '../config/district_teacher_education_config.yaml'))
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


def try_parse_percentage(value):
    """Parse a percentage value, handling various text and numeric formats.
    
    Args:
        value: The raw percentage value (could be text, float, etc.)
        
    Returns:
        Float value representing the percentage (0-100 scale), or None if parsing fails
    """
    if pd.isna(value):
        return None
    
    # Already a number, return as is
    if isinstance(value, (int, float)):
        return float(value)
    
    # Handle string values
    if isinstance(value, str):
        # Remove % symbol and other non-numeric chars except decimal point
        clean_value = re.sub(r'[^0-9\.]', '', value.replace(',', '.'))
        try:
            if clean_value:
                # Convert to float
                result = float(clean_value)
                
                # If value < 1, it's likely already been converted from percentage
                # e.g., 0.25 instead of 25%
                if result < 1 and result > 0:
                    result = result * 100
                    
                return result
        except ValueError:
            pass
    
    return None


def process_district_teacher_education_data(df, year, config):
    """Process district teacher education data from Excel file for a specific year.
    
    Args:
        df: DataFrame containing district teacher education data
        year: The year for this data
        config: Configuration dictionary with column mappings
        
    Returns:
        Tuple of (district entries, state entries) to be inserted
    """
    # Map education types to their IDs
    education_type_map = {
        'none': 1,              # None
        'bachelor': 2,          # Bachelor
        'masters': 3,           # Masters
        'beyond_masters': 4,    # Beyond Masters
    }
    
    district_entries = []
    state_entries = []
    district_count = 0
    entry_count = 0
    processed_districts = set()  # Track districts we've already processed for this year
    
    # Get state total column index and identifier text from config
    state_total_col = config.get('state_data_settings', {}).get('state_column_index', 3)
    state_identifier_text = config.get('state_data_settings', {}).get('state_identifier_text', 'state total')
    
    logger.info(f"Looking for state data in column {state_total_col} with identifier text '{state_identifier_text}'")
    
    # Get column indices for easier access
    district_id_col = config['column_mappings']['district_id']
    total_teachers_col = config['column_mappings']['total_teachers']
    bachelor_percent_col = config['column_mappings']['bachelor_percent']
    masters_percent_col = config['column_mappings']['masters_percent']
    beyond_masters_percent_col = config['column_mappings']['beyond_masters_percent']
    
    # Process each row in the DataFrame
    for index, row in df.iterrows():
        try:
            # Check if this is a state total row
            is_state_total = False
            
            # Check for state identifier text in the specified column
            if len(row) > state_total_col:
                state_value = row.iloc[state_total_col] if isinstance(state_total_col, int) else row[state_total_col]
                if isinstance(state_value, str) and state_identifier_text.lower() in state_value.lower().strip():
                    is_state_total = True
                    logger.info(f"Found state total row at index {index} for year {year}")
            
            if is_state_total:
                # Process state-level data
                # Get total teachers - use iloc for integer-based positional indexing
                total_teachers_raw = row.iloc[total_teachers_col] if isinstance(total_teachers_col, int) else row[total_teachers_col]
                # Convert to float if possible
                try:
                    total_teachers = float(total_teachers_raw) if not pd.isna(total_teachers_raw) else 0
                except (ValueError, TypeError):
                    logger.warning(f"Line {index+1}: Could not convert state total teachers value to number: {total_teachers_raw}")
                    total_teachers = 0
                    
                if pd.isna(total_teachers) or total_teachers <= 0:
                    logger.warning(f"Line {index+1}: Invalid total teacher count for state total: {total_teachers}")
                    continue

                # Get percentages for each education type - use iloc for integer-based positional indexing
                raw_bachelor_percent = row.iloc[bachelor_percent_col] if isinstance(bachelor_percent_col, int) else row[bachelor_percent_col]
                raw_masters_percent = row.iloc[masters_percent_col] if isinstance(masters_percent_col, int) else row[masters_percent_col]
                raw_beyond_masters_percent = row.iloc[beyond_masters_percent_col] if isinstance(beyond_masters_percent_col, int) else row[beyond_masters_percent_col]
                
                # Parse percentage values, handling text formats
                bachelor_percent = try_parse_percentage(raw_bachelor_percent)
                masters_percent = try_parse_percentage(raw_masters_percent)
                beyond_masters_percent = try_parse_percentage(raw_beyond_masters_percent)
                
                # Convert percentages to values
                education_values = {}
                if not pd.isna(bachelor_percent) and bachelor_percent > 0:
                    education_values['bachelor'] = round_to_two_decimal((bachelor_percent / 100) * total_teachers)
                else:
                    education_values['bachelor'] = 0
                    
                if not pd.isna(masters_percent) and masters_percent > 0:
                    education_values['masters'] = round_to_two_decimal((masters_percent / 100) * total_teachers)
                else:
                    education_values['masters'] = 0
                    
                if not pd.isna(beyond_masters_percent) and beyond_masters_percent > 0:
                    education_values['beyond_masters'] = round_to_two_decimal((beyond_masters_percent / 100) * total_teachers)
                else:
                    education_values['beyond_masters'] = 0
                
                # Calculate 'none' as the remainder to make the total add up
                total_with_education = sum(education_values.values())
                
                # Account for rounding errors (allow for small difference)
                if abs(total_with_education - total_teachers) <= 0.1:
                    education_values['none'] = 0  # Essentially zero due to rounding
                else:
                    education_values['none'] = round_to_two_decimal(total_teachers - total_with_education)
                
                # Add state entries for each education type
                for edu_type, value in education_values.items():
                    # Skip if value is zero or negative (could happen due to rounding)
                    if value <= 0:
                        continue
                        
                    state_entries.append({
                        'education_type_id': education_type_map[edu_type],
                        'year': year,
                        'value': value
                    })
                    logger.info(f"Added state teacher education entry for year {year}, type {edu_type}: {value}")
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
                    
                district_count += 1
                
                # Verify district exists in database
                exists_check = sa.text("""
                    SELECT EXISTS (SELECT 1 FROM district WHERE id = :district_id)
                """)
                district_exists = op.get_bind().execute(exists_check, {"district_id": district_id}).scalar()
                
                if not district_exists:
                    logger.warning(f"Line {index+1}: District ID {district_id} not found in database")
                    continue
                
                # Check if this district already has education data for this year
                existing_check = sa.text("""
                    SELECT EXISTS (
                        SELECT 1 FROM district_teacher_education 
                        WHERE district_id_fk = :district_id AND year = :year
                    )
                """)
                has_existing_data = op.get_bind().execute(
                    existing_check, 
                    {"district_id": district_id, "year": year}
                ).scalar()
                
                if has_existing_data:
                    continue
                
                # Get total teachers - use iloc for integer-based positional indexing
                total_teachers_raw = row.iloc[total_teachers_col] if isinstance(total_teachers_col, int) else row[total_teachers_col]
                # Convert to float if possible
                try:
                    total_teachers = float(total_teachers_raw) if not pd.isna(total_teachers_raw) else 0
                except (ValueError, TypeError):
                    logger.warning(f"Line {index+1}: Could not convert total teachers value to number: {total_teachers_raw}")
                    total_teachers = 0
                    
                if pd.isna(total_teachers) or total_teachers <= 0:
                    logger.warning(f"Line {index+1}: Invalid total teacher count for district {district_id}: {total_teachers}")
                    continue

                # Get percentages for each education type - use iloc for integer-based positional indexing
                raw_bachelor_percent = row.iloc[bachelor_percent_col] if isinstance(bachelor_percent_col, int) else row[bachelor_percent_col]
                raw_masters_percent = row.iloc[masters_percent_col] if isinstance(masters_percent_col, int) else row[masters_percent_col]
                raw_beyond_masters_percent = row.iloc[beyond_masters_percent_col] if isinstance(beyond_masters_percent_col, int) else row[beyond_masters_percent_col]
                
                # Parse percentage values, handling text formats
                bachelor_percent = try_parse_percentage(raw_bachelor_percent)
                masters_percent = try_parse_percentage(raw_masters_percent)
                beyond_masters_percent = try_parse_percentage(raw_beyond_masters_percent)
                
                # Convert percentages to values
                education_values = {}
                if not pd.isna(bachelor_percent) and bachelor_percent > 0:
                    education_values['bachelor'] = round_to_two_decimal((bachelor_percent / 100) * total_teachers)
                else:
                    education_values['bachelor'] = 0
                    
                if not pd.isna(masters_percent) and masters_percent > 0:
                    education_values['masters'] = round_to_two_decimal((masters_percent / 100) * total_teachers)
                else:
                    education_values['masters'] = 0
                    
                if not pd.isna(beyond_masters_percent) and beyond_masters_percent > 0:
                    education_values['beyond_masters'] = round_to_two_decimal((beyond_masters_percent / 100) * total_teachers)
                else:
                    education_values['beyond_masters'] = 0
                
                # Calculate 'none' as the remainder to make the total add up
                total_with_education = sum(education_values.values())
                
                # Account for rounding errors (allow for small difference)
                if abs(total_with_education - total_teachers) <= 0.1:
                    education_values['none'] = 0  # Essentially zero due to rounding
                else:
                    education_values['none'] = round_to_two_decimal(total_teachers - total_with_education)
                
                # Add district entries for each education type
                for edu_type, value in education_values.items():
                    # Skip if value is zero or negative (could happen due to rounding)
                    if value <= 0:
                        continue
                        
                    district_entries.append({
                        'district_id': district_id,
                        'education_type_id': education_type_map[edu_type],
                        'year': year,
                        'value': value
                    })
                    entry_count += 1
                
                # Mark this district as processed
                processed_districts.add(district_id)
                
        except Exception as e:
            # Get detailed stack trace
            stack_trace = traceback.format_exc()
            
            # Log error information
            logger.error(f"Error processing Line {index+1} for year {year}: {str(e)}")
            logger.debug(f"Stack trace: {stack_trace}")
            
            continue
    
    logger.info(f"Processed {district_count} districts with {entry_count} teacher education entries for year {year}")
    logger.info(f"Found {len(state_entries)} state teacher education entries for year {year}")
    return district_entries, state_entries


def generate_sql(district_entries, state_entries):
    """Generate SQL INSERT statements for district and state teacher education data.
    
    Args:
        district_entries: List of district education data entries to be inserted
        state_entries: List of state education data entries to be inserted
        
    Returns:
        String containing SQL statements
    """
    sql_statements = []
    
    # Add district data if present
    if district_entries:
        sql_statements.append("-- District Teacher Education data INSERT statements")
        
        # Generate district INSERT statements
        for entry in district_entries:
            sql_statements.append(
                f"INSERT INTO district_teacher_education (teacher_type_id_fk, district_id_fk, year, value, "
                f"date_created, date_updated) VALUES ("
                f"{entry['education_type_id']}, "
                f"{entry['district_id']}, "
                f"{entry['year']}, "
                f"{entry['value']}, "
                f"CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);"
            )
    
    # Add state data if present
    if state_entries:
        sql_statements.append("\n-- State Teacher Education data INSERT statements")
        
        # Generate state INSERT statements
        for entry in state_entries:
            sql_statements.append(
                f"INSERT INTO state_teacher_education (teacher_type_id_fk, year, value, "
                f"date_created, date_updated) VALUES ("
                f"{entry['education_type_id']}, "
                f"{entry['year']}, "
                f"{entry['value']}, "
                f"CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);"
            )
    
    return "\n".join(sql_statements)


def upgrade():
    """Load district teacher education data across multiple years."""
    logger.info("Starting District Teacher Education Data migration")
    
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
            input_pattern = config['file_settings']['teacher_education_file']
            base_dir = os.path.abspath(os.path.join(current_dir, os.path.dirname(input_pattern)))
            base_pattern = os.path.basename(input_pattern)
            
            # Remove asterisks and get the pattern parts
            pattern_parts = base_pattern.split('****')
            
            # Get years from config
            years = config['file_settings'].get('years', [])
            logger.info(f"Processing data for years: {years}")
            
            found_files = 0
            
            for year in years:
                file_pattern = f"{pattern_parts[0]}{year}{pattern_parts[1] if len(pattern_parts) > 1 else ''}"
                file_path = os.path.join(base_dir, file_pattern)
                
                # Check if the file exists
                if os.path.exists(file_path):
                    found_files += 1
                    logger.info(f"Processing file for year {year}")
                    
                    # Load the Excel file
                    try:
                        df = pd.read_excel(
                            file_path,
                            sheet_name=config['file_settings']['sheet_name'],
                            skiprows=config['file_settings']['start_row'] - 1
                        )
                        
                        # Process district and state teacher education entries for this file
                        district_year_entries, state_year_entries = process_district_teacher_education_data(df, year, config)
                        logger.info(f"Found {len(district_year_entries)} district teacher education entries for year {year}")
                        logger.info(f"Found {len(state_year_entries)} state teacher education entries for year {year}")
                        all_district_entries.extend(district_year_entries)
                        all_state_entries.extend(state_year_entries)
                    except Exception as e:
                        logger.error(f"Error processing file for year {year}: {e}")
                        # Continue to next file rather than failing completely
                        continue
                else:
                    logger.warning(f"File not found for year {year}")
            
            logger.info(f"Processed {found_files} files")
            logger.info(f"Total district teacher education entries found: {len(all_district_entries)}")
            logger.info(f"Total state teacher education entries found: {len(all_state_entries)}")
            
            if len(all_district_entries) == 0 and len(all_state_entries) == 0:
                logger.error("No teacher education entries were found! Check file paths and Excel structure.")
                raise Exception("No teacher education entries found")
            
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
                if "district_teacher_education" in statement:
                    district_executed += 1
                elif "state_teacher_education" in statement:
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
    """Remove district teacher education data and related objects."""
    logger.info("Starting District Teacher Education Data migration downgrade")
    
    # Remove all data from state_teacher_education table
    logger.info("Removing data from state_teacher_education table")
    op.execute("DELETE FROM state_teacher_education")
    
    # Remove all data from district_teacher_education table
    logger.info("Removing data from district_teacher_education table")
    op.execute("DELETE FROM district_teacher_education")
    
    logger.info("Downgrade completed successfully") 