"""
Shared building blocks for loading the state's data files into Postgres.

Used both by the Alembic data migrations (fresh database builds) and by the
`python -m app.etl` command (loading a new year into an existing database).
"""
import logging
import os
from typing import Iterable, Optional, Sequence

import yaml
from sqlalchemy import text
from sqlalchemy.engine import Connection

logger = logging.getLogger("app.etl")

CONFIG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "alembic", "config"))


def load_config(name: str) -> dict:
    """Load a YAML config from app/alembic/config by file name."""
    with open(os.path.join(CONFIG_DIR, name)) as f:
        return yaml.safe_load(f)


def config_path(relative_path: str) -> str:
    """Resolve a path written relative to app/alembic/config (e.g. "../assets/...")."""
    return os.path.abspath(os.path.join(CONFIG_DIR, relative_path))


def configured_years(file_settings: dict, years: Optional[Iterable[int]] = None) -> list:
    """The years to load: the requested ones, checked against the config's range, or the whole range."""
    start, end = int(file_settings["year_start"]), int(file_settings["year_end"])
    if years is None:
        return list(range(start, end + 1))
    years = sorted(set(int(y) for y in years))
    outside = [y for y in years if not start <= y <= end]
    if outside:
        raise ValueError(f"Years {outside} are outside the configured range {start}-{end}; update the config first")
    return years


def year_file(file_settings: dict, year: int) -> str:
    """Path of one year's input file; the config's file pattern uses **** for the year."""
    path = config_path(file_settings["default_input"].replace("****", str(year)))
    if not os.path.exists(path):
        raise FileNotFoundError(f"Input file for {year} not found: {path}")
    return path


def existing_ids(conn: Connection, table: str) -> set:
    """All ids in a lookup table, fetched once instead of checking row by row."""
    return {row[0] for row in conn.execute(text(f"SELECT id FROM {table}"))}


def upsert_rows(
    conn: Connection,
    table: str,
    columns: Sequence[str],
    key_columns: Sequence[str],
    rows: Sequence[tuple],
) -> dict:
    """
    Insert rows, or update them when their key already exists.

    Rows are copied into a temporary table and inserted in the order given, so a
    fresh build assigns ids in the same order as the original one-row-at-a-time
    inserts. Rows whose values are unchanged are left alone. Any database error
    raises; nothing is skipped silently.

    Returns counts of inserted, updated and unchanged rows.
    """
    value_columns = [c for c in columns if c not in key_columns]
    column_list = ", ".join(columns)
    staging = f"_etl_{table}"

    conn.execute(text(
        f"CREATE TEMP TABLE {staging} AS SELECT {column_list} FROM {table} WITH NO DATA"
    ))
    conn.execute(text(f"ALTER TABLE {staging} ADD COLUMN _ord BIGINT"))

    dbapi_connection = conn.connection.dbapi_connection
    with dbapi_connection.cursor() as cursor:
        with cursor.copy(f"COPY {staging} ({column_list}, _ord) FROM STDIN") as copy:
            for ord_, row in enumerate(rows):
                copy.write_row((*row, ord_))

    changed = " OR ".join(f"{table}.{c} IS DISTINCT FROM EXCLUDED.{c}" for c in value_columns)
    updates = ", ".join([f"{c} = EXCLUDED.{c}" for c in value_columns] + ["date_updated = CURRENT_TIMESTAMP"])
    result = conn.execute(text(f"""
        INSERT INTO {table} ({column_list})
        SELECT {column_list} FROM {staging} ORDER BY _ord
        ON CONFLICT ({", ".join(key_columns)}) DO UPDATE SET {updates}
        WHERE {changed}
        RETURNING (xmax = 0) AS inserted
    """))
    flags = [row.inserted for row in result]
    conn.execute(text(f"DROP TABLE {staging}"))

    counts = {"inserted": sum(flags), "updated": len(flags) - sum(flags)}
    counts["unchanged"] = len(rows) - len(flags)
    logger.info(f"{table}: {counts['inserted']} inserted, {counts['updated']} updated, "
                f"{counts['unchanged']} unchanged")
    return counts


def refresh_dependent_views(conn: Connection, table: str) -> list:
    """Refresh the materialized views built on a table, if any exist yet."""
    views = [row[0] for row in conn.execute(text("""
        SELECT DISTINCT v.oid::regclass::text
        FROM pg_depend d
        JOIN pg_rewrite r ON r.oid = d.objid
        JOIN pg_class v ON v.oid = r.ev_class AND v.relkind = 'm'
        WHERE d.refobjid = CAST(:table AS regclass)
    """), {"table": table})]
    for view in views:
        conn.execute(text(f"REFRESH MATERIALIZED VIEW {view}"))
        logger.info(f"Refreshed materialized view {view}")
    return views
