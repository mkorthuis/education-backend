import logging
from collections import defaultdict
from typing import List, Optional

from fastapi import HTTPException
from sqlmodel import Session, select

from app.model.location import SAU, District, Town, TownDistrictLink
from app.model.question_two import DistrictQuestionTwo, SauQuestionTwo, TownQuestionTwo
from app.schema.question_two_schema import DistrictQuestionTwoGet, SauQuestionTwoGet, TownQuestionTwoGet

logger = logging.getLogger(__name__)


def _towns(towns: Optional[str]) -> List[str]:
    return [town for town in (towns or "").split("; ") if town]


class QuestionTwoService:
    def get_district_results(
        self,
        session: Session,
        *,
        year: Optional[int] = None,
        district_id: Optional[int] = None,
        passed: Optional[bool] = None,
    ) -> List[DistrictQuestionTwoGet]:
        """Each district's Question 2 result, by year and then district name"""
        try:
            stmt = select(DistrictQuestionTwo, District.name).join(
                District, DistrictQuestionTwo.district_id_fk == District.id
            )
            if year is not None:
                stmt = stmt.where(DistrictQuestionTwo.year == year)
            if district_id is not None:
                stmt = stmt.where(DistrictQuestionTwo.district_id_fk == district_id)
            if passed is not None:
                stmt = stmt.where(DistrictQuestionTwo.passed == passed)
            stmt = stmt.order_by(DistrictQuestionTwo.year, District.name)
            return [
                DistrictQuestionTwoGet(
                    id=result.id,
                    district_id=result.district_id_fk,
                    district_name=name,
                    year=result.year,
                    yes_votes=result.yes_votes,
                    no_votes=result.no_votes,
                    yes_percentage=float(result.yes_percentage),
                    passed=result.passed,
                    towns=_towns(result.towns),
                    is_official=result.is_official,
                    note=result.note,
                )
                for result, name in session.exec(stmt).all()
            ]
        except Exception as e:
            logger.error(f"Error fetching Question 2 results: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch Question 2 results")

    def get_sau_results(
        self,
        session: Session,
        *,
        year: Optional[int] = None,
        sau_id: Optional[int] = None,
        passed: Optional[bool] = None,
    ) -> List[SauQuestionTwoGet]:
        """Each SAU's Question 2 result, by year and then SAU number, with the SAU's districts that voted"""
        try:
            stmt = select(SauQuestionTwo, SAU.name).join(SAU, SauQuestionTwo.sau_id_fk == SAU.id)
            if year is not None:
                stmt = stmt.where(SauQuestionTwo.year == year)
            if sau_id is not None:
                stmt = stmt.where(SauQuestionTwo.sau_id_fk == sau_id)
            if passed is not None:
                stmt = stmt.where(SauQuestionTwo.passed == passed)
            stmt = stmt.order_by(SauQuestionTwo.year, SauQuestionTwo.sau_id_fk)
            # The districts in each SAU that voted that year
            districts = defaultdict(list)
            voted = select(District.sau_id_fk, District.name, DistrictQuestionTwo.year).join(
                DistrictQuestionTwo, DistrictQuestionTwo.district_id_fk == District.id
            ).order_by(District.name)
            for sau, name, voted_year in session.exec(voted).all():
                districts[(sau, voted_year)].append(name)
            return [
                SauQuestionTwoGet(
                    id=result.id,
                    sau_id=result.sau_id_fk,
                    sau_name=name,
                    districts=districts[(result.sau_id_fk, result.year)],
                    year=result.year,
                    yes_votes=result.yes_votes,
                    no_votes=result.no_votes,
                    yes_percentage=float(result.yes_percentage),
                    passed=result.passed,
                    towns=_towns(result.towns),
                    is_official=result.is_official,
                    note=result.note,
                )
                for result, name in session.exec(stmt).all()
            ]
        except Exception as e:
            logger.error(f"Error fetching Question 2 SAU results: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch Question 2 SAU results")

    def get_town_results(
        self,
        session: Session,
        *,
        year: Optional[int] = None,
        town_id: Optional[int] = None,
        district_id: Optional[int] = None,
    ) -> List[TownQuestionTwoGet]:
        """Each town's own Question 2 vote, by year and then town name; district_id gives that district's towns"""
        try:
            stmt = select(TownQuestionTwo, Town.name).join(Town, TownQuestionTwo.town_id_fk == Town.id)
            if year is not None:
                stmt = stmt.where(TownQuestionTwo.year == year)
            if town_id is not None:
                stmt = stmt.where(TownQuestionTwo.town_id_fk == town_id)
            if district_id is not None:
                stmt = stmt.join(TownDistrictLink, TownDistrictLink.town_id_fk == TownQuestionTwo.town_id_fk).where(
                    TownDistrictLink.district_id_fk == district_id
                )
            stmt = stmt.order_by(TownQuestionTwo.year, Town.name)
            return [
                TownQuestionTwoGet(
                    id=result.id,
                    town_id=result.town_id_fk,
                    town_name=name,
                    year=result.year,
                    yes_votes=result.yes_votes,
                    no_votes=result.no_votes,
                    yes_percentage=float(result.yes_percentage),
                    is_official=result.is_official,
                    note=result.note,
                )
                for result, name in session.exec(stmt).all()
            ]
        except Exception as e:
            logger.error(f"Error fetching Question 2 town results: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch Question 2 town results")


question_two_service = QuestionTwoService()
