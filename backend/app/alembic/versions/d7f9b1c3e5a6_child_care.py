"""Licensed child care programs

From NH DHHS's Child Care Search (child_care_config.yaml):

- Lookups: child_care_program_type (the search's types of care), child_care_quality_rating,
  child_care_region (DHHS's 7 child care regions, by their number; not the region table's school
  regions), county, child_care_license_status, child_care_availability and child_care_feature_category,
  from the config's fixed lists; child_care_review_type and child_care_feature, added as they appear
- child_care_program: one row per program with its latest details: license, ages, contact, town
- child_care_program_snapshot: each download's license status, capacity, availability and vacancies
  for each program
- child_care_program_hours, child_care_program_rate: the hours and rates on each program's latest
  page. A page can have several schedules, each with its own days, hours and rates; they have no
  names, so each different one is numbered (schedule)
- child_care_program_feature_xref: each program's license types and its latest page's lists
- child_care_inspection: the licensing visits on its pages, kept from every saved download

And three views adding up each download's programs: town_child_care, district_child_care (a town's
programs count toward the district that teaches its kindergarten, so a town in an elementary and a
cooperative district counts once) and state_child_care. They're plain views: there are under a
thousand programs, and the district view follows the current town-district links.

Revision ID: d7f9b1c3e5a6
Revises: c6e8a0b2d4f7
Create Date: 2026-11-13 21:30:00.000000

"""
from alembic import op
import logging

from app.etl import child_care

logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = 'd7f9b1c3e5a6'
down_revision = 'c6e8a0b2d4f7'
branch_labels = None
depends_on = None

# The lookup tables with only a name, and its length
LOOKUPS = {"child_care_quality_rating": 30, "child_care_region": 100, "county": 50, "child_care_license_status": 30,
           "child_care_availability": 100, "child_care_review_type": 50}
TABLES = ("child_care_program_type", *LOOKUPS, "child_care_feature_category", "child_care_feature", "child_care_program", "child_care_program_snapshot",
          "child_care_program_hours", "child_care_program_rate", "child_care_program_feature_xref", "child_care_inspection")
AGE_GROUPS = "('Infant', 'Toddler', 'Preschool', 'School Age')"
VIEWS = ("town_child_care", "district_child_care", "state_child_care")
TIMESTAMPS = """
    date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP"""
# Each view's totals for a group of programs in one download
TOTALS = """
    COUNT(*) AS programs,
    SUM(s.capacity) AS capacity,
    COUNT(*) FILTER (WHERE t.is_licensed) AS licensed_programs,
    COALESCE(SUM(s.capacity) FILTER (WHERE t.is_licensed), 0) AS licensed_capacity,
    SUM(s.infant_capacity) AS infant_capacity,
    SUM(s.toddler_capacity) AS toddler_capacity,
    COUNT(*) FILTER (WHERE p.infant) AS infant_programs,
    COUNT(*) FILTER (WHERE p.toddler) AS toddler_programs,
    COUNT(*) FILTER (WHERE p.preschool) AS preschool_programs,
    COUNT(*) FILTER (WHERE p.school_age) AS school_age_programs,
    SUM(s.infant_vacancies) AS infant_vacancies,
    SUM(s.toddler_vacancies) AS toddler_vacancies,
    SUM(s.preschool_vacancies) AS preschool_vacancies,
    SUM(s.school_age_vacancies) AS school_age_vacancies"""
PROGRAMS = """
    child_care_program_snapshot s
    JOIN child_care_program p ON p.id = s.program_id_fk
    JOIN child_care_program_type t ON t.id = p.program_type_id_fk"""


def upgrade():
    logger.info("Starting child care migration upgrade")

    op.execute(
        f"""
        CREATE TABLE child_care_program_type (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            is_licensed BOOLEAN NOT NULL,{TIMESTAMPS},
            CONSTRAINT unique_child_care_program_type_name UNIQUE (name)
        )
        """
    )
    for table, length in LOOKUPS.items():
        op.execute(
            f"""
            CREATE TABLE {table} (
                id SERIAL PRIMARY KEY,
                name VARCHAR({length}) NOT NULL,{TIMESTAMPS},
                CONSTRAINT unique_{table}_name UNIQUE (name)
            )
            """
        )
    op.execute(
        f"""
        CREATE TABLE child_care_feature_category (
            id SERIAL PRIMARY KEY,
            code VARCHAR(30) NOT NULL,
            name VARCHAR(100) NOT NULL,{TIMESTAMPS},
            CONSTRAINT unique_child_care_feature_category_code UNIQUE (code),
            CONSTRAINT unique_child_care_feature_category_name UNIQUE (name)
        )
        """
    )
    op.execute(
        f"""
        CREATE TABLE child_care_feature (
            id SERIAL PRIMARY KEY,
            category_id_fk INTEGER NOT NULL,
            name VARCHAR(255) NOT NULL,{TIMESTAMPS},
            CONSTRAINT fk_child_care_feature_category FOREIGN KEY (category_id_fk) REFERENCES child_care_feature_category(id),
            CONSTRAINT unique_child_care_feature UNIQUE (category_id_fk, name)
        )
        """
    )
    op.execute(
        f"""
        CREATE TABLE child_care_program (
            id SERIAL PRIMARY KEY,
            source_id VARCHAR(18) NOT NULL,
            provider_number VARCHAR(20) NOT NULL,
            name VARCHAR(255) NOT NULL,
            program_type_id_fk INTEGER NOT NULL,
            license_issue_date DATE,
            license_expiration_date DATE,
            min_age_months NUMERIC(5,1),
            max_age_months NUMERIC(5,1),
            infant BOOLEAN,
            toddler BOOLEAN,
            preschool BOOLEAN,
            school_age BOOLEAN,
            age_groups_source VARCHAR(10),
            head_start BOOLEAN,
            early_head_start BOOLEAN,
            accepts_scholarship BOOLEAN NOT NULL,
            preventive_protective_care BOOLEAN,
            quality_rating_id_fk INTEGER,
            gsq_step SMALLINT,
            issued_to VARCHAR(255),
            main_contact VARCHAR(255),
            phone VARCHAR(50),
            email VARCHAR(255),
            email_hidden BOOLEAN,
            street VARCHAR(255),
            city VARCHAR(100),
            zip VARCHAR(10),
            town_id_fk INTEGER,
            county_id_fk INTEGER,
            region_id_fk INTEGER,
            mailing_street VARCHAR(255),
            mailing_city VARCHAR(100),
            mailing_zip VARCHAR(10),
            latitude NUMERIC(9,6),
            longitude NUMERIC(9,6),
            details_updated DATE,
            is_current BOOLEAN NOT NULL,{TIMESTAMPS},
            CONSTRAINT fk_child_care_program_type FOREIGN KEY (program_type_id_fk) REFERENCES child_care_program_type(id),
            CONSTRAINT fk_child_care_program_quality_rating FOREIGN KEY (quality_rating_id_fk) REFERENCES child_care_quality_rating(id),
            CONSTRAINT fk_child_care_program_town FOREIGN KEY (town_id_fk) REFERENCES town(id),
            CONSTRAINT fk_child_care_program_county FOREIGN KEY (county_id_fk) REFERENCES county(id),
            CONSTRAINT fk_child_care_program_region FOREIGN KEY (region_id_fk) REFERENCES child_care_region(id),
            CONSTRAINT unique_child_care_program_source_id UNIQUE (source_id),
            CONSTRAINT unique_child_care_program_provider_number UNIQUE (provider_number),
            CONSTRAINT check_child_care_program_age_groups_source CHECK (age_groups_source IN ('listed', 'license', 'age_range')),
            CONSTRAINT check_child_care_program_gsq_step CHECK (gsq_step BETWEEN 0 AND 4)
        )
        """
    )
    op.execute("CREATE INDEX idx_child_care_program_town ON child_care_program(town_id_fk)")
    op.execute(
        f"""
        CREATE TABLE child_care_program_snapshot (
            id SERIAL PRIMARY KEY,
            program_id_fk INTEGER NOT NULL,
            as_of DATE NOT NULL,
            license_status_id_fk INTEGER,
            capacity INTEGER NOT NULL,
            infant_capacity INTEGER,
            toddler_capacity INTEGER,
            availability_id_fk INTEGER,
            infant_vacancies INTEGER,
            toddler_vacancies INTEGER,
            preschool_vacancies INTEGER,
            school_age_vacancies INTEGER,
            vacancies_updated DATE,{TIMESTAMPS},
            CONSTRAINT fk_child_care_program_snapshot_program FOREIGN KEY (program_id_fk) REFERENCES child_care_program(id) ON DELETE CASCADE,
            CONSTRAINT fk_child_care_program_snapshot_license_status FOREIGN KEY (license_status_id_fk) REFERENCES child_care_license_status(id),
            CONSTRAINT fk_child_care_program_snapshot_availability FOREIGN KEY (availability_id_fk) REFERENCES child_care_availability(id),
            CONSTRAINT unique_child_care_program_snapshot UNIQUE (program_id_fk, as_of),
            CONSTRAINT check_child_care_program_snapshot_capacity CHECK (capacity >= 0)
        )
        """
    )
    op.execute("CREATE INDEX idx_child_care_program_snapshot_as_of ON child_care_program_snapshot(as_of)")
    op.execute(
        f"""
        CREATE TABLE child_care_program_hours (
            id SERIAL PRIMARY KEY,
            program_id_fk INTEGER NOT NULL,
            schedule SMALLINT NOT NULL DEFAULT 1,
            day_of_week SMALLINT NOT NULL,
            opens TIME,
            closes TIME,{TIMESTAMPS},
            CONSTRAINT fk_child_care_program_hours_program FOREIGN KEY (program_id_fk) REFERENCES child_care_program(id) ON DELETE CASCADE,
            CONSTRAINT unique_child_care_program_hours UNIQUE (program_id_fk, schedule, day_of_week, opens, closes),
            CONSTRAINT check_child_care_program_hours_day CHECK (day_of_week BETWEEN 1 AND 7)
        )
        """
    )
    op.execute(
        f"""
        CREATE TABLE child_care_program_rate (
            id SERIAL PRIMARY KEY,
            program_id_fk INTEGER NOT NULL,
            schedule SMALLINT NOT NULL DEFAULT 1,
            age_group VARCHAR(20) NOT NULL,
            period VARCHAR(10) NOT NULL,
            amount NUMERIC(8,2) NOT NULL,{TIMESTAMPS},
            CONSTRAINT fk_child_care_program_rate_program FOREIGN KEY (program_id_fk) REFERENCES child_care_program(id) ON DELETE CASCADE,
            CONSTRAINT unique_child_care_program_rate UNIQUE (program_id_fk, schedule, age_group, period),
            CONSTRAINT check_child_care_program_rate_age_group CHECK (age_group IN {AGE_GROUPS}),
            CONSTRAINT check_child_care_program_rate_period CHECK (period IN ('hourly', 'daily', 'weekly', 'monthly'))
        )
        """
    )
    op.execute(
        f"""
        CREATE TABLE child_care_program_feature_xref (
            id SERIAL PRIMARY KEY,
            program_id_fk INTEGER NOT NULL,
            feature_id_fk INTEGER NOT NULL,{TIMESTAMPS},
            CONSTRAINT fk_child_care_program_feature_program FOREIGN KEY (program_id_fk) REFERENCES child_care_program(id) ON DELETE CASCADE,
            CONSTRAINT fk_child_care_program_feature_feature FOREIGN KEY (feature_id_fk) REFERENCES child_care_feature(id),
            CONSTRAINT unique_child_care_program_feature_xref UNIQUE (program_id_fk, feature_id_fk)
        )
        """
    )
    op.execute(
        f"""
        CREATE TABLE child_care_inspection (
            id SERIAL PRIMARY KEY,
            program_id_fk INTEGER NOT NULL,
            visit_id VARCHAR(18),
            review_date DATE NOT NULL,
            review_type_id_fk INTEGER,
            items_reviewed INTEGER,
            items_compliant INTEGER,
            document_url TEXT,{TIMESTAMPS},
            CONSTRAINT fk_child_care_inspection_program FOREIGN KEY (program_id_fk) REFERENCES child_care_program(id) ON DELETE CASCADE,
            CONSTRAINT fk_child_care_inspection_review_type FOREIGN KEY (review_type_id_fk) REFERENCES child_care_review_type(id),
            CONSTRAINT unique_child_care_inspection_visit UNIQUE (visit_id)
        )
        """
    )
    op.execute("CREATE INDEX idx_child_care_program_feature_feature ON child_care_program_feature_xref(feature_id_fk)")
    op.execute("CREATE INDEX idx_child_care_inspection_program ON child_care_inspection(program_id_fk)")
    for table in TABLES:
        op.execute(
            f"""
            CREATE TRIGGER trigger_update_{table}_timestamp
            BEFORE UPDATE ON {table}
            FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
            """
        )

    op.execute(
        f"""
        CREATE VIEW town_child_care AS
        SELECT p.town_id_fk, s.as_of,{TOTALS}
        FROM {PROGRAMS}
        WHERE p.town_id_fk IS NOT NULL
        GROUP BY p.town_id_fk, s.as_of
        """
    )
    op.execute(
        f"""
        CREATE VIEW district_child_care AS
        WITH town_district AS (
            -- Each town's district for young children: the one that teaches kindergarten, when a town
            -- is in an elementary district and a cooperative one (Amherst and Souhegan)
            SELECT DISTINCT ON (x.town_id_fk) x.town_id_fk, x.district_id_fk
            FROM town_district_xref x
            ORDER BY x.town_id_fk,
                     EXISTS (SELECT 1 FROM district_grade_xref g JOIN grades k ON k.id = g.grade_id_fk
                             WHERE g.district_id_fk = x.district_id_fk AND k.name = 'Kindergarten') DESC,
                     x.district_id_fk
        )
        SELECT d.district_id_fk, s.as_of,{TOTALS}
        FROM {PROGRAMS}
        JOIN town_district d ON d.town_id_fk = p.town_id_fk
        GROUP BY d.district_id_fk, s.as_of
        """
    )
    op.execute(
        f"""
        CREATE VIEW state_child_care AS
        SELECT s.as_of,{TOTALS}
        FROM {PROGRAMS}
        GROUP BY s.as_of
        """
    )

    # Every download in app/alembic/config/child_care_config.yaml from app/alembic/assets/child-care
    child_care.load(op.get_bind())

    logger.info("Child care migration upgrade completed successfully")


def downgrade():
    for view in VIEWS:
        op.execute(f"DROP VIEW IF EXISTS {view}")
    for table in reversed(TABLES):
        op.execute(f"DROP TABLE IF EXISTS {table} CASCADE")
