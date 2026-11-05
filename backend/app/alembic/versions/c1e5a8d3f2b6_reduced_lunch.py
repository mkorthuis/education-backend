"""Free and reduced-price lunch eligibility

School, district and state counts of K-12 students and those eligible for free or reduced-price
lunch, as of October 1, from iPlatform's "Free Reduced K-12 School Lunch Eligibility Rates by
School" report.

Revision ID: c1e5a8d3f2b6
Revises: a7c4e2f9b1d3
Create Date: 2026-11-05 09:00:00.000000

"""
from alembic import op
import logging

from app.etl import reduced_lunch

logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = 'c1e5a8d3f2b6'
down_revision = 'a7c4e2f9b1d3'
branch_labels = None
depends_on = None

# (table, location column and its foreign key, or None for the state table)
TABLES = (
    ("school_reduced_lunch", "school_id_fk", "school"),
    ("district_reduced_lunch", "district_id_fk", "district"),
    ("state_reduced_lunch", None, None),
)


def upgrade():
    logger.info("Starting reduced lunch migration upgrade")

    for table, location, location_table in TABLES:
        location_column = f"{location} INTEGER NOT NULL," if location else ""
        location_fk = (f"CONSTRAINT fk_{table}_{location_table} FOREIGN KEY ({location}) "
                       f"REFERENCES {location_table}(id) ON DELETE CASCADE,") if location else ""
        key = f"{location}, year" if location else "year"
        op.execute(
            f"""
            CREATE TABLE {table} (
                id SERIAL PRIMARY KEY,
                {location_column}
                year INTEGER NOT NULL,
                enrollment INTEGER,
                eligible INTEGER,
                date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                {location_fk}
                CONSTRAINT unique_{table}_year UNIQUE ({key})
            )
            """
        )
        op.execute(f"CREATE INDEX idx_{table}_year ON {table}(year)")
        if location:
            op.execute(f"CREATE INDEX idx_{table}_{location_table} ON {table}({location})")
        op.execute(
            f"""
            CREATE TRIGGER trigger_update_{table}_timestamp
            BEFORE UPDATE ON {table}
            FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
            """
        )

    # Load every year in app/alembic/config/reduced_lunch_config.yaml
    reduced_lunch.load(op.get_bind())

    logger.info("Reduced lunch migration upgrade completed successfully")


def downgrade():
    for table, _, _ in reversed(TABLES):
        op.execute(f"DROP TABLE IF EXISTS {table} CASCADE")
