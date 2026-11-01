"""School Early Exit

Revision ID: b3c5d7e9fa12
Revises: f7e9d0b8c6a4
Create Date: 2024-10-01 12:00:00.000000

"""
from alembic import op
import logging

from app.etl import early_exit

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# Revision identifiers, used by Alembic.
revision = 'b3c5d7e9fa12'
down_revision = 'f7e9d0b8c6a4'
branch_labels = None
depends_on = None

# ----------------------------
# Alembic upgrade / downgrade
# ----------------------------

def upgrade():
    logger.info("Starting School Early Exit migration upgrade")

    # 1. Create tables
    op.execute(
        """
        CREATE TABLE school_early_exit (
            id SERIAL PRIMARY KEY,
            school_id_fk INTEGER NOT NULL,
            year INTEGER NOT NULL,
            adjusted_fall_enrollment INTEGER,
            earned_hiset INTEGER,
            enrolled_in_college INTEGER,
            dropped_out INTEGER,
            missing INTEGER,
            annual_early_exit_percentage NUMERIC(15,4),
            four_year_early_exit_percentage NUMERIC(15,4),
            annual_dropout_percentage NUMERIC(15,4),
            four_year_dropout_percentage NUMERIC(15,4),
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_school_early_exit_school FOREIGN KEY (school_id_fk) REFERENCES school(id) ON DELETE CASCADE,
            CONSTRAINT unique_school_early_exit_year UNIQUE (school_id_fk, year)
        )
        """
    )

    # Indexes
    op.execute("CREATE INDEX idx_school_early_exit_school ON school_early_exit(school_id_fk)")
    op.execute("CREATE INDEX idx_school_early_exit_year ON school_early_exit(year)")

    # Trigger
    op.execute(
        """
        CREATE TRIGGER trigger_update_school_early_exit_timestamp
        BEFORE UPDATE ON school_early_exit
        FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
        """
    )

    # State table
    op.execute(
        """
        CREATE TABLE state_early_exit (
            id SERIAL PRIMARY KEY,
            year INTEGER NOT NULL,
            adjusted_fall_enrollment INTEGER,
            earned_hiset INTEGER,
            enrolled_in_college INTEGER,
            dropped_out INTEGER,
            missing INTEGER,
            annual_early_exit_percentage NUMERIC(15,4),
            four_year_early_exit_percentage NUMERIC(15,4),
            annual_dropout_percentage NUMERIC(15,4),
            four_year_dropout_percentage NUMERIC(15,4),
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT unique_state_early_exit_year UNIQUE (year)
        )
        """
    )

    # Index on year for state table
    op.execute("CREATE INDEX idx_state_early_exit_year ON state_early_exit(year)")

    # 2. Load data: every year in app/alembic/config/school_early_exit_config.yaml
    early_exit.load(op.get_bind())

    logger.info("School Early Exit migration upgrade completed successfully")


def downgrade():
    logger.info("Downgrading School Early Exit migration")
    op.execute("DROP TABLE IF EXISTS school_early_exit CASCADE")
    op.execute("DROP TABLE IF EXISTS state_early_exit CASCADE")
    logger.info("Downgrade completed successfully") 