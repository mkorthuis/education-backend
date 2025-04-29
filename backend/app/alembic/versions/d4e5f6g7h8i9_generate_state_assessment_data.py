"""Generate State Assessment Data (2009-2017)

Revision ID: d4e5f6g7h8i9
Revises: c3d4e5f6g7h8
Create Date: 2023-07-23 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
import logging
import pandas as pd
import numpy as np

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# Revision identifiers, used by Alembic
revision = 'd4e5f6g7h8i9'
down_revision = 'c3d4e5f6g7h8'
branch_labels = None
depends_on = None


def get_assessment_subgroup_id(conn, subgroup_name='All students'):
    """Get the subgroup ID for 'All students'."""
    query = f"SELECT id FROM assessment_subgroup WHERE name = '{subgroup_name}'"
    result = conn.execute(sa.text(query))
    row = result.fetchone()
    if not row:
        # Throw an error if subgroup doesn't exist
        raise ValueError(f"Assessment subgroup '{subgroup_name}' does not exist. Please create it before running this migration.")
    return row[0]


def get_district_assessment_data(conn, year, subject_id, grade_id, subgroup_id):
    """Get assessment data for all districts for a specific year, subject, grade, and subgroup."""
    grade_condition = "grade_id_fk IS NULL" if grade_id is None else f"grade_id_fk = {grade_id}"
    
    query = f"""
    SELECT
        district_id_fk,
        total_fay_students_low,
        total_fay_students_high,
        level_1_percentage,
        level_1_percentage_exception,
        level_2_percentage,
        level_2_percentage_exception,
        level_3_percentage,
        level_3_percentage_exception,
        level_4_percentage,
        level_4_percentage_exception,
        above_proficient_percentage,
        above_proficient_percentage_exception,
        average_score
    FROM
        assessment_district
    WHERE
        year = {year}
        AND assessment_subject_id_fk = {subject_id}
        AND {grade_condition}
        AND assessment_subgroup_id_fk = {subgroup_id}
    """
    
    result = conn.execute(sa.text(query))
    district_data = []
    
    for row in result:
        district_data.append({
            'district_id': row[0],
            'total_fay_students_low': row[1],
            'total_fay_students_high': row[2],
            'level_1_percentage': row[3],
            'level_1_percentage_exception': row[4],
            'level_2_percentage': row[5],
            'level_2_percentage_exception': row[6],
            'level_3_percentage': row[7],
            'level_3_percentage_exception': row[8],
            'level_4_percentage': row[9],
            'level_4_percentage_exception': row[10],
            'above_proficient_percentage': row[11],
            'above_proficient_percentage_exception': row[12],
            'average_score': row[13]
        })
    
    return district_data


def combine_exception_values(values, weights):
    """Determine the most appropriate exception value based on weighted counts."""
    if not values or all(v is None for v in values):
        return None
    
    # Filter out None values
    valid_values = [(v, w) for v, w in zip(values, weights) if v is not None]
    if not valid_values:
        return None
    
    # Count occurrences weighted by student count
    exceptions = {}
    for value, weight in valid_values:
        exceptions[value] = exceptions.get(value, 0) + weight
    
    # Return the most common exception
    return max(exceptions.items(), key=lambda x: x[1])[0]


def calculate_weighted_average(values, weights):
    """Calculate weighted average, handling None values."""
    valid_data = [(v, w) for v, w in zip(values, weights) if v is not None]
    if not valid_data:
        return None
    
    total_weight = sum(w for _, w in valid_data)
    if total_weight == 0:
        return None
    
    # Convert decimal.Decimal to float before multiplication
    weighted_sum = sum(float(v) * float(w) for v, w in valid_data)
    return weighted_sum / float(total_weight)


def aggregate_state_data(conn, year, subject_id, grade_id, subgroup_id):
    """Aggregate district-level data into state-level data."""
    # Get all district assessment data for this combination
    district_data = get_district_assessment_data(conn, year, subject_id, grade_id, subgroup_id)
    
    if not district_data:
        logger.warning(f"No district assessment data found for year {year}, subject {subject_id}, grade {grade_id}")
        return None
    
    # Define fields to process
    percentage_fields = [
        'level_1_percentage',
        'level_2_percentage',
        'level_3_percentage',
        'level_4_percentage',
        'above_proficient_percentage',
        'average_score'
    ]
    
    exception_fields = [
        'level_1_percentage_exception',
        'level_2_percentage_exception',
        'level_3_percentage_exception',
        'level_4_percentage_exception',
        'above_proficient_percentage_exception'
    ]
    
    # Initialize data collection structures
    percentage_values = {field: [] for field in percentage_fields}
    exception_values = {field: [] for field in exception_fields}
    weights = []
    student_counts = {'low': [], 'high': []}
    
    # Process all districts in a single loop
    for data in district_data:
        # Check if any percentage field has the TOO_FEW_SAMPLES exception
        has_too_few_samples = False
        for i, field in enumerate(percentage_fields):
            if field != 'average_score':  # Skip average_score as it doesn't have an exception
                exception_field = exception_fields[i]
                if data[exception_field] == 'TOO_FEW_SAMPLES':
                    has_too_few_samples = True
                    break
        
        # Skip this district if it has TOO_FEW_SAMPLES exception
        if has_too_few_samples:
            continue
        
        # Calculate weight for this district
        low = data['total_fay_students_low'] or 0
        high = data['total_fay_students_high'] or 0
        
        # Collect student counts
        if data['total_fay_students_low'] is not None:
            student_counts['low'].append(data['total_fay_students_low'])
        if data['total_fay_students_high'] is not None:
            student_counts['high'].append(data['total_fay_students_high'])
        
        # Determine weight for this district
        if low and high:
            weight = (low + high) / 2
        elif low:
            weight = low
        elif high:
            weight = high
        else:
            weight = 1  # Default weight if no student count is available
        
        weights.append(weight)
        
        # Handle special exception cases and collect values
        for i, field in enumerate(percentage_fields):
            if field == 'average_score':
                # Average score doesn't have exceptions
                percentage_values[field].append(data[field])
                continue
                
            exception_field = exception_fields[i]
            percentage_value = data[field]
            exception_value = data[exception_field]
            
            # Apply exception handling logic
            if exception_value == 'SCORE_UNDER_10':
                # Use 9% for SCORE_UNDER_10
                percentage_values[field].append(9.0)
                exception_values[exception_field].append(exception_value)
            elif exception_value == 'SCORE_OVER_90':
                # Use 91% for SCORE_OVER_90
                percentage_values[field].append(91.0)
                exception_values[exception_field].append(exception_value)
            else:
                # Normal processing for other cases
                percentage_values[field].append(percentage_value)
                exception_values[exception_field].append(exception_value)
    
    # If no valid districts remain after filtering, return None
    if not weights:
        logger.warning(f"No valid district data found after filtering exceptions for year {year}, subject {subject_id}, grade {grade_id}")
        return None
    
    # Calculate aggregated values
    aggregated_data = {}
    
    # Calculate total student counts
    total_low = sum(student_counts['low']) if student_counts['low'] else None
    total_high = sum(student_counts['high']) if student_counts['high'] else None
    
    aggregated_data['total_fay_students_low'] = total_low if total_low and total_low > 0 else None
    aggregated_data['total_fay_students_high'] = total_high if total_high and total_high > 0 else None
    
    # Calculate weighted averages for percentage fields
    for field in percentage_fields:
        aggregated_data[field] = calculate_weighted_average(percentage_values[field], weights)
    
    # Determine exception values
    for field in exception_fields:
        aggregated_data[field] = combine_exception_values(exception_values[field], weights)
    
    return aggregated_data


def generate_state_assessment_data(conn, years_range, grades):
    """Generate state assessment data for specified years and grades."""
    
    # Get subgroup ID for 'All students'
    subgroup_id = get_assessment_subgroup_id(conn)
    
    # Get all subjects
    query = "SELECT id, name FROM assessment_subject ORDER BY id"
    subjects = conn.execute(sa.text(query)).fetchall()
    
    # Get grade IDs once
    grade_ids = {}
    for grade in grades:
        if grade == 'All Grades':
            grade_ids[grade] = None
        else:
            grade_query = f"SELECT id FROM grades WHERE name = 'Grade {grade}'"
            grade_result = conn.execute(sa.text(grade_query))
            grade_row = grade_result.fetchone()
            if not grade_row:
                logger.warning(f"Grade 'Grade {grade}' not found in database")
                continue
            grade_ids[grade] = grade_row[0]
    
    # Track statistics
    records_generated = 0
    
    # Generate insert statements
    insert_statements = []
    
    for year in years_range:
        logger.info(f"Processing state data for year: {year}")
        
        for subject_id, subject_name in subjects:
            for grade, grade_id in grade_ids.items():
                # Skip if grade ID wasn't found
                if grade != 'All Grades' and grade not in grade_ids:
                    continue
                
                # Check if state assessment data already exists
                check_query = f"""
                SELECT id FROM assessment_state 
                WHERE year = {year} 
                AND assessment_subject_id_fk = {subject_id}
                AND {'grade_id_fk IS NULL' if grade_id is None else f'grade_id_fk = {grade_id}'}
                AND assessment_subgroup_id_fk = {subgroup_id}
                """
                
                existing = conn.execute(sa.text(check_query)).fetchone()
                if existing:
                    logger.debug(f"State data already exists for year {year}, subject {subject_id}, grade {grade_id}")
                    continue
                
                # Aggregate data from districts
                aggregated_data = aggregate_state_data(conn, year, subject_id, grade_id, subgroup_id)
                
                if not aggregated_data:
                    continue
                
                # Format values for SQL
                values = [
                    str(subject_id),   # assessment_subject_id_fk
                    str(year),         # year
                    'NULL' if grade_id is None else str(grade_id),  # grade_id_fk
                    str(subgroup_id),  # assessment_subgroup_id_fk
                    'NULL' if aggregated_data['total_fay_students_low'] is None else str(aggregated_data['total_fay_students_low']),
                    'NULL' if aggregated_data['total_fay_students_high'] is None else str(aggregated_data['total_fay_students_high']),
                    'NULL' if aggregated_data['level_1_percentage'] is None else str(aggregated_data['level_1_percentage']),
                    'NULL' if aggregated_data['level_1_percentage_exception'] is None else f"'{aggregated_data['level_1_percentage_exception']}'",
                    'NULL' if aggregated_data['level_2_percentage'] is None else str(aggregated_data['level_2_percentage']),
                    'NULL' if aggregated_data['level_2_percentage_exception'] is None else f"'{aggregated_data['level_2_percentage_exception']}'",
                    'NULL' if aggregated_data['level_3_percentage'] is None else str(aggregated_data['level_3_percentage']),
                    'NULL' if aggregated_data['level_3_percentage_exception'] is None else f"'{aggregated_data['level_3_percentage_exception']}'",
                    'NULL' if aggregated_data['level_4_percentage'] is None else str(aggregated_data['level_4_percentage']),
                    'NULL' if aggregated_data['level_4_percentage_exception'] is None else f"'{aggregated_data['level_4_percentage_exception']}'",
                    'NULL' if aggregated_data['above_proficient_percentage'] is None else str(aggregated_data['above_proficient_percentage']),
                    'NULL' if aggregated_data['above_proficient_percentage_exception'] is None else f"'{aggregated_data['above_proficient_percentage_exception']}'",
                    'NULL',  # participate_percentage
                    'NULL',  # mean_sgp
                    'NULL' if aggregated_data['average_score'] is None else str(aggregated_data['average_score'])
                ]
                
                # Create insert statement
                insert_sql = f"""
                INSERT INTO assessment_state (
                    assessment_subject_id_fk, year, grade_id_fk, assessment_subgroup_id_fk,
                    total_fay_students_low, total_fay_students_high,
                    level_1_percentage, level_1_percentage_exception,
                    level_2_percentage, level_2_percentage_exception,
                    level_3_percentage, level_3_percentage_exception,
                    level_4_percentage, level_4_percentage_exception,
                    above_proficient_percentage, above_proficient_percentage_exception,
                    participate_percentage, mean_sgp, average_score
                ) VALUES (
                    {', '.join(values)}
                )
                """
                
                insert_statements.append(insert_sql)
                records_generated += 1
    
    logger.info(f"Generated {records_generated} state assessment records")
    return insert_statements


def upgrade():
    """Upgrade function to generate state assessment data."""
    try:
        conn = op.get_bind()
        
        # Define years range and grades
        years_range = range(2009, 2018)  # 2009 to 2017
        grades = ['3', '4', '5', '6', '7', '8', '11', 'All Grades']
        
        # Generate state data
        insert_statements = generate_state_assessment_data(conn, years_range, grades)
        
        # Execute statements
        executed = 0
        for stmt in insert_statements:
            try:
                conn.execute(sa.text(stmt))
                executed += 1
            except Exception as e:
                logger.error(f"Error executing statement: {e}")
                logger.error(f"Statement: {stmt[:300]}...")
                raise
        
        logger.info(f"Successfully executed {executed} SQL statements")
        
    except Exception as e:
        logger.error(f"Error during migration: {e}")
        raise


def downgrade():
    """Downgrade function to remove generated state assessment data."""
    try:
        conn = op.get_bind()
        
        # Delete generated state data for 2009-2017
        delete_sql = """
        DELETE FROM assessment_state
        WHERE year BETWEEN 2009 AND 2017
        """
        
        conn.execute(sa.text(delete_sql))
        logger.info("Successfully removed generated state assessment data for years 2009-2017")
        
    except Exception as e:
        logger.error(f"Error during downgrade: {e}")
        raise 