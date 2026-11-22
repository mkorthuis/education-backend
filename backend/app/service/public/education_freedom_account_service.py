from typing import List, Optional
from sqlmodel import Session, func, select
from fastapi import HTTPException

from app.model.education_freedom_account import (
    EducationFreedomAccountEntryType,
    EducationFreedomAccountEntryTypeValue,
    EducationFreedomAccountEntry,
    EducationFreedomAccountEntryState,
    EducationFreedomAccountCategory, EducationFreedomAccountExpenditure, EducationFreedomAccountProvider,
    EducationFreedomAccountServed,
)
from app.model.location import TownDistrictLink
from app.schema.education_freedom_account_schema import (
    EducationFreedomAccountEntryGet,
    EFAEntryTypeGet,
    EFAEntryStateGet
)

class EducationFreedomAccountService:
    def get_entry_types_with_values(self, session: Session, year: Optional[int] = None) -> List[EFAEntryTypeGet]:
        """
        Get all education freedom account entry types with their values.
        If year is provided, returns values for that specific year.
        If year is not provided, returns values for all years.
        
        Args:
            session: The database session
            year: Optional year to filter by
            
        Returns:
            List[EFAEntryTypeGet]: A list of entry types with their values
        """
        # Base query to join entry types with their values
        statement = (
            select(
                EducationFreedomAccountEntryType.id,
                EducationFreedomAccountEntryType.name,
                EducationFreedomAccountEntryType.description,
                EducationFreedomAccountEntryTypeValue.year,
                EducationFreedomAccountEntryTypeValue.value
            )
            .join(
                EducationFreedomAccountEntryTypeValue,
                EducationFreedomAccountEntryType.id == EducationFreedomAccountEntryTypeValue.education_freedom_account_entry_type_id_fk
            )
        )
        
        # Apply year filter if provided
        if year is not None:
            statement = statement.where(EducationFreedomAccountEntryTypeValue.year == year)
            
        # Order by entry type ID and year
        statement = statement.order_by(
            EducationFreedomAccountEntryType.id,
            EducationFreedomAccountEntryTypeValue.year.desc()
        )
        
        results = session.exec(statement).all()
        
        if not results:
            detail = "No education freedom account entry type values found"
            if year is not None:
                detail += f" for year {year}"
            raise HTTPException(status_code=404, detail=detail)
            
        # Convert results to EFAEntryTypeGet objects
        return [
            EFAEntryTypeGet(
                id=result[0],
                name=result[1],
                description=result[2],
                year=result[3],
                value=result[4]
            )
            for result in results
        ]
    
    def get_entries(
        self, 
        session: Session, 
        year: Optional[int] = None,
        district_id: Optional[int] = None,
        town_id: Optional[int] = None
    ) -> List[EducationFreedomAccountEntryGet]:
        """
        Get education freedom account entries, optionally filtered by year, district ID, and town ID.
        
        Args:
            session: The database session
            year: Optional year to filter by
            district_id: Optional district ID to filter by
            town_id: Optional town ID to filter by (if both district_id and town_id are provided, district_id takes precedence)
            
        Returns:
            List[EducationFreedomAccountEntryGet]: A list of entries
        """
        # Base query for entries
        statement = select(EducationFreedomAccountEntry)
        
        # Apply year filter if provided
        if year is not None:
            statement = statement.where(EducationFreedomAccountEntry.year == year)
        
        # Apply district_id filter if provided
        if district_id is not None:
            # We need to join with the town_district_xref table to filter by district_id
            # First, get all town IDs that belong to the district
            town_ids_stmt = select(TownDistrictLink.town_id_fk).where(
                TownDistrictLink.district_id_fk == district_id
            )
            town_ids = session.exec(town_ids_stmt).all()
            
            if not town_ids:
                raise HTTPException(
                    status_code=404,
                    detail=f"No towns found for district ID {district_id}"
                )
            
            # Filter entries by these town IDs
            statement = statement.where(EducationFreedomAccountEntry.town_id_fk.in_(town_ids))
        # Apply town_id filter if provided and district_id is not provided
        elif town_id is not None:
            statement = statement.where(EducationFreedomAccountEntry.town_id_fk == town_id)
            
        # Order by town ID and year (most recent first)
        statement = statement.order_by(
            EducationFreedomAccountEntry.town_id_fk, 
            EducationFreedomAccountEntry.year.desc()
        )
        
        results = session.exec(statement).all()
        
        if not results:
            detail = "No education freedom account entries found"
            if year is not None:
                detail += f" for year {year}"
            if district_id is not None:
                detail += f" for district ID {district_id}"
            elif town_id is not None:
                detail += f" for town ID {town_id}"
            raise HTTPException(status_code=404, detail=detail)
        
        # Convert to response schema
        return [EducationFreedomAccountEntryGet.model_validate(result.model_dump()) for result in results]

    def get_state_entries(
        self, 
        session: Session, 
        year: Optional[int] = None,
        entry_type_id: Optional[int] = None
    ) -> List[EFAEntryStateGet]:
        """
        Get state-level education freedom account entries from the materialized view,
        optionally filtered by year and entry type ID.
        
        Args:
            session: The database session
            year: Optional year to filter by
            entry_type_id: Optional entry type ID to filter by
            
        Returns:
            List[EFAEntryStateGet]: A list of state-level entries
        """
        statement = select(EducationFreedomAccountEntryState)
        
        # Apply filters if provided
        if year is not None:
            statement = statement.where(EducationFreedomAccountEntryState.year == year)
            
        if entry_type_id is not None:
            statement = statement.where(
                EducationFreedomAccountEntryState.education_freedom_account_entry_type_id_fk == entry_type_id
            )
            
        # Order by year (most recent first) and entry type ID
        statement = statement.order_by(
            EducationFreedomAccountEntryState.year.desc(),
            EducationFreedomAccountEntryState.education_freedom_account_entry_type_id_fk
        )
        
        # Execute query
        results = session.exec(statement).all()
        
        # Convert to response schema
        return [EFAEntryStateGet.model_validate(result.model_dump()) for result in results]

    def get_private_school_payments(self, session: Session, school_id: Optional[int] = None) -> List[dict]:
        """EFA money paid to the private schools on the state's list, and the students they served (see
        app/etl/education_freedom_account_provider.py): a row per school with the names the reports give it, its
        payments by school year and category, and its students by calendar year (listed only at 10 or more)"""
        provider, expenditure, category, served = (EducationFreedomAccountProvider, EducationFreedomAccountExpenditure,
                                                   EducationFreedomAccountCategory, EducationFreedomAccountServed)
        statement = select(provider).where(provider.school_id_fk.is_not(None)).order_by(provider.school_id_fk, provider.name)
        if school_id is not None:
            statement = statement.where(provider.school_id_fk == school_id)
        schools = {}
        for row in session.exec(statement):
            schools.setdefault(row.school_id_fk, {"school_id": row.school_id_fk, "providers": [], "payments": [], "served": []})
            schools[row.school_id_fk]["providers"].append(row.name)
        in_schools = provider.school_id_fk.in_(list(schools))
        statement = (select(provider.school_id_fk, expenditure.year, category.code, category.name, func.sum(expenditure.amount))
                     .join(provider, provider.id == expenditure.provider_id)
                     .join(category, category.id == expenditure.category_id)
                     .where(in_schools)
                     .group_by(provider.school_id_fk, expenditure.year, category.code, category.name)
                     .order_by(expenditure.year, category.code))
        for school, year, code, name, amount in session.exec(statement):
            schools[school]["payments"].append({"year": year, "category_code": code, "category_name": name, "amount": amount})
        statement = (select(provider.school_id_fk, served.calendar_year, func.sum(served.students))
                     .join(provider, provider.id == served.provider_id)
                     .where(in_schools)
                     .group_by(provider.school_id_fk, served.calendar_year)
                     .order_by(served.calendar_year))
        for school, calendar_year, students in session.exec(statement):
            schools[school]["served"].append({"calendar_year": calendar_year, "students": students})
        return [schools[school] for school in sorted(schools)]

# Create singleton instance
education_freedom_account_service = EducationFreedomAccountService() 