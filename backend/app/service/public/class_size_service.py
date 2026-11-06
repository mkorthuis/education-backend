import logging
from typing import List, Optional
from sqlmodel import Session, select
from fastapi import HTTPException

from app.model.class_size import (
    SchoolClassSize,
    DistrictClassSize,
    StateClassSize,
)
from app.model.location import School
from app.model.measurement import Measurement, MeasurementType
from app.schema.class_size_schema import (
    SchoolClassSizeGet,
    DistrictClassSizeGet,
    StateClassSizeGet,
)

logger = logging.getLogger(__name__)


class ClassSizeService:
    MEASUREMENT_NAME = "Average Class Size"

    def _all_grades_by_entity(self, session: Session, entity_column, entity_ids: set, years: set) -> dict:
        """
        "Average Class Size" measurement values for the given schools or districts and years, in one
        query, keyed by (entity id, year). entity_column is Measurement.school_id_fk or
        Measurement.district_id_fk. The first value per key wins, as the per-row lookup's .first() did.
        """
        if not entity_ids:
            return {}
        stmt = select(entity_column, Measurement.year, Measurement.field).join(
            MeasurementType, Measurement.measurement_type_id_fk == MeasurementType.id
        ).where(
            MeasurementType.name == self.MEASUREMENT_NAME,
            entity_column.in_(entity_ids),
            Measurement.year.in_(years),
        )
        values = {}
        for entity_id, year, value in session.exec(stmt).all():
            values.setdefault((entity_id, year), value)
        return values

    # School-level
    def get_school_class_size(
        self,
        session: Session,
        *,
        year: Optional[int] = None,
        district_id: Optional[int] = None,
        school_id: Optional[int] = None,
    ) -> List[SchoolClassSizeGet]:
        try:
            stmt = select(SchoolClassSize, School).join(
                School, SchoolClassSize.school_id_fk == School.id
            )
            if year is not None:
                stmt = stmt.where(SchoolClassSize.year == year)
            if district_id is not None:
                stmt = stmt.where(School.district_id_fk == district_id)
            if school_id is not None:
                stmt = stmt.where(SchoolClassSize.school_id_fk == school_id)

            rows = session.exec(stmt).all()
            all_grades = self._all_grades_by_entity(
                session, Measurement.school_id_fk, {cs.school_id_fk for cs, _ in rows}, {cs.year for cs, _ in rows}
            )
            response: List[SchoolClassSizeGet] = []
            for cs, school in rows:
                all_grade_val = all_grades.get((cs.school_id_fk, cs.year))
                data = {
                    "id": cs.id,
                    "school_id": cs.school_id_fk,
                    "district_id": school.district_id_fk if school else None,
                    "year": cs.year,
                    "grades_1_2": cs.grade_1_2,
                    "grades_3_4": cs.grade_3_4,
                    "grades_5_8": cs.grade_5_8,
                    "all_grades": all_grade_val,
                }
                response.append(SchoolClassSizeGet.model_validate(data))
            return response
        except Exception as e:
            logger.error(f"Error fetching school class size data: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch school class size data")

    # District-level
    def get_district_class_size(
        self,
        session: Session,
        *,
        year: Optional[int] = None,
        district_id: Optional[int] = None,
    ) -> List[DistrictClassSizeGet]:
        try:
            stmt = select(DistrictClassSize)
            if year is not None:
                stmt = stmt.where(DistrictClassSize.year == year)
            if district_id is not None:
                stmt = stmt.where(DistrictClassSize.district_id_fk == district_id)

            rows = session.exec(stmt).all()
            all_grades = self._all_grades_by_entity(
                session, Measurement.district_id_fk, {cs.district_id_fk for cs in rows}, {cs.year for cs in rows}
            )
            response: List[DistrictClassSizeGet] = []
            for cs in rows:
                all_grade_val = all_grades.get((cs.district_id_fk, cs.year))
                data = {
                    "id": cs.id,
                    "district_id": cs.district_id_fk,
                    "year": cs.year,
                    "grades_1_2": cs.grade_1_2,
                    "grades_3_4": cs.grade_3_4,
                    "grades_5_8": cs.grade_5_8,
                    "all_grades": all_grade_val,
                }
                response.append(DistrictClassSizeGet.model_validate(data))
            return response
        except Exception as e:
            logger.error(f"Error fetching district class size data: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch district class size data")

    # State-level
    def get_state_class_size(
        self,
        session: Session,
        *,
        year: Optional[int] = None,
    ) -> List[StateClassSizeGet]:
        try:
            stmt = select(StateClassSize)
            if year is not None:
                stmt = stmt.where(StateClassSize.year == year)

            result = session.exec(stmt)
            response: List[StateClassSizeGet] = []
            for cs in result:
                data = {
                    "id": cs.id,
                    "year": cs.year,
                    "grades_1_2": cs.grade_1_2,
                    "grades_3_4": cs.grade_3_4,
                    "grades_5_8": cs.grade_5_8,
                    "all_grades": cs.all_grades,
                }
                response.append(StateClassSizeGet.model_validate(data))
            return response
        except Exception as e:
            logger.error(f"Error fetching state class size data: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch state class size data")


class_size_service = ClassSizeService() 