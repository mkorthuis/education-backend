"""generate enrollment data

Revision ID: ad0f7f2e3016
Revises: 97bda4348f5c
Create Date: 2025-03-24 20:35:04.769291

"""
from alembic import op

from app.etl import enrollment


# revision identifiers, used by Alembic.
revision = 'ad0f7f2e3016'
down_revision = '97bda4348f5c'
branch_labels = None
depends_on = None


def upgrade():
    # Every year in app/alembic/config/generate_enrollment_config.yaml
    enrollment.load(op.get_bind())


def downgrade():
    # Remove all enrollment data
    op.execute("DELETE FROM school_enrollment")
