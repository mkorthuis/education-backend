"""Adequacy aid: NH DOE's adequate education grant calculation for each town, and each district's share

From NH DOE's adequacy aid workbooks, FY2020-FY2027 (adequacy_aid_config.yaml):

- adequacy_aid_year: each fiscal year, its status and the DOE's files
- adequacy_aid_component: every part of the calculation in any year, with its unit and role
- adequacy_aid_parameter, adequacy_aid_step: each year's rates and thresholds, and the steps of its calculation,
  with formulas the load checks against the DOE's figures and plain-English explanations
- town_adequacy_aid, state_adequacy_aid: each town's value for each part, as the DOE publishes it, and the DOE's
  statewide totals
- district_adequacy_aid_share: each district's share of each member town's grant and SWEPT

And materialized views for the site: town_adequacy_aid_summary (a town's calculation as columns) and
district_adequacy_aid (a district's grant, SWEPT kept and total aid, beside the adequacy aid it reported in its
financial report). Each has a unique index, so a load refreshes them concurrently.

Revision ID: c2e4a6b8d0f1
Revises: b9d1f3a5c7e8
Create Date: 2026-11-14 18:00:00.000000

"""
from alembic import op
import logging

from app.etl import adequacy_aid

logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = 'c2e4a6b8d0f1'
down_revision = 'b9d1f3a5c7e8'
branch_labels = None
depends_on = None

TABLES = ("adequacy_aid_year", "adequacy_aid_component", "adequacy_aid_parameter", "adequacy_aid_step",
          "town_adequacy_aid", "state_adequacy_aid", "district_adequacy_aid_share")
VIEWS = ("town_adequacy_aid_summary", "district_adequacy_aid")
TIMESTAMPS = """
    date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP"""
# town_adequacy_aid_summary's columns: each a component's value
SUMMARY_COLUMNS = {
    "resident_adm": "resident_adm_base", "base_aid": "base_adequacy_aid",
    "frl_adm": "frl_adm", "frl_aid": "frl_differentiated_aid",
    "sped_adm": "sped_adm", "sped_aid": "sped_differentiated_aid",
    "ell_adm": "ell_adm", "ell_aid": "ell_differentiated_aid",
    "home_education_adm": "home_education_adm", "home_education_aid": "home_education_aid",
    "grade3_reading_adm": "grade3_reading_adm", "grade3_reading_aid": "grade3_reading_differentiated_aid",
    "total_cost": "total_cost_adequate_education", "swept": "swept", "equalized_valuation": "equalized_valuation",
    "extraordinary_need_grant": "extraordinary_need_grant", "fiscal_capacity_disparity_aid": "fiscal_capacity_disparity_aid",
    "preliminary_grant": "preliminary_grant", "adequacy_grant": "adequacy_grant",
}


def _quoted(values):
    return ", ".join(f"'{v}'" for v in values)


def upgrade():
    logger.info("Starting adequacy aid migration upgrade")

    op.execute(
        f"""
        CREATE TABLE adequacy_aid_year (
            id SERIAL PRIMARY KEY,
            fiscal_year SMALLINT NOT NULL,
            school_year VARCHAR(7) NOT NULL,
            status VARCHAR(10) NOT NULL,
            as_of DATE NOT NULL,
            summary_url TEXT NOT NULL,
            split_url TEXT,
            explained_url TEXT,{TIMESTAMPS},
            CONSTRAINT unique_adequacy_aid_year UNIQUE (fiscal_year),
            CONSTRAINT check_adequacy_aid_year_status CHECK (status IN ({_quoted(adequacy_aid.STATUSES)}))
        )
        """
    )
    op.execute(
        f"""
        CREATE TABLE adequacy_aid_component (
            id SERIAL PRIMARY KEY,
            code VARCHAR(60) NOT NULL,
            name VARCHAR(150) NOT NULL,
            description TEXT NOT NULL,
            unit VARCHAR(20) NOT NULL,
            role VARCHAR(20) NOT NULL,
            sort SMALLINT NOT NULL,{TIMESTAMPS},
            CONSTRAINT unique_adequacy_aid_component_code UNIQUE (code),
            CONSTRAINT check_adequacy_aid_component_unit CHECK (unit IN ({_quoted(adequacy_aid.COMPONENT_UNITS)})),
            CONSTRAINT check_adequacy_aid_component_role CHECK (role IN ({_quoted(adequacy_aid.ROLES)}))
        )
        """
    )
    op.execute(
        f"""
        CREATE TABLE adequacy_aid_parameter (
            id SERIAL PRIMARY KEY,
            fiscal_year SMALLINT NOT NULL,
            code VARCHAR(60) NOT NULL,
            name VARCHAR(150) NOT NULL,
            value NUMERIC(18,9) NOT NULL,
            unit VARCHAR(25) NOT NULL,
            citation TEXT NOT NULL,
            source_url TEXT NOT NULL,{TIMESTAMPS},
            CONSTRAINT fk_adequacy_aid_parameter_year FOREIGN KEY (fiscal_year) REFERENCES adequacy_aid_year(fiscal_year) ON DELETE CASCADE,
            CONSTRAINT unique_adequacy_aid_parameter UNIQUE (fiscal_year, code),
            CONSTRAINT check_adequacy_aid_parameter_unit CHECK (unit IN ({_quoted(adequacy_aid.PARAMETER_UNITS)}))
        )
        """
    )
    op.execute(
        f"""
        CREATE TABLE adequacy_aid_step (
            id SERIAL PRIMARY KEY,
            fiscal_year SMALLINT NOT NULL,
            step SMALLINT NOT NULL,
            component_id_fk INTEGER NOT NULL,
            formula TEXT,
            tolerance NUMERIC(10,2) NOT NULL,
            explanation TEXT NOT NULL,
            citation TEXT NOT NULL,{TIMESTAMPS},
            CONSTRAINT fk_adequacy_aid_step_year FOREIGN KEY (fiscal_year) REFERENCES adequacy_aid_year(fiscal_year) ON DELETE CASCADE,
            CONSTRAINT fk_adequacy_aid_step_component FOREIGN KEY (component_id_fk) REFERENCES adequacy_aid_component(id),
            CONSTRAINT unique_adequacy_aid_step UNIQUE (fiscal_year, step),
            CONSTRAINT unique_adequacy_aid_step_component UNIQUE (fiscal_year, component_id_fk)
        )
        """
    )
    op.execute(
        f"""
        CREATE TABLE town_adequacy_aid (
            id SERIAL PRIMARY KEY,
            town_id_fk INTEGER NOT NULL,
            fiscal_year SMALLINT NOT NULL,
            component_id_fk INTEGER NOT NULL,
            value NUMERIC(18,4) NOT NULL,{TIMESTAMPS},
            CONSTRAINT fk_town_adequacy_aid_town FOREIGN KEY (town_id_fk) REFERENCES town(id) ON DELETE CASCADE,
            CONSTRAINT fk_town_adequacy_aid_year FOREIGN KEY (fiscal_year) REFERENCES adequacy_aid_year(fiscal_year) ON DELETE CASCADE,
            CONSTRAINT fk_town_adequacy_aid_component FOREIGN KEY (component_id_fk) REFERENCES adequacy_aid_component(id),
            CONSTRAINT unique_town_adequacy_aid UNIQUE (town_id_fk, fiscal_year, component_id_fk)
        )
        """
    )
    op.execute("CREATE INDEX idx_town_adequacy_aid_year ON town_adequacy_aid(fiscal_year, component_id_fk)")
    op.execute(
        f"""
        CREATE TABLE state_adequacy_aid (
            id SERIAL PRIMARY KEY,
            fiscal_year SMALLINT NOT NULL,
            component_id_fk INTEGER NOT NULL,
            value NUMERIC(18,4) NOT NULL,{TIMESTAMPS},
            CONSTRAINT fk_state_adequacy_aid_year FOREIGN KEY (fiscal_year) REFERENCES adequacy_aid_year(fiscal_year) ON DELETE CASCADE,
            CONSTRAINT fk_state_adequacy_aid_component FOREIGN KEY (component_id_fk) REFERENCES adequacy_aid_component(id),
            CONSTRAINT unique_state_adequacy_aid UNIQUE (fiscal_year, component_id_fk)
        )
        """
    )
    op.execute(
        f"""
        CREATE TABLE district_adequacy_aid_share (
            id SERIAL PRIMARY KEY,
            district_id_fk INTEGER NOT NULL,
            town_id_fk INTEGER NOT NULL,
            fiscal_year SMALLINT NOT NULL,
            adequacy_grant NUMERIC(14,2) NOT NULL,
            swept_retained NUMERIC(14,2) NOT NULL,
            source VARCHAR(10) NOT NULL,{TIMESTAMPS},
            CONSTRAINT fk_district_adequacy_aid_share_district FOREIGN KEY (district_id_fk) REFERENCES district(id) ON DELETE CASCADE,
            CONSTRAINT fk_district_adequacy_aid_share_town FOREIGN KEY (town_id_fk) REFERENCES town(id) ON DELETE CASCADE,
            CONSTRAINT fk_district_adequacy_aid_share_year FOREIGN KEY (fiscal_year) REFERENCES adequacy_aid_year(fiscal_year) ON DELETE CASCADE,
            CONSTRAINT unique_district_adequacy_aid_share UNIQUE (district_id_fk, town_id_fk, fiscal_year),
            CONSTRAINT check_district_adequacy_aid_share_source CHECK (source IN ({_quoted(adequacy_aid.SHARE_SOURCES)}))
        )
        """
    )
    op.execute("CREATE INDEX idx_district_adequacy_aid_share_town ON district_adequacy_aid_share(town_id_fk, fiscal_year)")
    for table in TABLES:
        op.execute(
            f"""
            CREATE TRIGGER trigger_update_{table}_timestamp
            BEFORE UPDATE ON {table}
            FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
            """
        )

    # Every year in app/alembic/config/adequacy_aid_config.yaml from app/alembic/assets/adequacy-aid
    adequacy_aid.load(op.get_bind())

    value = "MAX(a.value) FILTER (WHERE c.code = '{}')"
    columns = ",\n            ".join(f"{value.format(code)} AS {name}" for name, code in SUMMARY_COLUMNS.items())
    op.execute(
        f"""
        CREATE MATERIALIZED VIEW town_adequacy_aid_summary AS
        SELECT a.town_id_fk, a.fiscal_year,
            {columns},
            -- Stabilization, relief aid and other years' programs
            SUM(a.value) FILTER (WHERE c.role = 'added_aid'
                AND c.code NOT IN ('extraordinary_need_grant', 'fiscal_capacity_disparity_aid')) AS other_added_aid,
            SUM(a.value) FILTER (WHERE c.role = 'hold_harmless') AS hold_harmless,
            -- The DOE's total from FY2022; before that, the grant plus SWEPT
            COALESCE({value.format('final_total_state_grant')},
                     {value.format('adequacy_grant')} + {value.format('swept')}) AS total_state_aid,
            GREATEST({value.format('swept')} - {value.format('total_cost_adequate_education')}, 0) AS swept_above_cost
        FROM town_adequacy_aid a JOIN adequacy_aid_component c ON c.id = a.component_id_fk
        GROUP BY a.town_id_fk, a.fiscal_year
        """
    )
    op.execute("CREATE UNIQUE INDEX idx_town_adequacy_aid_summary ON town_adequacy_aid_summary (town_id_fk, fiscal_year)")
    op.execute(
        """
        CREATE MATERIALIZED VIEW district_adequacy_aid AS
        WITH shares AS (
            SELECT district_id_fk, fiscal_year, SUM(adequacy_grant) AS adequacy_grant,
                   SUM(swept_retained) AS swept_retained, COUNT(*) AS member_towns
            FROM district_adequacy_aid_share GROUP BY district_id_fk, fiscal_year
        ), reported AS (
            -- "Adequacy Aid Grant" in the district's financial report (DOE-25) for the same fiscal year
            SELECT f.district_id_fk, f.year AS fiscal_year, SUM(r.value) AS reported_adequacy_grant
            FROM revenue r
            JOIN doe_form f ON f.id = r.doe_form_id_fk
            JOIN revenue_entry_type t ON t.id = r.revenue_entry_type_id_fk
            WHERE t.name = 'Adequacy Aid Grant'
            GROUP BY f.district_id_fk, f.year
        )
        SELECT s.district_id_fk, s.fiscal_year, s.adequacy_grant, s.swept_retained,
               s.adequacy_grant + s.swept_retained AS total_state_aid, s.member_towns,
               r.reported_adequacy_grant, r.reported_adequacy_grant - s.adequacy_grant AS reported_difference
        FROM shares s
        LEFT JOIN reported r ON r.district_id_fk = s.district_id_fk AND r.fiscal_year = s.fiscal_year
        """
    )
    op.execute("CREATE UNIQUE INDEX idx_district_adequacy_aid ON district_adequacy_aid (district_id_fk, fiscal_year)")

    logger.info("Adequacy aid migration upgrade completed successfully")


def downgrade():
    for view in VIEWS:
        op.execute(f"DROP MATERIALIZED VIEW IF EXISTS {view}")
    for table in reversed(TABLES):
        op.execute(f"DROP TABLE IF EXISTS {table} CASCADE")
