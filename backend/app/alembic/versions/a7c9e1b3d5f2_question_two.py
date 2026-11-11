"""Question 2 results by district, SAU and town

Ballot Question 2, required by HB 1300 (2026 chapter 324) at the 2026 and 2028 general elections:
a school property tax cap, adopted by each school district's vote, and a 6% cap on SAU central-office
spending, adopted by each SAU's vote.

- district_question_two: one row per district and election year, with the yes and no votes, the
  yes share, whether the district adopted the school tax cap (60% yes or more), the towns whose votes
  make up its total, and whether the results are official
- sau_question_two: the same per SAU, with whether it adopted the SAU spending cap
- town_question_two: each town's own votes, which decide neither cap on their own

Each has a note where the source's listing needs one. The 2026 results are WMUR's unofficial tally
(see question_two_config.yaml).

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
    logger.info("Starting Question 2 migration upgrade")

    # The place each table is by, and whether its vote decides a cap
    for table, place, decides in (("district_question_two", "district", True), ("sau_question_two", "sau", True),
                                  ("town_question_two", "town", False)):
        op.execute(
            f"""
            CREATE TABLE {table} (
                id SERIAL PRIMARY KEY,
                {place}_id_fk INTEGER NOT NULL,
                year INTEGER NOT NULL,
                yes_votes INTEGER NOT NULL,
                no_votes INTEGER NOT NULL,
                yes_percentage NUMERIC(5,2) NOT NULL,
                {"passed BOOLEAN NOT NULL, towns TEXT," if decides else ""}
                is_official BOOLEAN NOT NULL DEFAULT FALSE,
                note TEXT,
                date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                CONSTRAINT fk_{table}_{place} FOREIGN KEY ({place}_id_fk) REFERENCES {place}(id) ON DELETE CASCADE,
                CONSTRAINT unique_{table}_year UNIQUE ({place}_id_fk, year),
                CONSTRAINT check_{table}_votes CHECK (yes_votes >= 0 AND no_votes >= 0)
            )
            """
        )
        op.execute(f"CREATE INDEX idx_{table}_{place} ON {table}({place}_id_fk)")
        op.execute(
            f"""
            CREATE TRIGGER trigger_update_{table}_timestamp
            BEFORE UPDATE ON {table}
            FOR EACH ROW EXECUTE FUNCTION update_date_updated_column()
            """
        )

    # Every election in app/alembic/config/question_two_config.yaml
    question_two.load(op.get_bind())

    logger.info("Question 2 migration upgrade completed successfully")


def downgrade():
    for table in ("town_question_two", "sau_question_two", "district_question_two"):
        op.execute(f"DROP TABLE IF EXISTS {table} CASCADE")
