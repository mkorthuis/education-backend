"""Private schools' tuition, as each school publishes it

school_tuition_source has each private school's school year: whether it publishes its tuition, the page
and the day it was read, and who gets financial aid as it words it; school_tuition
its rates by grade band and kind (standard, day, boarding, parishioner...), with annual tuition and the
fees every student pays. Read from the schools' own websites. See app/etl/private_tuition.py.

Revision ID: e08d3d3437f7
Revises: 05a281bc6d1c
Create Date: 2026-11-21 18:00:00.000000

"""
from alembic import op
import logging

from app.etl import private_tuition

logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = 'e08d3d3437f7'
down_revision = '05a281bc6d1c'
branch_labels = None
depends_on = None

TABLES = ("school_tuition_source", "school_tuition")


def listed(values) -> str:
    return ", ".join(f"'{value}'" for value in values)


def upgrade():
    logger.info("Creating school_tuition_source and school_tuition")
    op.execute(f"""
        CREATE TABLE school_tuition_source (
            id SERIAL PRIMARY KEY,
            school_id_fk INTEGER NOT NULL,
            year INTEGER NOT NULL,
            status VARCHAR(20) NOT NULL,
            source_url TEXT,
            retrieved_on DATE NOT NULL,
            with_aid VARCHAR(100),
            note TEXT,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_school_tuition_source_school FOREIGN KEY (school_id_fk) REFERENCES school(id) ON DELETE CASCADE,
            CONSTRAINT unique_school_tuition_source_year UNIQUE (school_id_fk, year),
            CONSTRAINT check_school_tuition_source_status CHECK (status IN ({listed(private_tuition.STATUSES)}))
        )
    """)
    op.execute(f"""
        CREATE TABLE school_tuition (
            id SERIAL PRIMARY KEY,
            school_id_fk INTEGER NOT NULL,
            year INTEGER NOT NULL,
            rate_no INTEGER NOT NULL,
            band VARCHAR(100) NOT NULL,
            lowest_grade_id_fk INTEGER NOT NULL,
            highest_grade_id_fk INTEGER NOT NULL,
            rate_type VARCHAR(20) NOT NULL,
            rate_label VARCHAR(200),
            tuition NUMERIC(10,2) NOT NULL,
            required_fee NUMERIC(10,2),
            fee_note TEXT,
            rate_note TEXT,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_school_tuition_source FOREIGN KEY (school_id_fk, year)
                REFERENCES school_tuition_source(school_id_fk, year) ON DELETE CASCADE,
            CONSTRAINT fk_school_tuition_lowest_grade FOREIGN KEY (lowest_grade_id_fk) REFERENCES grades(id),
            CONSTRAINT fk_school_tuition_highest_grade FOREIGN KEY (highest_grade_id_fk) REFERENCES grades(id),
            CONSTRAINT unique_school_tuition_rate UNIQUE (school_id_fk, year, rate_no),
            CONSTRAINT check_school_tuition_rate_type CHECK (rate_type IN ({listed(private_tuition.RATE_TYPES)}))
        )
    """)
    for table in TABLES:
        op.execute(f"""
            CREATE TRIGGER trigger_update_{table}_timestamp
            BEFORE UPDATE ON {table}
            FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
        """)

    # app/alembic/assets/private-tuition
    counts = private_tuition.load(op.get_bind())
    logger.info(f"Loaded private schools' tuition: {counts}")


def downgrade():
    for table in reversed(TABLES):
        op.execute(f"DROP TABLE IF EXISTS {table} CASCADE")
