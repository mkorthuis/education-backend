"""Current districts and schools

Districts and schools stay in the database after they leave the state's lists (their
history is kept); is_current marks the ones in the latest lists, which the API lists.

Revision ID: a7c4e2f9b1d3
Revises: 8f7e6d5c4b3a
Create Date: 2026-11-01 21:30:00.000000

"""
from alembic import op

from app.etl import location


# revision identifiers, used by Alembic.
revision = 'a7c4e2f9b1d3'
down_revision = '8f7e6d5c4b3a'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("ALTER TABLE district ADD COLUMN is_current BOOLEAN NOT NULL DEFAULT TRUE")
    op.execute("ALTER TABLE school ADD COLUMN is_current BOOLEAN NOT NULL DEFAULT TRUE")
    # The lists were loaded before the column existed; mark the ones the latest lists leave out
    config = location.load_config(location.CONFIG)
    latest = location.read_year(config, int(config['file_settings']['year_end']))
    location.mark_current(op.get_bind(), latest)


def downgrade():
    op.execute("ALTER TABLE school DROP COLUMN is_current")
    op.execute("ALTER TABLE district DROP COLUMN is_current")
