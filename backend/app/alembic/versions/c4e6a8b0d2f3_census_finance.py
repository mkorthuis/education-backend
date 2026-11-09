"""Census school finance by state

School system revenue by state, FY2010-FY2024, from the Census Bureau's Annual Survey of School
System Finances:

- census_revenue_item: Census's revenue items (Title I, property taxes, ...), each with its source
  (federal, state or local) and the category Census's summary tables put it in
- census_state_revenue: each state's and the nation's revenue by item and year, in thousand dollars
- census_state_enrollment: the fall enrollment Census uses for per-pupil amounts

The states, DC and the nation (US) are rows of the jurisdiction table NAEP added.

Revision ID: c4e6a8b0d2f3
Revises: b3d5f7a9c1e2
Create Date: 2026-11-09 03:00:00.000000

"""
from alembic import op
import logging

from app.etl import census_finance

logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = 'c4e6a8b0d2f3'
down_revision = 'b3d5f7a9c1e2'
branch_labels = None
depends_on = None

TABLES = ("census_revenue_item", "census_state_revenue", "census_state_enrollment")


def upgrade():
    logger.info("Starting Census school finance migration upgrade")

    op.execute(
        """
        CREATE TABLE census_revenue_item (
            id SERIAL PRIMARY KEY,
            code VARCHAR(10) NOT NULL,
            name VARCHAR(255) NOT NULL,
            source VARCHAR(10) NOT NULL,
            category VARCHAR(100) NOT NULL,
            display_order INTEGER NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT unique_census_revenue_item_code UNIQUE (code),
            CONSTRAINT check_census_revenue_item_source CHECK (source IN ('federal', 'state', 'local'))
        )
        """
    )
    op.execute(
        """
        CREATE TABLE census_state_revenue (
            id SERIAL PRIMARY KEY,
            year INTEGER NOT NULL,
            jurisdiction_id_fk INTEGER NOT NULL,
            census_revenue_item_id_fk INTEGER NOT NULL,
            amount_thousands BIGINT NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_census_state_revenue_jurisdiction FOREIGN KEY (jurisdiction_id_fk) REFERENCES jurisdiction(id),
            CONSTRAINT fk_census_state_revenue_item FOREIGN KEY (census_revenue_item_id_fk) REFERENCES census_revenue_item(id),
            CONSTRAINT unique_census_state_revenue UNIQUE (year, jurisdiction_id_fk, census_revenue_item_id_fk)
        )
        """
    )
    op.execute("CREATE INDEX idx_census_state_revenue_year ON census_state_revenue(year)")
    op.execute("CREATE INDEX idx_census_state_revenue_jurisdiction ON census_state_revenue(jurisdiction_id_fk)")
    op.execute(
        """
        CREATE TABLE census_state_enrollment (
            id SERIAL PRIMARY KEY,
            year INTEGER NOT NULL,
            jurisdiction_id_fk INTEGER NOT NULL,
            enrollment INTEGER NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_census_state_enrollment_jurisdiction FOREIGN KEY (jurisdiction_id_fk) REFERENCES jurisdiction(id),
            CONSTRAINT unique_census_state_enrollment UNIQUE (year, jurisdiction_id_fk)
        )
        """
    )
    for table in TABLES:
        op.execute(
            f"""
            CREATE TRIGGER trigger_update_{table}_timestamp
            BEFORE UPDATE ON {table}
            FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
            """
        )

    # Load every year in app/alembic/config/census_finance_config.yaml from app/alembic/assets/census-finance
    census_finance.load(op.get_bind())

    logger.info("Census school finance migration upgrade completed successfully")


def downgrade():
    for table in reversed(TABLES):
        op.execute(f"DROP TABLE IF EXISTS {table} CASCADE")
    # The nation's row was added for this data; NAEP doesn't use it
    op.execute("DELETE FROM jurisdiction WHERE code = 'US'")
