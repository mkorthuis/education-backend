from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any, Optional

from app.api.v1.deps import SessionDep
from app.service.public.summary_service import SummaryService

router = APIRouter()

class SummaryRequest(BaseModel):
    """Request model for summary endpoint."""
    message: str = "I am a Jelly Donut"

class SummaryResponse(BaseModel):
    """Response model for summary endpoint."""
    summary: str
    provider: str
    model: str
    usage: Dict[str, Any] = {}

@router.post("/summary",
    summary="Generate summary using LLM",
    description="Send a message to the LLM provider (Gemini) and get a summary response",
    response_description="Summary response from LLM")
async def generate_summary(request: SummaryRequest) -> SummaryResponse:
    """
    Generate a summary using the configured LLM provider.
    
    Args:
        request: The request containing the message to summarize.
        
    Returns:
        A summary response from the LLM provider.
    """
    try:
        summary_service = SummaryService()
        result = summary_service.generate_basic_summary(request.message)
        
        return SummaryResponse(
            summary=result["summary"],
            provider=result["provider"],
            model=result["model"],
            usage=result["usage"]
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating summary: {str(e)}"
        )

class DistrictComparisonRequest(BaseModel):
    """Request model for district comparison endpoint."""
    district_id: int
    year: Optional[int] = None
    assessment_subgroup_id: Optional[int] = None
    assessment_subject_id: Optional[int] = None
    grade_id: Optional[int] = None

class DistrictComparisonResponse(BaseModel):
    """Response model for district comparison endpoint."""
    summary: str
    provider: str
    model: str
    usage: Dict[str, Any] = {}
    district_data_count: int
    state_data_count: int

@router.post("/district-comparison",
    summary="Compare district assessment data with state data using LLM",
    description="Get district and state assessment data, then use Gemini to compare and provide feedback on how the district compares to state averages",
    response_description="Comparison analysis from LLM")
async def compare_district_assessments(
    request: DistrictComparisonRequest,
    session: SessionDep
) -> DistrictComparisonResponse:
    """
    Compare district assessment data with state assessment data using Gemini.
    
    Args:
        request: The request containing district ID and optional filters.
        session: Database session.
        
    Returns:
        A comparison analysis from the LLM provider.
    """
    try:
        summary_service = SummaryService()
        result = summary_service.generate_district_comparison(
            session=session,
            district_id=request.district_id,
            year=request.year,
            assessment_subgroup_id=request.assessment_subgroup_id,
            assessment_subject_id=request.assessment_subject_id,
            grade_id=request.grade_id
        )
        
        return DistrictComparisonResponse(
            summary=result["summary"],
            provider=result["provider"],
            model=result["model"],
            usage=result["usage"],
            district_data_count=result["district_data_count"],
            state_data_count=result["state_data_count"]
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating district comparison: {str(e)}"
        )

class ComprehensiveDistrictSummaryRequest(BaseModel):
    """Request model for comprehensive district summary endpoint."""
    district_id: int
    year: Optional[int] = None

class ComprehensiveDistrictSummaryResponse(BaseModel):
    """Response model for comprehensive district summary endpoint."""
    comprehensive_summary: Dict[str, Any]
    academic_summary: Dict[str, Any]
    financial_summary: Dict[str, Any]
    graduation_summary: Dict[str, Any]
    safety_summary: Dict[str, Any]
    staff_summary: Dict[str, Any]
    enrollment_summary: Dict[str, Any]

@router.post("/comprehensive-district-summary",
    summary="Generate comprehensive district summary using all data types",
    description="Generate a comprehensive district analysis using academic, financial, graduation, safety, staff, and enrollment data, then provide an executive summary",
    response_description="Comprehensive district analysis from LLM")
async def generate_comprehensive_district_summary(
    request: ComprehensiveDistrictSummaryRequest,
    session: SessionDep
) -> ComprehensiveDistrictSummaryResponse:
    """
    Generate a comprehensive district summary using all available data types.
    
    Args:
        request: The request containing district ID and optional year filter.
        session: Database session.
        
    Returns:
        A comprehensive district analysis from the LLM provider.
    """
    try:
        summary_service = SummaryService()
        result = summary_service.generate_comprehensive_district_summary(
            session=session,
            district_id=request.district_id,
            year=request.year
        )
        
        return ComprehensiveDistrictSummaryResponse(
            comprehensive_summary=result["comprehensive_summary"],
            academic_summary=result["academic_summary"],
            financial_summary=result["financial_summary"],
            graduation_summary=result["graduation_summary"],
            safety_summary=result["safety_summary"],
            staff_summary=result["staff_summary"],
            enrollment_summary=result["enrollment_summary"]
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating comprehensive district summary: {str(e)}"
        )

 