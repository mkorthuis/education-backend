from sqlmodel import Session, select
from typing import List, Optional, Dict, Any

from app.model.assessment import (
    AssessmentSubject, AssessmentSubgroup, AssessmentDistrict, AssessmentSchool, AssessmentState, AssessmentMetrics
)
from app.model.location import District, School
from app.service.dataset_query import fail, list_types

# grade_id value that selects the all-grades rows (stored with a NULL grade_id_fk)
ALL_GRADES = 999

# The 17 result columns shared by the state, district and school tables
METRIC_FIELDS = tuple(AssessmentMetrics.model_fields)


def apply_assessment_filters(statement, model, year=None, assessment_subgroup_id=None,
                             assessment_subject_id=None, grade_id=None):
    """Apply common filters to assessment queries"""
    if year is not None:
        statement = statement.where(model.year == year)

    if assessment_subgroup_id is not None:
        statement = statement.where(model.assessment_subgroup_id_fk == assessment_subgroup_id)

    if assessment_subject_id is not None:
        statement = statement.where(model.assessment_subject_id_fk == assessment_subject_id)

    if grade_id is not None:
        if grade_id == ALL_GRADES:
            statement = statement.where(model.grade_id_fk.is_(None))
        else:
            statement = statement.where(model.grade_id_fk == grade_id)

    return statement


def assessment_data(assessment_model, district_name: Optional[str] = None, school_name: Optional[str] = None,
                    district_id: Optional[int] = None, school_id: Optional[int] = None) -> Dict[str, Any]:
    """Create the assessment response dictionary from a loaded assessment row"""
    return {
        "id": assessment_model.id,
        "year": assessment_model.year,
        "district_id": district_id,
        "school_id": school_id,
        "assessment_subgroup_id": assessment_model.assessment_subgroup_id_fk,
        "assessment_subject_id": assessment_model.assessment_subject_id_fk,
        "grade_id": assessment_model.grade_id_fk,
        **{field: getattr(assessment_model, field) for field in METRIC_FIELDS},
        "district_name": district_name,
        "school_name": school_name
    }


def _assessment_columns(model) -> list:
    """Columns of an assessment table, labelled with their response field names"""
    return [
        model.id,
        model.year,
        model.assessment_subgroup_id_fk.label("assessment_subgroup_id"),
        model.assessment_subject_id_fk.label("assessment_subject_id"),
        model.grade_id_fk.label("grade_id"),
        *(getattr(model, field) for field in METRIC_FIELDS),
    ]


def _rows(session: Session, statement) -> List[Dict[str, Any]]:
    """Run a statement and return response dicts, with any missing location fields set to None"""
    empty = {"district_id": None, "school_id": None, "district_name": None, "school_name": None}
    return [{**empty, **row} for row in session.exec(statement).mappings()]


class AssessmentService:
    def get_assessment_subgroups(self, session: Session) -> List[dict]:
        """Get all assessment subgroups"""
        return list_types(session, AssessmentSubgroup, "assessment subgroups", ("id", "name", "description"))

    def get_assessment_subjects(self, session: Session) -> List[dict]:
        """Get all assessment subjects"""
        return list_types(session, AssessmentSubject, "assessment subjects", ("id", "name", "description"))

    def get_state_assessments(
        self,
        session: Session,
        year: Optional[int] = None,
        assessment_subgroup_id: Optional[int] = None,
        assessment_subject_id: Optional[int] = None,
        grade_id: Optional[int] = None
    ) -> List[dict]:
        """Get state level assessment data with optional filters"""
        try:
            statement = select(*_assessment_columns(AssessmentState))
            statement = apply_assessment_filters(
                statement, AssessmentState, year, assessment_subgroup_id, assessment_subject_id, grade_id
            )
            return _rows(session, statement)
        except Exception:
            raise fail("state assessment data")

    def get_district_assessments(
        self,
        session: Session,
        district_id: Optional[int] = None,
        year: Optional[int] = None,
        assessment_subgroup_id: Optional[int] = None,
        assessment_subject_id: Optional[int] = None,
        grade_id: Optional[int] = None
    ) -> List[dict]:
        """Get district level assessment data with optional filters"""
        try:
            statement = select(
                *_assessment_columns(AssessmentDistrict),
                AssessmentDistrict.district_id_fk.label("district_id"),
                District.name.label("district_name"),
            ).select_from(AssessmentDistrict).join(
                District,
                AssessmentDistrict.district_id_fk == District.id
            )
            statement = apply_assessment_filters(
                statement, AssessmentDistrict, year, assessment_subgroup_id, assessment_subject_id, grade_id
            )

            # Add district-specific filter
            if district_id is not None:
                statement = statement.where(AssessmentDistrict.district_id_fk == district_id)

            return _rows(session, statement)
        except Exception:
            raise fail("district assessment data")

    def get_school_assessments(
        self,
        session: Session,
        school_id: Optional[int] = None,
        district_id: Optional[int] = None,
        year: Optional[int] = None,
        assessment_subgroup_id: Optional[int] = None,
        assessment_subject_id: Optional[int] = None,
        grade_id: Optional[int] = None
    ) -> List[dict]:
        """Get school level assessment data with optional filters"""
        try:
            statement = select(
                *_assessment_columns(AssessmentSchool),
                AssessmentSchool.school_id_fk.label("school_id"),
                School.district_id_fk.label("district_id"),
                District.name.label("district_name"),
                School.name.label("school_name"),
            ).select_from(AssessmentSchool).join(
                School,
                AssessmentSchool.school_id_fk == School.id
            ).join(
                District,
                School.district_id_fk == District.id
            )
            statement = apply_assessment_filters(
                statement, AssessmentSchool, year, assessment_subgroup_id, assessment_subject_id, grade_id
            )

            # Add school-specific filters
            if school_id is not None:
                statement = statement.where(AssessmentSchool.school_id_fk == school_id)

            if district_id is not None:
                # Filter by district through the School model
                statement = statement.where(School.district_id_fk == district_id)

            return _rows(session, statement)
        except Exception:
            raise fail("school assessment data")

assessment_service = AssessmentService()
