from fastapi import APIRouter, Query, Path, HTTPException
from typing import List, Optional
from uuid import UUID

from app.api.v1.deps import SessionDep
from app.schema.education_freedom_account_schema import (
    EducationFreedomAccountEntryGet,
    EFAEntryTypeGet,
    EFAEntryStateGet
)
from app.service.public.education_freedom_account_service import education_freedom_account_service
from app.core.cache import cache_response

router = APIRouter()

@router.get("/entry-type",
    response_model=List[EFAEntryTypeGet],
    summary="Get education freedom account entry types",
    description="Retrieves all education freedom account entry types with their values. If year is provided, returns data for that specific year, otherwise returns data for all years.",
    response_description="Education freedom account entry types with values")
@cache_response("efa_entry_types")
async def get_education_freedom_account_entry_types(
    session: SessionDep,
    year: Optional[int] = Query(None, description="Optional year to filter by. If not provided, returns data for all years.")
):
    """
    Get all education freedom account entry types with their values.
    
    If year is provided, returns data for that specific year.
    If year is not provided, returns data for all years.
    
    The data includes:
    - Entry type ID
    - Entry type name
    - Entry type description
    - Year
    - Value
    """
    return education_freedom_account_service.get_entry_types_with_values(
        session=session,
        year=year
    )

@router.get("/entry",
    response_model=List[EducationFreedomAccountEntryGet],
    summary="Get education freedom account entries",
    description="Retrieves education freedom account entries, optionally filtered by year, district ID, and town ID. If no filters are provided, returns all entries.",
    response_description="Education freedom account entries")
@cache_response("efa_entries")
async def get_education_freedom_account_entries(
    session: SessionDep,
    year: Optional[int] = Query(None, description="Optional year to filter by. If not provided, returns data for all years."),
    district_id: Optional[int] = Query(None, description="Optional district ID to filter by"),
    town_id: Optional[int] = Query(None, description="Optional town ID to filter by. Note: If both district_id and town_id are provided, district_id takes precedence.")
):
    """
    Get education freedom account entries, optionally filtered by year, district ID, and town ID.
    
    If year is provided, returns data for that specific year. If not provided, returns data for all years.
    If district_id is provided, returns data for all towns in that district.
    If town_id is provided (and district_id is not), returns data for that specific town.
    If no filters are provided, returns all entries ordered by town ID and year.
    
    Note: If both district_id and town_id are provided, district_id takes precedence.
    
    The data includes:
    - Entry ID
    - Town ID
    - Year
    - ADM (Average Daily Membership)
    - Entry type ID
    - Value
    """
    return education_freedom_account_service.get_entries(
        session=session,
        year=year,
        district_id=district_id,
        town_id=town_id
    )

@router.get("/state-entry",
    response_model=List[EFAEntryStateGet],
    summary="Get state-level education freedom account entries",
    description="Retrieves state-level education freedom account entries (aggregated from the materialized view), optionally filtered by year and entry type ID.",
    response_description="State-level education freedom account entries")
@cache_response("efa_state_entries")
async def get_state_education_freedom_account_entries(
    session: SessionDep,
    year: Optional[int] = Query(None, description="Optional year to filter by"),
    entry_type_id: Optional[int] = Query(None, description="Optional entry type ID to filter by")
):
    """
    Get state-level education freedom account entries, optionally filtered by year and entry type ID.
    
    If year is provided, returns data for that specific year.
    If entry_type_id is provided, returns data for that specific entry type.
    If neither is provided, returns data for all available years and entry types in descending order by year (most recent first).
    
    The data includes:
    - Year
    - Entry type ID
    - Value (sum of all town values for that entry type and year)
    """
    return education_freedom_account_service.get_state_entries(
        session=session,
        year=year,
        entry_type_id=entry_type_id
    ) 