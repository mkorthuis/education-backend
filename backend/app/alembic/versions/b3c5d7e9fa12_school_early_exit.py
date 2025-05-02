"""School Early Exit

Revision ID: b3c5d7e9fa12
Revises: f7e9d0b8c6a4
Create Date: 2024-10-01 12:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
import pandas as pd
import yaml
import logging
import os
import re
from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# Revision identifiers, used by Alembic.
revision = 'b3c5d7e9fa12'
down_revision = 'f7e9d0b8c6a4'
branch_labels = None
depends_on = None

# ----------------------------
# Helper / Utility Functions
# ----------------------------

def load_config():
    """Load configuration from YAML file. Raises if the file is missing or invalid."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.abspath(os.path.join(current_dir, '../config/school_early_exit_config.yaml'))
    logger.info(f"Attempting to load configuration from: {config_path}")

    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
            logger.info(f"Successfully loaded configuration: {config}")
            return config
    except Exception as e:
        logger.error(f"Failed to load configuration file: {e}")
        raise


def clean_numeric(value):
    """Return float value stripped of non-numeric chars, else None."""
    if pd.isna(value) or value == "":
        return None
    if isinstance(value, (int, float)):
        return float(value)
    cleaned = re.sub(r'[^0-9.-]', '', str(value))
    try:
        return float(cleaned) if cleaned else None
    except ValueError:
        logger.debug(f"Unable to parse numeric value from '{value}'")
        return None


def round_four_decimal(value):
    if value is None:
        return None
    return float(Decimal(str(value)).quantize(Decimal('0.0001'), rounding=ROUND_HALF_UP))


def get_school_id_by_name(conn, name):
    """Return school id matching (case-insensitive) the given trimmed name or None."""
    query = sa.text("SELECT id FROM school WHERE lower(trim(name)) = lower(trim(:name)) LIMIT 1")
    result = conn.execute(query, {"name": name})
    row = result.fetchone()
    return row[0] if row else None


def get_school_id_by_id(conn, sid):
    try:
        sid_int = int(float(sid))
    except (ValueError, TypeError):
        return None
    result = conn.execute(sa.text("SELECT id FROM school WHERE id = :id"), {"id": sid_int}).fetchone()
    return result[0] if result else None


def process_school_early_exit(df, year, config):
    """Extract school and state early exit entries from a DataFrame for a given year.

    Returns (school_entries, state_entry_or_none)
    """
    mappings = config['column_mappings']
    name_col = mappings['school_name']

    # Map of column keys to index for numeric fields
    numeric_cols = {k: v for k, v in mappings.items() if k != 'school_name'}

    school_entries = []
    state_entry = None
    processed_rows = 0
    conn = op.get_bind()
    seen_schools = set()

    percentage_fields = [
        'annual_early_exit_percentage',
        '4_year_early_exit_percentage',
        'annual_dropout_percentage',
        '4_year_dropout_percentage'
    ]

    for idx, row in df.iterrows():
        # Log entire row for inspection
        logger.info(f"Row {idx}: {row.tolist()}")

        # Detect state total flag first (may occur on rows where school name column is blank)
        state_flag_match = False
        if year <= 2019:
            flag_val = row.iloc[5] if len(row) > 5 else None
        else:
            flag_val = row.iloc[3] if len(row) > 3 else None

        if isinstance(flag_val, str) and flag_val.strip().lower() == 'state total':
            state_flag_match = True

        raw_name = row.iloc[name_col] if len(row) > name_col else None
        cell_val_str = str(raw_name).strip() if raw_name is not None else ""

        if state_flag_match:
            data = {}
            for key, col_idx in numeric_cols.items():
                effective_idx = col_idx - 1 if (year <= 2019 and key in percentage_fields) else col_idx
                val = row.iloc[effective_idx] if len(row) > effective_idx else None
                num_val = clean_numeric(val)
                if key in ['adjusted_fall_enrollment', 'earned_hiset', 'enrolled_in_college', 'dropped_out', 'missing']:
                    num_val = int(float(num_val)) if num_val is not None else None
                else:
                    num_val = round_four_decimal(num_val)
                data[key] = num_val
            state_entry = {
                'year': year,
                **data
            }
            logger.info(f"State total row detected: {state_entry}")
            continue

        # Skip rows without a school identifier after processing possible state row
        if pd.isna(raw_name) or cell_val_str == "":
            continue

        # Determine school_id based on year and column content
        if year <= 2019:
            school_id = get_school_id_by_id(conn, cell_val_str)
        else:
            school_id = get_school_id_by_name(conn, cell_val_str)
        if not school_id:
            logger.debug(f"School not found for name '{cell_val_str}' (row {idx + 1})")
            continue

        # Avoid duplicates
        if school_id in seen_schools:
            continue
        seen_schools.add(school_id)

        data = {}
        has_value = False
        for key, col_idx in numeric_cols.items():
            effective_idx = col_idx - 1 if (year <= 2019 and key in percentage_fields) else col_idx
            val = row.iloc[effective_idx] if len(row) > effective_idx else None
            num_val = clean_numeric(val)
            # Skip adjusted_fall_enrollment and missing for years <=2019
            if year <= 2019 and key in ['adjusted_fall_enrollment', 'missing']:
                num_val = None
            else:
                if key in ['adjusted_fall_enrollment', 'earned_hiset', 'enrolled_in_college', 'dropped_out', 'missing']:
                    num_val = int(float(num_val)) if num_val is not None else None
                else:
                    num_val = round_four_decimal(num_val)
            data[key] = num_val
            if num_val is not None and ((isinstance(num_val, (int, float)) and num_val != 0)):
                has_value = True

        if not has_value:
            continue

        entry = {
            'school_id': school_id,
            'year': year,
            **data
        }
        school_entries.append(entry)
        processed_rows += 1

    logger.info(f"Processed {processed_rows} school early exit entries for {year}; state row present: {state_entry is not None}")
    return school_entries, state_entry


def format_sql_value(val):
    return 'NULL' if val is None else str(val)


def generate_sql(school_entries, state_entries):
    total_entries = len(school_entries) + len(state_entries)
    logger.info(f"Generating SQL for {total_entries} entries (schools: {len(school_entries)}, states: {len(state_entries)})")

    sql_statements = ["-- Insert school early exit data"]

    for e in school_entries:
        sql_statements.append(
            "INSERT INTO school_early_exit "
            "(school_id_fk, year, adjusted_fall_enrollment, earned_hiset, enrolled_in_college, dropped_out, missing, annual_early_exit_percentage, \"four_year_early_exit_percentage\", annual_dropout_percentage, \"four_year_dropout_percentage\", date_created, date_updated) VALUES "
            f"({e['school_id']}, {e['year']}, {format_sql_value(e['adjusted_fall_enrollment'])}, {format_sql_value(e['earned_hiset'])}, "
            f"{format_sql_value(e['enrolled_in_college'])}, {format_sql_value(e['dropped_out'])}, {format_sql_value(e['missing'])}, "
            f"{format_sql_value(e['annual_early_exit_percentage'])}, {format_sql_value(e['4_year_early_exit_percentage'])}, "
            f"{format_sql_value(e['annual_dropout_percentage'])}, {format_sql_value(e['4_year_dropout_percentage'])}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);"
        )

    if state_entries:
        sql_statements.append("-- Insert state early exit data")
    for s in state_entries:
        sql_statements.append(
            "INSERT INTO state_early_exit "
            "(year, adjusted_fall_enrollment, earned_hiset, enrolled_in_college, dropped_out, missing, annual_early_exit_percentage, \"four_year_early_exit_percentage\", annual_dropout_percentage, \"four_year_dropout_percentage\", date_created, date_updated) VALUES "
            f"({s['year']}, {format_sql_value(s['adjusted_fall_enrollment'])}, {format_sql_value(s['earned_hiset'])}, "
            f"{format_sql_value(s['enrolled_in_college'])}, {format_sql_value(s['dropped_out'])}, {format_sql_value(s['missing'])}, "
            f"{format_sql_value(s['annual_early_exit_percentage'])}, {format_sql_value(s['4_year_early_exit_percentage'])}, "
            f"{format_sql_value(s['annual_dropout_percentage'])}, {format_sql_value(s['4_year_dropout_percentage'])}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);"
        )

    return "\n".join(sql_statements)

# ----------------------------
# Alembic upgrade / downgrade
# ----------------------------

def upgrade():
    logger.info("Starting School Early Exit migration upgrade")

    # 1. Create tables
    op.execute(
        """
        CREATE TABLE school_early_exit (
            id SERIAL PRIMARY KEY,
            school_id_fk INTEGER NOT NULL,
            year INTEGER NOT NULL,
            adjusted_fall_enrollment INTEGER,
            earned_hiset INTEGER,
            enrolled_in_college INTEGER,
            dropped_out INTEGER,
            missing INTEGER,
            annual_early_exit_percentage NUMERIC(15,4),
            four_year_early_exit_percentage NUMERIC(15,4),
            annual_dropout_percentage NUMERIC(15,4),
            four_year_dropout_percentage NUMERIC(15,4),
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_school_early_exit_school FOREIGN KEY (school_id_fk) REFERENCES school(id) ON DELETE CASCADE,
            CONSTRAINT unique_school_early_exit_year UNIQUE (school_id_fk, year)
        )
        """
    )

    # Indexes
    op.execute("CREATE INDEX idx_school_early_exit_school ON school_early_exit(school_id_fk)")
    op.execute("CREATE INDEX idx_school_early_exit_year ON school_early_exit(year)")

    # Trigger
    op.execute(
        """
        CREATE TRIGGER trigger_update_school_early_exit_timestamp
        BEFORE UPDATE ON school_early_exit
        FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
        """
    )

    # State table
    op.execute(
        """
        CREATE TABLE state_early_exit (
            id SERIAL PRIMARY KEY,
            year INTEGER NOT NULL,
            adjusted_fall_enrollment INTEGER,
            earned_hiset INTEGER,
            enrolled_in_college INTEGER,
            dropped_out INTEGER,
            missing INTEGER,
            annual_early_exit_percentage NUMERIC(15,4),
            four_year_early_exit_percentage NUMERIC(15,4),
            annual_dropout_percentage NUMERIC(15,4),
            four_year_dropout_percentage NUMERIC(15,4),
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT unique_state_early_exit_year UNIQUE (year)
        )
        """
    )

    # Index on year for state table
    op.execute("CREATE INDEX idx_state_early_exit_year ON state_early_exit(year)")

    # 2. Load data
    try:
        config = load_config()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        cache_dir = os.path.abspath(os.path.join(current_dir, config['file_settings']['sql_cache_dir']))
        cache_file = os.path.join(cache_dir, f"{revision}_cache.sql")
        logger.info(f"SQL cache file: {cache_file}")

        if os.path.exists(cache_file):
            logger.info("Loading SQL from cache")
            with open(cache_file, 'r') as f:
                sql_statements = f.read()
        else:
            school_entries = []
            state_entries = []
            pattern = config['file_settings']['default_input']
            base_dir = os.path.abspath(os.path.join(current_dir, os.path.dirname(pattern)))
            base_pattern = os.path.basename(pattern)
            parts = base_pattern.split('****')

            year_start = int(config['file_settings']['year_start'])
            year_end = int(config['file_settings']['year_end'])

            for year in range(year_start, year_end + 1):
                file_name = f"{parts[0]}{year}{parts[1] if len(parts) > 1 else ''}"
                file_path = os.path.join(base_dir, file_name)
                if not os.path.exists(file_path):
                    logger.warning(f"File not found for year {year}: {file_path}")
                    continue
                logger.info(f"Processing file for year {year}: {file_path}")
                try:
                    df = pd.read_excel(file_path)
                except Exception as e:
                    logger.error(f"Error reading {file_path}: {e}")
                    raise
                school_year_entries, state_entry = process_school_early_exit(df, year, config)
                school_entries.extend(school_year_entries)
                if state_entry:
                    state_entries.append(state_entry)

            if not school_entries and not state_entries:
                raise Exception("No school early exit data processed.")

            sql_statements = generate_sql(school_entries, state_entries)
            os.makedirs(cache_dir, exist_ok=True)
            with open(cache_file, 'w') as f:
                f.write(sql_statements)
            logger.info("SQL cache saved")

        # 3. Execute SQL
        executed = 0
        skipped = 0
        for stmt in sql_statements.split(';'):
            statement = stmt.strip()
            if not statement:
                continue
            try:
                op.execute(sa.text(statement))
                executed += 1
                if executed % 200 == 0:
                    logger.info(f"{executed} statements executed")
            except Exception as e:
                if 'duplicate key' in str(e).lower():
                    skipped += 1
                else:
                    logger.error(f"Error executing statement: {e}\nStatement: {statement[:200]}…")
                    raise
        logger.info(f"SQL execution complete: {executed} executed, {skipped} skipped (duplicates)")

    except Exception as e:
        logger.error(f"Critical error in School Early Exit migration: {e}")
        raise

    logger.info("School Early Exit migration upgrade completed successfully")


def downgrade():
    logger.info("Downgrading School Early Exit migration")
    op.execute("DROP TABLE IF EXISTS school_early_exit CASCADE")
    op.execute("DROP TABLE IF EXISTS state_early_exit CASCADE")
    logger.info("Downgrade completed successfully") 