from fastapi import APIRouter, Query, Path, HTTPException
from typing import List, Optional
from uuid import UUID

from app.api.v1.deps import SessionDep
from app.schema.finance_schema import (
    DOEFormGet, BalanceSheetGet, RevenueGet, ExpenditureGet,
    FinancialReportGet
)
from app.service.public.finance_service import finance_service

router = APIRouter()

@router.get("/report", 
    response_model=FinancialReportGet,
    summary="Get financial report",
    description="Retrieves a comprehensive financial report for a specific district and year, including DOE form data and all related financial data.",
    response_description="Financial report with DOE form and related financial data")
def get_financial_report(
    session: SessionDep,
    district_id: int = Query(..., description="District ID"),
    year: int = Query(..., description="Year of the financial report")
):
    """
    Get a comprehensive financial report for a specific district and year.
    
    This includes:
    - DOE Form data
    - Balance sheets
    - Revenues
    - Expenditures
    
    All related data is included with appropriate details.
    """
    return finance_service.get_financial_report(
        session=session,
        district_id=district_id,
        year=year
    ) 