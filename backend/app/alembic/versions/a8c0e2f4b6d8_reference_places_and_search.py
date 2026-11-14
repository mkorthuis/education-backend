"""Reference library: shared topics, more kinds of place, search, number tables, and who serves a district

So the town research can be loaded (town/ in the education folder, and recommendations A1, A2, A3,
A5 and A8 there):

- reference_fact: a stable key (file#topic#position), its file and the file's own heading for the
  topic, two more kinds of place (an SAU, a school outside New Hampshire) with at most one place per
  fact, and a full-text search column the Ask's lookup ranks by
- reference_table: the library's number tables (ride times, contract terms, census counts), which
  the loader used to skip
- outside_school: schools outside New Hampshire that its students attend on public tuition
- district_service: where each district's students go for the grades it doesn't run, which the
  lookup follows, so a Jackson question also sees facts about Kennett High and Fryeburg Academy

Topics are now shared across files: one reference_topic row per slug, its facts from every file.

Revision ID: a8c0e2f4b6d8
Revises: d7f9b1c3e5a6
Create Date: 2026-11-13 23:00:00.000000

"""
from alembic import op
import logging

from app.etl import reference

logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = 'a8c0e2f4b6d8'
down_revision = 'd7f9b1c3e5a6'
branch_labels = None
depends_on = None

NEW_TABLES = ("outside_school", "district_service", "reference_table")


def upgrade():
    logger.info("Starting reference places and search migration upgrade")

    op.execute(
        """
        CREATE TABLE outside_school (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            state VARCHAR(2) NOT NULL,
            kind VARCHAR(30) NOT NULL,
            url VARCHAR(500),
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT unique_outside_school_name UNIQUE (name, state),
            CONSTRAINT check_outside_school_kind CHECK (kind IN ('public_district', 'public_school', 'private_academy', 'private_school'))
        )
        """
    )
    op.execute(
        """
        CREATE TABLE district_service (
            id SERIAL PRIMARY KEY,
            district_id_fk INTEGER NOT NULL,
            receiving_district_id_fk INTEGER,
            outside_school_id_fk INTEGER,
            grade_low SMALLINT NOT NULL,
            grade_high SMALLINT NOT NULL,
            arrangement VARCHAR(30) NOT NULL,
            starts DATE,
            ends DATE,
            source_url VARCHAR(1000) NOT NULL,
            note TEXT,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_district_service_district FOREIGN KEY (district_id_fk) REFERENCES district(id),
            CONSTRAINT fk_district_service_receiving FOREIGN KEY (receiving_district_id_fk) REFERENCES district(id),
            CONSTRAINT fk_district_service_outside FOREIGN KEY (outside_school_id_fk) REFERENCES outside_school(id),
            CONSTRAINT check_district_service_one_receiver CHECK (num_nonnulls(receiving_district_id_fk, outside_school_id_fk) = 1),
            CONSTRAINT check_district_service_grades CHECK (grade_low BETWEEN 0 AND 12 AND grade_high BETWEEN grade_low AND 12),
            CONSTRAINT check_district_service_arrangement CHECK (arrangement IN ('tuition_contract', 'area_agreement', 'cooperative', 'choice', 'no_contract'))
        )
        """
    )
    op.execute("CREATE INDEX idx_district_service_district ON district_service(district_id_fk)")

    # Facts: a stable key, where each came from, two more kinds of place, and search
    op.execute("ALTER TABLE reference_topic ALTER COLUMN source_file TYPE VARCHAR(200)")
    op.execute(
        """
        ALTER TABLE reference_fact
            ADD COLUMN fact_key VARCHAR(300),
            ADD COLUMN source_file VARCHAR(200),
            ADD COLUMN section_title VARCHAR(255),
            ADD COLUMN sau_id_fk INTEGER,
            ADD COLUMN outside_school_id_fk INTEGER,
            ADD CONSTRAINT fk_reference_fact_sau FOREIGN KEY (sau_id_fk) REFERENCES sau(id),
            ADD CONSTRAINT fk_reference_fact_outside FOREIGN KEY (outside_school_id_fk) REFERENCES outside_school(id),
            ADD CONSTRAINT check_reference_fact_one_place
                CHECK (num_nonnulls(district_id_fk, town_id_fk, sau_id_fk, outside_school_id_fk) <= 1)
        """
    )
    op.execute(
        """
        ALTER TABLE reference_fact
            ADD COLUMN search TSVECTOR GENERATED ALWAYS AS (
                setweight(to_tsvector('english', COALESCE(section_title, '')), 'B') ||
                setweight(to_tsvector('english', statement), 'A') ||
                setweight(to_tsvector('english', COALESCE(citation, '')), 'C')
            ) STORED
        """
    )
    op.execute("CREATE INDEX idx_reference_fact_search ON reference_fact USING GIN (search)")
    op.execute("CREATE INDEX idx_reference_fact_topic_district ON reference_fact(reference_topic_id_fk, district_id_fk)")
    op.execute("CREATE INDEX idx_reference_fact_town ON reference_fact(town_id_fk)")
    op.execute("CREATE INDEX idx_reference_fact_sau ON reference_fact(sau_id_fk)")
    op.execute("CREATE INDEX idx_reference_fact_outside ON reference_fact(outside_school_id_fk)")

    op.execute(
        """
        CREATE TABLE reference_table (
            id SERIAL PRIMARY KEY,
            slug VARCHAR(100) NOT NULL,
            title VARCHAR(255) NOT NULL,
            source_file VARCHAR(200) NOT NULL,
            unit TEXT,
            period TEXT,
            source TEXT,
            source_url VARCHAR(1000),
            as_of DATE,
            as_of_text TEXT,
            note TEXT,
            reference_topic_id_fk INTEGER,
            district_id_fk INTEGER,
            town_id_fk INTEGER,
            sau_id_fk INTEGER,
            outside_school_id_fk INTEGER,
            columns JSONB NOT NULL,
            rows JSONB NOT NULL,
            display_order INTEGER NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT unique_reference_table_slug UNIQUE (slug),
            CONSTRAINT fk_reference_table_topic FOREIGN KEY (reference_topic_id_fk) REFERENCES reference_topic(id) ON DELETE SET NULL,
            CONSTRAINT fk_reference_table_district FOREIGN KEY (district_id_fk) REFERENCES district(id),
            CONSTRAINT fk_reference_table_town FOREIGN KEY (town_id_fk) REFERENCES town(id),
            CONSTRAINT fk_reference_table_sau FOREIGN KEY (sau_id_fk) REFERENCES sau(id),
            CONSTRAINT fk_reference_table_outside FOREIGN KEY (outside_school_id_fk) REFERENCES outside_school(id),
            CONSTRAINT check_reference_table_one_place
                CHECK (num_nonnulls(district_id_fk, town_id_fk, sau_id_fk, outside_school_id_fk) <= 1)
        )
        """
    )
    op.execute("CREATE INDEX idx_reference_table_topic ON reference_table(reference_topic_id_fk)")

    for table in NEW_TABLES:
        op.execute(
            f"""
            CREATE TRIGGER trigger_update_{table}_timestamp
            BEFORE UPDATE ON {table}
            FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
            """
        )

    # Reload, which fills the new columns, then require them
    reference.load(op.get_bind())
    op.execute(
        """
        ALTER TABLE reference_fact
            ALTER COLUMN fact_key SET NOT NULL,
            ALTER COLUMN source_file SET NOT NULL,
            ALTER COLUMN section_title SET NOT NULL,
            ADD CONSTRAINT unique_reference_fact_key UNIQUE (fact_key)
        """
    )

    logger.info("Reference places and search migration upgrade completed successfully")


def downgrade():
    op.execute("DROP TABLE IF EXISTS reference_table CASCADE")
    op.execute(
        """
        ALTER TABLE reference_fact
            DROP CONSTRAINT IF EXISTS unique_reference_fact_key,
            DROP CONSTRAINT IF EXISTS check_reference_fact_one_place,
            DROP COLUMN IF EXISTS search,
            DROP COLUMN IF EXISTS outside_school_id_fk,
            DROP COLUMN IF EXISTS sau_id_fk,
            DROP COLUMN IF EXISTS section_title,
            DROP COLUMN IF EXISTS source_file,
            DROP COLUMN IF EXISTS fact_key
        """
    )
    op.execute("DROP INDEX IF EXISTS idx_reference_fact_topic_district")
    op.execute("DROP INDEX IF EXISTS idx_reference_fact_town")
    op.execute("DROP TABLE IF EXISTS district_service CASCADE")
    op.execute("DROP TABLE IF EXISTS outside_school CASCADE")
