"""District Average Class Size

Revision ID: e6d8c9b7a4f3
Revises: d4e5f6g7h8i9
Create Date: 2024-09-01 12:00:00.000000

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

# Revision identifiers, used by Alembic
revision = 'e6d8c9b7a4f3'
down_revision = 'd4e5f6g7h8i9'
branch_labels = None
depends_on = None


# ----------------------------
# Helper / Utility Functions
# ----------------------------

def load_config():
    """Load configuration from YAML file or create a default one if missing."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.abspath(os.path.join(current_dir, '../config/district_average_class_size_config.yaml'))
    logger.info(f"Attempting to load configuration from: {config_path}")

    default_config = {
        'file_settings': {
            'default_input': '../assets/average-class-size/district/****-District-Average-Class-Size.xlsx',
            'year_start': 2012,
            'year_end': 2025,
            'sql_cache_dir': '../sql_cache'
        },
        'column_mappings': {
            'district_id': 2,   # Column C (0-indexed)
            'grade_1_2': 4,     # Column E
            'grade_3_4': 5,     # Column F
            'grade_5_8': 6      # Column G
        },
        'state_row_identifier': {
            'column_index': 3,           # Column D (0-indexed)
            'identifier_text': 'state average'
        }
    }

    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
            logger.info(f"Successfully loaded configuration: {config}")
            return config
    except Exception as e:
        logger.warning(f"Could not load configuration file ({e}). Creating default config at: {config_path}")
        # Create config directory if it doesn't exist
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        # Write default config
        with open(config_path, 'w') as f:
            yaml.dump(default_config, f)
        logger.info("Default configuration file created.")
        return default_config


def clean_numeric(value):
    """Clean numeric values by removing non-numeric characters (except decimal point). Returns float or None."""
    if pd.isna(value) or value == "":
        return None

    if isinstance(value, (int, float)):
        return float(value)

    value_str = str(value)
    cleaned_str = re.sub(r'[^0-9.-]', '', value_str)
    try:
        return float(cleaned_str) if cleaned_str else None
    except ValueError:
        logger.debug(f"Unable to parse numeric value from '{value}'")
        return None


def round_two_decimal(value):
    """Round a float value to two decimal places using HALF_UP."""
    if value is None:
        return None
    return float(Decimal(str(value)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))


def process_district_class_size(df, year, config):
    """Process a DataFrame and extract district class size records for the given year."""
    mappings = config['column_mappings']
    district_id_col = mappings['district_id']
    grade_cols = {
        'grade_1_2': mappings['grade_1_2'],
        'grade_3_4': mappings['grade_3_4'],
        'grade_5_8': mappings['grade_5_8']
    }

    entries = []
    processed_rows = 0
    seen_districts = set()

    for idx, row in df.iterrows():
        raw_district_id = row.iloc[district_id_col] if len(row) > district_id_col else None
        try:
            district_id = int(float(raw_district_id)) if pd.notna(raw_district_id) else None
        except (ValueError, TypeError):
            district_id = None

        if district_id is None:
            continue

        # Skip if we've already processed this district ID
        if district_id in seen_districts:
            continue

        seen_districts.add(district_id)

        # Validate district exists in DB
        exists_check = sa.text("SELECT EXISTS (SELECT 1 FROM district WHERE id = :district_id)")
        district_exists = op.get_bind().execute(exists_check, {"district_id": district_id}).scalar()
        if not district_exists:
            logger.debug(f"Skipping non-existent district ID {district_id} (row {idx + 1})")
            continue

        # Extract numeric values for each grade band
        grades_data = {}
        has_value = False
        for key, col_idx in grade_cols.items():
            val = row.iloc[col_idx] if len(row) > col_idx else None
            num_val = round_two_decimal(clean_numeric(val))
            grades_data[key] = num_val
            if num_val is not None and num_val > 0:
                has_value = True

        if not has_value:
            # Skip rows that contain no usable data
            continue

        entry = {
            'district_id': district_id,
            'year': year,
            **grades_data
        }
        entries.append(entry)
        processed_rows += 1

    logger.info(f"Processed {processed_rows} district class size entries for {year}")
    return entries


def process_state_class_size(df, year, config):
    """Extract state-level class size for a given year if present."""
    state_settings = config.get('state_row_identifier', {})
    id_col = state_settings.get('column_index', 3)
    identifier = state_settings.get('identifier_text', 'state average').lower().strip()

    # Grade columns follow same indices used for district bands
    grade_cols = {
        'grade_1_2': config['column_mappings']['grade_1_2'],
        'grade_3_4': config['column_mappings']['grade_3_4'],
        'grade_5_8': config['column_mappings']['grade_5_8']
    }

    for idx, row in df.iterrows():
        cell_val = row.iloc[id_col] if len(row) > id_col else None
        if isinstance(cell_val, str) and cell_val.strip().lower() == identifier:
            grades_data = {}
            has_value = False
            for key, col_idx in grade_cols.items():
                val = row.iloc[col_idx] if len(row) > col_idx else None
                num_val = round_two_decimal(clean_numeric(val))
                grades_data[key] = num_val
                if num_val is not None and num_val > 0:
                    has_value = True
            if not has_value:
                return None
            entry = {
                'year': year,
                **grades_data
            }
            return entry
    return None


def format_sql_value(val):
    """Return a SQL-safe value representation (NULL or numeric string)."""
    return 'NULL' if val is None else str(val)


def generate_sql(district_entries, state_entries):
    """Generate SQL INSERT statements for district and state class size entries."""
    logger.info(
        f"Generating SQL: {len(district_entries)} district entries, {len(state_entries)} state entries"
    )

    sql_statements = ["-- Insert district class size data"]

    for e in district_entries:
        sql_statements.append(
            "INSERT INTO district_class_size "
            "(district_id_fk, year, grade_1_2, grade_3_4, grade_5_8, date_created, date_updated) VALUES "
            f"({e['district_id']}, {e['year']}, {format_sql_value(e['grade_1_2'])}, "
            f"{format_sql_value(e['grade_3_4'])}, {format_sql_value(e['grade_5_8'])}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);"
        )

    if state_entries:
        sql_statements.append("-- Insert state class size data")
        for s in state_entries:
            sql_statements.append(
                "INSERT INTO state_class_size "
                "(year, grade_1_2, grade_3_4, grade_5_8, date_created, date_updated) VALUES "
                f"({s['year']}, {format_sql_value(s['grade_1_2'])}, {format_sql_value(s['grade_3_4'])}, "
                f"{format_sql_value(s['grade_5_8'])}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);"
            )

    return "\n".join(sql_statements)


# ----------------------------
# Alembic upgrade / downgrade
# ----------------------------

def upgrade():
    """Create district_class_size table and load data."""
    logger.info("Starting District Class Size migration upgrade")

    # 1. Create table
    logger.info("Creating district_class_size table")
    op.execute("""
        CREATE TABLE district_class_size (
            id SERIAL PRIMARY KEY,
            district_id_fk INTEGER NOT NULL,
            year INTEGER NOT NULL,
            grade_1_2 NUMERIC(15,2),
            grade_3_4 NUMERIC(15,2),
            grade_5_8 NUMERIC(15,2),
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_district_class_size_district FOREIGN KEY (district_id_fk) REFERENCES district(id) ON DELETE CASCADE,
            CONSTRAINT unique_district_year UNIQUE (district_id_fk, year)
        )
    """)

    # 2. Indexes
    logger.info("Creating indexes for district_class_size table")
    op.execute("CREATE INDEX idx_district_class_size_district ON district_class_size(district_id_fk)")
    op.execute("CREATE INDEX idx_district_class_size_year ON district_class_size(year)")

    # 3. Trigger for district_class_size date_updated
    logger.info("Creating trigger for district_class_size table")
    op.execute("""
        CREATE TRIGGER trigger_update_district_class_size_timestamp
        BEFORE UPDATE ON district_class_size
        FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
    """)

    # 4. Create state_class_size table (must exist before data insert)
    logger.info("Creating state_class_size table")
    op.execute("""
        CREATE TABLE state_class_size (
            id SERIAL PRIMARY KEY,
            year INTEGER NOT NULL,
            grade_1_2 NUMERIC(15,2),
            grade_3_4 NUMERIC(15,2),
            grade_5_8 NUMERIC(15,2),
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT unique_state_year UNIQUE (year)
        )
    """)

    # Index and trigger for state_class_size
    op.execute("CREATE INDEX idx_state_class_size_year ON state_class_size(year)")
    op.execute("""
        CREATE TRIGGER trigger_update_state_class_size_timestamp
        BEFORE UPDATE ON state_class_size
        FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
    """)

    # 5. Load data
    try:
        logger.info("Loading configuration and preparing data to insert")
        config = load_config()
        current_dir = os.path.dirname(os.path.abspath(__file__))

        cache_dir = os.path.abspath(os.path.join(current_dir, config['file_settings']['sql_cache_dir']))
        cache_file = os.path.join(cache_dir, f"{revision}_cache.sql")
        logger.info(f"Cache file path: {cache_file}")

        # If cached SQL exists, use it
        if os.path.exists(cache_file):
            logger.info("Using cached SQL statements")
            with open(cache_file, 'r') as f:
                sql_statements = f.read()
        else:
            logger.info("No cache file found; processing input files")
            district_entries = []
            state_entries = []

            input_pattern = config['file_settings']['default_input']
            base_dir = os.path.abspath(os.path.join(current_dir, os.path.dirname(input_pattern)))
            base_pattern = os.path.basename(input_pattern)
            pattern_parts = base_pattern.split('****')

            year_start = int(config['file_settings']['year_start'])
            year_end = int(config['file_settings']['year_end'])

            for year in range(year_start, year_end + 1):
                file_name = f"{pattern_parts[0]}{year}{pattern_parts[1] if len(pattern_parts) > 1 else ''}"
                file_path = os.path.join(base_dir, file_name)

                if not os.path.exists(file_path):
                    logger.warning(f"File not found for year {year}: {file_path}")
                    continue

                logger.info(f"Processing file for year {year}: {file_path}")
                try:
                    df = pd.read_excel(file_path)
                except Exception as e:
                    logger.error(f"Error reading Excel file {file_path}: {e}")
                    raise

                year_district_entries = process_district_class_size(df, year, config)
                district_entries.extend(year_district_entries)

                state_entry = process_state_class_size(df, year, config)
                if state_entry:
                    state_entries.append(state_entry)

            if not district_entries and not state_entries:
                logger.error("No class size data was processed; aborting migration")
                raise Exception("No data processed for class size migration")

            sql_statements = generate_sql(district_entries, state_entries)

            # Save to cache
            os.makedirs(cache_dir, exist_ok=True)
            with open(cache_file, 'w') as f:
                f.write(sql_statements)
            logger.info(f"SQL cache written to {cache_file}")

        # 6. Execute SQL
        logger.info("Executing SQL statements")
        executed = 0
        skipped = 0
        for statement in sql_statements.split(';'):
            stmt = statement.strip()
            if not stmt:
                continue
            try:
                op.execute(sa.text(stmt))
                executed += 1
                if executed % 200 == 0:
                    logger.info(f"{executed} statements executed so far")
            except Exception as e:
                if 'duplicate key' in str(e).lower():
                    skipped += 1
                    logger.debug(f"Skipped duplicate: {stmt[:120]} …")
                else:
                    logger.error(f"Failed executing statement: {e}\nStatement: {stmt[:200]}…")
                    raise
        logger.info(f"SQL execution complete: {executed} executed, {skipped} skipped (duplicates)")

    except Exception as e:
        logger.error(f"Critical error during district class size migration: {e}")
        raise

    logger.info("District & State Class Size migration upgrade completed successfully")


def downgrade():
    """Drop district_class_size table."""
    logger.info("Starting downgrade for District & State Class Size migration")
    op.execute("DROP TABLE IF EXISTS state_class_size CASCADE")
    op.execute("DROP TABLE IF EXISTS district_class_size CASCADE")
    logger.info("Downgrade completed successfully") 