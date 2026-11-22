"""Private schools' enrollment by grade on October 1, 2011-12 to 2025-26

From NHED's iPlatform report "NonPublic School Enrollments by Grade": school_private_enrollment has each
private school's students by grade (preschool to grade 12 and postgraduate), shaped like the public
schools' school_enrollment but apart from it; school_private_enrollment_total its ungraded students and
total. See app/etl/private_enrollment.py.

Revision ID: 05a281bc6d1c
Revises: 245723fed117
Create Date: 2026-11-21 22:00:00.000000

"""
from alembic import op
import logging

from app.etl import private_enrollment

logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = '05a281bc6d1c'
down_revision = '245723fed117'
branch_labels = None
depends_on = None

TABLES = ("school_private_enrollment_total", "school_private_enrollment")


def upgrade():
    logger.info("Creating school_private_enrollment and school_private_enrollment_total")
    op.execute("""
        CREATE TABLE school_private_enrollment_total (
            id SERIAL PRIMARY KEY,
            school_id_fk INTEGER NOT NULL,
            year INTEGER NOT NULL,
            ungraded_elementary INTEGER NOT NULL,
            ungraded_secondary INTEGER NOT NULL,
            total INTEGER NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_school_private_enrollment_total_school FOREIGN KEY (school_id_fk) REFERENCES school(id) ON DELETE CASCADE,
            CONSTRAINT unique_school_private_enrollment_total UNIQUE (school_id_fk, year)
        )
    """)
    op.execute("CREATE INDEX idx_school_private_enrollment_total_year ON school_private_enrollment_total(year)")
    op.execute("""
        CREATE TABLE school_private_enrollment (
            id SERIAL PRIMARY KEY,
            school_id_fk INTEGER NOT NULL,
            grade_id_fk INTEGER NOT NULL,
            year INTEGER NOT NULL,
            enrollment INTEGER NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_school_private_enrollment_total FOREIGN KEY (school_id_fk, year)
                REFERENCES school_private_enrollment_total(school_id_fk, year) ON DELETE CASCADE,
            CONSTRAINT fk_school_private_enrollment_grade FOREIGN KEY (grade_id_fk) REFERENCES grades(id),
            CONSTRAINT unique_school_private_enrollment UNIQUE (school_id_fk, grade_id_fk, year)
        )
    """)
    op.execute("CREATE INDEX idx_school_private_enrollment_year ON school_private_enrollment(year)")
    for table in TABLES:
        op.execute(f"""
            CREATE TRIGGER trigger_update_{table}_timestamp
            BEFORE UPDATE ON {table}
            FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
        """)

    # Every year in app/alembic/config/private_enrollment_config.yaml
    counts = private_enrollment.load(op.get_bind())
    logger.info(f"Loaded private schools' enrollment: {counts}")


def downgrade():
    for table in reversed(TABLES):
        op.execute(f"DROP TABLE IF EXISTS {table} CASCADE")
