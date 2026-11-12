from collections import defaultdict
from datetime import date
from typing import Dict, List, Optional
from sqlalchemy.orm import selectinload
from sqlmodel import Session, func, select
from fastapi import HTTPException

from app.model.location import SAU, District, Region, SchoolType, Grade, Town, School
from app.model.assessment import AssessmentSchool
from app.model.enrollment import SchoolEnrollment
from app.model.outcome import SchoolGraduationCohort
from app.model.safety import SchoolBullying, SchoolHarassment, SchoolRestraint, SchoolSafety, SchoolSeclusion, SchoolTruancy
from app.schema.location_schema import (
    SAUGet, DistrictGet, RegionGet, SchoolTypeGet, 
    GradeGet, TownGet, SchoolGet
)

# The topics a school's own figures come in, with the tables that hold them (a school has safety
# figures when any of the safety tables has a row for it, as the school safety page decides)
SCHOOL_TOPICS = {
    "enrollment": [SchoolEnrollment],
    "test_scores": [AssessmentSchool],
    "graduation": [SchoolGraduationCohort],
    "safety": [SchoolSafety, SchoolHarassment, SchoolTruancy, SchoolBullying, SchoolRestraint, SchoolSeclusion],
}
GRADE_12_ID = 14


class LocationService:
    def get_saus(
        self, 
        session: Session,
        district_id: Optional[int] = None
    ) -> List[SAUGet]:
        """Get all SAUs, optionally filtering by district ID."""
        if district_id is not None:
            # Get the district first to check if it exists
            district = session.get(District, district_id)
            if not district:
                raise HTTPException(status_code=404, detail="District not found")
            
            # If the district has an SAU, return only that SAU
            if district.sau_id_fk is not None:
                sau = session.get(SAU, district.sau_id_fk)
                return [SAUGet.from_orm(sau)] if sau else []
            return []
        
        # If no district_id filter, return all SAUs
        statement = select(SAU).options(selectinload(SAU.staff))
        return [SAUGet.from_orm(sau) for sau in session.exec(statement).all()]

    def get_sau_by_id(self, session: Session, sau_id: int) -> SAUGet:
        """Get SAU by ID."""
        sau = session.get(SAU, sau_id)
        if not sau:
            raise HTTPException(status_code=404, detail="SAU not found")
        return SAUGet.from_orm(sau)

    def get_districts(
        self, 
        session: Session, 
        is_public: Optional[bool] = None,
        school_id: Optional[int] = None,
        include_former: bool = False,
        kind: Optional[str] = None
    ) -> List[DistrictGet]:
        """
        Get districts, optionally filtering by public status, kind ('district', 'charter' or
        'private') and/or school ID.

        Only districts in the state's current list, unless include_former is set; a school's
        district is returned whether or not it is current.
        """
        
        # Towns and grades are loaded for all districts at once instead of per district
        statement = select(District).options(selectinload(District.towns), selectinload(District.grades))
        
        # Apply filters
        if is_public is not None:
            statement = statement.where(District.is_public == is_public)
        if kind is not None:
            statement = statement.where(District.kind == kind)

        if school_id is None and not include_former:
            statement = statement.where(District.is_current)
        
        if school_id is not None:
            school = session.get(School, school_id)
            if not school:
                raise HTTPException(status_code=404, detail="School not found")
            statement = statement.where(District.id == school.district_id_fk)
        
        districts = session.exec(statement).all()
        result = []
        
        for district in districts:
            # Create a temporary copy of the district data
            district_dict = {
                "id": district.id,
                "name": district.name,
                "sau_id_fk": district.sau_id_fk,
                "is_public": district.is_public,
                "is_current": district.is_current,
                "kind": district.kind
            }
            
            # Add town IDs list instead of town objects
            district_dict["towns"] = [town.id for town in district.towns] if district.towns else []
            
            # Add grade list
            district_dict["grades"] = [GradeGet.from_orm(grade) for grade in district.grades] if district.grades else []
            
            # Create DistrictGet object from dictionary using Pydantic v2 method
            result.append(DistrictGet.model_validate(district_dict))
            
        return result

    def get_district_by_id(self, session: Session, district_id: int) -> DistrictGet:
        """Get district by ID."""
        district = session.get(District, district_id)
        if not district:
            raise HTTPException(status_code=404, detail="District not found")
        
        # Create a temporary copy of the district data
        district_dict = {
            "id": district.id,
            "name": district.name,
            "sau_id_fk": district.sau_id_fk,
            "is_public": district.is_public,
            "is_current": district.is_current,
            "kind": district.kind
        }
        
        # Add town IDs list instead of town objects
        district_dict["towns"] = [town.id for town in district.towns] if district.towns else []
        
        # Add grade list
        district_dict["grades"] = [GradeGet.from_orm(grade) for grade in district.grades] if district.grades else []
        
        # Create DistrictGet object from dictionary using Pydantic v2 method
        return DistrictGet.model_validate(district_dict)

    def get_schools(
        self, 
        session: Session,
        district_id: Optional[int] = None,
        include_former: bool = False,
        kind: Optional[str] = None
    ) -> List[SchoolGet]:
        """
        Get schools in the state's current list (or all, with include_former), optionally by district
        ID or by their district's kind ('district', 'charter' or 'private').
        """
        # Grades, school type and district are loaded for all schools at once instead of per school
        statement = select(School).options(
            selectinload(School.grades), selectinload(School.school_type), selectinload(School.district))
        
        if district_id is not None:
            statement = statement.where(School.district_id_fk == district_id)
        if kind is not None:
            statement = statement.where(School.district_id_fk.in_(select(District.id).where(District.kind == kind)))

        if not include_former:
            statement = statement.where(School.is_current)
            
        schools = session.exec(statement).all()
        enrollments = self._enrollments_by_school(session, [school.id for school in schools])
        result = []
        
        not_yet = self._not_yet_reported(session, schools)
        for school in schools:
            school_data = self._school_get(school)
            self._set_latest_enrollment(school_data, enrollments.get(school.id, []))
            school_data.not_yet_reported = not_yet.get(school.id, [])
            result.append(school_data)
            
        return result

    def get_school_by_id(self, session: Session, school_id: int) -> SchoolGet:
        """Get school by ID."""
        school = session.get(School, school_id)
        if not school:
            raise HTTPException(status_code=404, detail="School not found")
        
        school_data = self._school_get(school)
        enrollments = self._enrollments_by_school(session, [school.id])
        self._set_latest_enrollment(school_data, enrollments.get(school.id, []))
        school_data.not_yet_reported = self._not_yet_reported(session, [school]).get(school.id, [])
        return school_data

    @staticmethod
    def _not_yet_reported(session: Session, schools: List[School]) -> Dict[int, List[str]]:
        """
        For each school that opened after the latest school year a topic's figures cover (on or after
        July 1 of the year the latest one ends), the topics it has no figures in yet: a new school's
        first enrollment, test results, graduation and safety figures come in later years' files.
        Graduation only for a school with a grade 12. Schools with figures, or without an open date,
        aren't listed.
        """
        recent = [school for school in schools if school.open_date]
        if not recent:
            return {}
        result: Dict[int, List[str]] = defaultdict(list)
        for topic, tables in SCHOOL_TOPICS.items():
            latest = max((session.exec(select(func.max(table.year))).one() or 0) for table in tables)
            if not latest:
                continue
            cutoff = date(latest, 7, 1)
            candidates = [
                school.id for school in recent
                if school.open_date >= cutoff
                and (topic != "graduation" or any(grade.id == GRADE_12_ID for grade in school.grades))
            ]
            if not candidates:
                continue
            reported = set()
            for table in tables:
                reported.update(session.exec(select(table.school_id_fk).where(table.school_id_fk.in_(candidates)).distinct()).all())
            for school_id in candidates:
                if school_id not in reported:
                    result[school_id].append(topic)
        return result

    @staticmethod
    def _school_get(school: School) -> SchoolGet:
        """A school as the API returns it, with its district's kind."""
        school_data = SchoolGet.from_orm(school)
        school_data.kind = school.district.kind if school.district else None
        return school_data

    def _enrollments_by_school(self, session: Session, school_ids: List[int]) -> Dict[int, list]:
        """The given schools' (enrollment, grade) rows for each school's latest year, in one query, grouped by school."""
        if not school_ids:
            return {}
        latest = select(
            SchoolEnrollment.school_id_fk, func.max(SchoolEnrollment.year).label("year")
        ).where(
            SchoolEnrollment.school_id_fk.in_(school_ids)
        ).group_by(SchoolEnrollment.school_id_fk).subquery()
        statement = select(SchoolEnrollment, Grade).join(
            Grade, SchoolEnrollment.grade_id_fk == Grade.id
        ).join(
            latest, (SchoolEnrollment.school_id_fk == latest.c.school_id_fk) & (SchoolEnrollment.year == latest.c.year)
        )
        by_school: Dict[int, list] = {}
        for enrollment, grade in session.exec(statement).all():
            by_school.setdefault(enrollment.school_id_fk, []).append((enrollment, grade))
        return by_school

    def _set_latest_enrollment(self, school_data: SchoolGet, enrollments: list) -> None:
        """Set a school's enrollment by grade for its latest year, from its (enrollment, grade) rows."""
        if not enrollments:
            school_data.latest_enrollment = {}
            school_data.enrollment = {}
            return
        
        # Determine the latest year in memory
        latest_year = max(enrollment.year for enrollment, _ in enrollments)
        
        # Filter to only include the latest year's enrollments
        latest_enrollments = [(enrollment, grade) for enrollment, grade in enrollments if enrollment.year == latest_year]
        
        # Create a dictionary of grade ID to enrollment
        enrollment_by_id = {}
        # Create a dictionary of grade name to enrollment
        enrollment_by_name = {}
        total_enrollment = 0
        
        for enrollment, grade in latest_enrollments:
            enrollment_by_id[grade.id] = enrollment.enrollment
            enrollment_by_name[grade.name] = enrollment.enrollment
            total_enrollment += enrollment.enrollment
        
        # Add total enrollment
        enrollment_by_name['total'] = total_enrollment
        
        school_data.enrollment = enrollment_by_id
        school_data.latest_enrollment = enrollment_by_name

    def get_regions(self, session: Session) -> List[RegionGet]:
        """Get all regions."""
        return [RegionGet.from_orm(region) for region in session.exec(select(Region)).all()]

    def get_region_by_id(self, session: Session, region_id: int) -> RegionGet:
        """Get region by ID."""
        region = session.get(Region, region_id)
        if not region:
            raise HTTPException(status_code=404, detail="Region not found")
        return RegionGet.from_orm(region)

    def get_school_types(self, session: Session) -> List[SchoolTypeGet]:
        """Get all school types."""
        return [SchoolTypeGet.from_orm(st) for st in session.exec(select(SchoolType)).all()]

    def get_school_type_by_id(self, session: Session, school_type_id: int) -> SchoolTypeGet:
        """Get school type by ID."""
        school_type = session.get(SchoolType, school_type_id)
        if not school_type:
            raise HTTPException(status_code=404, detail="School type not found")
        return SchoolTypeGet.from_orm(school_type)

    def get_grades(self, session: Session) -> List[GradeGet]:
        """Get all grades."""
        return [GradeGet.from_orm(grade) for grade in session.exec(select(Grade)).all()]

    def get_grade_by_id(self, session: Session, grade_id: int) -> GradeGet:
        """Get grade by ID."""
        grade = session.get(Grade, grade_id)
        if not grade:
            raise HTTPException(status_code=404, detail="Grade not found")
        return GradeGet.from_orm(grade)

    def get_towns(
        self, 
        session: Session,
        district_id: Optional[int] = None
    ) -> List[TownGet]:
        """Get all towns, optionally filtering by district ID."""
        
        if district_id is not None:
            # For filtering by district_id, we need to query through the link table
            # Since it's a many-to-many relationship
            from app.model.location import TownDistrictLink
            
            # Get town IDs linked to this district
            statement = select(TownDistrictLink.town_id_fk).where(
                TownDistrictLink.district_id_fk == district_id
            )
            # When selecting a single column, SQLModel returns the values directly (not as tuples)
            town_ids = session.exec(statement).all()
            
            # Then get the towns with those IDs
            if town_ids:
                statement = select(Town).where(Town.id.in_(town_ids)).options(selectinload(Town.districts))
                towns = session.exec(statement).all()
            else:
                towns = []
        else:
            # If no district_id filter, get all towns
            towns = session.exec(select(Town).options(selectinload(Town.districts))).all()
        
        result = []
        
        for town in towns:
            # Create a temporary copy of the town data
            town_dict = {
                "id": town.id,
                "name": town.name
            }
            
            # Add district IDs list instead of district objects
            town_dict["district_ids"] = [district.id for district in town.districts] if town.districts else []
            
            # Create TownGet object from dictionary using Pydantic v2 method
            result.append(TownGet.model_validate(town_dict))
            
        return result

    def get_town_by_id(self, session: Session, town_id: int) -> TownGet:
        """Get town by ID."""
        town = session.get(Town, town_id)
        if not town:
            raise HTTPException(status_code=404, detail="Town not found")
        
        # Create a temporary copy of the town data
        town_dict = {
            "id": town.id,
            "name": town.name
        }
        
        # Add district IDs list instead of district objects
        town_dict["district_ids"] = [district.id for district in town.districts] if town.districts else []
        
        # Create TownGet object from dictionary using Pydantic v2 method
        return TownGet.model_validate(town_dict)

location_service = LocationService() 