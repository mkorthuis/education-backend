from sqlalchemy.orm import Session, selectinload
from sqlmodel import select, col, or_, and_
from typing import List, Optional, Dict, Any, Union
from fastapi import HTTPException
import logging

from app.model.safety import (
    SchoolSafetyType, SchoolSafety, SchoolTruancy,
    SchoolDisciplineIncidentType, SchoolDisciplineIncident,
    SchoolDisciplineCountType, SchoolDisciplineCount,
    SchoolBullyingType, SchoolBullying,
    SchoolBullyingClassificationType, SchoolBullyingClassification,
    SchoolBullyingImpactType, SchoolBullyingImpact,
    SchoolHarassmentClassification, SchoolHarassment,
    SchoolRestraint, SchoolSeclusion
)
from app.model.location import School, District
from app.schema.safety_schema import (
    SchoolSafetyTypeGet, SchoolSafetyGet, TruancyGet,
    DisciplineIncidentTypeGet, DisciplineIncidentGet,
    DisciplineCountTypeGet, DisciplineCountGet,
    BullyingTypeGet, BullyingGet,
    BullyingClassificationTypeGet, BullyingClassificationGet,
    BullyingImpactTypeGet, BullyingImpactGet,
    HarassmentClassificationGet, HarassmentGet,
    RestraintGet, SeclusionGet
)

logger = logging.getLogger(__name__)

class SafetyService:
    def get_safety_types(self, session: Session) -> List[SchoolSafetyTypeGet]:
        """Get all school safety types"""
        try:
            result = session.exec(select(SchoolSafetyType).order_by(SchoolSafetyType.name)).all()
            return [SchoolSafetyTypeGet.model_validate(r.dict()) for r in result]
        except Exception as e:
            logger.error(f"Error fetching school safety types: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch school safety types")
            
    def get_discipline_incident_types(self, session: Session) -> List[DisciplineIncidentTypeGet]:
        """Get all discipline incident types"""
        try:
            result = session.exec(select(SchoolDisciplineIncidentType).order_by(SchoolDisciplineIncidentType.name)).all()
            return [DisciplineIncidentTypeGet.model_validate(r.dict()) for r in result]
        except Exception as e:
            logger.error(f"Error fetching discipline incident types: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch discipline incident types")
            
    def get_discipline_count_types(self, session: Session) -> List[DisciplineCountTypeGet]:
        """Get all discipline count types"""
        try:
            result = session.exec(select(SchoolDisciplineCountType).order_by(SchoolDisciplineCountType.name)).all()
            return [DisciplineCountTypeGet.model_validate(r.dict()) for r in result]
        except Exception as e:
            logger.error(f"Error fetching discipline count types: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch discipline count types")
            
    def get_bullying_types(self, session: Session) -> List[BullyingTypeGet]:
        """Get all bullying types"""
        try:
            result = session.exec(select(SchoolBullyingType).order_by(SchoolBullyingType.name)).all()
            return [BullyingTypeGet.model_validate(r.dict()) for r in result]
        except Exception as e:
            logger.error(f"Error fetching bullying types: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch bullying types")
            
    def get_bullying_classification_types(self, session: Session) -> List[BullyingClassificationTypeGet]:
        """Get all bullying classification types"""
        try:
            result = session.exec(select(SchoolBullyingClassificationType).order_by(SchoolBullyingClassificationType.name)).all()
            return [BullyingClassificationTypeGet.model_validate(r.dict()) for r in result]
        except Exception as e:
            logger.error(f"Error fetching bullying classification types: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch bullying classification types")
            
    def get_bullying_impact_types(self, session: Session) -> List[BullyingImpactTypeGet]:
        """Get all bullying impact types"""
        try:
            result = session.exec(select(SchoolBullyingImpactType).order_by(SchoolBullyingImpactType.name)).all()
            return [BullyingImpactTypeGet.model_validate(r.dict()) for r in result]
        except Exception as e:
            logger.error(f"Error fetching bullying impact types: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch bullying impact types")
            
    def get_harassment_classifications(self, session: Session) -> List[HarassmentClassificationGet]:
        """Get all harassment classifications"""
        try:
            result = session.exec(select(SchoolHarassmentClassification).order_by(SchoolHarassmentClassification.name)).all()
            return [HarassmentClassificationGet.model_validate(r.dict()) for r in result]
        except Exception as e:
            logger.error(f"Error fetching harassment classifications: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch harassment classifications")
    
    def _apply_common_filters(self, statement, model, year=None, school_id=None, district_id=None):
        """Apply common filters for safety-related queries"""
        if year is not None:
            statement = statement.where(model.year == year)
            
        if school_id is not None:
            statement = statement.where(model.school_id_fk == school_id)
            
        if district_id is not None:
            # Join to School to filter by district_id
            statement = statement.join(
                School, 
                model.school_id_fk == School.id
            ).where(School.district_id_fk == district_id)
            
        return statement
    
    def get_school_safety(
        self, 
        session: Session, 
        year: Optional[int] = None,
        school_id: Optional[int] = None,
        district_id: Optional[int] = None,
        safety_type_id: Optional[int] = None
    ) -> List[SchoolSafetyGet]:
        """Get school safety data with optional filters"""
        try:
            # Create base query
            statement = select(
                SchoolSafety,
                SchoolSafetyType
            ).join(
                School,
                SchoolSafety.school_id_fk == School.id
            ).join(
                SchoolSafetyType,
                SchoolSafety.school_safety_type_id_fk == SchoolSafetyType.id
            )
            
            # Apply common filters
            statement = self._apply_common_filters(statement, SchoolSafety, year, school_id, district_id)
            
            # Apply specific filter
            if safety_type_id is not None:
                statement = statement.where(SchoolSafety.school_safety_type_id_fk == safety_type_id)
                
            # Execute query
            result = session.exec(statement)
            
            safety_data = []
            for safety, safety_type in result:
                safety_type_data = safety_type.dict()
                
                data = {
                    "id": safety.id,
                    "school_id": safety.school_id_fk,
                    "year": safety.year,
                    "count": safety.count,
                    "safety_type": SchoolSafetyTypeGet.model_validate(safety_type_data)
                }
                safety_data.append(SchoolSafetyGet.model_validate(data))
                
            return safety_data
        except Exception as e:
            logger.error(f"Error fetching school safety data: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch school safety data")
    
    def get_truancy(
        self, 
        session: Session, 
        year: Optional[int] = None,
        school_id: Optional[int] = None,
        district_id: Optional[int] = None
    ) -> List[TruancyGet]:
        """Get truancy data with optional filters"""
        try:
            # Create base query
            statement = select(
                SchoolTruancy
            ).join(
                School,
                SchoolTruancy.school_id_fk == School.id
            )
            
            # Apply common filters
            statement = self._apply_common_filters(statement, SchoolTruancy, year, school_id, district_id)
                
            # Execute query
            result = session.exec(statement)
            
            truancy_data = []
            for truancy in result:
                data = {
                    "id": truancy.id,
                    "school_id": truancy.school_id_fk,
                    "year": truancy.year,
                    "count": truancy.count
                }
                truancy_data.append(TruancyGet.model_validate(data))
                
            return truancy_data
        except Exception as e:
            logger.error(f"Error fetching truancy data: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch truancy data")
    
    def get_discipline_incidents(
        self, 
        session: Session, 
        year: Optional[int] = None,
        school_id: Optional[int] = None,
        district_id: Optional[int] = None,
        discipline_incident_type_id: Optional[int] = None
    ) -> List[DisciplineIncidentGet]:
        """Get discipline incident data with optional filters"""
        try:
            # Create base query
            statement = select(
                SchoolDisciplineIncident,
                SchoolDisciplineIncidentType
            ).join(
                School,
                SchoolDisciplineIncident.school_id_fk == School.id
            ).join(
                SchoolDisciplineIncidentType,
                SchoolDisciplineIncident.school_discipline_incident_type_id_fk == SchoolDisciplineIncidentType.id
            )
            
            # Apply common filters
            statement = self._apply_common_filters(statement, SchoolDisciplineIncident, year, school_id, district_id)
            
            # Apply specific filter
            if discipline_incident_type_id is not None:
                statement = statement.where(SchoolDisciplineIncident.school_discipline_incident_type_id_fk == discipline_incident_type_id)
                
            # Execute query
            result = session.exec(statement)
            
            incident_data = []
            for incident, incident_type in result:
                incident_type_data = incident_type.dict()
                
                data = {
                    "id": incident.id,
                    "school_id": incident.school_id_fk,
                    "year": incident.year,
                    "count": incident.count,
                    "incident_type": DisciplineIncidentTypeGet.model_validate(incident_type_data)
                }
                incident_data.append(DisciplineIncidentGet.model_validate(data))
                
            return incident_data
        except Exception as e:
            logger.error(f"Error fetching discipline incident data: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch discipline incident data")
    
    def get_discipline_counts(
        self, 
        session: Session, 
        year: Optional[int] = None,
        school_id: Optional[int] = None,
        district_id: Optional[int] = None,
        discipline_count_type_id: Optional[int] = None
    ) -> List[DisciplineCountGet]:
        """Get discipline count data with optional filters"""
        try:
            # Create base query
            statement = select(
                SchoolDisciplineCount,
                SchoolDisciplineCountType
            ).join(
                School,
                SchoolDisciplineCount.school_id_fk == School.id
            ).join(
                SchoolDisciplineCountType,
                SchoolDisciplineCount.school_discipline_count_type_id_fk == SchoolDisciplineCountType.id
            )
            
            # Apply common filters
            statement = self._apply_common_filters(statement, SchoolDisciplineCount, year, school_id, district_id)
            
            # Apply specific filter
            if discipline_count_type_id is not None:
                statement = statement.where(SchoolDisciplineCount.school_discipline_count_type_id_fk == discipline_count_type_id)
                
            # Execute query
            result = session.exec(statement)
            
            count_data = []
            for count, count_type in result:
                count_type_data = count_type.dict()
                
                data = {
                    "id": count.id,
                    "school_id": count.school_id_fk,
                    "year": count.year,
                    "count": count.count,
                    "count_type": DisciplineCountTypeGet.model_validate(count_type_data)
                }
                count_data.append(DisciplineCountGet.model_validate(data))
                
            return count_data
        except Exception as e:
            logger.error(f"Error fetching discipline count data: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch discipline count data")
    
    def get_bullying(
        self, 
        session: Session, 
        year: Optional[int] = None,
        school_id: Optional[int] = None,
        district_id: Optional[int] = None,
        bullying_type_id: Optional[int] = None
    ) -> List[BullyingGet]:
        """Get bullying data with optional filters"""
        try:
            # Create base query
            statement = select(
                SchoolBullying,
                SchoolBullyingType
            ).join(
                School,
                SchoolBullying.school_id_fk == School.id
            ).join(
                SchoolBullyingType,
                SchoolBullying.school_bullying_type_id_fk == SchoolBullyingType.id
            )
            
            # Apply common filters
            statement = self._apply_common_filters(statement, SchoolBullying, year, school_id, district_id)
            
            # Apply specific filter
            if bullying_type_id is not None:
                statement = statement.where(SchoolBullying.school_bullying_type_id_fk == bullying_type_id)
                
            # Execute query
            result = session.exec(statement)
            
            bullying_data = []
            for bullying, bullying_type in result:
                bullying_type_data = bullying_type.dict()
                
                data = {
                    "id": bullying.id,
                    "school_id": bullying.school_id_fk,
                    "year": bullying.year,
                    "reported": bullying.reported,
                    "investigated_actual": bullying.investigated_actual,
                    "bullying_type": BullyingTypeGet.model_validate(bullying_type_data)
                }
                bullying_data.append(BullyingGet.model_validate(data))
                
            return bullying_data
        except Exception as e:
            logger.error(f"Error fetching bullying data: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch bullying data")
    
    def get_bullying_classifications(
        self, 
        session: Session, 
        year: Optional[int] = None,
        school_id: Optional[int] = None,
        district_id: Optional[int] = None,
        bullying_classification_type_id: Optional[int] = None
    ) -> List[BullyingClassificationGet]:
        """Get bullying classification data with optional filters"""
        try:
            # Create base query
            statement = select(
                SchoolBullyingClassification,
                SchoolBullyingClassificationType
            ).join(
                School,
                SchoolBullyingClassification.school_id_fk == School.id
            ).join(
                SchoolBullyingClassificationType,
                SchoolBullyingClassification.school_bullying_classification_type_id_fk == SchoolBullyingClassificationType.id
            )
            
            # Apply common filters
            statement = self._apply_common_filters(statement, SchoolBullyingClassification, year, school_id, district_id)
            
            # Apply specific filter
            if bullying_classification_type_id is not None:
                statement = statement.where(SchoolBullyingClassification.school_bullying_classification_type_id_fk == bullying_classification_type_id)
                
            # Execute query
            result = session.exec(statement)
            
            classification_data = []
            for classification, classification_type in result:
                classification_type_data = classification_type.dict()
                
                data = {
                    "id": classification.id,
                    "school_id": classification.school_id_fk,
                    "year": classification.year,
                    "count": classification.count,
                    "classification_type": BullyingClassificationTypeGet.model_validate(classification_type_data)
                }
                classification_data.append(BullyingClassificationGet.model_validate(data))
                
            return classification_data
        except Exception as e:
            logger.error(f"Error fetching bullying classification data: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch bullying classification data")
    
    def get_bullying_impacts(
        self, 
        session: Session, 
        year: Optional[int] = None,
        school_id: Optional[int] = None,
        district_id: Optional[int] = None,
        bullying_impact_type_id: Optional[int] = None
    ) -> List[BullyingImpactGet]:
        """Get bullying impact data with optional filters"""
        try:
            # Create base query
            statement = select(
                SchoolBullyingImpact,
                SchoolBullyingImpactType
            ).join(
                School,
                SchoolBullyingImpact.school_id_fk == School.id
            ).join(
                SchoolBullyingImpactType,
                SchoolBullyingImpact.school_bullying_impact_type_id_fk == SchoolBullyingImpactType.id
            )
            
            # Apply common filters
            statement = self._apply_common_filters(statement, SchoolBullyingImpact, year, school_id, district_id)
            
            # Apply specific filter
            if bullying_impact_type_id is not None:
                statement = statement.where(SchoolBullyingImpact.school_bullying_impact_type_id_fk == bullying_impact_type_id)
                
            # Execute query
            result = session.exec(statement)
            
            impact_data = []
            for impact, impact_type in result:
                impact_type_data = impact_type.dict()
                
                data = {
                    "id": impact.id,
                    "school_id": impact.school_id_fk,
                    "year": impact.year,
                    "count": impact.count,
                    "impact_type": BullyingImpactTypeGet.model_validate(impact_type_data)
                }
                impact_data.append(BullyingImpactGet.model_validate(data))
                
            return impact_data
        except Exception as e:
            logger.error(f"Error fetching bullying impact data: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch bullying impact data")
    
    def get_harassment(
        self, 
        session: Session, 
        year: Optional[int] = None,
        school_id: Optional[int] = None,
        district_id: Optional[int] = None,
        harassment_classification_id: Optional[int] = None
    ) -> List[HarassmentGet]:
        """Get harassment data with optional filters"""
        try:
            # Create base query
            statement = select(
                SchoolHarassment,
                SchoolHarassmentClassification
            ).join(
                School,
                SchoolHarassment.school_id_fk == School.id
            ).join(
                SchoolHarassmentClassification,
                SchoolHarassment.school_harassment_classification_id_fk == SchoolHarassmentClassification.id
            )
            
            # Apply common filters
            statement = self._apply_common_filters(statement, SchoolHarassment, year, school_id, district_id)
            
            # Apply specific filter
            if harassment_classification_id is not None:
                statement = statement.where(SchoolHarassment.school_harassment_classification_id_fk == harassment_classification_id)
                
            # Execute query
            result = session.exec(statement)
            
            harassment_data = []
            for harassment, classification in result:
                classification_data = classification.dict()
                
                data = {
                    "id": harassment.id,
                    "school_id": harassment.school_id_fk,
                    "year": harassment.year,
                    "incident_count": harassment.incident_count,
                    "student_impact_count": harassment.student_impact_count,
                    "student_engaged_count": harassment.student_engaged_count,
                    "classification": HarassmentClassificationGet.model_validate(classification_data)
                }
                harassment_data.append(HarassmentGet.model_validate(data))
                
            return harassment_data
        except Exception as e:
            logger.error(f"Error fetching harassment data: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch harassment data")
    
    def get_restraint(
        self, 
        session: Session, 
        year: Optional[int] = None,
        school_id: Optional[int] = None,
        district_id: Optional[int] = None
    ) -> List[RestraintGet]:
        """Get restraint data with optional filters"""
        try:
            # Create base query
            statement = select(
                SchoolRestraint
            ).join(
                School,
                SchoolRestraint.school_id_fk == School.id
            )
            
            # Apply common filters
            statement = self._apply_common_filters(statement, SchoolRestraint, year, school_id, district_id)
                
            # Execute query
            result = session.exec(statement)
            
            restraint_data = []
            for restraint in result:
                data = {
                    "id": restraint.id,
                    "school_id": restraint.school_id_fk,
                    "year": restraint.year,
                    "generated": restraint.generated,
                    "active_investigation": restraint.active_investigation,
                    "closed_investigation": restraint.closed_investigation,
                    "bodily_injury": restraint.bodily_injury,
                    "serious_injury": restraint.serious_injury
                }
                restraint_data.append(RestraintGet.model_validate(data))
                
            return restraint_data
        except Exception as e:
            logger.error(f"Error fetching restraint data: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch restraint data")
    
    def get_seclusion(
        self, 
        session: Session, 
        year: Optional[int] = None,
        school_id: Optional[int] = None,
        district_id: Optional[int] = None
    ) -> List[SeclusionGet]:
        """Get seclusion data with optional filters"""
        try:
            # Create base query
            statement = select(
                SchoolSeclusion
            ).join(
                School,
                SchoolSeclusion.school_id_fk == School.id
            )
            
            # Apply common filters
            statement = self._apply_common_filters(statement, SchoolSeclusion, year, school_id, district_id)
                
            # Execute query
            result = session.exec(statement)
            
            seclusion_data = []
            for seclusion in result:
                data = {
                    "id": seclusion.id,
                    "school_id": seclusion.school_id_fk,
                    "year": seclusion.year,
                    "generated": seclusion.generated,
                    "active_investigation": seclusion.active_investigation,
                    "closed_investigation": seclusion.closed_investigation
                }
                seclusion_data.append(SeclusionGet.model_validate(data))
                
            return seclusion_data
        except Exception as e:
            logger.error(f"Error fetching seclusion data: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch seclusion data")


safety_service = SafetyService() 