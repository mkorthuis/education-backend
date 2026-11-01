"""
Data loading (ETL) for the state's published data files.

Each dataset module exposes load(conn, years=None). The Alembic data migrations call
it for every configured year when building a fresh database; `python -m app.etl`
loads specific years into an existing database.
"""
