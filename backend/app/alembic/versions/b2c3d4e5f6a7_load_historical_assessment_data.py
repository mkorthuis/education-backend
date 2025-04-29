"""Load Historical Assessment Data (2009-2017)

Revision ID: b2c3d4e5f6a7
Revises: a1b2c3d4e5f6
Create Date: 2023-07-21 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
import pandas as pd
import logging
import os
import yaml
import re

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# Revision identifiers, used by Alembic
revision = 'b2c3d4e5f6a7'
down_revision = 'a1b2c3d4e5f6'
branch_labels = None
depends_on = None

# Config path 
CONFIG_PATH = "app/alembic/config/assessment_historical_data_config.yaml"


def load_config(config_path=CONFIG_PATH):
    """Load configuration from YAML file."""
    try:
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        # Try alternative path
        alt_path = "backend/{}".format(config_path)
        try:
            with open(alt_path, 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            logger.error("Config file not found at {} or {}".format(config_path, alt_path))
            raise
    except Exception as e:
        logger.error("Error loading config: {}".format(e))
        raise


def parse_assessment_percentage(value):
    """Parse assessment percentage values, identifying special cases."""
    if pd.isna(value) or value == '' or value == '-' or value == 'NULL':
        return None, None
    
    # Check for special notation
    if isinstance(value, str):
        if '*' in value:
            return None, 'TOO_FEW_SAMPLES'
        elif '<' in value and '10' in value:
            return None, 'SCORE_UNDER_10'
        elif '>' in value and '90' in value:
            return None, 'SCORE_OVER_90'
        
        # Try to extract numeric value
        try:
            # Remove % and other non-numeric characters
            cleaned = re.sub(r'[^0-9.]', '', value)
            if cleaned == '':
                return None, None
            return float(cleaned), None
        except ValueError:
            return None, None
    
    elif isinstance(value, (int, float)):
        return float(value), None
    
    return None, None


def parse_student_range(value):
    """Parse student range in format 'low-high'."""
    if pd.isna(value) or value == '' or value == '-' or value == 'NULL':
        return None, None
    
    if isinstance(value, str):
        # Remove commas from the string before processing
        value = value.replace(',', '')
        
        # Try to extract range values
        match = re.search(r'(\d+)\s*-\s*(\d+)', value)
        if match:
            try:
                low = int(match.group(1))
                high = int(match.group(2))
                return low, high
            except ValueError:
                pass
        
        # Try as single value
        try:
            num = int(float(re.sub(r'[^0-9.]', '', value)))
            return num, num
        except ValueError:
            pass
    
    elif isinstance(value, (int, float)):
        num = int(value)
        return num, num
    
    return None, None


def get_assessment_subject_id(subject):
    """Get assessment subject ID from subject name."""
    subject_map = {
        'Math': 1,
        'Reading': 2,
        'Science': 3,
        'MAT': 1,
        'REA': 2,
        'SCI': 3,
        'mat': 1,
        'rea': 2,
        'sci': 3
    }
    return subject_map.get(subject)


def get_grade_id(grade_name, conn):
    """Get grade ID from grade name."""
    try:
        if pd.isna(grade_name) or not grade_name:
            return None
        
        # Handle special case for historical data: grade 0 means "All Grades"
        if str(grade_name).strip() == '0':
            return None  # All grades is represented as NULL in the database
        
        # Standardize grade name
        grade_name = str(grade_name).strip().lower()
        if grade_name == 'all':
            return None
        
        if grade_name.startswith('0') and len(grade_name) > 1 and grade_name[1:].isdigit():
            grade_name = grade_name[1:]
            
        query = "SELECT id FROM grades WHERE name = 'Grade {}'".format(grade_name.replace("'", "''"))
        result = conn.execute(sa.text(query))
        row = result.fetchone()
        return row[0] if row else None
    except Exception as e:
        logger.error("Error querying grade ID for {}: {}".format(grade_name, e))
        return None


def format_sql_value(value, is_exception=False):
    """Format a value for SQL insertion."""
    if value is None:
        return 'NULL'
    elif is_exception and value is not None:
        return "'{}'".format(value)
    else:
        return str(value)


def process_historical_assessment_data(config, file_path, conn, year):
    """Process historical assessment data from CSV file and return SQL insert statements."""
    # Get school name translations from config
    school_name_translations = config.get('school_name_translations', {})
    
    # Track subgroups for creation
    subgroups = {}
    next_subgroup_id = 1
    
    # Get current subgroups from database
    try:
        query = "SELECT id, name FROM assessment_subgroup"
        result = conn.execute(sa.text(query))
        for row in result:
            subgroups[row[1]] = row[0]
            next_subgroup_id = max(next_subgroup_id, row[0] + 1)
    except Exception as e:
        logger.warning("Could not retrieve existing subgroups: {}".format(e))
    
    # Check if 'All students' subgroup exists, create if not
    if 'All students' not in subgroups:
        subgroups['All students'] = next_subgroup_id
        # Will be inserted before data
        next_subgroup_id += 1
    
    # SQL statements for inserts, organized by type
    subgroup_insert_statements = []  # Statements to create subgroups (must be executed first)
    data_insert_statements = []      # Statements to insert actual assessment data (must be executed after subgroups)
    
    # Track missing entities
    missing_schools = {}
    missing_districts = {}
    missing_grades = {}
    
    try:
        # Read CSV file
        df = pd.read_csv(file_path, dtype=str, encoding='latin1')
        
        logger.info("Processing {} assessment data, found {} rows".format(year, len(df)))
        
        # Log the columns
        columns = list(df.columns)
        logger.info("File columns: {}".format(columns))
        
        # Process each row
        for idx, row in df.iterrows():
            try:
                # Skip if missing essential data
                if pd.isna(row.get('subject')):
                    continue
                
                # Determine the level (state, district, school)
                level = row.get('replevel')
                if pd.isna(level):
                    continue
                
                level = level.strip()
                
                # Get subject ID
                subject = row.get('subject')
                subject_id = get_assessment_subject_id(subject)
                if subject_id is None:
                    logger.warning("Unknown subject: {}".format(subject))
                    continue
                
                # In historical data (2009-2017), we only have "All students" as subgroup
                subgroup = 'All students'
                subgroup_id = subgroups[subgroup]
                
                # Parse year (from file or use the year param)
                year_val = row.get('yearid', year)
                if pd.isna(year_val):
                    year_val = year
                else:
                    try:
                        year_val = int(float(year_val))
                    except ValueError:
                        year_val = year
                
                # Parse grade
                grade_name = row.get('grade', '0')
                grade_id = get_grade_id(grade_name, conn)
                
                # Parse student count range
                students_low, students_high = parse_student_range(row.get('NumberStudents'))
                
                # Parse percentage fields with exception handling
                level1_pct, level1_exc = parse_assessment_percentage(row.get('plevel1'))
                level2_pct, level2_exc = parse_assessment_percentage(row.get('plevel2'))
                level3_pct, level3_exc = parse_assessment_percentage(row.get('plevel3'))
                level4_pct, level4_exc = parse_assessment_percentage(row.get('plevel4'))
                above_prof_pct, above_prof_exc = parse_assessment_percentage(row.get('pAboveprof'))
                
                # Parse other numeric fields - in historical data, we only have average score in column Q
                participate_pct = None  # We don't have this in historical data
                mean_sgp = None  # We don't have this in historical data
                
                avg_score = None
                if not pd.isna(row.get('AvgScore')) and row.get('AvgScore') != 'NULL':
                    try:
                        avg_score = float(row.get('AvgScore'))
                    except (ValueError, TypeError):
                        avg_score = None
                
                # Common values for all levels
                common_values = [
                    str(subject_id),
                    str(year_val),
                    format_sql_value(grade_id),
                    str(subgroup_id),
                    format_sql_value(students_low),
                    format_sql_value(students_high),
                    format_sql_value(level1_pct),
                    format_sql_value(level1_exc, is_exception=True),
                    format_sql_value(level2_pct),
                    format_sql_value(level2_exc, is_exception=True),
                    format_sql_value(level3_pct),
                    format_sql_value(level3_exc, is_exception=True),
                    format_sql_value(level4_pct),
                    format_sql_value(level4_exc, is_exception=True),
                    format_sql_value(above_prof_pct),
                    format_sql_value(above_prof_exc, is_exception=True),
                    format_sql_value(participate_pct),
                    format_sql_value(mean_sgp),
                    format_sql_value(avg_score)
                ]
                
                # Create SQL statements based on level
                if level == 'sta':  # State Level
                    state_sql = "INSERT INTO assessment_state (assessment_subject_id_fk, year, grade_id_fk, assessment_subgroup_id_fk, total_fay_students_low, total_fay_students_high, level_1_percentage, level_1_percentage_exception, level_2_percentage, level_2_percentage_exception, level_3_percentage, level_3_percentage_exception, level_4_percentage, level_4_percentage_exception, above_proficient_percentage, above_proficient_percentage_exception, participate_percentage, mean_sgp, average_score) VALUES ({})".format(', '.join(common_values))
                    data_insert_statements.append(state_sql)
                    
                elif level == 'dis':  # District Level
                    # Get district ID directly from the CSV
                    district_id = row.get('discode')
                    if pd.isna(district_id) or not district_id or district_id == 'NULL':
                        # Log missing district
                        district_name = row.get('disname')
                        if district_name and not pd.isna(district_name) and district_name != 'NULL':
                            if district_name not in missing_districts:
                                missing_districts[district_name] = {'id': 'Missing', 'years': set()}
                            missing_districts[district_name]['years'].add(year_val)
                        continue
                    
                    # Verify district ID exists in database
                    try:
                        check_query = "SELECT id FROM district WHERE id = {}".format(district_id)
                        check_result = conn.execute(sa.text(check_query))
                        if not check_result.fetchone():
                            # District ID doesn't exist
                            district_name = row.get('disname')
                            if district_name and not pd.isna(district_name) and district_name != 'NULL':
                                if district_name not in missing_districts:
                                    missing_districts[district_name] = {'id': district_id, 'years': set()}
                                missing_districts[district_name]['years'].add(year_val)
                            continue
                    except Exception as e:
                        logger.warning("Error verifying district ID {}: {}".format(district_id, e))
                        continue
                    
                    # District level insert
                    district_sql = "INSERT INTO assessment_district (district_id_fk, assessment_subject_id_fk, year, grade_id_fk, assessment_subgroup_id_fk, total_fay_students_low, total_fay_students_high, level_1_percentage, level_1_percentage_exception, level_2_percentage, level_2_percentage_exception, level_3_percentage, level_3_percentage_exception, level_4_percentage, level_4_percentage_exception, above_proficient_percentage, above_proficient_percentage_exception, participate_percentage, mean_sgp, average_score) VALUES ({}, {})".format(district_id, ', '.join(common_values))
                    data_insert_statements.append(district_sql)
                    
                elif level == 'sch':  # School Level
                    # Get school ID directly from the CSV
                    school_id = row.get('schcode')
                    if pd.isna(school_id) or not school_id or school_id == 'NULL' or school_id == '0':
                        # Skip schools with no ID
                        school_name = row.get('schname')
                        if school_name and not pd.isna(school_name) and school_name != 'NULL':
                            if school_name not in missing_schools:
                                missing_schools[school_name] = {'id': 'Missing', 'years': set()}
                            missing_schools[school_name]['years'].add(year_val)
                        continue
                    
                    # Verify school ID exists in database
                    try:
                        check_query = "SELECT id FROM school WHERE id = {}".format(school_id)
                        check_result = conn.execute(sa.text(check_query))
                        if not check_result.fetchone():
                            # School ID doesn't exist
                            school_name = row.get('schname')
                            if school_name and not pd.isna(school_name) and school_name != 'NULL':
                                if school_name not in missing_schools:
                                    missing_schools[school_name] = {'id': school_id, 'years': set()}
                                missing_schools[school_name]['years'].add(year_val)
                            continue
                    except Exception as e:
                        logger.warning("Error verifying school ID {}: {}".format(school_id, e))
                        continue
                    
                    # School level insert
                    school_sql = "INSERT INTO assessment_school (school_id_fk, assessment_subject_id_fk, year, grade_id_fk, assessment_subgroup_id_fk, total_fay_students_low, total_fay_students_high, level_1_percentage, level_1_percentage_exception, level_2_percentage, level_2_percentage_exception, level_3_percentage, level_3_percentage_exception, level_4_percentage, level_4_percentage_exception, above_proficient_percentage, above_proficient_percentage_exception, participate_percentage, mean_sgp, average_score) VALUES ({}, {})".format(school_id, ', '.join(common_values))
                    data_insert_statements.append(school_sql)
            
            except Exception as e:
                logger.error("Error processing row {}: {}".format(idx, e))
                continue
                
    except Exception as e:
        logger.error("Error processing file {}: {}".format(file_path, e))
    
    # Log missing schools and districts
    if missing_schools:
        missing_schools_list = []
        for school, info in missing_schools.items():
            years_str = ', '.join(str(y) for y in sorted(info['years']))
            missing_schools_list.append("{} (ID: {}): years [{}]".format(school, info['id'], years_str))
        
        missing_schools_log = "\n- ".join(sorted(missing_schools_list))
        logger.warning("The following schools were not found in the database:\n- {}".format(missing_schools_log))
    
    if missing_districts:
        missing_districts_list = []
        for district, info in missing_districts.items():
            years_str = ', '.join(str(y) for y in sorted(info['years']))
            missing_districts_list.append("{} (ID: {}): years [{}]".format(district, info['id'], years_str))
        
        missing_districts_log = "\n- ".join(sorted(missing_districts_list))
        logger.warning("The following districts were not found in the database:\n- {}".format(missing_districts_log))
    
    # Check if we need to insert the 'All students' subgroup
    if 'All students' in subgroups and subgroups['All students'] >= next_subgroup_id - 1:
        subgroup_insert_statements.append(
            "INSERT INTO assessment_subgroup (id, name, description) VALUES ({}, 'All students', NULL)".format(
                subgroups['All students']
            )
        )
    
    # Return statements in correct dependency order - subgroups first, then data
    insert_statements = subgroup_insert_statements + data_insert_statements
    logger.info("Generated {} insert statements for {} assessment data, {} for subgroups".format(
        len(insert_statements), year, len(subgroup_insert_statements)))
    
    return insert_statements


def upgrade():
    """Alembic upgrade function to load historical assessment data."""
    try:
        # Load configuration
        config = load_config()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Get range of years from config
        year_start = int(config['file_settings']['year_start'])
        year_end = int(config['file_settings']['year_end'])
        
        # Check for existing cache file
        cache_dir = os.path.abspath(os.path.join(current_dir, config['file_settings']['sql_cache_dir']))
        cache_file = os.path.join(cache_dir, "{}_cache.sql".format(revision))
        
        # Use cached SQL if available
        if os.path.exists(cache_file):
            logger.info("Using cached SQL from {}".format(cache_file))
            with open(cache_file, 'r') as f:
                sql_statements = [stmt for stmt in f.read().split(';') if stmt.strip()]
        else:
            logger.info("Processing historical assessment data from {} to {} and generating SQL statements".format(
                year_start, year_end))
            
            # Get database connection for entity lookups
            conn = op.get_bind()
            
            # Process each year's data
            all_sql_statements = []
            for year in range(year_start, year_end + 1):
                # Define the assessment data file path for this year
                file_path = os.path.join(
                    current_dir, 
                    "../assets/assessments/assessments-{}.csv".format(year)
                )
                
                # Check alternative paths if file not found
                if not os.path.exists(file_path):
                    alt_path = os.path.join(
                        current_dir, 
                        "../../alembic/assets/assessments/assessments-{}.csv".format(year)
                    )
                    if os.path.exists(alt_path):
                        file_path = alt_path
                    else:
                        logger.warning("Assessment data file for year {} not found at {} or {}".format(
                            year, file_path, alt_path))
                        continue
                
                # Process this year's assessment data
                year_statements = process_historical_assessment_data(config, file_path, conn, year)
                all_sql_statements.extend(year_statements)
                
                logger.info("Processed assessment data for year {}, added {} SQL statements".format(
                    year, len(year_statements)))
            
            # Use the combined statements
            sql_statements = all_sql_statements
            
            # Save to cache
            os.makedirs(cache_dir, exist_ok=True)
            with open(cache_file, 'w') as f:
                f.write(';\n'.join(stmt.strip() for stmt in sql_statements))
            
            logger.info("Cached {} SQL statements to {}".format(len(sql_statements), cache_file))
        
        # Execute SQL statements
        executed = 0
        for statement in sql_statements:
            statement = statement.strip()
            if not statement:  # Skip empty statements
                continue
                
            try:
                op.execute(sa.text(statement))
                executed += 1
            except Exception as e:
                if "duplicate key" in str(e).lower():
                    logger.warning("Duplicate key error (continuing): {}".format(str(e)[:100]))
                else:
                    logger.error("Error executing SQL statement: {}".format(e))
                    logger.error("Statement: {}".format(statement[:300]))
                    break
            
        logger.info("Successfully executed {} SQL statements".format(executed))
            
    except Exception as e:
        logger.error("Error during migration: {}".format(e))
        raise


def downgrade():
    """Alembic downgrade function to remove historical assessment data."""
    try:
        # Load configuration to get year range
        config = load_config()
        year_start = int(config['file_settings']['year_start'])
        year_end = int(config['file_settings']['year_end'])
        
        # Build delete statements for each year
        delete_statements = []
        for year in range(year_start, year_end + 1):
            delete_statements.extend([
                "DELETE FROM assessment_school WHERE year = {}".format(year),
                "DELETE FROM assessment_district WHERE year = {}".format(year),
                "DELETE FROM assessment_state WHERE year = {}".format(year)
            ])
        
        # Execute delete statements
        for statement in delete_statements:
            op.execute(sa.text(statement))
            
        logger.info("Successfully deleted historical assessment data for years {}-{}".format(
            year_start, year_end))
    except Exception as e:
        logger.error("Error during downgrade: {}".format(e))
        raise 