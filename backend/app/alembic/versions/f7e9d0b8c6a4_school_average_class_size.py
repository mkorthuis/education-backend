"""School Average Class Size

Revision ID: f7e9d0b8c6a4
Revises: e6d8c9b7a4f3
Create Date: 2024-09-02 12:00:00.000000

"""
from alembic import op
import logging

from app.etl import class_size

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# Revision identifiers, used by Alembic
revision = 'f7e9d0b8c6a4'
down_revision = 'e6d8c9b7a4f3'
branch_labels = None
depends_on = None

# ----------------------------
# Alembic upgrade / downgrade
# ----------------------------

def upgrade():
    logger.info("Starting School Class Size migration upgrade")

    # 1. Create table
    op.execute("""
        CREATE TABLE school_class_size (
            id SERIAL PRIMARY KEY,
            school_id_fk INTEGER NOT NULL,
            year INTEGER NOT NULL,
            grade_1_2 NUMERIC(15,2),
            grade_3_4 NUMERIC(15,2),
            grade_5_8 NUMERIC(15,2),
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_school_class_size_school FOREIGN KEY (school_id_fk) REFERENCES school(id) ON DELETE CASCADE,
            CONSTRAINT unique_school_average_class_size_year UNIQUE (school_id_fk, year)
        )
    """)

    # Indexes
    op.execute("CREATE INDEX idx_school_class_size_school ON school_class_size(school_id_fk)")
    op.execute("CREATE INDEX idx_school_class_size_year ON school_class_size(year)")

    # Trigger
    op.execute("""
        CREATE TRIGGER trigger_update_school_class_size_timestamp
        BEFORE UPDATE ON school_class_size
        FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
    """)

    # 2. Load data: every year in app/alembic/config/school_average_class_size_config.yaml
    class_size.load_school(op.get_bind())

    logger.info("School Class Size migration upgrade completed successfully")


def downgrade():
    logger.info("Downgrading School Class Size migration")
    op.execute("DROP TABLE IF EXISTS school_class_size CASCADE")
    logger.info("Downgrade completed successfully") 