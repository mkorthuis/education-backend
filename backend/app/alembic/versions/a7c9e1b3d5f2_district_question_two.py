"""District Question 2 results

Ballot Question 2, required by HB 1300 (2026 chapter 324) at the 2026 and 2028 general elections:
a school property tax cap, adopted by each school district's vote, and a 6% cap on SAU central-office
spending, adopted by each SAU's vote.

- district_question_two: one row per district and election year, with the yes and no votes, the
  yes share, whether the district adopted the school tax cap (60% yes or more) and whether the
  results are official. The 2026 results are WMUR's unofficial tally (see question_two_config.yaml).

Revision ID: a7c9e1b3d5f2
Revises: e2a4c6b8d0f1
Create Date: 2026-11-11 12:00:00.000000

"""
from alembic import op
import logging

from app.etl import question_two

logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = 'a7c9e1b3d5f2'
down_revision = 'e2a4c6b8d0f1'
branch_labels = None
depends_on = None


def upgrade():
    logger.info("Starting district Question 2 migration upgrade")

    op.execute(
        """
        CREATE TABLE district_question_two (
            id SERIAL PRIMARY KEY,
            district_id_fk INTEGER NOT NULL,
            year INTEGER NOT NULL,
            yes_votes INTEGER NOT NULL,
            no_votes INTEGER NOT NULL,
            yes_percentage NUMERIC(5,2) NOT NULL,
            passed BOOLEAN NOT NULL,
            is_official BOOLEAN NOT NULL DEFAULT FALSE,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            CONSTRAINT fk_district_question_two_district FOREIGN KEY (district_id_fk) REFERENCES district(id) ON DELETE CASCADE,
            CONSTRAINT unique_district_question_two_year UNIQUE (district_id_fk, year),
            CONSTRAINT check_district_question_two_votes CHECK (yes_votes >= 0 AND no_votes >= 0)
        )
        """
    )
    op.execute("CREATE INDEX idx_district_question_two_district ON district_question_two(district_id_fk)")
    op.execute(
        """
        CREATE TRIGGER trigger_update_district_question_two_timestamp
        BEFORE UPDATE ON district_question_two
        FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
        """
    )

    # Every election in app/alembic/config/question_two_config.yaml
    question_two.load(op.get_bind())

    logger.info("District Question 2 migration upgrade completed successfully")


def downgrade():
    op.execute("DROP TABLE IF EXISTS district_question_two CASCADE")
