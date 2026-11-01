"""State targets for measurement types (e.g. proficiency goals), from state_targets.csv."""
import logging
import os
from typing import Iterable, Optional

import pandas as pd
from sqlalchemy.engine import Connection

from app.etl.core import config_path, configured_years, load_config, refresh_dependent_views, upsert_rows
from app.etl.measurement import ids_by_name

logger = logging.getLogger("app.etl")

CONFIG = "state_targets_config.yaml"
TABLE = "measurement_state_target"
COLUMNS = ("measurement_type_id_fk", "year", "field")
KEY = ("measurement_type_id_fk", "year")


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """Load the given years (default: every configured year) into measurement_state_target."""
    config = load_config(CONFIG)
    years = configured_years(config["file_settings"], years)
    path = config_path(config["file_settings"]["state_targets_file"]["path"])
    if not os.path.exists(path):
        raise FileNotFoundError(f"Input file not found: {path}")
    df = pd.read_csv(path)
    duplicated = df[df.duplicated(["measurement_type_name", "year"])]
    if not duplicated.empty:
        raise ValueError(f"Duplicate targets in {path}: {duplicated.values.tolist()}")

    type_ids = ids_by_name(conn, "measurement_type")
    rows, unknown_types = [], set()
    for name, year, value in df[["measurement_type_name", "year", "target_value"]].itertuples(index=False):
        if int(year) not in years:
            continue
        if name in type_ids:
            rows.append((type_ids[name], int(year), float(value)))
        else:
            unknown_types.add(name)

    if unknown_types:
        # Targets for types missing from measurement_type are skipped, as the original migration did
        logger.warning(f"Skipped targets for {len(unknown_types)} unknown measurement types: {sorted(unknown_types)}")

    counts = upsert_rows(conn, TABLE, COLUMNS, KEY, rows)
    counts["views_refreshed"] = refresh_dependent_views(conn, TABLE)
    return counts
