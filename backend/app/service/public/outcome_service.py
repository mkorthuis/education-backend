import logging
from typing import List, Optional
from sqlmodel import Session, select
from fastapi import HTTPException

from app.model.outcome import (
    PostGraduationType,
    SchoolPostGraduation,
    StatePostGraduation,
    SchoolEarlyExit,
    StateEarlyExit,
)
from app.model.location import School
from app.schema.outcome_schema import (
    PostGraduationTypeGet,
    SchoolPostGraduationGet,
    StatePostGraduationGet,
    SchoolEarlyExitGet,
    StateEarlyExitGet,
)

logger = logging.getLogger(__name__)

class OutcomeService:
    # Post-graduation type
    def get_post_graduation_types(self, session: Session) -> List[PostGraduationTypeGet]:
        try:
            result = session.exec(select(PostGraduationType).order_by(PostGraduationType.name)).all()
            return [PostGraduationTypeGet.model_validate(r.dict()) for r in result]
        except Exception as e:
            logger.error(f"Error fetching post graduation types: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch post graduation types")

    # School post-grad
    def get_school_post_graduation(
        self, session: Session, year: Optional[int] = None, school_id: Optional[int] = None, pg_type_id: Optional[int] = None
    ) -> List[SchoolPostGraduationGet]:
        try:
            stmt = select(SchoolPostGraduation, PostGraduationType).join(PostGraduationType)
            if year is not None:
                stmt = stmt.where(SchoolPostGraduation.year == year)
            if school_id is not None:
                stmt = stmt.where(SchoolPostGraduation.school_id_fk == school_id)
            if pg_type_id is not None:
                stmt = stmt.where(SchoolPostGraduation.post_graduation_type_id_fk == pg_type_id)
            result = session.exec(stmt)
            data = []
            for spg, pg_type in result:
                item = {
                    "id": spg.id,
                    "school_id": spg.school_id_fk,
                    "year": spg.year,
                    "value": spg.value,
                    "post_graduation_type": PostGraduationTypeGet.model_validate(pg_type.dict()),
                }
                data.append(SchoolPostGraduationGet.model_validate(item))
            return data
        except Exception as e:
            logger.error(f"Error fetching school post graduation: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch school post graduation")

    # State post-grad
    def get_state_post_graduation(
        self, session: Session, year: Optional[int] = None, pg_type_id: Optional[int] = None
    ) -> List[StatePostGraduationGet]:
        try:
            stmt = select(StatePostGraduation, PostGraduationType).join(PostGraduationType)
            if year is not None:
                stmt = stmt.where(StatePostGraduation.year == year)
            if pg_type_id is not None:
                stmt = stmt.where(StatePostGraduation.post_graduation_type_id_fk == pg_type_id)
            result = session.exec(stmt)
            data = []
            for spg, pg_type in result:
                item = {
                    "id": spg.id,
                    "year": spg.year,
                    "value": spg.value,
                    "post_graduation_type": PostGraduationTypeGet.model_validate(pg_type.dict()),
                }
                data.append(StatePostGraduationGet.model_validate(item))
            return data
        except Exception as e:
            logger.error(f"Error fetching state post graduation: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch state post graduation")

    # School early exit
    def get_school_early_exit(
        self, session: Session, year: Optional[int] = None, school_id: Optional[int] = None
    ) -> List[SchoolEarlyExitGet]:
        try:
            stmt = select(SchoolEarlyExit)
            if year is not None:
                stmt = stmt.where(SchoolEarlyExit.year == year)
            if school_id is not None:
                stmt = stmt.where(SchoolEarlyExit.school_id_fk == school_id)
            result = session.exec(stmt).all()
            return [SchoolEarlyExitGet.model_validate(r.dict()) for r in result]
        except Exception as e:
            logger.error(f"Error fetching school early exit: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch school early exit")

    # State early exit
    def get_state_early_exit(self, session: Session, year: Optional[int] = None) -> List[StateEarlyExitGet]:
        try:
            stmt = select(StateEarlyExit)
            if year is not None:
                stmt = stmt.where(StateEarlyExit.year == year)
            result = session.exec(stmt).all()
            return [StateEarlyExitGet.model_validate(r.dict()) for r in result]
        except Exception as e:
            logger.error(f"Error fetching state early exit: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch state early exit")

outcome_service = OutcomeService() 