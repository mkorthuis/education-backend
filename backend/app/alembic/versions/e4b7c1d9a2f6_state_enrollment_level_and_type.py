"""State enrollment by level and by type of school

Renames state_enrollment, which holds average daily membership by school level, to
state_enrollment_level. Adds state_enrollment_type: statewide October 1 enrollment by type of school
(public district, public academy and joint maintenance agreement, public charter, interstate and
nonpublic) and grade, from iPlatform's "State Totals Ten Years Public and Private Fall Enrollments"
report, with enrollment_type listing the types.

Revision ID: e4b7c1d9a2f6
Revises: d8b2f4a6c9e1
Create Date: 2026-11-05 12:00:00.000000

"""
from alembic import op
import logging

from app.etl import enrollment_type

logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = 'e4b7c1d9a2f6'
down_revision = 'd8b2f4a6c9e1'
branch_labels = None
depends_on = None


def upgrade():
    logger.info("Starting state enrollment by level and type migration upgrade")

    op.execute("ALTER TABLE state_enrollment RENAME TO state_enrollment_level")
    op.execute("ALTER INDEX idx_state_enrollment_year RENAME TO idx_state_enrollment_level_year")

    op.execute(
        """
        CREATE TABLE enrollment_type (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT unique_enrollment_type_name UNIQUE (name)
        )
        """
    )
    op.execute(
        """
        CREATE TABLE state_enrollment_type (
            id SERIAL PRIMARY KEY,
            year INTEGER NOT NULL,
            enrollment_type_id_fk INTEGER NOT NULL,
            grade_id_fk INTEGER NOT NULL,
            enrollment INTEGER NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_state_enrollment_type_type FOREIGN KEY (enrollment_type_id_fk) REFERENCES enrollment_type(id),
            CONSTRAINT fk_state_enrollment_type_grade FOREIGN KEY (grade_id_fk) REFERENCES grades(id),
            CONSTRAINT unique_state_enrollment_type_year UNIQUE (year, enrollment_type_id_fk, grade_id_fk)
        )
        """
    )
    op.execute("CREATE INDEX idx_state_enrollment_type_year ON state_enrollment_type(year)")
    for table in ("enrollment_type", "state_enrollment_type"):
        op.execute(
            f"""
            CREATE TRIGGER trigger_update_{table}_timestamp
            BEFORE UPDATE ON {table}
            FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
            """
        )

    # Load every year in app/alembic/config/state_enrollment_type_config.yaml
    enrollment_type.load(op.get_bind())

    logger.info("State enrollment by level and type migration upgrade completed successfully")


def downgrade():
    op.execute("DROP TABLE IF EXISTS state_enrollment_type CASCADE")
    op.execute("DROP TABLE IF EXISTS enrollment_type CASCADE")
    op.execute("ALTER INDEX idx_state_enrollment_level_year RENAME TO idx_state_enrollment_year")
    op.execute("ALTER TABLE state_enrollment_level RENAME TO state_enrollment")
