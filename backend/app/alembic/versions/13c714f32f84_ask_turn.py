"""Ask conversations, saved to share by link

Each answered question on Ask a Question, saved so the address /ask/<share_id> shows its conversation:

- ask_turn: the question, the answer as the site showed it, the turn it followed up (parent_id),
  whether it was asked taking more time, the district or school page it came from, and a short
  random share_id for its address. The same question and answer after the same turn share one row
  (fingerprint). Nothing about who asked; kept for a year, like ask_question.

Revision ID: 13c714f32f84
Revises: e08d3d3437f7
Create Date: 2026-11-22 12:00:00.000000

"""
from alembic import op
import logging

logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = '13c714f32f84'
down_revision = 'e08d3d3437f7'
branch_labels = None
depends_on = None


def upgrade():
    logger.info("Creating ask_turn")
    op.execute(
        """
        CREATE TABLE ask_turn (
            id SERIAL PRIMARY KEY,
            share_id VARCHAR(16) NOT NULL UNIQUE,
            parent_id INTEGER REFERENCES ask_turn(id) ON DELETE SET NULL,
            question TEXT NOT NULL,
            answer JSONB NOT NULL,
            deep BOOLEAN NOT NULL DEFAULT FALSE,
            place_kind VARCHAR(10),
            place_id INTEGER,
            fingerprint VARCHAR(64) NOT NULL UNIQUE,
            date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    op.execute("CREATE INDEX idx_ask_turn_date_created ON ask_turn (date_created)")


def downgrade():
    op.execute("DROP TABLE IF EXISTS ask_turn")
