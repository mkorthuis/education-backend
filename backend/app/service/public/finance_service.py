from typing import List, Optional, Dict, Any
from sqlmodel import Session, select
from fastapi import HTTPException

from app.model.finance import (
    DOEForm, BalanceSheet, Revenue, Expenditure,
    BalanceEntryType, BalanceFundType,
    RevenueEntryType, RevenueFundType,
    ExpenditureEntryType, ExpenditureFundType
)
from app.model.location import District
from app.schema.finance_schema import (
    DOEFormGet, BalanceSheetGet, RevenueGet, ExpenditureGet,
    FinancialReportGet
)
from app.schema.location_schema import DistrictGet

class FinanceService:
    def get_doe_form(self, session: Session, district_id: int, year: int) -> Optional[DOEForm]:
        """Get DOE form by district_id and year."""
        statement = select(DOEForm).where(
            DOEForm.district_id_fk == district_id,
            DOEForm.year == year
        )
        return session.exec(statement).first()
    
    def get_balance_sheets(self, session: Session, doe_form_id: int) -> List[BalanceSheet]:
        """Get balance sheets for a DOE form."""
        statement = select(BalanceSheet).where(BalanceSheet.doe_form_id_fk == doe_form_id)
        return session.exec(statement).all()
    
    def get_revenues(self, session: Session, doe_form_id: int) -> List[Revenue]:
        """Get revenues for a DOE form."""
        statement = select(Revenue).where(Revenue.doe_form_id_fk == doe_form_id)
        return session.exec(statement).all()
    
    def get_expenditures(self, session: Session, doe_form_id: int) -> List[Expenditure]:
        """Get expenditures for a DOE form."""
        statement = select(Expenditure).where(Expenditure.doe_form_id_fk == doe_form_id)
        return session.exec(statement).all()
    
    def _enhance_balance_sheets(self, session: Session, balance_sheets: List[BalanceSheet]) -> List[BalanceSheetGet]:
        """Enhance balance sheets with related data."""
        result = []
        for bs in balance_sheets:
            # Get related entry type and fund type
            entry_type = session.get(BalanceEntryType, bs.balance_entry_type_id_fk)
            fund_type = session.get(BalanceFundType, bs.balance_fund_type_id_fk)
            
            # Convert to DTO
            bs_dto = BalanceSheetGet.from_orm(bs)
            
            # Add related data if available
            if entry_type:
                bs_dto.entry_type = entry_type
            
            if fund_type:
                bs_dto.fund_type = fund_type
                
            result.append(bs_dto)
            
        return result
    
    def _enhance_revenues(self, session: Session, revenues: List[Revenue]) -> List[RevenueGet]:
        """Enhance revenues with related data."""
        result = []
        for rev in revenues:
            # Get related entry type and fund type
            entry_type = session.get(RevenueEntryType, rev.revenue_entry_type_id_fk)
            fund_type = session.get(RevenueFundType, rev.revenue_fund_type_id_fk)
            
            # Convert to DTO
            rev_dto = RevenueGet.from_orm(rev)
            
            # Add related data if available
            if entry_type:
                rev_dto.entry_type = entry_type
            
            if fund_type:
                rev_dto.fund_type = fund_type
                
            result.append(rev_dto)
            
        return result
    
    def _enhance_expenditures(self, session: Session, expenditures: List[Expenditure]) -> List[ExpenditureGet]:
        """Enhance expenditures with related data."""
        result = []
        for exp in expenditures:
            # Get related entry type and fund type
            entry_type = session.get(ExpenditureEntryType, exp.expenditure_entry_type_id_fk)
            fund_type = session.get(ExpenditureFundType, exp.expenditure_fund_type_id_fk)
            
            # Convert to DTO
            exp_dto = ExpenditureGet.from_orm(exp)
            
            # Add related data if available
            if entry_type:
                exp_dto.entry_type = entry_type
            
            if fund_type:
                exp_dto.fund_type = fund_type
                
            result.append(exp_dto)
            
        return result
    
    def get_financial_report(self, session: Session, district_id: int, year: int) -> FinancialReportGet:
        """
        Get comprehensive financial report including DOE form and all related financial data
        for a specific district and year.
        """
        # Get the DOE form
        doe_form = self.get_doe_form(session, district_id, year)
        if not doe_form:
            raise HTTPException(
                status_code=404, 
                detail=f"Financial report not found for district ID {district_id} and year {year}"
            )
        
        # Get related data
        balance_sheets = self.get_balance_sheets(session, doe_form.id)
        revenues = self.get_revenues(session, doe_form.id)
        expenditures = self.get_expenditures(session, doe_form.id)
        
        # Enhance data with related entities
        enhanced_balance_sheets = self._enhance_balance_sheets(session, balance_sheets)
        enhanced_revenues = self._enhance_revenues(session, revenues)
        enhanced_expenditures = self._enhance_expenditures(session, expenditures)
        
        doe_form_dto = DOEFormGet.model_validate(doe_form.model_dump())

        
        return FinancialReportGet(
            doe_form=doe_form_dto,
            balance_sheets=enhanced_balance_sheets,
            revenues=enhanced_revenues,
            expenditures=enhanced_expenditures
        )

# Create singleton instance
finance_service = FinanceService() 