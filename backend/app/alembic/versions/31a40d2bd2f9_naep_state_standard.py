"""NAEP equivalents of state proficiency standards (NCES's state mapping study)

Where each state's standard for proficient performance on its own test falls on the NAEP scale, reading and math in
grades 4 and 8, from NCES's tables in assets/naep-state-mapping (naep_state_standard_config.yaml): the per-year tables
for 2009 to 2022, and the 2005–2009 comparison study's tables for 2005, 2007 and 2009, each as published.

- naep_state_standard: one row per NCES table, state, subject and grade: the NAEP equivalent score, its standard
  error, relative error and caution mark, the state's testing program, and NCES's footnotes on the state. A state NCES
  left out has no score.

Revision ID: 31a40d2bd2f9
Revises: dc3efd7f87f0
Create Date: 2026-11-15 15:00:00.000000

"""
from alembic import op
import logging

from app.etl import naep_state_standard

logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = '31a40d2bd2f9'
down_revision = 'dc3efd7f87f0'
branch_labels = None
depends_on = None


def upgrade():
    logger.info("Starting NAEP state standard migration upgrade")

    op.execute(
        """
        CREATE TABLE naep_state_standard (
            id SERIAL PRIMARY KEY,
            year INTEGER NOT NULL,
            jurisdiction_id_fk INTEGER NOT NULL,
            assessment_subject_id_fk INTEGER NOT NULL,
            grade_id_fk INTEGER NOT NULL,
            nces_table VARCHAR(10) NOT NULL,
            naep_equivalent DOUBLE PRECISION,
            standard_error DOUBLE PRECISION,
            relative_error DOUBLE PRECISION,
            caution BOOLEAN NOT NULL DEFAULT FALSE,
            testing_program VARCHAR(10),
            note TEXT,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_naep_state_standard_jurisdiction FOREIGN KEY (jurisdiction_id_fk) REFERENCES jurisdiction(id),
            CONSTRAINT fk_naep_state_standard_subject FOREIGN KEY (assessment_subject_id_fk) REFERENCES assessment_subject(id),
            CONSTRAINT fk_naep_state_standard_grade FOREIGN KEY (grade_id_fk) REFERENCES grades(id),
            CONSTRAINT unique_naep_state_standard UNIQUE (year, jurisdiction_id_fk, assessment_subject_id_fk, grade_id_fk,
                                                          nces_table),
            CONSTRAINT check_naep_state_standard_score CHECK ((naep_equivalent IS NULL) = (standard_error IS NULL))
        )
        """
    )
    op.execute("CREATE INDEX idx_naep_state_standard_jurisdiction ON naep_state_standard(jurisdiction_id_fk)")
    op.execute(
        """
        CREATE TRIGGER trigger_update_naep_state_standard_timestamp
        BEFORE UPDATE ON naep_state_standard
        FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
        """
    )

    # Load every table in app/alembic/config/naep_state_standard_config.yaml from app/alembic/assets/naep-state-mapping
    naep_state_standard.load(op.get_bind())

    logger.info("NAEP state standard migration upgrade completed successfully")


def downgrade():
    op.execute("DROP TABLE IF EXISTS naep_state_standard CASCADE")
