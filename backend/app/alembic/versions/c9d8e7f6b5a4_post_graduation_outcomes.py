"""Post Graduation Outcomes

Revision ID: c9d8e7f6b5a4
Revises: b3c5d7e9fa12
Create Date: 2024-10-01 12:30:00.000000

"""
from alembic import op
import logging

from app.etl import post_graduation

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# Revision identifiers, used by Alembic.
revision = 'c9d8e7f6b5a4'
down_revision = 'b3c5d7e9fa12'
branch_labels = None
depends_on = None

# ----------------------------
# Alembic upgrade / downgrade
# ----------------------------

def upgrade():
    logger.info("Starting Post Graduation Outcomes migration upgrade")

    # 1. Create tables
    op.execute(
        """
        CREATE TABLE post_graduation_type (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL UNIQUE,
            description TEXT,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    op.execute(
        """
        CREATE TABLE school_post_graduation (
            id SERIAL PRIMARY KEY,
            school_id_fk INTEGER NOT NULL,
            year INTEGER NOT NULL,
            post_graduation_type_id_fk INTEGER NOT NULL,
            value INTEGER NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_spg_school FOREIGN KEY (school_id_fk) REFERENCES school(id) ON DELETE CASCADE,
            CONSTRAINT fk_spg_type FOREIGN KEY (post_graduation_type_id_fk) REFERENCES post_graduation_type(id) ON DELETE CASCADE,
            CONSTRAINT unique_school_post_grad_year_type UNIQUE (school_id_fk, year, post_graduation_type_id_fk)
        )
        """
    )

    # State table
    op.execute(
        """
        CREATE TABLE state_post_graduation (
            id SERIAL PRIMARY KEY,
            year INTEGER NOT NULL,
            post_graduation_type_id_fk INTEGER NOT NULL,
            value INTEGER NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_spg_state_type FOREIGN KEY (post_graduation_type_id_fk) REFERENCES post_graduation_type(id) ON DELETE CASCADE,
            CONSTRAINT unique_state_post_grad_year_type UNIQUE (year, post_graduation_type_id_fk)
        )
        """
    )

    # Indexes
    op.execute("CREATE INDEX idx_spg_school ON school_post_graduation(school_id_fk)")
    op.execute("CREATE INDEX idx_spg_year ON school_post_graduation(year)")
    op.execute("CREATE INDEX idx_spg_type ON school_post_graduation(post_graduation_type_id_fk)")
    op.execute("CREATE INDEX idx_state_pg_year ON state_post_graduation(year)")
    op.execute("CREATE INDEX idx_state_pg_type ON state_post_graduation(post_graduation_type_id_fk)")

    # Trigger
    op.execute(
        """
        CREATE TRIGGER trigger_update_school_post_graduation_timestamp
        BEFORE UPDATE ON school_post_graduation
        FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
        """
    )

    # 2. Load data: the post_graduation_type rows, then every year in
    # app/alembic/config/post_graduation_outcomes_config.yaml
    post_graduation.load(op.get_bind())

    logger.info("Post Graduation Outcomes migration upgrade completed successfully")


def downgrade():
    logger.info("Downgrading Post Graduation Outcomes migration")
    op.execute("DROP TABLE IF EXISTS school_post_graduation CASCADE")
    op.execute("DROP TABLE IF EXISTS state_post_graduation CASCADE")
    op.execute("DROP TABLE IF EXISTS post_graduation_type CASCADE")
    logger.info("Downgrade completed successfully") 