from typing import List, Optional, Dict, Any
from sqlmodel import Session, select
from fastapi import HTTPException

from app.model.finance import (
    DOEForm, BalanceSheet, Revenue, Expenditure,
    BalanceEntryType, BalanceFundType,
    RevenueEntryType, RevenueFundType,
    ExpenditureEntryType, ExpenditureFundType,
    BalanceEntryCategory, BalanceEntrySuperCategory,
    RevenueEntryCategory, RevenueEntrySuperCategory,
    ExpenditureEntryCategory, ExpenditureEntrySuperCategory
)
from app.model.location import District
from app.schema.finance_schema import (
    DOEFormGet, BalanceSheetGet, RevenueGet, ExpenditureGet,
    FinancialReportGet, AllEntryTypesGet,
    BalanceEntryTypeGet, RevenueEntryTypeGet, ExpenditureEntryTypeGet,
    BalanceEntryCategoryGet, RevenueEntryCategoryGet, ExpenditureEntryCategoryGet,
    BalanceFundTypeGet, RevenueFundTypeGet, ExpenditureFundTypeGet,
    AllFundTypesGet
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
            bs_dto = BalanceSheetGet.from_orm(bs)
            result.append(bs_dto)
            
        return result
    
    def _enhance_revenues(self, session: Session, revenues: List[Revenue]) -> List[RevenueGet]:
        """Enhance revenues with related data."""
        result = []
        for rev in revenues:
            rev_dto = RevenueGet.from_orm(rev)
            result.append(rev_dto)
            
        return result
    
    def _enhance_expenditures(self, session: Session, expenditures: List[Expenditure]) -> List[ExpenditureGet]:
        """Enhance expenditures with related data."""
        result = []
        for exp in expenditures:
            exp_dto = ExpenditureGet.from_orm(exp)
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
    
    def get_balance_entry_types(self, session: Session) -> List[BalanceEntryTypeGet]:
        """Get all balance entry types with their categories and super categories."""
        # Get all balance entry types
        statement = select(BalanceEntryType)
        entry_types = session.exec(statement).all()
        
        # Enhance with category and super category
        result = []
        for entry_type in entry_types:
            # Get category
            category = session.get(BalanceEntryCategory, entry_type.balance_entry_category_type_id_fk)
            
            # Create enhanced entry type
            enhanced_entry_type = BalanceEntryTypeGet.model_validate(entry_type.model_dump())
            
            if category:
                # Get super category
                super_category = session.get(BalanceEntrySuperCategory, category.balance_entry_super_category_type_id_fk)
                
                # Create enhanced category
                enhanced_category = BalanceEntryCategoryGet.model_validate(category.model_dump())
                
                if super_category:
                    enhanced_category.super_category = super_category
                
                enhanced_entry_type.category = enhanced_category
            
            result.append(enhanced_entry_type)
        
        return result
    
    def get_revenue_entry_types(self, session: Session) -> List[RevenueEntryTypeGet]:
        """Get all revenue entry types with their categories and super categories."""
        # Get all revenue entry types
        statement = select(RevenueEntryType)
        entry_types = session.exec(statement).all()
        
        # Enhance with category and super category
        result = []
        for entry_type in entry_types:
            # Get category
            category = session.get(RevenueEntryCategory, entry_type.revenue_entry_category_type_id_fk)
            
            # Create enhanced entry type
            enhanced_entry_type = RevenueEntryTypeGet.model_validate(entry_type.model_dump())
            
            if category:
                # Get super category
                super_category = session.get(RevenueEntrySuperCategory, category.revenue_entry_super_category_type_id_fk)
                
                # Create enhanced category
                enhanced_category = RevenueEntryCategoryGet.model_validate(category.model_dump())
                
                if super_category:
                    enhanced_category.super_category = super_category
                
                enhanced_entry_type.category = enhanced_category
            
            result.append(enhanced_entry_type)
        
        return result
    
    def get_expenditure_entry_types(self, session: Session) -> List[ExpenditureEntryTypeGet]:
        """Get all expenditure entry types with their categories and super categories."""
        # Get all expenditure entry types
        statement = select(ExpenditureEntryType)
        entry_types = session.exec(statement).all()
        
        # Enhance with category and super category
        result = []
        for entry_type in entry_types:
            # Get category
            category = session.get(ExpenditureEntryCategory, entry_type.expenditure_entry_category_type_id_fk)
            
            # Create enhanced entry type
            enhanced_entry_type = ExpenditureEntryTypeGet.model_validate(entry_type.model_dump())
            
            if category:
                # Get super category
                super_category = session.get(ExpenditureEntrySuperCategory, category.expenditure_entry_super_category_type_id_fk)
                
                # Create enhanced category
                enhanced_category = ExpenditureEntryCategoryGet.model_validate(category.model_dump())
                
                if super_category:
                    enhanced_category.super_category = super_category
                
                enhanced_entry_type.category = enhanced_category
            
            result.append(enhanced_entry_type)
        
        return result
    
    def get_all_entry_types(self, session: Session) -> AllEntryTypesGet:
        """Get all entry types (balance, revenue, expenditure) with their categories and super categories."""
        balance_entry_types = self.get_balance_entry_types(session)
        revenue_entry_types = self.get_revenue_entry_types(session)
        expenditure_entry_types = self.get_expenditure_entry_types(session)
        
        return AllEntryTypesGet(
            balance_entry_types=balance_entry_types,
            revenue_entry_types=revenue_entry_types,
            expenditure_entry_types=expenditure_entry_types
        )
        
    def get_balance_fund_types(self, session: Session) -> List[BalanceFundTypeGet]:
        """Get all balance fund types."""
        statement = select(BalanceFundType)
        fund_types = session.exec(statement).all()
        
        result = []
        for fund_type in fund_types:
            fund_type_dto = BalanceFundTypeGet.model_validate(fund_type.model_dump())
            result.append(fund_type_dto)
            
        return result
    
    def get_revenue_fund_types(self, session: Session) -> List[RevenueFundTypeGet]:
        """Get all revenue fund types."""
        statement = select(RevenueFundType)
        fund_types = session.exec(statement).all()
        
        result = []
        for fund_type in fund_types:
            fund_type_dto = RevenueFundTypeGet.model_validate(fund_type.model_dump())
            result.append(fund_type_dto)
            
        return result
    
    def get_expenditure_fund_types(self, session: Session) -> List[ExpenditureFundTypeGet]:
        """Get all expenditure fund types."""
        statement = select(ExpenditureFundType)
        fund_types = session.exec(statement).all()
        
        result = []
        for fund_type in fund_types:
            fund_type_dto = ExpenditureFundTypeGet.model_validate(fund_type.model_dump())
            result.append(fund_type_dto)
            
        return result
        
    def get_all_fund_types(self, session: Session) -> AllFundTypesGet:
        """Get all fund types (balance, revenue, expenditure)."""
        balance_fund_types = self.get_balance_fund_types(session)
        revenue_fund_types = self.get_revenue_fund_types(session)
        expenditure_fund_types = self.get_expenditure_fund_types(session)
        
        return AllFundTypesGet(
            balance_fund_types=balance_fund_types,
            revenue_fund_types=revenue_fund_types,
            expenditure_fund_types=expenditure_fund_types
        )

# Create singleton instance
finance_service = FinanceService() 