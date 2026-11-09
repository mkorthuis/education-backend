"""Reference library

Cited facts about New Hampshire schools for the Ask to answer rules, terms, research and help
questions from, loaded from the Markdown files in app/alembic/assets/reference:

- reference_topic: a subject such as "What schools must do about bullying", with its kind (rule,
  term, how_it_works, research, programs or local) and a description the Ask chooses topics by
- reference_fact: one cited statement, with its source, the date it was checked, the date to check
  it again, and the district or town it's about, if one

Revision ID: d5f7b9c1e3a4
Revises: c4e6a8b0d2f3
Create Date: 2026-11-09 12:00:00.000000

"""
from alembic import op
import logging

from app.etl import reference

logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = 'd5f7b9c1e3a4'
down_revision = 'c4e6a8b0d2f3'
branch_labels = None
depends_on = None

TABLES = ("reference_topic", "reference_fact")


def upgrade():
    logger.info("Starting reference library migration upgrade")

    op.execute(
        """
        CREATE TABLE reference_topic (
            id SERIAL PRIMARY KEY,
            slug VARCHAR(100) NOT NULL,
            title VARCHAR(255) NOT NULL,
            kind VARCHAR(20) NOT NULL,
            question_type VARCHAR(30) NOT NULL,
            description TEXT NOT NULL,
            summary TEXT,
            source_file VARCHAR(100) NOT NULL,
            display_order INTEGER NOT NULL,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT unique_reference_topic_slug UNIQUE (slug),
            CONSTRAINT check_reference_topic_kind CHECK (kind IN ('rule', 'term', 'how_it_works', 'research', 'programs', 'local'))
        )
        """
    )
    op.execute(
        """
        CREATE TABLE reference_fact (
            id SERIAL PRIMARY KEY,
            reference_topic_id_fk INTEGER NOT NULL,
            position INTEGER NOT NULL,
            statement TEXT NOT NULL,
            citation VARCHAR(500),
            source_url VARCHAR(1000) NOT NULL,
            as_of DATE,
            as_of_text VARCHAR(255) NOT NULL,
            review_by DATE NOT NULL,
            note TEXT,
            district_id_fk INTEGER,
            town_id_fk INTEGER,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_reference_fact_topic FOREIGN KEY (reference_topic_id_fk) REFERENCES reference_topic(id) ON DELETE CASCADE,
            CONSTRAINT fk_reference_fact_district FOREIGN KEY (district_id_fk) REFERENCES district(id),
            CONSTRAINT fk_reference_fact_town FOREIGN KEY (town_id_fk) REFERENCES town(id)
        )
        """
    )
    op.execute("CREATE INDEX idx_reference_fact_topic ON reference_fact(reference_topic_id_fk)")
    op.execute("CREATE INDEX idx_reference_fact_district ON reference_fact(district_id_fk)")
    for table in TABLES:
        op.execute(
            f"""
            CREATE TRIGGER trigger_update_{table}_timestamp
            BEFORE UPDATE ON {table}
            FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
            """
        )

    # Load the files listed in app/alembic/config/reference_config.yaml
    reference.load(op.get_bind())

    logger.info("Reference library migration upgrade completed successfully")


def downgrade():
    for table in reversed(TABLES):
        op.execute(f"DROP TABLE IF EXISTS {table} CASCADE")
