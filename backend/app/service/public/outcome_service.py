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
    DistrictPostGraduation,
    DistrictEarlyExit,
)
from app.model.location import School
from app.schema.outcome_schema import (
    PostGraduationTypeGet,
    SchoolPostGraduationGet,
    StatePostGraduationGet,
    DistrictPostGraduationGet,
    SchoolEarlyExitGet,
    StateEarlyExitGet,
    DistrictEarlyExitGet,
)

logger = logging.getLogger(__name__)

class OutcomeService:
    # Post-graduation type
    def get_post_graduation_types(self, session: Session) -> List[PostGraduationTypeGet]:
        try:
            result = session.exec(select(PostGraduationType).order_by(PostGraduationType.name)).all()
            return [PostGraduationTypeGet.model_validate(r.__dict__) for r in result]
        except Exception as e:
            logger.error(f"Error fetching post graduation types: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch post graduation types")

    # School post-grad
    def get_school_post_graduation(
        self,
        session: Session,
        year: Optional[int] = None,
        school_id: Optional[int] = None,
        district_id: Optional[int] = None,
        pg_type_id: Optional[int] = None,
    ) -> List[SchoolPostGraduationGet]:
        try:
            stmt = (
                select(SchoolPostGraduation, PostGraduationType)
                .join(PostGraduationType)
                .join(School, School.id == SchoolPostGraduation.school_id_fk)
            )
            if year is not None:
                stmt = stmt.where(SchoolPostGraduation.year == year)
            if school_id is not None:
                stmt = stmt.where(SchoolPostGraduation.school_id_fk == school_id)
            if district_id is not None:
                stmt = stmt.where(School.district_id_fk == district_id)
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
                    "post_graduation_type": PostGraduationTypeGet.model_validate(pg_type.__dict__),
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
                    "post_graduation_type": PostGraduationTypeGet.model_validate(pg_type.__dict__),
                }
                data.append(StatePostGraduationGet.model_validate(item))
            return data
        except Exception as e:
            logger.error(f"Error fetching state post graduation: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch state post graduation")

    # School early exit
    def get_school_early_exit(
        self,
        session: Session,
        year: Optional[int] = None,
        school_id: Optional[int] = None,
        district_id: Optional[int] = None,
    ) -> List[SchoolEarlyExitGet]:
        try:
            stmt = select(SchoolEarlyExit).join(School, School.id == SchoolEarlyExit.school_id_fk)
            if year is not None:
                stmt = stmt.where(SchoolEarlyExit.year == year)
            if school_id is not None:
                stmt = stmt.where(SchoolEarlyExit.school_id_fk == school_id)
            if district_id is not None:
                stmt = stmt.where(School.district_id_fk == district_id)
            result = session.exec(stmt).all()
            data = []
            for early_exit in result:
                item = {
                    "id": early_exit.id,
                    "school_id": early_exit.school_id_fk,
                    "year": early_exit.year,
                    "adjusted_fall_enrollment": early_exit.adjusted_fall_enrollment,
                    "earned_hiset": early_exit.earned_hiset,
                    "enrolled_in_college": early_exit.enrolled_in_college,
                    "dropped_out": early_exit.dropped_out,
                    "missing": early_exit.missing,
                    "annual_early_exit_percentage": early_exit.annual_early_exit_percentage,
                    "four_year_early_exit_percentage": early_exit.four_year_early_exit_percentage,
                    "annual_dropout_percentage": early_exit.annual_dropout_percentage,
                    "four_year_dropout_percentage": early_exit.four_year_dropout_percentage,
                }
                data.append(SchoolEarlyExitGet.model_validate(item))
            return data
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
            data = []
            for early_exit in result:
                item = {
                    "id": early_exit.id,
                    "year": early_exit.year,
                    "adjusted_fall_enrollment": early_exit.adjusted_fall_enrollment,
                    "earned_hiset": early_exit.earned_hiset,
                    "enrolled_in_college": early_exit.enrolled_in_college,
                    "dropped_out": early_exit.dropped_out,
                    "missing": early_exit.missing,
                    "annual_early_exit_percentage": early_exit.annual_early_exit_percentage,
                    "four_year_early_exit_percentage": early_exit.four_year_early_exit_percentage,
                    "annual_dropout_percentage": early_exit.annual_dropout_percentage,
                    "four_year_dropout_percentage": early_exit.four_year_dropout_percentage,
                }
                data.append(StateEarlyExitGet.model_validate(item))
            return data
        except Exception as e:
            logger.error(f"Error fetching state early exit: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch state early exit")

    # District post-grad
    def get_district_post_graduation(
        self,
        session: Session,
        year: Optional[int] = None,
        district_id: Optional[int] = None,
        pg_type_id: Optional[int] = None,
    ) -> List[DistrictPostGraduationGet]:
        try:
            stmt = select(DistrictPostGraduation, PostGraduationType).join(PostGraduationType)
            if year is not None:
                stmt = stmt.where(DistrictPostGraduation.year == year)
            if district_id is not None:
                stmt = stmt.where(DistrictPostGraduation.district_id_fk == district_id)
            if pg_type_id is not None:
                stmt = stmt.where(DistrictPostGraduation.post_graduation_type_id_fk == pg_type_id)
            result = session.exec(stmt)
            data = []
            for dpg, pg_type in result:
                item = {
                    "district_id": dpg.district_id_fk,
                    "year": dpg.year,
                    "value": dpg.value,
                    "post_graduation_type": PostGraduationTypeGet.model_validate(pg_type.__dict__),
                }
                data.append(DistrictPostGraduationGet.model_validate(item))
            return data
        except Exception as e:
            logger.error(f"Error fetching district post graduation: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch district post graduation")

    # District early exit
    def get_district_early_exit(
        self,
        session: Session,
        year: Optional[int] = None,
        district_id: Optional[int] = None,
    ) -> List[DistrictEarlyExitGet]:
        try:
            stmt = select(DistrictEarlyExit)
            if year is not None:
                stmt = stmt.where(DistrictEarlyExit.year == year)
            if district_id is not None:
                stmt = stmt.where(DistrictEarlyExit.district_id_fk == district_id)
            result = session.exec(stmt).all()
            data = []
            for early_exit in result:
                item = {
                    "district_id": early_exit.district_id_fk,
                    "year": early_exit.year,
                    "adjusted_fall_enrollment": early_exit.adjusted_fall_enrollment,
                    "earned_hiset": early_exit.earned_hiset,
                    "enrolled_in_college": early_exit.enrolled_in_college,
                    "dropped_out": early_exit.dropped_out,
                    "missing": early_exit.missing,
                    "annual_early_exit_percentage": early_exit.annual_early_exit_percentage,
                    "four_year_early_exit_percentage": early_exit.four_year_early_exit_percentage,
                    "annual_dropout_percentage": early_exit.annual_dropout_percentage,
                    "four_year_dropout_percentage": early_exit.four_year_dropout_percentage,
                }
                data.append(DistrictEarlyExitGet.model_validate(item))
            return data
        except Exception as e:
            logger.error(f"Error fetching district early exit: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch district early exit")

outcome_service = OutcomeService() 