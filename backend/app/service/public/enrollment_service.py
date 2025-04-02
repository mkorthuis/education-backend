from typing import List, Optional
from sqlmodel import Session, select, func
from fastapi import HTTPException

from app.model.enrollment import SchoolEnrollment
from app.schema.enrollment_schema import SchoolEnrollmentGet

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

enrollment_service = EnrollmentService() 