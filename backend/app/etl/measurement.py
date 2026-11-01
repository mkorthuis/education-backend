"""
School and district metrics (measurement types and values), from the state's "school metrics" workbooks.

No later migration renames or reshapes the measurement tables, so the migration and
the `python -m app.etl` command run the same code against the same table names.
"""
import logging
import os
import re
from collections import Counter
from decimal import Decimal
from typing import Iterable, Optional

import pandas as pd
from sqlalchemy import text
from sqlalchemy.engine import Connection

from app.etl.core import (
    config_path, configured_years, existing_ids, load_config, refresh_dependent_views, replace_rows
)

logger = logging.getLogger("app.etl")

CONFIG = "generate_metrics_config.yaml"
TABLE = "measurement"
COLUMNS = ("school_id_fk", "district_id_fk", "measurement_type_id_fk", "year", "field")


def ids_by_name(conn: Connection, table: str) -> dict:
    """Map name to id in a lookup table without a unique name, refusing duplicate names."""
    rows = conn.execute(text(f"SELECT name, id FROM {table}")).all()
    ids = dict(rows)
    if len(ids) != len(rows):
        raise ValueError(f"{table} has duplicate names; cannot look rows up by name")
    return ids


def clean_value(value, config: dict) -> Optional[Decimal]:
    """A cell's number with %, $, <, > and spaces stripped; None for blanks and suppressed values."""
    special = config["special_values"]
    if pd.isna(value) or value == "" or value in special["null_values"]:
        return None
    value_str = str(value)
    if any(pattern in value_str for pattern in special["skip_patterns"]):
        return None
    # "<10.00%" and ">90.00%" keep only the number; elsewhere a minus sign is kept
    cleaned = re.sub(r"[^0-9.]" if value_str.startswith(("<", ">")) else r"[^0-9.-]", "", value_str)
    return Decimal(cleaned) if cleaned else None


def parse_types(df: pd.DataFrame, config: dict) -> tuple:
    """
    Category names, and (type name, category name) pairs grouped by category, in file order.

    The category is written on the first row of its section only, so an indicator
    belongs to the last category seen above it.
    """
    columns = config["column_mappings"]
    category_column, indicator_column = columns["indicator_category"], columns["indicator_name"]
    categories = {category: {} for category in df[category_column].dropna().unique()}

    current_category = None
    pairs = df[[category_column, indicator_column]].dropna(subset=[indicator_column]).drop_duplicates()
    for category, indicator in pairs.itertuples(index=False):
        if pd.notna(category):
            current_category = category
        if current_category is not None:
            categories[current_category][indicator] = None

    types = [(indicator, category) for category, indicators in categories.items() for indicator in indicators]
    duplicated = sorted(name for name, count in Counter(name for name, _ in types).items() if count > 1)
    if duplicated:
        raise ValueError(f"Indicators listed under more than one category: {duplicated}")
    return list(categories), types


def parse_values(df: pd.DataFrame, years: list, config: dict, entities: dict) -> None:
    """
    Add one workbook's (indicator, year, value) entries to `entities`, grouped by entity in order of first appearance.

    Indicator and entity type are written on the first row of their section only and
    carry down. Entities are keyed on the Entity ID cell as read, which sets the insert
    order: the 2024 workbook stores IDs as decimals ("15.0") and the older ones as
    integers ("15"), so its entities are not grouped with the older files' ones.
    """
    columns = config["column_mappings"]
    missing = [year for year in years if str(year) not in df.columns]
    if missing:
        raise ValueError(f"Year columns {missing} not found in the workbook")

    current_indicator = current_type = None
    for _, row in df.iterrows():
        entity_id, entity_type = row[columns["entity_id"]], row[columns["entity_type"]]
        if pd.notna(row[columns["indicator_name"]]):
            current_indicator = row[columns["indicator_name"]]
        if pd.notna(entity_type):
            current_type = str(entity_type).lower()
        if current_indicator is None or pd.isna(entity_id) or current_type is None:
            continue

        entity = entities.setdefault(str(entity_id), {"type": current_type, "values": []})
        if entity["type"] != current_type:
            raise ValueError(f"Entity ID {entity_id} is listed both as a {entity['type']} and a {current_type}")
        for year in years:
            value = clean_value(row[str(year)], config)
            if value is not None:
                entity["values"].append((current_indicator, year, value))


def add_missing_types(conn: Connection, categories: list, types: list) -> dict:
    """Insert the categories and types not in the database yet, in file order. Existing ones are kept."""
    known = ids_by_name(conn, "measurement_type_category")
    added = replace_rows(conn, "measurement_type_category", ("name",),
                         [(name,) for name in categories if name not in known])
    category_ids = ids_by_name(conn, "measurement_type_category")
    known = ids_by_name(conn, "measurement_type")
    added_types = replace_rows(conn, "measurement_type", ("name", "measurement_type_category_id_fk"),
                               [(name, category_ids[category]) for name, category in types if name not in known])
    return {"categories_inserted": added["inserted"], "types_inserted": added_types["inserted"]}


def load(conn: Connection, years: Optional[Iterable[int]] = None) -> dict:
    """
    Load the given years (default: every configured year) into measurement, adding new categories and types.

    measurement has no unique key covering both school and district rows (district rows
    have a NULL school_id_fk and the reverse), so the loaded years are deleted and
    inserted again, in the original order.
    """
    config = load_config(CONFIG)
    years = configured_years(config["file_settings"], years)
    files = [f for f in config["file_settings"]["files"] if set(f["years"]) & set(years)]
    unconfigured = sorted(set(years) - {year for f in files for year in f["years"]})
    if unconfigured:
        raise ValueError(f"No workbook configured for years {unconfigured}")

    categories, types, entities = {}, {}, {}
    for file in files:
        path = config_path(file["path"])
        if not os.path.exists(path):
            raise FileNotFoundError(f"Input file not found: {path}")
        df = pd.read_excel(path)
        file_categories, file_types = parse_types(df, config)
        categories.update(dict.fromkeys(file_categories))
        for name, category in file_types:
            types.setdefault(name, category)
        parse_values(df, [year for year in file["years"] if year in years], config, entities)

    counts = add_missing_types(conn, list(categories), list(types.items()))
    type_ids = ids_by_name(conn, "measurement_type")
    known = {"school": existing_ids(conn, "school"), "district": existing_ids(conn, "district")}

    rows, skipped = [], {}
    for key, entity in entities.items():
        entity_id = int(float(key))
        if entity_id not in known.get(entity["type"], ()):
            # Schools and districts missing from their tables (and other entity types) are skipped,
            # as the original migration did
            skipped_ids = skipped.setdefault(entity["type"], {})
            skipped_ids[entity_id] = skipped_ids.get(entity_id, 0) + len(entity["values"])
            continue
        school_id = entity_id if entity["type"] == "school" else None
        district_id = entity_id if entity["type"] == "district" else None
        for indicator, year, value in entity["values"]:
            rows.append((school_id, district_id, type_ids[indicator], year, value))

    for entity_type, skipped_ids in skipped.items():
        skipped_ids = {k: v for k, v in skipped_ids.items() if v}
        if skipped_ids:
            logger.warning(f"Skipped {sum(skipped_ids.values())} values for {len(skipped_ids)} unknown "
                           f"{entity_type} ids: {sorted(skipped_ids)}")

    counts.update(replace_rows(conn, TABLE, COLUMNS, rows, where="year = ANY(:years)", params={"years": years}))
    counts["views_refreshed"] = refresh_dependent_views(conn, TABLE)
    return counts
