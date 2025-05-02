"""School Average Class Size

Revision ID: f7e9d0b8c6a4
Revises: e6d8c9b7a4f3
Create Date: 2024-09-02 12:00:00.000000

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
revision = 'f7e9d0b8c6a4'
down_revision = 'e6d8c9b7a4f3'
branch_labels = None
depends_on = None

# ----------------------------
# Helper / Utility Functions
# ----------------------------

def load_config():
    """Load configuration or create a default one if missing."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.abspath(os.path.join(current_dir, '../config/school_average_class_size_config.yaml'))
    logger.info(f"Attempting to load configuration from: {config_path}")

    default_config = {
        'file_settings': {
            'default_input': '../assets/average-class-size/school/****-School-Average-Class-Size.xlsx',
            'year_start': 2012,
            'year_end': 2025,
            'sql_cache_dir': '../sql_cache'
        },
        'column_mappings': {
            'school_name': 4,   # Column E (0-indexed)
            'grade_1_2': 5,     # Column F
            'grade_3_4': 6,     # Column G
            'grade_5_8': 7      # Column H
        }
    }

    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
            logger.info(f"Successfully loaded configuration: {config}")
            return config
    except Exception as e:
        logger.warning(f"Could not load configuration file ({e}). Creating default config at: {config_path}")
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        with open(config_path, 'w') as f:
            yaml.dump(default_config, f)
        logger.info("Default configuration file created.")
        return default_config


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


def round_two_decimal(value):
    if value is None:
        return None
    return float(Decimal(str(value)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))


def get_school_id_by_name(conn, name):
    """Return school id matching (case-insensitive) the given trimmed name or None."""
    query = sa.text("SELECT id FROM school WHERE lower(trim(name)) = lower(trim(:name)) LIMIT 1")
    result = conn.execute(query, {"name": name})
    row = result.fetchone()
    return row[0] if row else None


def process_school_class_size(df, year, config):
    """Extract school class size entries from a DataFrame for a given year."""
    mappings = config['column_mappings']
    name_col = mappings['school_name']
    grade_cols = {
        'grade_1_2': mappings['grade_1_2'],
        'grade_3_4': mappings['grade_3_4'],
        'grade_5_8': mappings['grade_5_8']
    }

    entries = []
    processed_rows = 0
    conn = op.get_bind()
    seen_schools = set()

    for idx, row in df.iterrows():
        raw_name = row.iloc[name_col] if len(row) > name_col else None
        if pd.isna(raw_name) or str(raw_name).strip() == "":
            continue

        school_name = str(raw_name).strip()
        school_id = get_school_id_by_name(conn, school_name)
        if not school_id:
            logger.debug(f"School not found for name '{school_name}' (row {idx + 1})")
            continue

        # Skip if we've already processed this school ID
        if school_id in seen_schools:
            continue
        seen_schools.add(school_id)

        grades_data = {}
        has_value = False
        for key, col_idx in grade_cols.items():
            val = row.iloc[col_idx] if len(row) > col_idx else None
            num_val = round_two_decimal(clean_numeric(val))
            grades_data[key] = num_val
            if num_val is not None and num_val > 0:
                has_value = True

        if not has_value:
            continue

        entry = {
            'school_id': school_id,
            'year': year,
            **grades_data
        }
        entries.append(entry)
        processed_rows += 1

    logger.info(f"Processed {processed_rows} school class size entries for {year}")
    return entries


def format_sql_value(val):
    return 'NULL' if val is None else str(val)


def generate_sql(entries):
    logger.info(f"Generating SQL for {len(entries)} entries")
    sql_statements = ["-- Insert school class size data"]
    for e in entries:
        sql_statements.append(
            "INSERT INTO school_class_size "
            "(school_id_fk, year, grade_1_2, grade_3_4, grade_5_8, date_created, date_updated) VALUES "
            f"({e['school_id']}, {e['year']}, {format_sql_value(e['grade_1_2'])}, {format_sql_value(e['grade_3_4'])}, "
            f"{format_sql_value(e['grade_5_8'])}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);"
        )
    return "\n".join(sql_statements)

# ----------------------------
# Alembic upgrade / downgrade
# ----------------------------

def upgrade():
    logger.info("Starting School Class Size migration upgrade")

    # 1. Create table
    op.execute("""
        CREATE TABLE school_class_size (
            id SERIAL PRIMARY KEY,
            school_id_fk INTEGER NOT NULL,
            year INTEGER NOT NULL,
            grade_1_2 NUMERIC(15,2),
            grade_3_4 NUMERIC(15,2),
            grade_5_8 NUMERIC(15,2),
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_school_class_size_school FOREIGN KEY (school_id_fk) REFERENCES school(id) ON DELETE CASCADE,
            CONSTRAINT unique_school_average_class_size_year UNIQUE (school_id_fk, year)
        )
    """)

    # Indexes
    op.execute("CREATE INDEX idx_school_class_size_school ON school_class_size(school_id_fk)")
    op.execute("CREATE INDEX idx_school_class_size_year ON school_class_size(year)")

    # Trigger
    op.execute("""
        CREATE TRIGGER trigger_update_school_class_size_timestamp
        BEFORE UPDATE ON school_class_size
        FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
    """)

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
            entries = []
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
                year_entries = process_school_class_size(df, year, config)
                entries.extend(year_entries)

            if not entries:
                raise Exception("No school class size data processed.")

            sql_statements = generate_sql(entries)
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
        logger.error(f"Critical error in School Class Size migration: {e}")
        raise

    logger.info("School Class Size migration upgrade completed successfully")


def downgrade():
    logger.info("Downgrading School Class Size migration")
    op.execute("DROP TABLE IF EXISTS school_class_size CASCADE")
    logger.info("Downgrade completed successfully") 