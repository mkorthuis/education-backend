from typing import List, Dict, Any, Optional
import json
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlmodel import select

from app.service.internal.llm.llm_factory import LLMFactory
from app.service.public.assessment_service import AssessmentService
from app.service.public.finance_service import FinanceService
from app.service.public.outcome_service import OutcomeService
from app.service.public.safety_service import SafetyService
from app.service.public.staff_service import StaffService
from app.service.public.enrollment_service import EnrollmentService
from app.schema.assessment_schema import AssessmentGet, AssessmentGetSummary, AssessmentSubgroupGet, AssessmentSubjectGet
from app.model.assessment import AssessmentState, AssessmentDistrict, AssessmentSubgroup, AssessmentSubject
from app.model.location import District, Grade


class SummaryService:
    """Service for generating summaries and district comparisons using LLM."""
    
    def __init__(self):
        self.assessment_service = AssessmentService()
        self.finance_service = FinanceService()
        self.outcome_service = OutcomeService()
        self.safety_service = SafetyService()
        self.staff_service = StaffService()
        self.enrollment_service = EnrollmentService()
    
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
    
    def generate_comprehensive_district_summary(
        self,
        session: Session,
        district_id: int,
        year: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Generate a comprehensive district summary using all available data types.
        
        Args:
            session: Database session
            district_id: The ID of the district to analyze
            year: Optional year filter
            
        Returns:
            Dictionary containing comprehensive summary with all data type summaries
        """
        try:
            # Generate summaries for each data type
            academic_summary = self._generate_academic_summary(session, district_id, year)
            financial_summary = self._generate_financial_summary(session, district_id, year)
            graduation_summary = self._generate_graduation_summary(session, district_id, year)
            safety_summary = self._generate_safety_summary(session, district_id, year)
            staff_summary = self._generate_staff_summary(session, district_id, year)
            enrollment_summary = self._generate_enrollment_summary(session, district_id, year)
            
            # Combine all summaries and generate final comprehensive summary
            all_summaries = {
                "academic": academic_summary,
                "financial": financial_summary,
                "graduation": graduation_summary,
                "safety": safety_summary,
                "staff": staff_summary,
                "enrollment": enrollment_summary
            }
            
            # Generate comprehensive summary using LLM
            comprehensive_summary = self._generate_comprehensive_summary(all_summaries)
            
            return {
                "comprehensive_summary": comprehensive_summary,
                "academic_summary": academic_summary,
                "financial_summary": financial_summary,
                "graduation_summary": graduation_summary,
                "safety_summary": safety_summary,
                "staff_summary": staff_summary,
                "enrollment_summary": enrollment_summary
            }
            
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Error generating comprehensive district summary: {str(e)}"
            )
    
    def _generate_academic_summary(
        self,
        session: Session,
        district_id: int,
        year: Optional[int] = None
    ) -> Dict[str, Any]:
        """Generate academic assessment summary for a district."""
        try:
            # Get district assessment data
            district_assessments = self._get_district_assessments_with_details(
                session=session,
                district_id=district_id,
                year=year
            )
            
            # Get state assessment data
            state_assessments = self._get_state_assessments_with_details(
                session=session,
                year=year
            )
            
            if not district_assessments:
                return {"summary": "No academic data available", "data_count": 0}
            
            # Format data for LLM
            district_data = self._format_assessment_data(district_assessments)
            state_data = self._format_assessment_data(state_assessments)
            
            # Generate prompt for academic analysis
            prompt = f"""
            Analyze the academic assessment data for this district compared to state averages.
            
            DISTRICT DATA:
            {district_data}
            
            STATE DATA:
            {state_data}
            
            Provide a focused analysis of academic performance including:
            - Overall proficiency levels
            - Grade-level performance trends
            - Subject-specific strengths and weaknesses
            - Comparison to state averages
            - Key recommendations for improvement
            """
            
            response = LLMFactory.generate_text(prompt)
            
            return {
                "summary": response.text,
                "provider": response.provider,
                "model": response.model,
                "usage": response.usage,
                "data_count": len(district_assessments)
            }
            
        except Exception as e:
            return {"summary": f"Error generating academic summary: {str(e)}", "data_count": 0}
    
    def _generate_financial_summary(
        self,
        session: Session,
        district_id: int,
        year: Optional[int] = None
    ) -> Dict[str, Any]:
        """Generate financial summary for a district."""
        try:
            # TODO: Implement financial data retrieval and analysis
            # This is a stub for now
            prompt = f"""
            Analyze the financial data for district {district_id} for year {year or 'all available years'}.
            
            Provide analysis of:
            - Cost per pupil trends
            - Revenue and expenditure patterns
            - Financial efficiency metrics
            - Comparison to state averages
            - Key financial insights and recommendations
            """
            
            response = LLMFactory.generate_text(prompt)
            
            return {
                "summary": response.text,
                "provider": response.provider,
                "model": response.model,
                "usage": response.usage,
                "data_count": 0  # TODO: Implement actual data count
            }
            
        except Exception as e:
            return {"summary": f"Error generating financial summary: {str(e)}", "data_count": 0}
    
    def _generate_graduation_summary(
        self,
        session: Session,
        district_id: int,
        year: Optional[int] = None
    ) -> Dict[str, Any]:
        """Generate graduation summary for a district."""
        try:
            # TODO: Implement graduation data retrieval and analysis
            # This is a stub for now
            prompt = f"""
            Analyze the graduation and post-graduation data for district {district_id} for year {year or 'all available years'}.
            
            Provide analysis of:
            - Graduation rates and trends
            - Post-graduation outcomes
            - Early exit/dropout rates
            - Comparison to state averages
            - Key insights and recommendations
            """
            
            response = LLMFactory.generate_text(prompt)
            
            return {
                "summary": response.text,
                "provider": response.provider,
                "model": response.model,
                "usage": response.usage,
                "data_count": 0  # TODO: Implement actual data count
            }
            
        except Exception as e:
            return {"summary": f"Error generating graduation summary: {str(e)}", "data_count": 0}
    
    def _generate_safety_summary(
        self,
        session: Session,
        district_id: int,
        year: Optional[int] = None
    ) -> Dict[str, Any]:
        """Generate safety summary for a district."""
        try:
            # TODO: Implement safety data retrieval and analysis
            # This is a stub for now
            prompt = f"""
            Analyze the school safety data for district {district_id} for year {year or 'all available years'}.
            
            Provide analysis of:
            - Discipline incidents and trends
            - Bullying and harassment incidents
            - Restraint and seclusion data
            - Truancy rates
            - Comparison to state averages
            - Safety recommendations
            """
            
            response = LLMFactory.generate_text(prompt)
            
            return {
                "summary": response.text,
                "provider": response.provider,
                "model": response.model,
                "usage": response.usage,
                "data_count": 0  # TODO: Implement actual data count
            }
            
        except Exception as e:
            return {"summary": f"Error generating safety summary: {str(e)}", "data_count": 0}
    
    def _generate_staff_summary(
        self,
        session: Session,
        district_id: int,
        year: Optional[int] = None
    ) -> Dict[str, Any]:
        """Generate staff summary for a district."""
        try:
            # TODO: Implement staff data retrieval and analysis
            # This is a stub for now
            prompt = f"""
            Analyze the staff data for district {district_id} for year {year or 'all available years'}.
            
            Provide analysis of:
            - Staff counts and ratios
            - Teacher education levels
            - Teacher salary trends
            - Staff retention rates
            - Comparison to state averages
            - Staffing recommendations
            """
            
            response = LLMFactory.generate_text(prompt)
            
            return {
                "summary": response.text,
                "provider": response.provider,
                "model": response.model,
                "usage": response.usage,
                "data_count": 0  # TODO: Implement actual data count
            }
            
        except Exception as e:
            return {"summary": f"Error generating staff summary: {str(e)}", "data_count": 0}
    
    def _generate_enrollment_summary(
        self,
        session: Session,
        district_id: int,
        year: Optional[int] = None
    ) -> Dict[str, Any]:
        """Generate enrollment summary for a district."""
        try:
            # TODO: Implement enrollment data retrieval and analysis
            # This is a stub for now
            prompt = f"""
            Analyze the enrollment data for district {district_id} for year {year or 'all available years'}.
            
            Provide analysis of:
            - Enrollment trends and patterns
            - Grade-level enrollment distribution
            - Enrollment growth or decline
            - Comparison to state trends
            - Enrollment projections and recommendations
            """
            
            response = LLMFactory.generate_text(prompt)
            
            return {
                "summary": response.text,
                "provider": response.provider,
                "model": response.model,
                "usage": response.usage,
                "data_count": 0  # TODO: Implement actual data count
            }
            
        except Exception as e:
            return {"summary": f"Error generating enrollment summary: {str(e)}", "data_count": 0}
    
    def _generate_comprehensive_summary(self, all_summaries: Dict[str, Any]) -> Dict[str, Any]:
        """Generate a comprehensive summary combining all data type summaries."""
        try:
            # Create a structured summary of all data types
            summary_text = f"""
            ACADEMIC PERFORMANCE:
            {all_summaries.get('academic', {}).get('summary', 'No data available')}
            
            FINANCIAL ANALYSIS:
            {all_summaries.get('financial', {}).get('summary', 'No data available')}
            
            GRADUATION OUTCOMES:
            {all_summaries.get('graduation', {}).get('summary', 'No data available')}
            
            SCHOOL SAFETY:
            {all_summaries.get('safety', {}).get('summary', 'No data available')}
            
            STAFF ANALYSIS:
            {all_summaries.get('staff', {}).get('summary', 'No data available')}
            
            ENROLLMENT TRENDS:
            {all_summaries.get('enrollment', {}).get('summary', 'No data available')}
            """
            
            prompt = f"""
            Based on the following comprehensive district analysis, provide an executive summary that:
            
            {summary_text}
            
            Please provide:
            1. Executive Summary (2-3 paragraphs)
            2. Key Strengths (3-5 bullet points)
            3. Key Challenges (3-5 bullet points)
            4. Priority Recommendations (3-5 actionable items)
            5. Overall District Health Assessment (Excellent/Good/Fair/Needs Improvement)
            
            Focus on the most important insights and actionable recommendations for district leadership.
            """
            
            response = LLMFactory.generate_text(prompt)
            
            return {
                "summary": response.text,
                "provider": response.provider,
                "model": response.model,
                "usage": response.usage
            }
            
        except Exception as e:
            return {
                "summary": f"Error generating comprehensive summary: {str(e)}",
                "provider": "error",
                "model": "error",
                "usage": {}
            }
    
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