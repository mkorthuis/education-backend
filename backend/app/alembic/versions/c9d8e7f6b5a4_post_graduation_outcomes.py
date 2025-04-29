"""Post Graduation Outcomes

Revision ID: c9d8e7f6b5a4
Revises: b3c5d7e9fa12
Create Date: 2024-10-01 12:30:00.000000

"""
from alembic import op
import sqlalchemy as sa
import pandas as pd
import yaml
import logging
import os
import re
from datetime import datetime
from decimal import Decimal, ROUND_HALF_UP

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# Revision identifiers, used by Alembic.
revision = 'c9d8e7f6b5a4'
down_revision = 'b3c5d7e9fa12'
branch_labels = None
depends_on = None

# ----------------------------
# Constants
# ----------------------------

OUTCOME_TYPES = [
    ('4 Year College', 'Entering Four Year Colleges & Universities'),
    ('Less 4 Year College', 'Entering Less Than Four Years'),
    ('Addl. High School', 'Returning To Secondary Schools For Post Graduate Study'),
    ('Employed', 'Employed'),
    ('Armed Forces', 'Armed Forces'),
    ('Unemployed', 'Unemployed'),
    ('Unknown', 'Status Unknown'),
]

OUTCOME_ID_MAP = {
    '4_year_college': 1,
    'gt_4_year_college': 2,
    'addl_high_school': 3,
    'employed': 4,
    'armed_forces': 5,
    'unemployed': 6,
    'unknown': 7,
}

# ----------------------------
# Helper / Utility Functions
# ----------------------------

def load_config():
    """Load configuration from YAML file. Raises if missing/invalid."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.abspath(os.path.join(current_dir, '../config/post_graduation_outcomes_config.yaml'))
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
    if pd.isna(value) or value == "":
        return None
    if isinstance(value, (int, float)):
        return float(value)
    cleaned = re.sub(r'[^0-9.-]', '', str(value))
    try:
        return float(cleaned) if cleaned else None
    except ValueError:
        logger.debug(f"Unable to parse numeric from '{value}'")
        return None


def round_int(val: float):
    if val is None:
        return None
    return int(round(val))


def get_school_id(conn, school_id_raw):
    try:
        sid = int(school_id_raw)
    except (ValueError, TypeError):
        return None
    result = conn.execute(sa.text("SELECT id FROM school WHERE id = :id"), {"id": sid}).fetchone()
    return result[0] if result else None


def process_post_grad(df, year, config):
    """Return tuple (school_entries, state_entries) for a given year."""
    mappings = config['column_mappings']
    school_col = mappings['school_id']
    total_col = mappings['total_students']
    perc_cols = mappings['percentages']

    conn = op.get_bind()
    school_entries = []
    state_entries = []
    processed_rows = 0
    seen_schools = set()

    for _, row in df.iterrows():
        # Detect state total row (column F / index 5)
        state_flag = row.iloc[5] if len(row) > 5 else None
        if isinstance(state_flag, str) and state_flag.strip().lower() == 'state total':
            total_students = clean_numeric(row.iloc[total_col] if len(row) > total_col else None)
            if total_students is None or total_students <= 0:
                continue
            total_students = int(float(total_students))
            for key, col_idx in perc_cols.items():
                perc_val = clean_numeric(row.iloc[col_idx] if len(row) > col_idx else None)
                if perc_val is None or perc_val <= 0:
                    continue
                if perc_val <= 1:
                    perc_val *= 100
                count_val = round_int(total_students * (perc_val / 100))
                if count_val <= 0:
                    continue
                state_entries.append({
                    'year': year,
                    'post_graduation_type_id': OUTCOME_ID_MAP[key],
                    'value': count_val
                })
            continue  # move to next row after processing state

        raw_school = row.iloc[school_col] if len(row) > school_col else None
        school_id = get_school_id(conn, raw_school)
        if not school_id:
            continue

        if school_id in seen_schools:
            continue
        seen_schools.add(school_id)

        total_students = clean_numeric(row.iloc[total_col] if len(row) > total_col else None)
        if total_students is None or total_students <= 0:
            continue
        total_students = int(float(total_students))

        for key, col_idx in perc_cols.items():
            perc_val = clean_numeric(row.iloc[col_idx] if len(row) > col_idx else None)
            if perc_val is None or perc_val <= 0:
                continue
            # If percentage appears as 0-1 fraction, convert to percent value
            if perc_val <= 1:
                perc_val *= 100
            count_val = round_int(total_students * (perc_val / 100))
            if count_val <= 0:
                continue
            school_entries.append({
                'school_id': school_id,
                'year': year,
                'post_graduation_type_id': OUTCOME_ID_MAP[key],
                'value': count_val
            })
        processed_rows += 1

    logger.info(f"Processed {processed_rows} school rows for year {year}; state entries: {len(state_entries)}; school entries: {len(school_entries)}")
    return school_entries, state_entries


def format_sql_value(val):
    return 'NULL' if val is None else str(val)


def generate_sql(school_entries, state_entries):
    total = len(school_entries) + len(state_entries)
    logger.info(f"Generating SQL for {total} entries (schools: {len(school_entries)}, state: {len(state_entries)})")
    sql = ["-- Insert school post graduation data"]
    for e in school_entries:
        sql.append(
            "INSERT INTO school_post_graduation (school_id_fk, year, post_graduation_type_id_fk, value, date_created, date_updated) VALUES "
            f"({e['school_id']}, {e['year']}, {e['post_graduation_type_id']}, {e['value']}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);"
        )
    if state_entries:
        sql.append("-- Insert state post graduation data")
    for s in state_entries:
        sql.append(
            "INSERT INTO state_post_graduation (year, post_graduation_type_id_fk, value, date_created, date_updated) VALUES "
            f"({s['year']}, {s['post_graduation_type_id']}, {s['value']}, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);"
        )
    return "\n".join(sql)

# ----------------------------
# Alembic upgrade / downgrade
# ----------------------------

def upgrade():
    logger.info("Starting Post Graduation Outcomes migration upgrade")

    # 1. Create tables
    op.execute(
        """
        CREATE TABLE post_graduation_type (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            description TEXT,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    op.execute(
        """
        CREATE TABLE school_post_graduation (
            id SERIAL PRIMARY KEY,
            school_id_fk INTEGER NOT NULL,
            year INTEGER NOT NULL,
            post_graduation_type_id_fk INTEGER NOT NULL,
            value INTEGER NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_spg_school FOREIGN KEY (school_id_fk) REFERENCES school(id) ON DELETE CASCADE,
            CONSTRAINT fk_spg_type FOREIGN KEY (post_graduation_type_id_fk) REFERENCES post_graduation_type(id) ON DELETE CASCADE,
            CONSTRAINT unique_school_post_grad_year_type UNIQUE (school_id_fk, year, post_graduation_type_id_fk)
        )
        """
    )

    # State table
    op.execute(
        """
        CREATE TABLE state_post_graduation (
            id SERIAL PRIMARY KEY,
            year INTEGER NOT NULL,
            post_graduation_type_id_fk INTEGER NOT NULL,
            value INTEGER NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_spg_state_type FOREIGN KEY (post_graduation_type_id_fk) REFERENCES post_graduation_type(id) ON DELETE CASCADE,
            CONSTRAINT unique_state_post_grad_year_type UNIQUE (year, post_graduation_type_id_fk)
        )
        """
    )

    # Indexes
    op.execute("CREATE INDEX idx_spg_school ON school_post_graduation(school_id_fk)")
    op.execute("CREATE INDEX idx_spg_year ON school_post_graduation(year)")
    op.execute("CREATE INDEX idx_spg_type ON school_post_graduation(post_graduation_type_id_fk)")
    op.execute("CREATE INDEX idx_state_pg_year ON state_post_graduation(year)")
    op.execute("CREATE INDEX idx_state_pg_type ON state_post_graduation(post_graduation_type_id_fk)")

    # Trigger
    op.execute(
        """
        CREATE TRIGGER trigger_update_school_post_graduation_timestamp
        BEFORE UPDATE ON school_post_graduation
        FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
        """
    )

    # 2. Insert static post_graduation_type rows
    logger.info("Inserting static post_graduation_type data")
    conn = op.get_bind()
    for name, desc in OUTCOME_TYPES:
        logger.info(f"Inserting type {name}")
        stmt = sa.text(
            "INSERT INTO post_graduation_type (name, description, date_created, date_updated) VALUES (:name, :desc, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)"
        ).bindparams(name=name, desc=desc)
        try:
            op.execute(stmt)
        except Exception as e:
            if 'duplicate key' in str(e).lower() or 'unique' in str(e).lower():
                logger.debug(f"Type {name} already exists, skipping")
            else:
                raise

    # 3. Load data
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
                school_year_entries, state_year_entries = process_post_grad(df, year, config)
                school_entries.extend(school_year_entries)
                state_entries.extend(state_year_entries)

            if not school_entries and not state_entries:
                raise Exception("No post graduation data processed.")

            sql_statements = generate_sql(school_entries, state_entries)
            os.makedirs(cache_dir, exist_ok=True)
            with open(cache_file, 'w') as f:
                f.write(sql_statements)
            logger.info("SQL cache saved")

        # 4. Execute SQL
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
        logger.error(f"Critical error in Post Graduation Outcomes migration: {e}")
        raise

    logger.info("Post Graduation Outcomes migration upgrade completed successfully")


def downgrade():
    logger.info("Downgrading Post Graduation Outcomes migration")
    op.execute("DROP TABLE IF EXISTS school_post_graduation CASCADE")
    op.execute("DROP TABLE IF EXISTS state_post_graduation CASCADE")
    op.execute("DROP TABLE IF EXISTS post_graduation_type CASCADE")
    logger.info("Downgrade completed successfully") 