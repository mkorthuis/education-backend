"""Private schools' Form 990s: the organizations, who files for each school, their returns and revenue lines

private_org has each organization that files (or needn't file) a private school's 990, by EIN.
school_990_link gives each private school on the state's list its case: it files its own 990, an
operator's return covers it, it files only the 990-N postcard, it needn't file (church schools), it
has no IRS record, or the row isn't a school. private_org_990 holds the figures from the
organizations' 990 and 990-EZ returns, one row per organization and tax year, and
private_org_990_revenue_line each return's program service revenue lines, sorted into categories.
See app/etl/private_990.py.

Revision ID: 200eff24e113
Revises: 7a409f4c0a3e
Create Date: 2026-11-21 14:00:00.000000

"""
from alembic import op
import logging

from app.etl import private_990

logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = '200eff24e113'
down_revision = '7a409f4c0a3e'
branch_labels = None
depends_on = None

TABLES = ("private_org", "school_990_link", "private_org_990", "private_org_990_revenue_line")


def listed(values) -> str:
    return ", ".join(f"'{value}'" for value in values)


def upgrade():
    logger.info("Creating the private school 990 tables")
    op.execute("""
        CREATE TABLE private_org (
            id SERIAL PRIMARY KEY,
            ein CHAR(9) NOT NULL,
            name VARCHAR(255) NOT NULL,
            founded INTEGER,
            mission TEXT,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT unique_private_org_ein UNIQUE (ein)
        )
    """)
    op.execute(f"""
        CREATE TABLE school_990_link (
            id SERIAL PRIMARY KEY,
            school_id_fk INTEGER NOT NULL,
            status VARCHAR(30) NOT NULL,
            ein CHAR(9),
            note TEXT,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_school_990_link_school FOREIGN KEY (school_id_fk) REFERENCES school(id) ON DELETE CASCADE,
            CONSTRAINT fk_school_990_link_org FOREIGN KEY (ein) REFERENCES private_org(ein),
            CONSTRAINT unique_school_990_link_school UNIQUE (school_id_fk),
            CONSTRAINT check_school_990_link_status CHECK (status IN ({listed(private_990.STATUSES)}))
        )
    """)
    op.execute("CREATE INDEX idx_school_990_link_ein ON school_990_link(ein)")
    op.execute("""
        CREATE TABLE private_org_990 (
            id SERIAL PRIMARY KEY,
            ein CHAR(9) NOT NULL,
            tax_period_end DATE NOT NULL,
            form VARCHAR(10) NOT NULL,
            total_revenue BIGINT,
            prior_total_revenue BIGINT,
            program_service_revenue BIGINT,
            contributions BIGINT,
            government_grants BIGINT,
            investment_income BIGINT,
            investment_gains BIGINT,
            fundraising_event_income BIGINT,
            total_expenses BIGINT,
            prior_total_expenses BIGINT,
            program_expenses BIGINT,
            management_expenses BIGINT,
            fundraising_expenses BIGINT,
            salaries_benefits BIGINT,
            total_assets_eoy BIGINT,
            total_liabilities_eoy BIGINT,
            net_assets_eoy BIGINT,
            land_buildings_equipment_eoy BIGINT,
            public_investments_eoy BIGINT,
            tax_exempt_bonds_eoy BIGINT,
            employees INTEGER,
            volunteers INTEGER,
            paid_over_100k INTEGER,
            endowment_eoy BIGINT,
            endowment_board_designated_share NUMERIC(6,5),
            endowment_permanent_share NUMERIC(6,5),
            endowment_term_share NUMERIC(6,5),
            object_id VARCHAR(20) NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_private_org_990_org FOREIGN KEY (ein) REFERENCES private_org(ein) ON DELETE CASCADE,
            CONSTRAINT unique_private_org_990_return UNIQUE (ein, tax_period_end)
        )
    """)
    op.execute(f"""
        CREATE TABLE private_org_990_revenue_line (
            id SERIAL PRIMARY KEY,
            return_id INTEGER NOT NULL,
            line_no INTEGER NOT NULL,
            description VARCHAR(255) NOT NULL,
            business_code VARCHAR(10),
            amount BIGINT NOT NULL,
            category VARCHAR(30) NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_private_org_990_revenue_line_return FOREIGN KEY (return_id) REFERENCES private_org_990(id) ON DELETE CASCADE,
            CONSTRAINT unique_private_org_990_revenue_line UNIQUE (return_id, line_no),
            CONSTRAINT check_private_org_990_revenue_line_category CHECK (category IN ({listed(private_990.CATEGORIES)}))
        )
    """)
    op.execute("CREATE INDEX idx_private_org_990_revenue_line_category ON private_org_990_revenue_line(category)")
    for table in TABLES:
        op.execute(f"""
            CREATE TRIGGER trigger_update_{table}_timestamp
            BEFORE UPDATE ON {table}
            FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
        """)

    # The organizations, the link and every saved return (app/alembic/assets/private-990)
    counts = private_990.load(op.get_bind())
    logger.info(f"Loaded private schools' 990s: {counts}")


def downgrade():
    for table in reversed(TABLES):
        op.execute(f"DROP TABLE IF EXISTS {table} CASCADE")
