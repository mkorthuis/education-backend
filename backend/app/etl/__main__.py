"""
Load published data into the database.

    python -m app.etl load enrollment --year 2026            # load one year
    python -m app.etl load enrollment --year 2026 --dry-run  # show what would change, write nothing
    python -m app.etl fetch naep                             # download a dataset that comes from an online service

To add a new year: put the file in app/alembic/assets, raise year_end in the dataset's
config, then load that year. Rows are inserted, or updated when they already exist, so
loading the same year twice is safe. The API cache expires after CACHE_DEFAULT_TTL;
restart the web dynos to see new data immediately.
"""
import argparse
import logging
import sys

from app.core.db import engine
from app.etl import (
    assessment,
    census_finance,
    class_size,
    cost_per_pupil,
    early_exit,
    education_freedom_account,
    english_learner,
    enrollment,
    enrollment_type,
    finance,
    graduation_cohort,
    location,
    measurement,
    measurement_state_target,
    naep,
    post_graduation,
    reduced_lunch,
    reference,
    safety,
    staff,
    state_class_size,
    state_expenditure,
    teacher_education,
    teacher_salary,
    teacher_salary_band,
    town_enrollment,
)

DATASETS = {
    "assessment": assessment,
    "census-finance": census_finance,
    "class-size": class_size,
    "cost-per-pupil": cost_per_pupil,
    "early-exit": early_exit,
    "education-freedom-account": education_freedom_account,
    "english-learner": english_learner,
    "enrollment-type": enrollment_type,
    "enrollment": enrollment,
    "finance": finance,
    "graduation-cohort": graduation_cohort,
    "location": location,
    "measurement": measurement,
    "measurement-state-target": measurement_state_target,
    "naep": naep,
    "post-graduation": post_graduation,
    "reduced-lunch": reduced_lunch,
    "reference": reference,
    "safety": safety,
    "staff": staff,
    "state-class-size": state_class_size,
    "state-expenditure": state_expenditure,
    "teacher-education": teacher_education,
    "teacher-salary": teacher_salary,
    "teacher-salary-band": teacher_salary_band,
    "town-enrollment": town_enrollment,
}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="python -m app.etl", description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)
    load = commands.add_parser("load", help="load a dataset")
    load.add_argument("dataset", choices=sorted(DATASETS))
    load.add_argument("--year", type=int, action="append", dest="years",
                      help="year to load (repeatable); default: every configured year")
    load.add_argument("--dry-run", action="store_true", help="report the changes, then roll back")
    fetch = commands.add_parser("fetch", help="download a dataset's files from its online service into app/alembic/assets")
    fetch.add_argument("dataset", choices=sorted(name for name, module in DATASETS.items() if hasattr(module, "fetch")))
    args = parser.parse_args(argv)

    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
    if args.command == "fetch":
        print(f"Saved: {DATASETS[args.dataset].fetch()}")
        return 0
    with engine.connect() as conn:
        transaction = conn.begin()
        try:
            counts = DATASETS[args.dataset].load(conn, args.years)
        except Exception:
            transaction.rollback()
            raise
        if args.dry_run:
            transaction.rollback()
            print(f"Dry run, nothing written: {counts}")
        else:
            transaction.commit()
            print(f"Loaded: {counts}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
