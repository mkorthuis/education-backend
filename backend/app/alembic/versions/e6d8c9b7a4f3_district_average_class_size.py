"""District Average Class Size

Revision ID: e6d8c9b7a4f3
Revises: d4e5f6g7h8i9
Create Date: 2024-09-01 12:00:00.000000

"""
from alembic import op
import logging

from app.etl import class_size

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# Revision identifiers, used by Alembic
revision = 'e6d8c9b7a4f3'
down_revision = 'd4e5f6g7h8i9'
branch_labels = None
depends_on = None


# ----------------------------
# Alembic upgrade / downgrade
# ----------------------------

def upgrade():
    """Create district_class_size table and load data."""
    logger.info("Starting District Class Size migration upgrade")

    # 1. Create table
    logger.info("Creating district_class_size table")
    op.execute("""
        CREATE TABLE district_class_size (
            id SERIAL PRIMARY KEY,
            district_id_fk INTEGER NOT NULL,
            year INTEGER NOT NULL,
            grade_1_2 NUMERIC(15,2),
            grade_3_4 NUMERIC(15,2),
            grade_5_8 NUMERIC(15,2),
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_district_class_size_district FOREIGN KEY (district_id_fk) REFERENCES district(id) ON DELETE CASCADE,
            CONSTRAINT unique_district_average_class_size_year UNIQUE (district_id_fk, year)
        )
    """)

    # 2. Indexes
    logger.info("Creating indexes for district_class_size table")
    op.execute("CREATE INDEX idx_district_class_size_district ON district_class_size(district_id_fk)")
    op.execute("CREATE INDEX idx_district_class_size_year ON district_class_size(year)")

    # 3. Trigger for district_class_size date_updated
    logger.info("Creating trigger for district_class_size table")
    op.execute("""
        CREATE TRIGGER trigger_update_district_class_size_timestamp
        BEFORE UPDATE ON district_class_size
        FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
    """)

    # 4. Create state_class_size table (must exist before data insert)
    logger.info("Creating state_class_size table")
    op.execute("""
        CREATE TABLE state_class_size (
            id SERIAL PRIMARY KEY,
            year INTEGER NOT NULL,
            grade_1_2 NUMERIC(15,2),
            grade_3_4 NUMERIC(15,2),
            grade_5_8 NUMERIC(15,2),
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT unique_state_average_class_size_year UNIQUE (year)
        )
    """)

    # Index and trigger for state_class_size
    op.execute("CREATE INDEX idx_state_class_size_year ON state_class_size(year)")
    op.execute("""
        CREATE TRIGGER trigger_update_state_class_size_timestamp
        BEFORE UPDATE ON state_class_size
        FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
    """)

    # 5. Load data: every year in app/alembic/config/district_average_class_size_config.yaml
    class_size.load_district(op.get_bind())

    logger.info("District & State Class Size migration upgrade completed successfully")


def downgrade():
    """Drop district_class_size table."""
    logger.info("Starting downgrade for District & State Class Size migration")
    op.execute("DROP TABLE IF EXISTS state_class_size CASCADE")
    op.execute("DROP TABLE IF EXISTS district_class_size CASCADE")
    logger.info("Downgrade completed successfully") 