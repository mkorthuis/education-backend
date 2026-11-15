"""Special education aid: NH DOE's yearly table of each district's high-cost special education costs and state aid

From NH DOE's special education aid files, FY2021-FY2026 (special_education_aid_config.yaml):

- special_education_aid_year: each fiscal year of aid, the cost per student where aid begins, the appropriation,
  the proration and the DOE's statewide totals
- special_education_aid_band: each year's bands of a student's cost (as multiples of the state average cost per
  pupil) and the state's share of each, so a change in the formula (HB 1563 adds a band in FY2029) is new rows
- district_special_education_aid: each district's total cost, entitlement and aid paid, as the DOE publishes them
- district_special_education_aid_band: each district's costs in each band

And a materialized view for the site: district_special_education_aid_summary (a district's costs by band,
entitlement and aid, beside the special education aid it reported in its financial report). It has a unique index,
so a load refreshes it concurrently.

Revision ID: d3f5b7c9e1a2
Revises: c2e4a6b8d0f1
Create Date: 2026-11-14 20:00:00.000000

"""
from alembic import op
import logging

from app.etl import special_education_aid

logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = 'd3f5b7c9e1a2'
down_revision = 'c2e4a6b8d0f1'
branch_labels = None
depends_on = None

TABLES = ("special_education_aid_year", "special_education_aid_band", "district_special_education_aid",
          "district_special_education_aid_band")
VIEWS = ("district_special_education_aid_summary",)
TIMESTAMPS = """
    date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP"""


def _quoted(values):
    return ", ".join(f"'{v}'" for v in values)


def upgrade():
    logger.info("Starting special education aid migration upgrade")

    op.execute(
        f"""
        CREATE TABLE special_education_aid_year (
            id SERIAL PRIMARY KEY,
            fiscal_year SMALLINT NOT NULL,
            cost_school_year VARCHAR(7) NOT NULL,
            status VARCHAR(10) NOT NULL,
            as_of DATE,
            state_average_cost NUMERIC(10,2) NOT NULL,
            threshold_cost NUMERIC(12,2) NOT NULL,
            appropriation NUMERIC(14,2),
            proration_rate NUMERIC(9,7) NOT NULL,
            minimum_share NUMERIC(4,3),
            state_students_reported NUMERIC(7,1),
            state_students_highest_band NUMERIC(7,1),
            state_total_cost NUMERIC(15,2) NOT NULL,
            state_entitlement NUMERIC(15,2) NOT NULL,
            state_aid_paid NUMERIC(15,2) NOT NULL,
            source_url TEXT NOT NULL,
            page_url TEXT NOT NULL,
            note TEXT,{TIMESTAMPS},
            CONSTRAINT unique_special_education_aid_year UNIQUE (fiscal_year),
            CONSTRAINT check_special_education_aid_year_status CHECK (status IN ({_quoted(special_education_aid.STATUSES)})),
            CONSTRAINT check_special_education_aid_year_proration CHECK (proration_rate > 0 AND proration_rate <= 1),
            CONSTRAINT check_special_education_aid_year_minimum CHECK (minimum_share IS NULL OR minimum_share BETWEEN 0 AND 1)
        )
        """
    )
    op.execute(
        f"""
        CREATE TABLE special_education_aid_band (
            id SERIAL PRIMARY KEY,
            fiscal_year SMALLINT NOT NULL,
            band SMALLINT NOT NULL,
            from_multiple NUMERIC(4,2) NOT NULL,
            to_multiple NUMERIC(4,2),
            state_share NUMERIC(4,3) NOT NULL,
            label VARCHAR(100) NOT NULL,
            citation VARCHAR(255) NOT NULL,
            source_url TEXT NOT NULL,{TIMESTAMPS},
            CONSTRAINT fk_special_education_aid_band_year FOREIGN KEY (fiscal_year) REFERENCES special_education_aid_year(fiscal_year) ON DELETE CASCADE,
            CONSTRAINT unique_special_education_aid_band UNIQUE (fiscal_year, band),
            CONSTRAINT check_special_education_aid_band_share CHECK (state_share BETWEEN 0 AND 1),
            CONSTRAINT check_special_education_aid_band_multiples CHECK (to_multiple IS NULL OR to_multiple > from_multiple)
        )
        """
    )
    op.execute(
        f"""
        CREATE TABLE district_special_education_aid (
            id SERIAL PRIMARY KEY,
            district_id_fk INTEGER NOT NULL,
            fiscal_year SMALLINT NOT NULL,
            source_name VARCHAR(255) NOT NULL,
            students_reported NUMERIC(6,1),
            total_cost NUMERIC(14,2) NOT NULL,
            entitlement NUMERIC(14,2) NOT NULL,
            aid_paid NUMERIC(14,2) NOT NULL,{TIMESTAMPS},
            CONSTRAINT fk_district_special_education_aid_district FOREIGN KEY (district_id_fk) REFERENCES district(id) ON DELETE CASCADE,
            CONSTRAINT fk_district_special_education_aid_year FOREIGN KEY (fiscal_year) REFERENCES special_education_aid_year(fiscal_year) ON DELETE CASCADE,
            CONSTRAINT unique_district_special_education_aid UNIQUE (district_id_fk, fiscal_year),
            CONSTRAINT check_district_special_education_aid_amounts CHECK (entitlement >= 0 AND entitlement <= total_cost AND aid_paid >= 0)
        )
        """
    )
    op.execute("CREATE INDEX idx_district_special_education_aid_year ON district_special_education_aid(fiscal_year)")
    op.execute(
        f"""
        CREATE TABLE district_special_education_aid_band (
            id SERIAL PRIMARY KEY,
            district_special_education_aid_id_fk INTEGER NOT NULL,
            band SMALLINT NOT NULL,
            cost NUMERIC(14,2) NOT NULL,
            students NUMERIC(6,1),{TIMESTAMPS},
            CONSTRAINT fk_district_special_education_aid_band_aid FOREIGN KEY (district_special_education_aid_id_fk)
                REFERENCES district_special_education_aid(id) ON DELETE CASCADE,
            CONSTRAINT unique_district_special_education_aid_band UNIQUE (district_special_education_aid_id_fk, band),
            CONSTRAINT check_district_special_education_aid_band_cost CHECK (cost >= 0)
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

    # Every year in app/alembic/config/special_education_aid_config.yaml from app/alembic/assets/special-education-aid
    special_education_aid.load(op.get_bind())

    op.execute(
        """
        CREATE MATERIALIZED VIEW district_special_education_aid_summary AS
        WITH bands AS (
            -- What the district pays in full, what the state shares, and the part over 10 times the state average
            SELECT b.district_special_education_aid_id_fk AS aid_id,
                   SUM(b.cost) FILTER (WHERE y.state_share = 0) AS cost_below_threshold,
                   SUM(b.cost) FILTER (WHERE y.state_share > 0) AS cost_above_threshold,
                   SUM(b.cost) FILTER (WHERE y.from_multiple >= 10) AS cost_over_10_times
            FROM district_special_education_aid_band b
            JOIN district_special_education_aid a ON a.id = b.district_special_education_aid_id_fk
            JOIN special_education_aid_band y ON y.fiscal_year = a.fiscal_year AND y.band = b.band
            GROUP BY b.district_special_education_aid_id_fk
        ), reported AS (
            -- "Special Education Aid" in the district's financial report (DOE-25) for the same fiscal year
            SELECT f.district_id_fk, f.year AS fiscal_year, SUM(r.value) AS reported_aid
            FROM revenue r
            JOIN doe_form f ON f.id = r.doe_form_id_fk
            JOIN revenue_entry_type t ON t.id = r.revenue_entry_type_id_fk
            WHERE t.name = 'Special Education Aid'
            GROUP BY f.district_id_fk, f.year
        )
        SELECT a.district_id_fk, a.fiscal_year, y.cost_school_year, a.total_cost,
               b.cost_below_threshold, b.cost_above_threshold, b.cost_over_10_times,
               a.entitlement, a.aid_paid,
               ROUND(a.aid_paid / NULLIF(a.total_cost, 0), 4) AS share_of_cost_paid,
               r.reported_aid, r.reported_aid - a.aid_paid AS reported_difference
        FROM district_special_education_aid a
        JOIN special_education_aid_year y ON y.fiscal_year = a.fiscal_year
        JOIN bands b ON b.aid_id = a.id
        LEFT JOIN reported r ON r.district_id_fk = a.district_id_fk AND r.fiscal_year = a.fiscal_year
        """
    )
    op.execute("CREATE UNIQUE INDEX idx_district_special_education_aid_summary ON district_special_education_aid_summary (district_id_fk, fiscal_year)")

    logger.info("Special education aid migration upgrade completed successfully")


def downgrade():
    for view in VIEWS:
        op.execute(f"DROP MATERIALIZED VIEW IF EXISTS {view}")
    for table in reversed(TABLES):
        op.execute(f"DROP TABLE IF EXISTS {table} CASCADE")
