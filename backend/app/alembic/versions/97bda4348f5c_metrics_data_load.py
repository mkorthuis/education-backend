"""Metrics Data Load

Revision ID: 97bda4348f5c
Revises: 2aada939afdc
Create Date: 2024-11-25 12:52:34.621333

"""
from alembic import op

from app.etl import measurement


# revision identifiers, used by Alembic.
revision = '97bda4348f5c'
down_revision = '2aada939afdc'
branch_labels = None
depends_on = None


def upgrade():
    # Measurement categories, types and every workbook in app/alembic/config/generate_metrics_config.yaml
    measurement.load(op.get_bind())


def downgrade():
   pass
