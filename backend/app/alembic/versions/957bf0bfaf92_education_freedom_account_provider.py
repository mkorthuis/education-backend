"""Where Education Freedom Account money and students go, by provider

The Children's Scholarship Fund's EFA Expenditure Reports, 2021-22 to 2024-25: every provider paid,
by allowable category (education_freedom_account_expenditure, with education_freedom_account_category and education_freedom_account_provider), and its list of students
served by each provider with 10 or more, calendar 2025 (education_freedom_account_served). A provider that's a private school
on the state's list is linked to it. See app/etl/education_freedom_account_provider.py.

Revision ID: 957bf0bfaf92
Revises: 200eff24e113
Create Date: 2026-11-21 18:00:00.000000

"""
from alembic import op
import logging

from app.etl import education_freedom_account_provider

logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = '957bf0bfaf92'
down_revision = '200eff24e113'
branch_labels = None
depends_on = None

TABLES = ("education_freedom_account_category", "education_freedom_account_provider", "education_freedom_account_expenditure", "education_freedom_account_served")


def upgrade():
    logger.info("Creating the EFA provider tables")
    op.execute("""
        CREATE TABLE education_freedom_account_category (
            id SERIAL PRIMARY KEY,
            code VARCHAR(100) NOT NULL,
            name VARCHAR(400) NOT NULL,
            combined BOOLEAN NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT unique_education_freedom_account_category_code UNIQUE (code)
        )
    """)
    op.execute("""
        CREATE TABLE education_freedom_account_provider (
            id SERIAL PRIMARY KEY,
            name_key VARCHAR(255) NOT NULL,
            name VARCHAR(255) NOT NULL,
            school_id_fk INTEGER,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_education_freedom_account_provider_school FOREIGN KEY (school_id_fk) REFERENCES school(id) ON DELETE SET NULL,
            CONSTRAINT unique_education_freedom_account_provider_name_key UNIQUE (name_key)
        )
    """)
    op.execute("CREATE INDEX idx_education_freedom_account_provider_school ON education_freedom_account_provider(school_id_fk)")
    op.execute("""
        CREATE TABLE education_freedom_account_expenditure (
            id SERIAL PRIMARY KEY,
            year INTEGER NOT NULL,
            line_no INTEGER NOT NULL,
            category_id INTEGER NOT NULL,
            provider_id INTEGER NOT NULL,
            provider_as_published VARCHAR(255) NOT NULL,
            amount NUMERIC(12,2) NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_education_freedom_account_expenditure_category FOREIGN KEY (category_id) REFERENCES education_freedom_account_category(id),
            CONSTRAINT fk_education_freedom_account_expenditure_provider FOREIGN KEY (provider_id) REFERENCES education_freedom_account_provider(id),
            CONSTRAINT unique_education_freedom_account_expenditure_line UNIQUE (year, line_no)
        )
    """)
    op.execute("CREATE INDEX idx_education_freedom_account_expenditure_provider ON education_freedom_account_expenditure(provider_id)")
    op.execute("CREATE INDEX idx_education_freedom_account_expenditure_category_year ON education_freedom_account_expenditure(category_id, year)")
    op.execute("""
        CREATE TABLE education_freedom_account_served (
            id SERIAL PRIMARY KEY,
            calendar_year INTEGER NOT NULL,
            line_no INTEGER NOT NULL,
            provider_id INTEGER NOT NULL,
            provider_as_published VARCHAR(255) NOT NULL,
            students INTEGER NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_education_freedom_account_served_provider FOREIGN KEY (provider_id) REFERENCES education_freedom_account_provider(id),
            CONSTRAINT unique_education_freedom_account_served_line UNIQUE (calendar_year, line_no)
        )
    """)
    for table in TABLES:
        op.execute(f"""
            CREATE TRIGGER trigger_update_{table}_timestamp
            BEFORE UPDATE ON {table}
            FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
        """)

    # Every configured year (app/alembic/config/education_freedom_account_provider_config.yaml)
    counts = education_freedom_account_provider.load(op.get_bind())
    logger.info(f"Loaded EFA providers: {counts}")


def downgrade():
    for table in reversed(TABLES):
        op.execute(f"DROP TABLE IF EXISTS {table} CASCADE")
