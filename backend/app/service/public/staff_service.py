import logging
from typing import List, Optional
from sqlmodel import Session, select
from fastapi import HTTPException

from app.model.staff import (
    SchoolStaffType, 
    TeacherEducationType, 
    TeacherSalaryBandType,
    DistrictStaff,
    StateStaff,
    DistrictTeacherEducation,
    StateTeacherEducation,
    DistrictTeacherAverageSalary,
    StateTeacherAverageSalary,
    DistrictTeacherSalaryBand,
    StateTeacherSalaryBand
)
from app.model.location import District
from app.schema.staff_schema import (
    SchoolStaffTypeGet, 
    TeacherEducationTypeGet, 
    TeacherSalaryBandTypeGet,
    DistrictStaffGet,
    StateStaffGet,
    DistrictTeacherEducationGet,
    StateTeacherEducationGet,
    DistrictTeacherAverageSalaryGet,
    StateTeacherAverageSalaryGet,
    DistrictTeacherSalaryBandGet,
    StateTeacherSalaryBandGet
)

# Configure logger
logger = logging.getLogger(__name__)

class StaffService:
    def get_staff_types(self, session: Session) -> List[SchoolStaffTypeGet]:
        """Get all staff types"""
        try:
            result = session.exec(select(SchoolStaffType).order_by(SchoolStaffType.name)).all()
            return [SchoolStaffTypeGet.model_validate(r.dict()) for r in result]
        except Exception as e:
            logger.error(f"Error fetching staff types: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch staff types")
    
    def get_teacher_education_types(self, session: Session) -> List[TeacherEducationTypeGet]:
        """Get all teacher education types"""
        try:
            result = session.exec(select(TeacherEducationType).order_by(TeacherEducationType.name)).all()
            return [TeacherEducationTypeGet.model_validate(r.dict()) for r in result]
        except Exception as e:
            logger.error(f"Error fetching teacher education types: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch teacher education types")
    
    def get_teacher_salary_band_types(self, session: Session) -> List[TeacherSalaryBandTypeGet]:
        """Get all teacher salary band types"""
        try:
            result = session.exec(select(TeacherSalaryBandType).order_by(TeacherSalaryBandType.name)).all()
            return [TeacherSalaryBandTypeGet.model_validate(r.dict()) for r in result]
        except Exception as e:
            logger.error(f"Error fetching teacher salary band types: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch teacher salary band types")
    
    # District-level methods
    def get_district_staff(
        self, 
        session: Session, 
        year: Optional[int] = None,
        district_id: Optional[int] = None,
        staff_type_id: Optional[int] = None
    ) -> List[DistrictStaffGet]:
        """Get district staff data with optional filters"""
        try:
            # Create base query
            statement = select(
                DistrictStaff,
                SchoolStaffType
            ).join(
                District,
                DistrictStaff.district_id_fk == District.id
            ).join(
                SchoolStaffType,
                DistrictStaff.school_staff_type_id_fk == SchoolStaffType.id
            )
            
            # Apply filters
            if year is not None:
                statement = statement.where(DistrictStaff.year == year)
                
            if district_id is not None:
                statement = statement.where(DistrictStaff.district_id_fk == district_id)
                
            if staff_type_id is not None:
                statement = statement.where(DistrictStaff.school_staff_type_id_fk == staff_type_id)
                
            # Execute query
            result = session.exec(statement)
            
            staff_data = []
            for staff, staff_type in result:
                staff_type_data = staff_type.dict()
                
                data = {
                    "id": staff.id,
                    "district_id": staff.district_id_fk,
                    "year": staff.year,
                    "value": staff.value,
                    "staff_type": SchoolStaffTypeGet.model_validate(staff_type_data)
                }
                staff_data.append(DistrictStaffGet.model_validate(data))
                
            return staff_data
        except Exception as e:
            logger.error(f"Error fetching district staff data: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch district staff data")
    
    def get_district_teacher_education(
        self, 
        session: Session, 
        year: Optional[int] = None,
        district_id: Optional[int] = None,
        teacher_type_id: Optional[int] = None
    ) -> List[DistrictTeacherEducationGet]:
        """Get district teacher education data with optional filters"""
        try:
            # Create base query
            statement = select(
                DistrictTeacherEducation,
                TeacherEducationType
            ).join(
                District,
                DistrictTeacherEducation.district_id_fk == District.id
            ).join(
                TeacherEducationType,
                DistrictTeacherEducation.teacher_type_id_fk == TeacherEducationType.id
            )
            
            # Apply filters
            if year is not None:
                statement = statement.where(DistrictTeacherEducation.year == year)
                
            if district_id is not None:
                statement = statement.where(DistrictTeacherEducation.district_id_fk == district_id)
                
            if teacher_type_id is not None:
                statement = statement.where(DistrictTeacherEducation.teacher_type_id_fk == teacher_type_id)
                
            # Execute query
            result = session.exec(statement)
            
            education_data = []
            for education, teacher_type in result:
                teacher_type_data = teacher_type.dict()
                
                data = {
                    "id": education.id,
                    "district_id": education.district_id_fk,
                    "year": education.year,
                    "value": education.value,
                    "teacher_type": TeacherEducationTypeGet.model_validate(teacher_type_data)
                }
                education_data.append(DistrictTeacherEducationGet.model_validate(data))
                
            return education_data
        except Exception as e:
            logger.error(f"Error fetching district teacher education data: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch district teacher education data")
    
    def get_district_teacher_average_salary(
        self, 
        session: Session, 
        year: Optional[int] = None,
        district_id: Optional[int] = None
    ) -> List[DistrictTeacherAverageSalaryGet]:
        """Get district teacher average salary data with optional filters"""
        try:
            # Create base query
            statement = select(
                DistrictTeacherAverageSalary
            ).join(
                District,
                DistrictTeacherAverageSalary.district_id_fk == District.id
            )
            
            # Apply filters
            if year is not None:
                statement = statement.where(DistrictTeacherAverageSalary.year == year)
                
            if district_id is not None:
                statement = statement.where(DistrictTeacherAverageSalary.district_id_fk == district_id)
                
            # Execute query
            result = session.exec(statement)
            
            salary_data = []
            for salary in result:
                data = {
                    "id": salary.id,
                    "district_id": salary.district_id_fk,
                    "year": salary.year,
                    "salary": salary.salary
                }
                salary_data.append(DistrictTeacherAverageSalaryGet.model_validate(data))
                
            return salary_data
        except Exception as e:
            logger.error(f"Error fetching district teacher average salary data: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch district teacher average salary data")
    
    def get_district_teacher_salary_band(
        self, 
        session: Session, 
        year: Optional[int] = None,
        district_id: Optional[int] = None,
        salary_band_type_id: Optional[int] = None
    ) -> List[DistrictTeacherSalaryBandGet]:
        """Get district teacher salary band data with optional filters"""
        try:
            # Create base query
            statement = select(
                DistrictTeacherSalaryBand,
                TeacherSalaryBandType
            ).join(
                District,
                DistrictTeacherSalaryBand.district_id_fk == District.id
            ).join(
                TeacherSalaryBandType,
                DistrictTeacherSalaryBand.teacher_salary_band_type_id_fk == TeacherSalaryBandType.id
            )
            
            # Apply filters
            if year is not None:
                statement = statement.where(DistrictTeacherSalaryBand.year == year)
                
            if district_id is not None:
                statement = statement.where(DistrictTeacherSalaryBand.district_id_fk == district_id)
                
            if salary_band_type_id is not None:
                statement = statement.where(DistrictTeacherSalaryBand.teacher_salary_band_type_id_fk == salary_band_type_id)
                
            # Execute query
            result = session.exec(statement)
            
            salary_band_data = []
            for salary_band, salary_band_type in result:
                salary_band_type_data = salary_band_type.dict()
                
                data = {
                    "id": salary_band.id,
                    "district_id": salary_band.district_id_fk,
                    "year": salary_band.year,
                    "min_salary": salary_band.min_salary,
                    "max_salary": salary_band.max_salary,
                    "steps": salary_band.steps,
                    "salary_band_type": TeacherSalaryBandTypeGet.model_validate(salary_band_type_data)
                }
                salary_band_data.append(DistrictTeacherSalaryBandGet.model_validate(data))
                
            return salary_band_data
        except Exception as e:
            logger.error(f"Error fetching district teacher salary band data: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch district teacher salary band data")
    
    # State-level methods
    def get_state_staff(
        self, 
        session: Session, 
        year: Optional[int] = None,
        staff_type_id: Optional[int] = None
    ) -> List[StateStaffGet]:
        """Get state staff data with optional filters"""
        try:
            # Create base query
            statement = select(
                StateStaff,
                SchoolStaffType
            ).join(
                SchoolStaffType,
                StateStaff.school_staff_type_id_fk == SchoolStaffType.id
            )
            
            # Apply filters
            if year is not None:
                statement = statement.where(StateStaff.year == year)
                
            if staff_type_id is not None:
                statement = statement.where(StateStaff.school_staff_type_id_fk == staff_type_id)
                
            # Execute query
            result = session.exec(statement)
            
            staff_data = []
            for staff, staff_type in result:
                staff_type_data = staff_type.dict()
                
                data = {
                    "id": staff.id,
                    "year": staff.year,
                    "value": staff.value,
                    "staff_type": SchoolStaffTypeGet.model_validate(staff_type_data)
                }
                staff_data.append(StateStaffGet.model_validate(data))
                
            return staff_data
        except Exception as e:
            logger.error(f"Error fetching state staff data: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch state staff data")
    
    def get_state_teacher_education(
        self, 
        session: Session, 
        year: Optional[int] = None,
        teacher_type_id: Optional[int] = None
    ) -> List[StateTeacherEducationGet]:
        """Get state teacher education data with optional filters"""
        try:
            # Create base query
            statement = select(
                StateTeacherEducation,
                TeacherEducationType
            ).join(
                TeacherEducationType,
                StateTeacherEducation.teacher_type_id_fk == TeacherEducationType.id
            )
            
            # Apply filters
            if year is not None:
                statement = statement.where(StateTeacherEducation.year == year)
                
            if teacher_type_id is not None:
                statement = statement.where(StateTeacherEducation.teacher_type_id_fk == teacher_type_id)
                
            # Execute query
            result = session.exec(statement)
            
            education_data = []
            for education, teacher_type in result:
                teacher_type_data = teacher_type.dict()
                
                data = {
                    "id": education.id,
                    "year": education.year,
                    "value": education.value,
                    "teacher_type": TeacherEducationTypeGet.model_validate(teacher_type_data)
                }
                education_data.append(StateTeacherEducationGet.model_validate(data))
                
            return education_data
        except Exception as e:
            logger.error(f"Error fetching state teacher education data: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch state teacher education data")
    
    def get_state_teacher_average_salary(
        self, 
        session: Session, 
        year: Optional[int] = None
    ) -> List[StateTeacherAverageSalaryGet]:
        """Get state teacher average salary data with optional filters"""
        try:
            # Create base query
            statement = select(
                StateTeacherAverageSalary
            )
            
            # Apply filters
            if year is not None:
                statement = statement.where(StateTeacherAverageSalary.year == year)
                
            # Execute query
            result = session.exec(statement)
            
            salary_data = []
            for salary in result:
                data = {
                    "id": salary.id,
                    "year": salary.year,
                    "salary": salary.salary
                }
                salary_data.append(StateTeacherAverageSalaryGet.model_validate(data))
                
            return salary_data
        except Exception as e:
            logger.error(f"Error fetching state teacher average salary data: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch state teacher average salary data")
    
    def get_state_teacher_salary_band(
        self, 
        session: Session, 
        year: Optional[int] = None,
        salary_band_type_id: Optional[int] = None
    ) -> List[StateTeacherSalaryBandGet]:
        """Get state teacher salary band data with optional filters"""
        try:
            # Create base query
            statement = select(
                StateTeacherSalaryBand,
                TeacherSalaryBandType
            ).join(
                TeacherSalaryBandType,
                StateTeacherSalaryBand.teacher_salary_band_type_id_fk == TeacherSalaryBandType.id
            )
            
            # Apply filters
            if year is not None:
                statement = statement.where(StateTeacherSalaryBand.year == year)
                
            if salary_band_type_id is not None:
                statement = statement.where(StateTeacherSalaryBand.teacher_salary_band_type_id_fk == salary_band_type_id)
                
            # Execute query
            result = session.exec(statement)
            
            salary_band_data = []
            for salary_band, salary_band_type in result:
                salary_band_type_data = salary_band_type.dict()
                
                data = {
                    "teacher_salary_band_type_id": salary_band.teacher_salary_band_type_id_fk,
                    "year": salary_band.year,
                    "min_salary": salary_band.min_salary,
                    "max_salary": salary_band.max_salary,
                    "steps": salary_band.steps,
                    "salary_band_type": TeacherSalaryBandTypeGet.model_validate(salary_band_type_data)
                }
                salary_band_data.append(StateTeacherSalaryBandGet.model_validate(data))
                
            return salary_band_data
        except Exception as e:
            logger.error(f"Error fetching state teacher salary band data: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch state teacher salary band data")


staff_service = StaffService() 