"""
NH DOE's statewide average class size for all grades, from iExplore's Compare view, into
state_class_size.all_grades. The same table's grade band averages come from the class size
reports (the class-size dataset); this only fills in the all-grades figure.
"""
import logging
from typing import Iterable, Optional

import pandas as pd
from sqlalchemy.engine import Connection

from app.etl.core import config_path, configured_years, load_config, refresh_dependent_views, upsert_rows

logger = logging.getLogger("app.etl")

CONFIG = "state_average_class_size_config.yaml"
TABLE = "state_class_size"


def parse_file(df: pd.DataFrame, config: dict) -> dict:
    """{year: average class size} from one Compare export's Average Class Size rows."""
    columns = config["columns"]
    missing = [name for name in columns.values() if name not in df.columns]
    if missing:
        raise ValueError(f"Columns not in the export: {missing}")
    rows = df[df[columns["indicator"]].astype(str).str.strip() == config["indicator"]]
    values = {}
    for _, row in rows.iterrows():
        value = pd.to_numeric(row[columns["state"]], errors="coerce")
        if pd.notna(value):
            values[int(row[columns["year"]])] = round(float(value), 2)
    return values


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """
    Load the given years (default: every configured year) into state_class_size.all_grades.

    A year with no row yet (no grade band averages loaded) gets one with just this figure.
    """
    config = load_config(CONFIG)
    years = set(configured_years(config["file_settings"], years))

    values = {}
    for file in config["file_settings"]["files"]:
        first, last = file["year_range"]
        if not years & set(range(first, last + 1)):
            continue
        df = pd.read_csv(config_path(file["path"]), sep="\t", encoding="utf-16")
        # Each file supplies only its own years; later files win where they overlap
        values.update({year: value for year, value in parse_file(df, config).items() if first <= year <= last and year in years})

    missing = sorted(years - set(values))
    if missing:
        logger.warning(f"State average class size: no value for years {missing}")
    rows = sorted(values.items())
    counts = upsert_rows(conn, TABLE, ("year", "all_grades"), ("year",), rows)
    counts["views_refreshed"] = refresh_dependent_views(conn, TABLE)
    return {TABLE: counts}
