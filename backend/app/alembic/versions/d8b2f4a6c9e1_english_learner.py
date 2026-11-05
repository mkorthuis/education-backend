"""English learners

District and state counts of students enrolled, English learners and former English learners
being monitored, as of October 1, from iPlatform's "Limited English Proficiency Enrollment"
report. The state reports English learners by district only.

Revision ID: d8b2f4a6c9e1
Revises: c1e5a8d3f2b6
Create Date: 2026-11-05 09:10:00.000000

"""
from alembic import op
import logging

from app.etl import english_learner

logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = 'd8b2f4a6c9e1'
down_revision = 'c1e5a8d3f2b6'
branch_labels = None
depends_on = None

TABLES = (
    ("district_english_learner", "district_id_fk", "district"),
    ("state_english_learner", None, None),
)


def upgrade():
    logger.info("Starting English learner migration upgrade")

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
                monitor INTEGER,
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

    # Load every year in app/alembic/config/english_learner_config.yaml
    english_learner.load(op.get_bind())

    logger.info("English learner migration upgrade completed successfully")


def downgrade():
    for table, _, _ in reversed(TABLES):
        op.execute(f"DROP TABLE IF EXISTS {table} CASCADE")
