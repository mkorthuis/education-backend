"""School Data Load

Revision ID: 2aada939afdc
Revises: 36d545ef85b7
Create Date: 2024-11-21 19:43:20.752323

"""
from alembic import op

from app.etl import location


# revision identifiers, used by Alembic.
revision = '2aada939afdc'
down_revision = 'b4f374d72f78'
branch_labels = None
depends_on = None


def upgrade():
    # Every year in app/alembic/config/generate_schools_config.yaml
    location.load(op.get_bind())


def downgrade():
    pass
