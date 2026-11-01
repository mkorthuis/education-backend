"""Load Measurement State Targets

Revision ID: 65ab32afd32c
Revises: 21ea12af9faf
Create Date: 2024-04-02 01:33:00.000000

"""
from alembic import op
import sqlalchemy as sa
import pandas as pd
import logging

from app.etl import measurement_state_target
from app.etl.core import config_path, load_config

# Add this near the top of the file
logger = logging.getLogger('alembic.runtime.migration')

# revision identifiers, used by Alembic.
revision = '65ab32afd32c'
down_revision = '21ea12af9faf'
branch_labels = None
depends_on = None


def upgrade():
    """Insert measurement state targets."""
    # Every year in app/alembic/config/state_targets_config.yaml
    measurement_state_target.load(op.get_bind())


def downgrade():
    """Remove all measurement state targets inserted by this migration."""
    conn = op.get_bind()
    
    logger.info("Removing measurement state targets")
    
    # Load configuration and state targets data
    config = load_config(measurement_state_target.CONFIG)
    targets_df = pd.read_csv(config_path(config['file_settings']['state_targets_file']['path']))
    
    # For each row in the dataframe
    for _, row in targets_df.iterrows():
        measurement_type_name = row['measurement_type_name']
        year = row['year']
        
        # Find the measurement type ID
        measurement_type_check = sa.text("""
            SELECT id FROM measurement_type WHERE name = :name
        """)
        
        measurement_type_id = conn.execute(
            measurement_type_check, 
            {"name": measurement_type_name}
        ).scalar()
        
        if not measurement_type_id:
            logger.warning(f"Measurement type '{measurement_type_name}' not found. Skipping.")
            continue
            
        # Delete the target
        delete_stmt = sa.text("""
            DELETE FROM measurement_state_target 
            WHERE measurement_type_id_fk = :type_id AND year = :year
        """)
        
        result = conn.execute(
            delete_stmt, 
            {"type_id": measurement_type_id, "year": year}
        )
        
        logger.info(f"Removed {result.rowcount} state target(s) for '{measurement_type_name}' in {year}")
    
    logger.info("Completed removing measurement state targets")
