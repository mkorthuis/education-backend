"""Education Freedom Account

Revision ID: 854abd432fef
Revises: 49358ad1275f
Create Date: 2024-04-09 15:30:00.000000

"""
from alembic import op
import logging

from app.etl import education_freedom_account

# Configure logger
logger = logging.getLogger('alembic.runtime.migration')

# Revision identifiers, used by Alembic
revision = '854abd432fef'
down_revision = '49358ad1275f'
branch_labels = None
depends_on = None


def upgrade():
    logger.info("Starting Education Freedom Account migration upgrade")
    
    # Create new tables
    logger.info("Creating education_freedom_account_entry_type table")
    op.execute("""
        CREATE TABLE education_freedom_account_entry_type (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description TEXT,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
    """)

    logger.info("Creating education_freedom_account_entry_type_value table")
    op.execute("""
        CREATE TABLE education_freedom_account_entry_type_value (
            id SERIAL PRIMARY KEY,
            education_freedom_account_entry_type_id_fk INTEGER NOT NULL,
            year INTEGER NOT NULL,
            value NUMERIC(15, 2),
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_efa_entry_type
                FOREIGN KEY (education_freedom_account_entry_type_id_fk)
                REFERENCES education_freedom_account_entry_type(id)
                ON DELETE CASCADE,
            CONSTRAINT unique_efa_entry_type_value
                UNIQUE (education_freedom_account_entry_type_id_fk, year)
        )
    """)

    logger.info("Creating education_freedom_account_entry table")
    op.execute("""
        CREATE TABLE education_freedom_account_entry (
            id SERIAL PRIMARY KEY,
            town_id_fk INTEGER NOT NULL,
            year INTEGER NOT NULL,
            education_freedom_account_entry_type_id_fk INTEGER NOT NULL,
            value NUMERIC(15, 2),
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_efa_town
                FOREIGN KEY (town_id_fk)
                REFERENCES town(id)
                ON DELETE CASCADE,
            CONSTRAINT fk_efa_entry_type
                FOREIGN KEY (education_freedom_account_entry_type_id_fk)
                REFERENCES education_freedom_account_entry_type(id)
                ON DELETE CASCADE,
            CONSTRAINT unique_efa_entry
                UNIQUE (town_id_fk, year, education_freedom_account_entry_type_id_fk)
        )
    """)

    # Create triggers for the new tables
    logger.info("Creating triggers for tables")
    op.execute("""
        CREATE TRIGGER trigger_update_education_freedom_account_entry_type_timestamp
        BEFORE UPDATE ON education_freedom_account_entry_type
        FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
    """)

    op.execute("""
        CREATE TRIGGER trigger_update_education_freedom_account_entry_type_value_timestamp
        BEFORE UPDATE ON education_freedom_account_entry_type_value
        FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
    """)

    op.execute("""
        CREATE TRIGGER trigger_update_education_freedom_account_entry_timestamp
        BEFORE UPDATE ON education_freedom_account_entry
        FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
    """)

    # Create indexes
    logger.info("Creating indexes for tables")
    op.execute("CREATE INDEX idx_efa_entry_type_value_type ON education_freedom_account_entry_type_value(education_freedom_account_entry_type_id_fk)")
    op.execute("CREATE INDEX idx_efa_entry_type_value_year ON education_freedom_account_entry_type_value(year)")
    op.execute("CREATE INDEX idx_efa_entry_town ON education_freedom_account_entry(town_id_fk)")
    op.execute("CREATE INDEX idx_efa_entry_year ON education_freedom_account_entry(year)")
    op.execute("CREATE INDEX idx_efa_entry_type ON education_freedom_account_entry(education_freedom_account_entry_type_id_fk)")

    # Every year in app/alembic/config/generate_education_freedom_accounts.yaml
    logger.info("Starting data loading process")
    education_freedom_account.load(op.get_bind())

    logger.info("Migration completed successfully")


def downgrade():
    logger.info("Starting Education Freedom Account migration downgrade")
    # Drop tables in reverse order to handle dependencies
    logger.info("Dropping education_freedom_account_entry table")
    op.execute("DROP TABLE IF EXISTS education_freedom_account_entry CASCADE")
    logger.info("Dropping education_freedom_account_entry_type_value table")
    op.execute("DROP TABLE IF EXISTS education_freedom_account_entry_type_value CASCADE")
    logger.info("Dropping education_freedom_account_entry_type table")
    op.execute("DROP TABLE IF EXISTS education_freedom_account_entry_type CASCADE")
    logger.info("Downgrade completed successfully")