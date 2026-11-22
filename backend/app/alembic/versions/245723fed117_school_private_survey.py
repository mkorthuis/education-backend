"""The NCES Private School Survey for New Hampshire's private schools, 2017-18 to 2023-24

Each private school's answers in the four latest surveys (every two years): school_private_survey has
its type, affiliation and religious orientation, level and community, students, teachers and students
per teacher, male students and race shares, school day, and for a high school last year's seniors and
the share who went to a four-year college; school_private_survey_grade its students by grade. See
app/etl/private_school_survey.py.

Revision ID: 245723fed117
Revises: 957bf0bfaf92
Create Date: 2026-11-21 20:00:00.000000

"""
from alembic import op
import logging

from app.etl import private_school_survey

logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = '245723fed117'
down_revision = '957bf0bfaf92'
branch_labels = None
depends_on = None

TABLES = ("school_private_survey", "school_private_survey_grade")


def upgrade():
    logger.info("Creating school_private_survey and school_private_survey_grade")
    op.execute("""
        CREATE TABLE school_private_survey (
            id SERIAL PRIMARY KEY,
            school_id_fk INTEGER NOT NULL,
            year INTEGER NOT NULL,
            ppin VARCHAR(10) NOT NULL,
            typology VARCHAR(100),
            affiliation VARCHAR(50),
            religious_orientation VARCHAR(100),
            level VARCHAR(50),
            community_type VARCHAR(20),
            students INTEGER,
            students_with_preschool INTEGER,
            male_students INTEGER,
            seniors_prior_year INTEGER,
            to_four_year_college_pct INTEGER,
            teachers_fte NUMERIC(8,2),
            students_per_teacher NUMERIC(8,2),
            school_day_hours NUMERIC(4,2),
            pct_american_indian NUMERIC(5,2),
            pct_asian NUMERIC(5,2),
            pct_pacific_islander NUMERIC(5,2),
            pct_hispanic NUMERIC(5,2),
            pct_white NUMERIC(5,2),
            pct_black NUMERIC(5,2),
            pct_two_or_more_races NUMERIC(5,2),
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_school_private_survey_school FOREIGN KEY (school_id_fk) REFERENCES school(id) ON DELETE CASCADE,
            CONSTRAINT unique_school_private_survey_year UNIQUE (school_id_fk, year)
        )
    """)
    op.execute("CREATE INDEX idx_school_private_survey_year ON school_private_survey(year)")
    op.execute("""
        CREATE TABLE school_private_survey_grade (
            id SERIAL PRIMARY KEY,
            school_id_fk INTEGER NOT NULL,
            year INTEGER NOT NULL,
            grade_id_fk INTEGER NOT NULL,
            students INTEGER NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_school_private_survey_grade_survey FOREIGN KEY (school_id_fk, year)
                REFERENCES school_private_survey(school_id_fk, year) ON DELETE CASCADE,
            CONSTRAINT fk_school_private_survey_grade_grade FOREIGN KEY (grade_id_fk) REFERENCES grades(id),
            CONSTRAINT unique_school_private_survey_grade UNIQUE (school_id_fk, year, grade_id_fk)
        )
    """)
    for table in TABLES:
        op.execute(f"""
            CREATE TRIGGER trigger_update_{table}_timestamp
            BEFORE UPDATE ON {table}
            FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
        """)

    # Every survey year in app/alembic/config/private_school_survey_config.yaml
    counts = private_school_survey.load(op.get_bind())
    logger.info(f"Loaded the Private School Survey: {counts}")


def downgrade():
    for table in reversed(TABLES):
        op.execute(f"DROP TABLE IF EXISTS {table} CASCADE")
