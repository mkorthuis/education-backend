from fastapi import APIRouter, Query
from typing import List, Optional

from app.api.v1.deps import SessionDep
from app.schema.class_size_schema import (
    SchoolClassSizeGet,
    DistrictClassSizeGet,
    StateClassSizeGet,
)
from app.service.public.class_size_service import class_size_service
from app.core.cache import cache_response

router = APIRouter(prefix="/class-size", tags=["Class Size"])


@router.get(
    "/school",
    response_model=List[SchoolClassSizeGet],
    summary="Get school class size data",
    description="Retrieves school class size data with optional filters",
    response_description="List of school class size data",
)
@cache_response("class_size_school")
async def get_school_class_size(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description="Filter by year"),
    district_id: Optional[int] = Query(default=None, description="Filter by district ID"),
    school_id: Optional[int] = Query(default=None, description="Filter by school ID"),
):
    return class_size_service.get_school_class_size(
        session=session,
        year=year,
        district_id=district_id,
        school_id=school_id,
    )


@router.get(
    "/district",
    response_model=List[DistrictClassSizeGet],
    summary="Get district class size data",
    description="Retrieves district class size data with optional filters",
    response_description="List of district class size data",
)
@cache_response("class_size_district")
async def get_district_class_size(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description="Filter by year"),
    district_id: Optional[int] = Query(default=None, description="Filter by district ID"),
):
    return class_size_service.get_district_class_size(
        session=session,
        year=year,
        district_id=district_id,
    )


@router.get(
    "/state",
    response_model=List[StateClassSizeGet],
    summary="Get state class size data",
    description="Retrieves state-level class size data with optional filters",
    response_description="List of state class size data",
)
@cache_response("class_size_state")
async def get_state_class_size(
    session: SessionDep,
    year: Optional[int] = Query(default=None, description="Filter by year"),
):
    return class_size_service.get_state_class_size(
        session=session,
        year=year,
    ) 