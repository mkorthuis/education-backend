"""generate financial data

Revision ID: 21ea12af9faf
Revises: ad0f7f2e3016
Create Date: 2025-03-24 21:19:19.037357

"""
from alembic import op

from app.etl import finance


# revision identifiers, used by Alembic.
revision = '21ea12af9faf'
down_revision = 'ad0f7f2e3016'
branch_labels = None
depends_on = None


def upgrade():
    # Entry/category/fund types and every year in app/alembic/config/generate_finance_config.yaml.
    # The state total tables built from these forms don't exist yet at this point; the loader skips them.
    finance.load(op.get_bind())


def downgrade():
    """Execute the downgrade migration."""
    # Add downgrade logic if needed
    pass
