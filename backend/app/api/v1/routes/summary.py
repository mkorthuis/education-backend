from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

from app.service.internal.llm.llm_factory import LLMFactory

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
        # Use the LLM factory to generate text
        response = LLMFactory.generate_text(request.message)
        
        return SummaryResponse(
            summary=response.text,
            provider=response.provider,
            model=response.model,
            usage=response.usage
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating summary: {str(e)}"
        ) 