"""Ask question log

Every question asked on Ask a Question, so we can see what visitors ask and how the answers do:

- ask_question: the question's text, the earlier questions on the page it may follow up, whether it
  was asked taking more time, whether it came from the saved answers, its outcome and how long a
  new answer took. Nothing about who asked.

Revision ID: e2a4c6b8d0f1
Revises: d5f7b9c1e3a4
Create Date: 2026-11-09 20:00:00.000000

"""
from alembic import op
import logging

logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = 'e2a4c6b8d0f1'
down_revision = 'd5f7b9c1e3a4'
branch_labels = None
depends_on = None


def upgrade():
    logger.info("Starting ask question log migration upgrade")
    op.execute(
        """
        CREATE TABLE ask_question (
            id SERIAL PRIMARY KEY,
            question TEXT NOT NULL,
            earlier_questions JSONB NOT NULL DEFAULT '[]',
            deep BOOLEAN NOT NULL,
            cached BOOLEAN NOT NULL DEFAULT FALSE,
            status VARCHAR(20) NOT NULL DEFAULT 'asked',
            seconds DOUBLE PRECISION,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    op.execute("CREATE INDEX idx_ask_question_date_created ON ask_question (date_created)")
    logger.info("Completed ask question log migration upgrade")


def downgrade():
    logger.info("Starting ask question log migration downgrade")
    op.execute("DROP TABLE IF EXISTS ask_question")
    logger.info("Completed ask question log migration downgrade")
