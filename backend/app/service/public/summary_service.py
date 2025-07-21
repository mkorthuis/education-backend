from typing import List, Dict, Any, Optional
import json
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlmodel import select

from app.service.internal.llm.llm_factory import LLMFactory
from app.service.public.assessment_service import AssessmentService
from app.schema.assessment_schema import AssessmentGet, AssessmentGetSummary, AssessmentSubgroupGet, AssessmentSubjectGet
from app.model.assessment import AssessmentState, AssessmentDistrict, AssessmentSubgroup, AssessmentSubject
from app.model.location import District, Grade


class SummaryService:
    """Service for generating summaries and district comparisons using LLM."""
    
    def __init__(self):
        self.assessment_service = AssessmentService()
    
    def generate_basic_summary(self, message: str) -> Dict[str, Any]:
        """
        Generate a basic summary using the LLM.
        
        Args:
            message: The message to summarize
            
        Returns:
            Dictionary containing summary response with text, provider, model, and usage
        """
        try:
            # Create a simple JSON object with the message
            data = {"message": message}
            
            # Use the LLM factory to generate the summary
            response = LLMFactory.generate_text(json.dumps(data))
            
            return {
                "summary": response.text,
                "provider": response.provider,
                "model": response.model,
                "usage": response.usage
            }
            
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Error generating summary: {str(e)}"
            )
    
    def generate_district_comparison(
        self,
        session: Session,
        district_id: int,
        year: Optional[int] = None,
        assessment_subgroup_id: Optional[int] = None,
        assessment_subject_id: Optional[int] = None,
        grade_id: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Generate a district comparison analysis using LLM.
        
        Args:
            session: Database session
            district_id: The ID of the district to analyze
            year: Optional year filter
            assessment_subgroup_id: Optional subgroup filter
            assessment_subject_id: Optional subject filter
            grade_id: Optional grade filter
            
        Returns:
            Dictionary containing comparison response with summary, metadata, and data counts
        """
        try:
            # Get district assessment data with details
            district_assessments = self._get_district_assessments_with_details(
                session=session,
                district_id=district_id,
                year=year,
                assessment_subgroup_id=assessment_subgroup_id,
                assessment_subject_id=assessment_subject_id,
                grade_id=grade_id
            )
            
            # Get state assessment data with details
            state_assessments = self._get_state_assessments_with_details(
                session=session,
                year=year,
                assessment_subgroup_id=assessment_subgroup_id,
                assessment_subject_id=assessment_subject_id,
                grade_id=grade_id
            )
            
            if not district_assessments:
                raise HTTPException(
                    status_code=404,
                    detail=f"No assessment data found for district ID {district_id}"
                )
            
            # Prepare the prompt for Gemini
            district_name = district_assessments[0].district_name if district_assessments else "Unknown District"
            
            prompt = f"""
            I need you to analyze and compare assessment data for {district_name} (District ID: {district_id}) with state-level assessment data.

            The data is provided as JSON objects with the following structure:
            - Grouped by district (e.g., "Test District", "State")
            - Then by student subgroup (e.g., "All Students", "Economically Disadvantaged")
            - Then by grade level (e.g., "Grade 3", "Grade 8")
            - Then by subject (e.g., "Mathematics", "English Language Arts")
            - Finally by year (chronological order)

            DISTRICT ASSESSMENT DATA (JSON):
            {self._format_assessment_data(district_assessments)}

            STATE ASSESSMENT DATA (JSON):
            {self._format_assessment_data(state_assessments)}

            Please provide a focused analysis with the following priorities:

            PRIMARY FOCUS (Analyze in detail):
            1. "All Students" subgroup performance across all grades and subjects
            2. Gender-based comparisons (Male/Female) if available
            3. Grade-level performance trends and comparisons

            SECONDARY FOCUS (Only mention significant variations):
            4. Other demographic subgroups (e.g., "Economically Disadvantaged", "Students with Disabilities") - only call out if there are substantial differences from state averages or concerning trends
            5. Skip analysis of subgroups with minimal data (very small student counts)

            ANALYSIS REQUIREMENTS:
            - Compare the most recent year data against state averages
            - Identify trends over time and years where performance changed dramatically
            - Analyze participation rates: state if overall participation is in line with state averages or if specific groups show large variations
            - Focus on proficiency levels (below_proficient_%, near_proficient_%, proficient_%, above_proficient_%)
            - Highlight any significant gaps between district and state performance
            - Identify specific grades or subjects where the district excels or struggles

            Please format your response in a clear, structured manner suitable for educational stakeholders, with clear sections for:
            1. Overall Performance Summary
            2. Grade-Level Analysis
            3. Subject-Specific Performance
            4. Participation Rate Analysis
            5. Key Recommendations
            """
            
            # Use the LLM factory to generate the comparison
            response = LLMFactory.generate_text(prompt)
            
            return {
                "summary": response.text,
                "provider": response.provider,
                "model": response.model,
                "usage": response.usage,
                "district_data_count": len(district_assessments),
                "state_data_count": len(state_assessments)
            }
            
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Error generating district comparison: {str(e)}"
            )
    
    def _format_assessment_data(self, assessments: List[AssessmentGetSummary]) -> str:
        """
        Format assessment data as JSON for the LLM prompt, grouped by district, subgroup, grade, and subject.
        
        Args:
            assessments: List of assessment data
            
        Returns:
            JSON string representation of the grouped assessment data
        """
        if not assessments:
            return "No data available"
        
        # Group assessments by district, subgroup, grade, and subject
        grouped_data = {}
        
        for assessment in assessments:
            district = assessment.district_name or "State"
            subgroup = assessment.subgroup_name or f"Subgroup {assessment.assessment_subgroup_id}"
            grade = assessment.grade_name or "All Grades"
            subject = assessment.subject_name or f"Subject {assessment.assessment_subject_id}"
            year = assessment.year
            
            # Initialize nested structure if not exists
            if district not in grouped_data:
                grouped_data[district] = {}
            if subgroup not in grouped_data[district]:
                grouped_data[district][subgroup] = {}
            if grade not in grouped_data[district][subgroup]:
                grouped_data[district][subgroup][grade] = {}
            if subject not in grouped_data[district][subgroup][grade]:
                grouped_data[district][subgroup][grade][subject] = {}
            if year not in grouped_data[district][subgroup][grade][subject]:
                grouped_data[district][subgroup][grade][subject][year] = []
            
            # Convert assessment to dictionary (without district since it's now the top-level key)
            assessment_dict = {
                "students": f"{assessment.total_fay_students_low or 0}-{assessment.total_fay_students_high or 0}",
                "below_proficient_%": assessment.level_1_percentage if assessment.level_1_percentage is not None else "less than 10%",
                "near_proficient_%": assessment.level_2_percentage if assessment.level_2_percentage is not None else "less than 10%",
                "proficient_%": assessment.level_3_percentage if assessment.level_3_percentage is not None else "less than 10%",
                "above_proficient_%": assessment.level_4_percentage if assessment.level_4_percentage is not None else "less than 10%",
                "participation_percentage": assessment.participate_percentage
            }
            
            grouped_data[district][subgroup][grade][subject][year].append(assessment_dict)
        
        # Convert to JSON string with proper formatting
        return json.dumps(grouped_data, indent=2)
    
    def _get_district_assessments_with_details(
        self,
        session: Session,
        district_id: Optional[int] = None,
        year: Optional[int] = None,
        assessment_subgroup_id: Optional[int] = None,
        assessment_subject_id: Optional[int] = None,
        grade_id: Optional[int] = None
    ) -> List[AssessmentGetSummary]:
        """Get district level assessment data with subgroup and grade details"""
        try:
            # Create a query selecting the models with relationships
            statement = select(
                AssessmentDistrict,
                District,
                AssessmentSubgroup,
                AssessmentSubject,
                Grade
            ).join(
                District, 
                AssessmentDistrict.district_id_fk == District.id
            ).join(
                AssessmentSubgroup,
                AssessmentDistrict.assessment_subgroup_id_fk == AssessmentSubgroup.id
            ).join(
                AssessmentSubject,
                AssessmentDistrict.assessment_subject_id_fk == AssessmentSubject.id
            ).join(
                Grade,
                AssessmentDistrict.grade_id_fk == Grade.id,
                isouter=True  # Use outer join for grade since it can be null
            )
            
            # Apply common filters
            statement = self._apply_common_filters(
                statement, 
                AssessmentDistrict, 
                year, 
                assessment_subgroup_id, 
                assessment_subject_id, 
                grade_id
            )
            
            # Add district-specific filter
            if district_id is not None:
                statement = statement.where(AssessmentDistrict.district_id_fk == district_id)
            
            result = session.exec(statement)
            
            assessments = []
            for district_assmt, district, subgroup, subject, grade in result:
                assessment_data = self._create_assessment_data(
                    district_assmt,
                    district_name=district.name,
                    district_id=district_assmt.district_id_fk
                )
                # Add subgroup and grade information
                assessment_data.update({
                    "subgroup_name": subgroup.name,
                    "subject_name": subject.name,
                    "grade_name": grade.name if grade else "All Grades"
                })
                assessments.append(AssessmentGetSummary.model_validate(assessment_data))
                
            return assessments
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to fetch district assessment data: {str(e)}"
            )
    
    def _get_state_assessments_with_details(
        self,
        session: Session,
        year: Optional[int] = None,
        assessment_subgroup_id: Optional[int] = None,
        assessment_subject_id: Optional[int] = None,
        grade_id: Optional[int] = None
    ) -> List[AssessmentGetSummary]:
        """Get state level assessment data with subgroup and grade details"""
        try:
            # Create a query selecting the models with relationships
            statement = select(
                AssessmentState,
                AssessmentSubgroup,
                AssessmentSubject,
                Grade
            ).join(
                AssessmentSubgroup,
                AssessmentState.assessment_subgroup_id_fk == AssessmentSubgroup.id
            ).join(
                AssessmentSubject,
                AssessmentState.assessment_subject_id_fk == AssessmentSubject.id
            ).join(
                Grade,
                AssessmentState.grade_id_fk == Grade.id,
                isouter=True  # Use outer join for grade since it can be null
            )
            
            # Apply common filters
            statement = self._apply_common_filters(
                statement, 
                AssessmentState, 
                year, 
                assessment_subgroup_id, 
                assessment_subject_id, 
                grade_id
            )
            
            result = session.exec(statement)
            
            assessments = []
            for state, subgroup, subject, grade in result:
                assessment_data = self._create_assessment_data(state)
                # Add subgroup and grade information
                assessment_data.update({
                    "subgroup_name": subgroup.name,
                    "subject_name": subject.name,
                    "grade_name": grade.name if grade else "All Grades"
                })
                assessments.append(AssessmentGetSummary.model_validate(assessment_data))
                
            return assessments
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to fetch state assessment data: {str(e)}"
            )
    
    def _apply_common_filters(self, statement, model, year=None, assessment_subgroup_id=None, 
                             assessment_subject_id=None, grade_id=None):
        """Apply common filters to assessment queries"""
        if year is not None:
            statement = statement.where(model.year == year)
            
        if assessment_subgroup_id is not None:
            statement = statement.where(model.assessment_subgroup_id_fk == assessment_subgroup_id)
            
        if assessment_subject_id is not None:
            statement = statement.where(model.assessment_subject_id_fk == assessment_subject_id)
            
        if grade_id is not None:
            if grade_id == 999:
                # Special case: grade_id 999 searches for NULL grade_id_fk
                statement = statement.where(model.grade_id_fk.is_(None))
            else:
                statement = statement.where(model.grade_id_fk == grade_id)
            
        return statement
    
    def _create_assessment_data(self, 
                               assessment_model,
                               district_name: Optional[str] = None,
                               school_name: Optional[str] = None,
                               district_id: Optional[int] = None,
                               school_id: Optional[int] = None) -> Dict[str, Any]:
        """Create assessment data dictionary from assessment model"""
        return {
            "id": assessment_model.id,
            "year": assessment_model.year,
            "district_id": district_id,
            "school_id": school_id,
            "assessment_subgroup_id": assessment_model.assessment_subgroup_id_fk,
            "assessment_subject_id": assessment_model.assessment_subject_id_fk,
            "grade_id": assessment_model.grade_id_fk,
            "total_fay_students_low": assessment_model.total_fay_students_low,
            "total_fay_students_high": assessment_model.total_fay_students_high,
            "level_1_percentage": assessment_model.level_1_percentage,
            "level_1_percentage_exception": assessment_model.level_1_percentage_exception,
            "level_2_percentage": assessment_model.level_2_percentage,
            "level_2_percentage_exception": assessment_model.level_2_percentage_exception,
            "level_3_percentage": assessment_model.level_3_percentage,
            "level_3_percentage_exception": assessment_model.level_3_percentage_exception,
            "level_4_percentage": assessment_model.level_4_percentage,
            "level_4_percentage_exception": assessment_model.level_4_percentage_exception,
            "above_proficient_percentage": assessment_model.above_proficient_percentage,
            "above_proficient_percentage_exception": assessment_model.above_proficient_percentage_exception,
            "participate_percentage": assessment_model.participate_percentage,
            "mean_sgp": assessment_model.mean_sgp,
            "average_score": assessment_model.average_score,
            "district_name": district_name,
            "school_name": school_name
        } 