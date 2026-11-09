"""NAEP results by state

NAEP (the Nation's Report Card) reading and math results in grades 4 and 8 for every state, DC, the
Department of Defense schools (DoDEA) and the nation's public schools, 2003 on, from NCES's NAEP
Data Service:

- jurisdiction: the places NAEP reports on, by NAEP's codes (NH; NP for the national public average)
- naep_measure: average scale score, and the shares at or above NAEP Basic and Proficient and at Advanced
- naep_student_group: NAEP's student groups: all students, sex, economic status, disability status,
  race/ethnicity, school location and English learner status
- naep_result: each measure for every place and year
- naep_comparison: NAEP's significance tests of one place and year against another place or year

Revision ID: b3d5f7a9c1e2
Revises: f5a7c9e2b4d8
Create Date: 2026-11-08 22:00:00.000000

"""
from alembic import op
import logging

from app.etl import naep

logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = 'b3d5f7a9c1e2'
down_revision = 'f5a7c9e2b4d8'
branch_labels = None
depends_on = None

TABLES = ("jurisdiction", "naep_measure", "naep_student_group", "naep_result", "naep_comparison")


def upgrade():
    logger.info("Starting NAEP migration upgrade")

    op.execute(
        """
        CREATE TABLE jurisdiction (
            id SERIAL PRIMARY KEY,
            code VARCHAR(4) NOT NULL,
            name VARCHAR(255) NOT NULL,
            kind VARCHAR(20) NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT unique_jurisdiction_code UNIQUE (code),
            CONSTRAINT check_jurisdiction_kind CHECK (kind IN ('state', 'nation', 'other'))
        )
        """
    )
    op.execute(
        """
        CREATE TABLE naep_measure (
            id SERIAL PRIMARY KEY,
            code VARCHAR(10) NOT NULL,
            name VARCHAR(255) NOT NULL,
            unit VARCHAR(20) NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT unique_naep_measure_code UNIQUE (code),
            CONSTRAINT check_naep_measure_unit CHECK (unit IN ('score', 'percent'))
        )
        """
    )
    op.execute(
        """
        CREATE TABLE naep_student_group (
            id SERIAL PRIMARY KEY,
            variable VARCHAR(20) NOT NULL,
            value VARCHAR(10) NOT NULL,
            variable_name VARCHAR(255) NOT NULL,
            name VARCHAR(255) NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT unique_naep_student_group UNIQUE (variable, value)
        )
        """
    )
    op.execute(
        """
        CREATE TABLE naep_result (
            id SERIAL PRIMARY KEY,
            year INTEGER NOT NULL,
            jurisdiction_id_fk INTEGER NOT NULL,
            assessment_subject_id_fk INTEGER NOT NULL,
            grade_id_fk INTEGER NOT NULL,
            naep_measure_id_fk INTEGER NOT NULL,
            naep_student_group_id_fk INTEGER NOT NULL,
            value DOUBLE PRECISION,
            is_displayable BOOLEAN NOT NULL DEFAULT TRUE,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_naep_result_jurisdiction FOREIGN KEY (jurisdiction_id_fk) REFERENCES jurisdiction(id),
            CONSTRAINT fk_naep_result_subject FOREIGN KEY (assessment_subject_id_fk) REFERENCES assessment_subject(id),
            CONSTRAINT fk_naep_result_grade FOREIGN KEY (grade_id_fk) REFERENCES grades(id),
            CONSTRAINT fk_naep_result_measure FOREIGN KEY (naep_measure_id_fk) REFERENCES naep_measure(id),
            CONSTRAINT fk_naep_result_student_group FOREIGN KEY (naep_student_group_id_fk) REFERENCES naep_student_group(id),
            CONSTRAINT unique_naep_result UNIQUE (year, jurisdiction_id_fk, assessment_subject_id_fk, grade_id_fk,
                                                  naep_measure_id_fk, naep_student_group_id_fk)
        )
        """
    )
    op.execute("CREATE INDEX idx_naep_result_year ON naep_result(year)")
    op.execute("CREATE INDEX idx_naep_result_jurisdiction ON naep_result(jurisdiction_id_fk)")
    op.execute(
        """
        CREATE TABLE naep_comparison (
            id SERIAL PRIMARY KEY,
            year INTEGER NOT NULL,
            jurisdiction_id_fk INTEGER NOT NULL,
            other_year INTEGER NOT NULL,
            other_jurisdiction_id_fk INTEGER NOT NULL,
            assessment_subject_id_fk INTEGER NOT NULL,
            grade_id_fk INTEGER NOT NULL,
            naep_measure_id_fk INTEGER NOT NULL,
            naep_student_group_id_fk INTEGER NOT NULL,
            basis VARCHAR(20) NOT NULL,
            result VARCHAR(20) NOT NULL,
            difference DOUBLE PRECISION,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_naep_comparison_jurisdiction FOREIGN KEY (jurisdiction_id_fk) REFERENCES jurisdiction(id),
            CONSTRAINT fk_naep_comparison_other_jurisdiction FOREIGN KEY (other_jurisdiction_id_fk) REFERENCES jurisdiction(id),
            CONSTRAINT fk_naep_comparison_subject FOREIGN KEY (assessment_subject_id_fk) REFERENCES assessment_subject(id),
            CONSTRAINT fk_naep_comparison_grade FOREIGN KEY (grade_id_fk) REFERENCES grades(id),
            CONSTRAINT fk_naep_comparison_measure FOREIGN KEY (naep_measure_id_fk) REFERENCES naep_measure(id),
            CONSTRAINT fk_naep_comparison_student_group FOREIGN KEY (naep_student_group_id_fk) REFERENCES naep_student_group(id),
            CONSTRAINT unique_naep_comparison UNIQUE (year, jurisdiction_id_fk, other_year, other_jurisdiction_id_fk,
                                                      assessment_subject_id_fk, grade_id_fk, naep_measure_id_fk,
                                                      naep_student_group_id_fk, basis),
            CONSTRAINT check_naep_comparison_basis CHECK (basis IN ('all_jurisdictions', 'pair')),
            CONSTRAINT check_naep_comparison_result CHECK (result IN ('higher', 'lower', 'not_significant'))
        )
        """
    )
    op.execute("CREATE INDEX idx_naep_comparison_year ON naep_comparison(year)")
    op.execute("CREATE INDEX idx_naep_comparison_jurisdiction ON naep_comparison(jurisdiction_id_fk)")
    for table in TABLES:
        op.execute(
            f"""
            CREATE TRIGGER trigger_update_{table}_timestamp
            BEFORE UPDATE ON {table}
            FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
            """
        )

    # Load every year in app/alembic/config/naep_config.yaml from the files in app/alembic/assets/naep
    naep.load(op.get_bind())

    logger.info("NAEP migration upgrade completed successfully")


def downgrade():
    for table in reversed(TABLES):
        op.execute(f"DROP TABLE IF EXISTS {table} CASCADE")
