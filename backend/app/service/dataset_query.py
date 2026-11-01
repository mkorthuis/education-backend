"""
Shared query helper for datasets stored as one table per level (school, district, state).

Safety, staff and outcome data all follow the same shape: a data table per level with a
year, some value columns and, optionally, a lookup "type" table returned as a nested
{id, name, ...} object. Each dataset is described once with a Dataset, and fetch_dataset
builds the query and returns plain response dicts.
"""
from dataclasses import dataclass, field
from typing import List, Optional
import logging

from fastapi import HTTPException
from sqlmodel import Session, select

from app.model.location import School, District

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Dataset:
    """One dataset: its table at each level and the fields it returns."""
    tables: dict                             # level ("school", "district", "state") -> table model
    value_fields: tuple                      # response fields; ("response_name", "column") when they differ
    label: str                               # error text: "Failed to fetch {level} {label}"
    level_labels: dict = field(default_factory=dict)  # per-level error text, when it isn't "{level} {label}"
    type_model: Optional[type] = None        # lookup table joined in for the nested type object
    type_fk: Optional[str] = None            # column on the data tables pointing at type_model
    type_key: Optional[str] = None           # response field holding the nested type object
    type_fields: tuple = ("id", "name")      # type_model columns returned in the nested object
    type_join_first: bool = False            # join the type table before the location table
    join_district: bool = True               # district-level queries join District


def fail(label: str) -> HTTPException:
    logger.exception(f"Error fetching {label}")
    return HTTPException(status_code=500, detail=f"Failed to fetch {label}")


def list_types(session: Session, type_model, label: str, fields: tuple = ("id", "name")) -> List[dict]:
    """Get all rows of a lookup table, ordered by name"""
    try:
        statement = select(*(getattr(type_model, f) for f in fields)).order_by(type_model.name)
        return [dict(row) for row in session.exec(statement).mappings()]
    except Exception:
        raise fail(label)


def fetch_dataset(
    session: Session,
    dataset: Dataset,
    level: str,
    year: Optional[int] = None,
    school_id: Optional[int] = None,
    district_id: Optional[int] = None,
    type_id: Optional[int] = None
) -> List[dict]:
    """
    Get one dataset at one level as response dicts.

    Selects only the columns the response needs. The joins and filters match the
    original hand-written queries, so the query plan and row order are unchanged.
    """
    model = dataset.tables[level]
    label = dataset.level_labels.get(level, f"{level} {dataset.label}")

    try:
        columns = []
        if hasattr(model, "id"):
            columns.append(model.id)
        if level == "school":
            columns.append(model.school_id_fk.label("school_id"))
        elif level == "district":
            columns.append(model.district_id_fk.label("district_id"))
        columns.append(model.year)
        for value_field in dataset.value_fields:
            name, column = value_field if isinstance(value_field, tuple) else (value_field, value_field)
            columns.append(getattr(model, column).label(name))
        if dataset.type_model is not None:
            columns.extend(getattr(dataset.type_model, f).label(f"_type_{f}") for f in dataset.type_fields)

        location_join = None
        if level == "school":
            location_join = (School, model.school_id_fk == School.id)
        elif level == "district" and dataset.join_district:
            location_join = (District, model.district_id_fk == District.id)
        type_join = None
        if dataset.type_model is not None:
            type_fk = getattr(model, dataset.type_fk)
            type_join = (dataset.type_model, type_fk == dataset.type_model.id)

        statement = select(*columns).select_from(model)
        joins = [type_join, location_join] if dataset.type_join_first else [location_join, type_join]
        for join in joins:
            if join is not None:
                statement = statement.join(*join)

        if year is not None:
            statement = statement.where(model.year == year)
        if school_id is not None:
            statement = statement.where(model.school_id_fk == school_id)
        if district_id is not None:
            if level == "school":
                statement = statement.where(School.district_id_fk == district_id)
            else:
                statement = statement.where(model.district_id_fk == district_id)
        if type_id is not None:
            statement = statement.where(type_fk == type_id)

        rows = []
        for row in session.exec(statement).mappings():
            data = dict(row)
            if dataset.type_model is not None:
                data[dataset.type_key] = {f: data.pop(f"_type_{f}") for f in dataset.type_fields}
            rows.append(data)
        return rows
    except Exception:
        raise fail(label)
