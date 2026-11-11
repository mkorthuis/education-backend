import logging
from typing import List, Optional

from fastapi import HTTPException
from sqlmodel import Session, select

from app.model.location import District
from app.model.question_two import DistrictQuestionTwo
from app.schema.question_two_schema import DistrictQuestionTwoGet

logger = logging.getLogger(__name__)


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
                    is_official=result.is_official,
                )
                for result, name in session.exec(stmt).all()
            ]
        except Exception as e:
            logger.error(f"Error fetching Question 2 results: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch Question 2 results")


question_two_service = QuestionTwoService()
