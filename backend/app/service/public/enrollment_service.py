from typing import List, Optional
from sqlalchemy.orm import selectinload
from sqlmodel import Session, select, func, and_
from fastapi import HTTPException

from app.model.enrollment import SchoolEnrollment, StateEnrollment, TownEnrollment, TownEnrollmentState
from app.model.location import District, Grade, School, TownDistrictLink
from app.schema.enrollment_schema import SchoolEnrollmentGet, StateEnrollmentGet, StateSchoolCountGet, TownEnrollmentGet, TownEnrollmentStateGet

class EnrollmentService:
    def get_school_enrollments(
        self, 
        session: Session,
        school_id: int,
        year: Optional[int] = None
    ) -> List[SchoolEnrollmentGet]:
        """
        Get school enrollments for a specific school, optionally filtering by year.
        
        Args:
            session: Database session
            school_id: ID of the school to get enrollments for
            year: Optional year to filter enrollments by
            
        Returns:
            List of school enrollments
        """
        statement = select(SchoolEnrollment).where(
            SchoolEnrollment.school_id_fk == school_id
        ).options(selectinload(SchoolEnrollment.grade))
        
        if year is not None:
            statement = statement.where(SchoolEnrollment.year == year)
            
        enrollments = session.exec(statement).all()
        return [SchoolEnrollmentGet.from_orm(enrollment) for enrollment in enrollments]
    
    def get_latest_school_enrollments(
        self, 
        session: Session,
        school_id: int
    ) -> List[SchoolEnrollmentGet]:
        # Enrollments for the school's latest year, in one query (grades loaded in one batch)
        latest_year = select(func.max(SchoolEnrollment.year)).where(
            SchoolEnrollment.school_id_fk == school_id
        ).scalar_subquery()
        statement = select(SchoolEnrollment).where(
            SchoolEnrollment.school_id_fk == school_id,
            SchoolEnrollment.year == latest_year
        ).options(selectinload(SchoolEnrollment.grade))
        
        enrollments = session.exec(statement).all()
        if not enrollments:
            # The school has no enrollment rows at all
            raise HTTPException(status_code=404, detail="No enrollment data found for this school")
        return [SchoolEnrollmentGet.from_orm(enrollment) for enrollment in enrollments]

    def get_town_enrollments(
        self,
        session: Session,
        town_id: Optional[int] = None,
        district_id: Optional[int] = None,
        year: Optional[int] = None
    ) -> List[TownEnrollmentGet]:
        """
        Get town enrollments, optionally filtered by town ID, district ID, and year.
        
        Args:
            session: Database session
            town_id: Optional ID of the town to get enrollments for
            district_id: Optional ID of the district to get enrollments for
            year: Optional year to filter enrollments by
            
        Returns:
            List of town enrollments with grade information
        """
        if district_id is not None and town_id is not None:
            # If both district_id and town_id are provided, district_id takes precedence
            # Check if the town belongs to the district
            town_district_check = select(func.count()).where(
                and_(
                    TownDistrictLink.district_id_fk == district_id,
                    TownDistrictLink.town_id_fk == town_id
                )
            )
            count = session.exec(town_district_check).one()
            
            if count == 0:
                raise HTTPException(
                    status_code=404, 
                    detail=f"Town ID {town_id} is not part of District ID {district_id}"
                )
        
        district_towns = select(TownDistrictLink.town_id_fk).where(
            TownDistrictLink.district_id_fk == district_id
        )
        if district_id is not None:
            # Towns in the district, as a subquery (one round trip)
            statement = select(TownEnrollment).where(
                TownEnrollment.town_id_fk.in_(district_towns)
            )
        else:
            # Standard query with no district filter
            statement = select(TownEnrollment)
        statement = statement.options(selectinload(TownEnrollment.grade))
        
        # Apply additional filters
        if town_id is not None and district_id is None:
            statement = statement.where(TownEnrollment.town_id_fk == town_id)
            
        if year is not None:
            statement = statement.where(TownEnrollment.year == year)
            
        # Order by town ID, year, and grade ID for consistent results
        statement = statement.order_by(
            TownEnrollment.town_id_fk, 
            TownEnrollment.year.desc(), 
            TownEnrollment.grade_id_fk
        )
            
        enrollments = session.exec(statement).all()
        
        # If filtering and nothing found, return 404
        if not enrollments:
            if district_id is not None:
                if session.exec(district_towns.limit(1)).first() is None:
                    raise HTTPException(
                        status_code=404, 
                        detail=f"No towns found in district ID {district_id}"
                    )
                if year is not None:
                    raise HTTPException(
                        status_code=404, 
                        detail=f"No enrollment data found for district ID {district_id} in year {year}"
                    )
                else:
                    raise HTTPException(
                        status_code=404, 
                        detail=f"No enrollment data found for district ID {district_id}"
                    )
            elif town_id is not None:
                if year is not None:
                    raise HTTPException(
                        status_code=404, 
                        detail=f"No enrollment data found for town ID {town_id} in year {year}"
                    )
                else:
                    raise HTTPException(
                        status_code=404, 
                        detail=f"No enrollment data found for town ID {town_id}"
                    )
            
        return [TownEnrollmentGet.from_orm(enrollment) for enrollment in enrollments]

    def get_state_school_counts(self, session: Session) -> List[StateSchoolCountGet]:
        """
        Count, for each year, the public schools with any students in kindergarten to grade 12 and
        the public school districts those schools belong to (districts that run their own schools).
        Preschool-only programs and charter schools (which are their own, non-public districts)
        aren't counted.

        Returns:
            One row per year, oldest first
        """
        statement = (
            select(
                SchoolEnrollment.year,
                func.count(func.distinct(SchoolEnrollment.school_id_fk)).label("schools"),
                func.count(func.distinct(School.district_id_fk)).label("districts"),
            )
            .join(School, School.id == SchoolEnrollment.school_id_fk)
            .join(District, and_(District.id == School.district_id_fk, District.is_public))
            .join(Grade, and_(Grade.id == SchoolEnrollment.grade_id_fk, Grade.name != "Preschool"))
            .where(SchoolEnrollment.enrollment > 0)
            .group_by(SchoolEnrollment.year)
            .order_by(SchoolEnrollment.year)
        )
        return [StateSchoolCountGet(year=year, schools=schools, districts=districts)
                for year, schools, districts in session.exec(statement).all()]

    def get_state_enrollments(
        self,
        session: Session,
        year: Optional[int] = None
    ) -> List[StateEnrollmentGet]:
        """
        Get state-level enrollment data, optionally filtered by year.
        
        Args:
            session: Database session
            year: Optional year to filter enrollments by
            
        Returns:
            List of state enrollment records
        """
        statement = select(StateEnrollment)
        
        if year is not None:
            statement = statement.where(StateEnrollment.year == year)
            
        # Order by year descending to get most recent first
        statement = statement.order_by(StateEnrollment.year.desc())
            
        enrollments = session.exec(statement).all()
        
        if not enrollments and year is not None:
            raise HTTPException(status_code=404, detail=f"No state enrollment data found for year {year}")
            
        return [StateEnrollmentGet.from_orm(enrollment) for enrollment in enrollments]

    def get_town_enrollment_state(
        self,
        session: Session,
        year: Optional[int] = None,
        grade_id: Optional[int] = None
    ) -> List[TownEnrollmentStateGet]:
        """
        Get state-level town enrollment data aggregated by year and grade.
        
        Args:
            session: Database session
            year: Optional year to filter by
            grade_id: Optional grade ID to filter by
            
        Returns:
            List of town enrollment state records with grade information
        """
        statement = select(TownEnrollmentState).options(selectinload(TownEnrollmentState.grade))
        
        # Apply filters if provided
        if year is not None:
            statement = statement.where(TownEnrollmentState.year == year)
            
        if grade_id is not None:
            statement = statement.where(TownEnrollmentState.grade_id_fk == grade_id)
            
        # Order by year descending and grade ID for consistent results
        statement = statement.order_by(
            TownEnrollmentState.year.desc(), 
            TownEnrollmentState.grade_id_fk
        )
            
        state_records = session.exec(statement).all()
        
        # If filtering and no results found, raise 404
        if not state_records and (year is not None or grade_id is not None):
            if year is not None and grade_id is not None:
                raise HTTPException(
                    status_code=404, 
                    detail=f"No state-level town enrollment data found for year {year} and grade ID {grade_id}"
                )
            elif year is not None:
                raise HTTPException(
                    status_code=404, 
                    detail=f"No state-level town enrollment data found for year {year}"
                )
            else:
                raise HTTPException(
                    status_code=404, 
                    detail=f"No state-level town enrollment data found for grade ID {grade_id}"
                )
            
        return [TownEnrollmentStateGet.from_orm(record) for record in state_records]

enrollment_service = EnrollmentService() 