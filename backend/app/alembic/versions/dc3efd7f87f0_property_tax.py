"""Property tax: each town's tax rates (NH DRA) and school taxes (NH DOE's valuations report)

From the two CSVs in assets/property-tax (property_tax_config.yaml): DRA's tax rates for tax years 2014-2025 and the
DOE's valuations report for 2011-2025, each as published. The files they were read from are in the repo:
assets/property-tax/dra (DRA's) and assets/equalized-value (the DOE's); DATA_SOURCES.md says where each was first
downloaded.

Each table's tax_year is the starting year: rates set in the fall of 2025 are tax year 2025 and pay for 2025-26 (the
site's other tables count school years by the ending year, FY2026).

- town_property_tax: DRA's rates per $1,000 (municipal, county, local education, state education, total), the
  equalization ratio, full value rate, valuations and, from 2018, the school tax dollars
- town_school_tax: the DOE report's row for each town: its district and, for a member town, its cooperative (as site
  district ids), school tax dollars, valuations, and rates per $1,000 of assessed and of equalized value
- town_school_tax_coop_share: the part of a town's local school tax that goes to a cooperative

And a materialized view for the site: town_property_tax_summary (each town and tax year, DRA's rates beside the DOE's
dollars, and the school share of the total rate). It has a unique index, so a load refreshes it concurrently.

Revision ID: dc3efd7f87f0
Revises: d3f5b7c9e1a2
Create Date: 2026-11-15 09:00:00.000000

"""
from alembic import op
import logging

from app.etl import property_tax

logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = 'dc3efd7f87f0'
down_revision = 'd3f5b7c9e1a2'
branch_labels = None
depends_on = None

TABLES = ("town_property_tax", "town_school_tax", "town_school_tax_coop_share")
VIEWS = ("town_property_tax_summary",)
TIMESTAMPS = """
    date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP"""
# Rates per $1,000 to the cent; dollars and valuations as the DOE prints them, some with fractions of a cent
RATE = "NUMERIC(6,2)"
DOLLARS = "NUMERIC(18,6)"


def upgrade():
    logger.info("Starting property tax migration upgrade")

    op.execute(
        f"""
        CREATE TABLE town_property_tax (
            id SERIAL PRIMARY KEY,
            town_id_fk INTEGER NOT NULL,
            tax_year INTEGER NOT NULL,
            dra_name VARCHAR(100) NOT NULL,
            municipal_rate {RATE},
            county_rate {RATE},
            local_education_rate {RATE} NOT NULL,
            state_education_rate {RATE} NOT NULL,
            total_rate {RATE},
            equalization_ratio {RATE},
            full_value_tax_rate {RATE},
            assessed_valuation {DOLLARS},
            assessed_valuation_with_utilities {DOLLARS},
            total_tax_commitment {DOLLARS},
            local_school_tax_effort {DOLLARS},
            state_education_tax_effort {DOLLARS},
            date_rate_set DATE NOT NULL,
            note TEXT,{TIMESTAMPS},
            CONSTRAINT fk_town_property_tax_town FOREIGN KEY (town_id_fk) REFERENCES town(id) ON DELETE CASCADE,
            CONSTRAINT unique_town_property_tax UNIQUE (town_id_fk, tax_year)
        )
        """
    )
    op.execute("CREATE INDEX idx_town_property_tax_year ON town_property_tax(tax_year)")
    op.execute(
        f"""
        CREATE TABLE town_school_tax (
            id SERIAL PRIMARY KEY,
            town_id_fk INTEGER NOT NULL,
            tax_year INTEGER NOT NULL,
            district_id_fk INTEGER,
            cooperative_district_id_fk INTEGER,
            assessed_valuation {DOLLARS} NOT NULL,
            assessed_valuation_with_utilities {DOLLARS} NOT NULL,
            equalized_valuation {DOLLARS} NOT NULL,
            equalized_valuation_with_utilities {DOLLARS} NOT NULL,
            local_education_tax {DOLLARS} NOT NULL,
            other_local_tax {DOLLARS} NOT NULL,
            state_education_tax {DOLLARS} NOT NULL,
            rate_local_education {RATE} NOT NULL,
            rate_other_local {RATE} NOT NULL,
            rate_state_education {RATE} NOT NULL,
            rate_total {RATE} NOT NULL,
            equalized_rate_local_education {RATE} NOT NULL,
            equalized_rate_other_local {RATE} NOT NULL,
            equalized_rate_state_education {RATE} NOT NULL,
            equalized_rate_total {RATE} NOT NULL,
            note TEXT,{TIMESTAMPS},
            CONSTRAINT fk_town_school_tax_town FOREIGN KEY (town_id_fk) REFERENCES town(id) ON DELETE CASCADE,
            CONSTRAINT fk_town_school_tax_district FOREIGN KEY (district_id_fk) REFERENCES district(id) ON DELETE SET NULL,
            CONSTRAINT fk_town_school_tax_cooperative FOREIGN KEY (cooperative_district_id_fk) REFERENCES district(id) ON DELETE SET NULL,
            CONSTRAINT unique_town_school_tax UNIQUE (town_id_fk, tax_year)
        )
        """
    )
    op.execute("CREATE INDEX idx_town_school_tax_year ON town_school_tax(tax_year)")
    op.execute("CREATE INDEX idx_town_school_tax_district ON town_school_tax(district_id_fk)")
    op.execute(
        f"""
        CREATE TABLE town_school_tax_coop_share (
            id SERIAL PRIMARY KEY,
            town_school_tax_id_fk INTEGER NOT NULL,
            district_id_fk INTEGER NOT NULL,
            footnote CHAR(1) NOT NULL,
            local_education_tax {DOLLARS} NOT NULL,{TIMESTAMPS},
            CONSTRAINT fk_town_school_tax_coop_share_tax FOREIGN KEY (town_school_tax_id_fk) REFERENCES town_school_tax(id) ON DELETE CASCADE,
            CONSTRAINT fk_town_school_tax_coop_share_district FOREIGN KEY (district_id_fk) REFERENCES district(id) ON DELETE CASCADE,
            CONSTRAINT unique_town_school_tax_coop_share UNIQUE (town_school_tax_id_fk, district_id_fk)
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

    # Every year in app/alembic/config/property_tax_config.yaml from app/alembic/assets/property-tax
    property_tax.load(op.get_bind())

    op.execute(
        """
        CREATE MATERIALIZED VIEW town_property_tax_summary AS
        SELECT COALESCE(r.town_id_fk, s.town_id_fk) AS town_id_fk,
               COALESCE(r.tax_year, s.tax_year) AS tax_year,
               -- The school year it pays for: 2025-26 for tax year 2025
               COALESCE(r.tax_year, s.tax_year) || '-' || LPAD(((COALESCE(r.tax_year, s.tax_year) + 1) % 100)::TEXT, 2, '0') AS school_year,
               s.district_id_fk,
               -- DRA's rates per $1,000 of assessed value
               r.municipal_rate, r.county_rate, r.local_education_rate, r.state_education_rate, r.total_rate,
               r.equalization_ratio, r.full_value_tax_rate, r.assessed_valuation, r.total_tax_commitment, r.date_rate_set,
               -- The DOE's school tax dollars and rates
               s.local_education_tax, s.other_local_tax, s.state_education_tax, s.equalized_valuation_with_utilities,
               s.rate_local_education AS doe_rate_local_education, s.rate_state_education AS doe_rate_state_education,
               s.rate_total AS doe_rate_total, s.equalized_rate_local_education, s.equalized_rate_state_education,
               s.equalized_rate_total,
               -- The school share of the total rate (local and state education): DRA's rates, or before 2014 the DOE's
               CASE WHEN r.total_rate IS NOT NULL
                    THEN ROUND(100 * (r.local_education_rate + r.state_education_rate) / NULLIF(r.total_rate, 0), 1)
                    ELSE ROUND(100 * (s.rate_local_education + s.rate_state_education) / NULLIF(s.rate_total, 0), 1)
               END AS school_share_of_total_rate
        FROM town_property_tax r
        FULL JOIN town_school_tax s ON s.town_id_fk = r.town_id_fk AND s.tax_year = r.tax_year
        """
    )
    op.execute("CREATE UNIQUE INDEX idx_town_property_tax_summary ON town_property_tax_summary (town_id_fk, tax_year)")

    logger.info("Property tax migration upgrade completed successfully")


def downgrade():
    for view in VIEWS:
        op.execute(f"DROP MATERIALIZED VIEW IF EXISTS {view}")
    for table in reversed(TABLES):
        op.execute(f"DROP TABLE IF EXISTS {table} CASCADE")
