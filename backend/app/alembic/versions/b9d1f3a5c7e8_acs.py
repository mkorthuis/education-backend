"""Census American Community Survey 5-year estimates for towns, school districts and the state

From Census's ACS summary files (acs_config.yaml), the 2020-2024 and 2015-2019 releases:

- Lookups: acs_topic, acs_annotation (the codes Census gives in place of a number), acs_release
- acs_table, acs_variable: the 64 tables loaded and their 1,195 values, each with its column name in
  the views, unit and description (acs_variables.csv); acs_variable_release: which releases have each
  value, and whether it means the same in each; acs_measure: the summary's 40 measures, with their
  labels, descriptions, units and formulas
- acs_town, acs_district: the Census area each town and school district is
- town_acs_estimate, district_acs_estimate, state_acs_estimate: every value, with its margin of error,
  for every release

And materialized views the API reads, generated from the variables (app.etl.acs.view_statements), for
each level: one per topic with a column per value and its margin of error ({level}_acs_{topic}), and a
summary of 40 measures with margins of error and reliability ({level}_acs_summary). Each has a unique
index, so a load refreshes them concurrently. acs_reliability() rates an estimate by its coefficient
of variation.

Revision ID: b9d1f3a5c7e8
Revises: a8c0e2f4b6d8
Create Date: 2026-11-14 12:00:00.000000

"""
from alembic import op
import logging

from app.etl import acs
from app.etl.core import load_config

logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = 'b9d1f3a5c7e8'
down_revision = 'a8c0e2f4b6d8'
branch_labels = None
depends_on = None

TIMESTAMPS = """
    date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP"""
TABLES = ("acs_topic", "acs_annotation", "acs_release", "acs_table", "acs_variable", "acs_variable_release",
          "acs_measure", "acs_town", "acs_district", "town_acs_estimate", "district_acs_estimate", "state_acs_estimate")
# Each level's estimate table: its place column and that column's table
PLACES = {"town": ("town_id_fk", "town"), "district": ("district_id_fk", "district"), "state": None}


def upgrade():
    logger.info("Starting ACS migration upgrade")

    op.execute(
        f"""
        CREATE TABLE acs_topic (
            id SERIAL PRIMARY KEY,
            code VARCHAR(30) NOT NULL,
            name VARCHAR(100) NOT NULL,{TIMESTAMPS},
            CONSTRAINT unique_acs_topic_code UNIQUE (code)
        )
        """
    )
    op.execute(
        f"""
        CREATE TABLE acs_annotation (
            id SERIAL PRIMARY KEY,
            code INTEGER NOT NULL,
            name VARCHAR(255) NOT NULL,{TIMESTAMPS},
            CONSTRAINT unique_acs_annotation_code UNIQUE (code)
        )
        """
    )
    op.execute(
        f"""
        CREATE TABLE acs_release (
            id SERIAL PRIMARY KEY,
            year SMALLINT NOT NULL,
            period VARCHAR(9) NOT NULL,
            dollars_year SMALLINT NOT NULL,
            source_url TEXT NOT NULL,{TIMESTAMPS},
            CONSTRAINT unique_acs_release_year UNIQUE (year)
        )
        """
    )
    op.execute(
        f"""
        CREATE TABLE acs_table (
            id SERIAL PRIMARY KEY,
            code VARCHAR(10) NOT NULL,
            title TEXT NOT NULL,
            universe TEXT NOT NULL,
            topic_id_fk INTEGER NOT NULL,
            tier VARCHAR(10) NOT NULL,
            why TEXT NOT NULL,{TIMESTAMPS},
            CONSTRAINT fk_acs_table_topic FOREIGN KEY (topic_id_fk) REFERENCES acs_topic(id),
            CONSTRAINT unique_acs_table_code UNIQUE (code),
            CONSTRAINT check_acs_table_tier CHECK (tier IN ('core', 'extended'))
        )
        """
    )
    op.execute(
        f"""
        CREATE TABLE acs_variable (
            id SERIAL PRIMARY KEY,
            code VARCHAR(12) NOT NULL,
            table_id_fk INTEGER NOT NULL,
            line SMALLINT NOT NULL,
            column_name VARCHAR(59) NOT NULL,
            label TEXT NOT NULL,
            description TEXT NOT NULL,
            unit VARCHAR(20) NOT NULL,{TIMESTAMPS},
            CONSTRAINT fk_acs_variable_table FOREIGN KEY (table_id_fk) REFERENCES acs_table(id),
            CONSTRAINT unique_acs_variable_code UNIQUE (code),
            CONSTRAINT unique_acs_variable_column_name UNIQUE (column_name),
            CONSTRAINT check_acs_variable_unit CHECK (unit IN ({', '.join(repr(u) for u in acs.UNITS)}))
        )
        """
    )
    op.execute(
        f"""
        CREATE TABLE acs_variable_release (
            id SERIAL PRIMARY KEY,
            variable_id_fk INTEGER NOT NULL,
            release_year SMALLINT NOT NULL,
            label TEXT NOT NULL,
            comparability VARCHAR(10) NOT NULL,{TIMESTAMPS},
            CONSTRAINT fk_acs_variable_release_variable FOREIGN KEY (variable_id_fk) REFERENCES acs_variable(id) ON DELETE CASCADE,
            CONSTRAINT fk_acs_variable_release_release FOREIGN KEY (release_year) REFERENCES acs_release(year),
            CONSTRAINT unique_acs_variable_release UNIQUE (variable_id_fk, release_year),
            CONSTRAINT check_acs_variable_release_comparability CHECK (comparability IN ({', '.join(repr(c) for c in acs.COMPARABILITY)}))
        )
        """
    )
    op.execute(
        f"""
        CREATE TABLE acs_measure (
            id SERIAL PRIMARY KEY,
            name VARCHAR(59) NOT NULL,
            sort SMALLINT NOT NULL,
            label VARCHAR(100) NOT NULL,
            description TEXT NOT NULL,
            unit VARCHAR(20) NOT NULL,
            kind VARCHAR(5) NOT NULL,
            formula TEXT NOT NULL,{TIMESTAMPS},
            CONSTRAINT unique_acs_measure_name UNIQUE (name),
            CONSTRAINT check_acs_measure_unit CHECK (unit IN ({', '.join(repr(u) for u in acs.UNITS)})),
            CONSTRAINT check_acs_measure_kind CHECK (kind IN ({', '.join(repr(k) for k in acs.MEASURE_KINDS)}))
        )
        """
    )
    op.execute(
        f"""
        CREATE TABLE acs_town (
            id SERIAL PRIMARY KEY,
            town_id_fk INTEGER NOT NULL,
            census_geo_id VARCHAR(20) NOT NULL,
            census_name TEXT NOT NULL,{TIMESTAMPS},
            CONSTRAINT fk_acs_town_town FOREIGN KEY (town_id_fk) REFERENCES town(id) ON DELETE CASCADE,
            CONSTRAINT unique_acs_town UNIQUE (town_id_fk),
            CONSTRAINT unique_acs_town_census_geo_id UNIQUE (census_geo_id)
        )
        """
    )
    op.execute(
        f"""
        CREATE TABLE acs_district (
            id SERIAL PRIMARY KEY,
            district_id_fk INTEGER NOT NULL,
            census_geo_id VARCHAR(20) NOT NULL,
            census_name TEXT NOT NULL,
            census_type VARCHAR(10) NOT NULL,{TIMESTAMPS},
            CONSTRAINT fk_acs_district_district FOREIGN KEY (district_id_fk) REFERENCES district(id) ON DELETE CASCADE,
            CONSTRAINT unique_acs_district UNIQUE (district_id_fk),
            CONSTRAINT unique_acs_district_census_geo_id UNIQUE (census_geo_id),
            CONSTRAINT check_acs_district_census_type CHECK (census_type IN ({', '.join(repr(t) for t in acs.DISTRICT_TYPES)}))
        )
        """
    )
    for level, place in PLACES.items():
        table = f"{level}_acs_estimate"
        place_column = f"\n            {place[0]} INTEGER NOT NULL," if place else ""
        place_key = f"{place[0]}, " if place else ""
        place_fk = (f"\n            CONSTRAINT fk_{table}_{place[1]} FOREIGN KEY ({place[0]}) REFERENCES {place[1]}(id) ON DELETE CASCADE,"
                    if place else "")
        op.execute(
            f"""
            CREATE TABLE {table} (
                id SERIAL PRIMARY KEY,{place_column}
                release_year SMALLINT NOT NULL,
                variable_id_fk INTEGER NOT NULL,
                estimate NUMERIC,
                moe NUMERIC,
                estimate_annotation_id_fk INTEGER,
                moe_annotation_id_fk INTEGER,{TIMESTAMPS},{place_fk}
                CONSTRAINT fk_{table}_release FOREIGN KEY (release_year) REFERENCES acs_release(year),
                CONSTRAINT fk_{table}_variable FOREIGN KEY (variable_id_fk) REFERENCES acs_variable(id) ON DELETE CASCADE,
                CONSTRAINT fk_{table}_estimate_annotation FOREIGN KEY (estimate_annotation_id_fk) REFERENCES acs_annotation(id),
                CONSTRAINT fk_{table}_moe_annotation FOREIGN KEY (moe_annotation_id_fk) REFERENCES acs_annotation(id),
                CONSTRAINT unique_{table} UNIQUE ({place_key}release_year, variable_id_fk)
            )
            """
        )
        op.execute(f"CREATE INDEX idx_{table}_variable ON {table}(variable_id_fk, release_year)")
    for table in TABLES:
        op.execute(
            f"""
            CREATE TRIGGER trigger_update_{table}_timestamp
            BEFORE UPDATE ON {table}
            FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
            """
        )

    config = load_config(acs.CONFIG)
    op.execute(acs.reliability_function(config))

    # Every release in app/alembic/config/acs_config.yaml from app/alembic/assets/acs
    acs.load(op.get_bind())

    # The views, filled as they're made
    for statement in acs.view_statements(config, acs.read_variables()):
        op.execute(statement)

    logger.info("ACS migration upgrade completed successfully")


def downgrade():
    for view in reversed(acs.view_names(load_config(acs.CONFIG))):
        op.execute(f"DROP MATERIALIZED VIEW IF EXISTS {view}")
    op.execute("DROP FUNCTION IF EXISTS acs_reliability(NUMERIC, NUMERIC)")
    for table in reversed(TABLES):
        op.execute(f"DROP TABLE IF EXISTS {table} CASCADE")
