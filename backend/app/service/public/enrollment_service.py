from typing import List, Optional
from sqlmodel import Session, select, func, and_, join
from fastapi import HTTPException

from app.model.enrollment import SchoolEnrollment, StateEnrollment, TownEnrollment, TownEnrollmentState
from app.model.location import Town, TownDistrictLink
from app.schema.enrollment_schema import SchoolEnrollmentGet, StateEnrollmentGet, TownEnrollmentGet, TownEnrollmentStateGet

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
        statement = select(SchoolEnrollment).where(SchoolEnrollment.school_id_fk == school_id)
        
        if year is not None:
            statement = statement.where(SchoolEnrollment.year == year)
            
        enrollments = session.exec(statement).all()
        return [SchoolEnrollmentGet.from_orm(enrollment) for enrollment in enrollments]
    
    def get_latest_school_enrollments(
        self, 
        session: Session,
        school_id: int
    ) -> List[SchoolEnrollmentGet]:
        # First check if the school exists
        school_exists = session.exec(
            select(func.count()).where(SchoolEnrollment.school_id_fk == school_id)
        ).one()
        
        if school_exists == 0:
            raise HTTPException(status_code=404, detail="No enrollment data found for this school")
        
        # Get the latest year for which we have enrollment data for this school
        latest_year = session.exec(
            select(func.max(SchoolEnrollment.year)).where(SchoolEnrollment.school_id_fk == school_id)
        ).one()
        
        if latest_year is None:
            return []
        
        # Get enrollments for the latest year
        statement = select(SchoolEnrollment).where(
            SchoolEnrollment.school_id_fk == school_id,
            SchoolEnrollment.year == latest_year
        )
        
        enrollments = session.exec(statement).all()
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
        
        if district_id is not None:
            # Get towns in the district
            subquery = select(TownDistrictLink.town_id_fk).where(
                TownDistrictLink.district_id_fk == district_id
            ).distinct()
            
            town_ids = session.exec(subquery).all()
            
            if not town_ids:
                raise HTTPException(
                    status_code=404, 
                    detail=f"No towns found in district ID {district_id}"
                )
            
            # Build query with town IDs from the district
            statement = select(TownEnrollment).where(
                TownEnrollment.town_id_fk.in_(town_ids)
            )
        else:
            # Standard query with no district filter
            statement = select(TownEnrollment)
        
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
        statement = select(TownEnrollmentState)
        
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