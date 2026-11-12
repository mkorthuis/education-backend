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
FORMER_SCHOOLS_CONFIG = "former_schools_config.yaml"


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


def whole_number(value) -> Optional[int]:
    """A spreadsheet cell as an int, or None when it is blank or not a whole number."""
    if value is None or isinstance(value, str) and not value.strip():
        return None
    try:
        number = float(value)
    except (TypeError, ValueError):
        return None
    if number != number:  # NaN, pandas' blank cell
        return None
    return int(number) if number == int(number) else None


def existing_ids(conn: Connection, table: str) -> set:
    """All ids in a lookup table, fetched once instead of checking row by row."""
    return {row[0] for row in conn.execute(text(f"SELECT id FROM {table}"))}


def has_column(conn: Connection, table: str, column: str) -> bool:
    """
    Whether a table has a column yet. The migrations that load data call today's loaders, so a
    loader writing a column a later migration adds checks for it first.
    """
    return conn.execute(text("""
        SELECT EXISTS (SELECT 1 FROM information_schema.columns
                       WHERE table_name = :table AND column_name = :column)
    """), {"table": table, "column": column}).scalar()


def known_school_ids(conn: Connection) -> dict:
    """
    The school id for each id the state's files use: every school's own id, plus the old ids of
    schools the state renumbered (renumbered_schools in former_schools_config.yaml), so their
    earlier rows load under the current school.
    """
    ids = {school_id: school_id for school_id in existing_ids(conn, "school")}
    renumbered = load_config(FORMER_SCHOOLS_CONFIG).get("renumbered_schools") or {}
    missing = sorted(new for new in renumbered.values() if new not in ids)
    if missing:
        raise ValueError(f"{FORMER_SCHOOLS_CONFIG} renumbers schools to ids that aren't in the database: {missing}")
    ids.update(renumbered)
    return ids


def lookup_ids(conn: Connection, table: str, key_column: str = "name") -> dict:
    """Map a lookup table's key column (default: name) to its id."""
    return {row[0]: row[1] for row in conn.execute(text(f"SELECT {key_column}, id FROM {table}"))}


def _stage_rows(conn: Connection, table: str, columns: Sequence[str], rows: Sequence[tuple]) -> str:
    """Copy rows into a temporary table shaped like `table`, keeping their order in an _ord column."""
    column_list = ", ".join(columns)
    staging = f"_etl_{table}"
    conn.execute(text(f"DROP TABLE IF EXISTS {staging}"))
    conn.execute(text(f"CREATE TEMP TABLE {staging} AS SELECT {column_list} FROM {table} WITH NO DATA"))
    conn.execute(text(f"ALTER TABLE {staging} ADD COLUMN _ord BIGINT"))

    dbapi_connection = conn.connection.dbapi_connection
    with dbapi_connection.cursor() as cursor:
        with cursor.copy(f"COPY {staging} ({column_list}, _ord) FROM STDIN") as copy:
            for ord_, row in enumerate(rows):
                copy.write_row((*row, ord_))
    return staging


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
    staging = _stage_rows(conn, table, columns, rows)
    same_key = " AND ".join(f"t.{c} = s.{c}" for c in key_columns)

    # Update changed rows, then insert only new ones. (INSERT ... ON CONFLICT would draw an
    # id from the sequence for every row, leaving gaps on each reload of unchanged data.)
    updated = 0
    if value_columns:
        changed = " OR ".join(f"t.{c} IS DISTINCT FROM s.{c}" for c in value_columns)
        updates = ", ".join([f"{c} = s.{c}" for c in value_columns] + ["date_updated = CURRENT_TIMESTAMP"])
        updated = conn.execute(text(
            f"UPDATE {table} t SET {updates} FROM {staging} s WHERE {same_key} AND ({changed})"
        )).rowcount
    inserted = conn.execute(text(f"""
        INSERT INTO {table} ({column_list})
        SELECT {column_list} FROM {staging} s
        WHERE NOT EXISTS (SELECT 1 FROM {table} t WHERE {same_key})
        ORDER BY _ord
    """)).rowcount
    conn.execute(text(f"DROP TABLE {staging}"))

    counts = {"inserted": inserted, "updated": updated}
    counts["unchanged"] = len(rows) - inserted - updated
    logger.info(f"{table}: {counts['inserted']} inserted, {counts['updated']} updated, "
                f"{counts['unchanged']} unchanged")
    return counts


def replace_rows(
    conn: Connection,
    table: str,
    columns: Sequence[str],
    rows: Sequence[tuple],
    where: Optional[str] = None,
    params: Optional[dict] = None,
) -> dict:
    """
    Delete the rows matching `where` (e.g. "year = ANY(:years)"), then insert `rows` in order.

    For tables without a unique key to upsert on. With where=None nothing is deleted,
    which is what a fresh build into an empty table needs. Rows reloaded this way get
    new ids. Any database error raises.

    Returns counts of deleted and inserted rows.
    """
    deleted = 0
    if where is not None:
        deleted = conn.execute(text(f"DELETE FROM {table} WHERE {where}"), params or {}).rowcount
    column_list = ", ".join(columns)
    staging = _stage_rows(conn, table, columns, rows)
    inserted = conn.execute(text(
        f"INSERT INTO {table} ({column_list}) SELECT {column_list} FROM {staging} ORDER BY _ord"
    )).rowcount
    conn.execute(text(f"DROP TABLE {staging}"))

    logger.info(f"{table}: {deleted} deleted, {inserted} inserted")
    return {"deleted": deleted, "inserted": inserted}


def refresh_dependent_views(conn: Connection, table: str) -> list:
    """
    Refresh the materialized views built on a table, if any exist yet.

    A view with a plain unique index (no expressions, no WHERE) is refreshed CONCURRENTLY,
    which lets the API keep reading it while the load runs. Any other view gets a plain
    refresh, which blocks reads of that view until the load commits.
    """
    views = conn.execute(text("""
        SELECT DISTINCT v.oid::regclass::text,
               EXISTS (SELECT 1 FROM pg_index i
                       WHERE i.indrelid = v.oid AND i.indisunique AND i.indisvalid
                         AND i.indpred IS NULL AND i.indexprs IS NULL) AND v.relispopulated
        FROM pg_depend d
        JOIN pg_rewrite r ON r.oid = d.objid
        JOIN pg_class v ON v.oid = r.ev_class AND v.relkind = 'm'
        WHERE d.refobjid = CAST(:table AS regclass)
    """), {"table": table}).all()
    for view, concurrently in views:
        conn.execute(text(f"REFRESH MATERIALIZED VIEW {'CONCURRENTLY ' if concurrently else ''}{view}"))
        logger.info(f"Refreshed materialized view {view}{' concurrently' if concurrently else ''}")
    return [view for view, _ in views]
