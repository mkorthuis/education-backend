from typing import List, Optional

from sqlalchemy.orm import aliased
from sqlmodel import Session, select

from app.model.assessment import AssessmentSubject
from app.model.location import Grade
from app.model.naep import Jurisdiction, NaepComparison, NaepMeasure, NaepResult, NaepStudentGroup


def _jurisdiction(place: Jurisdiction) -> dict:
    return {"id": place.id, "code": place.code, "name": place.name, "kind": place.kind}


def _common(subject: AssessmentSubject, grade: Grade, measure: NaepMeasure, group: NaepStudentGroup) -> dict:
    return {
        "subject": {"id": subject.id, "name": subject.name, "description": subject.description},
        "grade": {"id": grade.id, "name": grade.name},
        "measure": {"id": measure.id, "code": measure.code, "name": measure.name, "unit": measure.unit},
        "student_group": {"id": group.id, "variable": group.variable, "value": group.value, "name": group.name},
    }


class NaepService:
    def get_jurisdictions(self, session: Session) -> List[Jurisdiction]:
        """The places NAEP reports on: the national public average, the states and DC, and DoDEA."""
        return session.exec(select(Jurisdiction).order_by(Jurisdiction.id)).all()

    def get_measures(self, session: Session) -> List[NaepMeasure]:
        return session.exec(select(NaepMeasure).order_by(NaepMeasure.id)).all()

    def get_student_groups(self, session: Session) -> List[NaepStudentGroup]:
        return session.exec(select(NaepStudentGroup).order_by(NaepStudentGroup.id)).all()

    def get_results(self, session: Session, year: Optional[int] = None, assessment_subject_id: Optional[int] = None,
                    grade_id: Optional[int] = None, naep_measure_id: Optional[int] = None,
                    naep_student_group_id: Optional[int] = None, jurisdiction: Optional[str] = None) -> List[dict]:
        """NAEP figures, oldest year first, then by subject, grade, measure and place."""
        statement = (
            select(NaepResult, Jurisdiction, AssessmentSubject, Grade, NaepMeasure, NaepStudentGroup)
            .join(Jurisdiction, Jurisdiction.id == NaepResult.jurisdiction_id_fk)
            .join(AssessmentSubject, AssessmentSubject.id == NaepResult.assessment_subject_id_fk)
            .join(Grade, Grade.id == NaepResult.grade_id_fk)
            .join(NaepMeasure, NaepMeasure.id == NaepResult.naep_measure_id_fk)
            .join(NaepStudentGroup, NaepStudentGroup.id == NaepResult.naep_student_group_id_fk)
            .order_by(NaepResult.year, AssessmentSubject.id, Grade.id, NaepMeasure.id, NaepStudentGroup.id, Jurisdiction.id)
        )
        if year is not None:
            statement = statement.where(NaepResult.year == year)
        if assessment_subject_id is not None:
            statement = statement.where(NaepResult.assessment_subject_id_fk == assessment_subject_id)
        if grade_id is not None:
            statement = statement.where(NaepResult.grade_id_fk == grade_id)
        if naep_measure_id is not None:
            statement = statement.where(NaepResult.naep_measure_id_fk == naep_measure_id)
        if naep_student_group_id is not None:
            statement = statement.where(NaepResult.naep_student_group_id_fk == naep_student_group_id)
        if jurisdiction is not None:
            statement = statement.where(Jurisdiction.code == jurisdiction.upper())
        return [
            {
                "id": row.id,
                "year": row.year,
                "jurisdiction": _jurisdiction(place),
                **_common(subject, grade, measure, group),
                "value": row.value,
                "is_displayable": row.is_displayable,
            }
            for row, place, subject, grade, measure, group in session.exec(statement).all()
        ]

    def get_comparisons(self, session: Session, year: Optional[int] = None, other_year: Optional[int] = None,
                        assessment_subject_id: Optional[int] = None, grade_id: Optional[int] = None,
                        naep_measure_id: Optional[int] = None, naep_student_group_id: Optional[int] = None,
                        jurisdiction: Optional[str] = None, other_jurisdiction: Optional[str] = None,
                        basis: Optional[str] = None) -> List[dict]:
        """NAEP's significance tests, oldest year first, then by subject, grade, measure and the places compared."""
        other = aliased(Jurisdiction)
        statement = (
            select(NaepComparison, Jurisdiction, other, AssessmentSubject, Grade, NaepMeasure, NaepStudentGroup)
            .join(Jurisdiction, Jurisdiction.id == NaepComparison.jurisdiction_id_fk)
            .join(other, other.id == NaepComparison.other_jurisdiction_id_fk)
            .join(AssessmentSubject, AssessmentSubject.id == NaepComparison.assessment_subject_id_fk)
            .join(Grade, Grade.id == NaepComparison.grade_id_fk)
            .join(NaepMeasure, NaepMeasure.id == NaepComparison.naep_measure_id_fk)
            .join(NaepStudentGroup, NaepStudentGroup.id == NaepComparison.naep_student_group_id_fk)
            .order_by(NaepComparison.year, AssessmentSubject.id, Grade.id, NaepMeasure.id, NaepStudentGroup.id,
                      Jurisdiction.id, NaepComparison.other_year, other.id, NaepComparison.basis)
        )
        if year is not None:
            statement = statement.where(NaepComparison.year == year)
        if other_year is not None:
            statement = statement.where(NaepComparison.other_year == other_year)
        if assessment_subject_id is not None:
            statement = statement.where(NaepComparison.assessment_subject_id_fk == assessment_subject_id)
        if grade_id is not None:
            statement = statement.where(NaepComparison.grade_id_fk == grade_id)
        if naep_measure_id is not None:
            statement = statement.where(NaepComparison.naep_measure_id_fk == naep_measure_id)
        if naep_student_group_id is not None:
            statement = statement.where(NaepComparison.naep_student_group_id_fk == naep_student_group_id)
        if jurisdiction is not None:
            statement = statement.where(Jurisdiction.code == jurisdiction.upper())
        if other_jurisdiction is not None:
            statement = statement.where(other.code == other_jurisdiction.upper())
        if basis is not None:
            statement = statement.where(NaepComparison.basis == basis)
        return [
            {
                "id": row.id,
                "year": row.year,
                "jurisdiction": _jurisdiction(place),
                "other_year": row.other_year,
                "other_jurisdiction": _jurisdiction(other_place),
                **_common(subject, grade, measure, group),
                "basis": row.basis,
                "result": row.result,
                "difference": row.difference,
            }
            for row, place, other_place, subject, grade, measure, group in session.exec(statement).all()
        ]


naep_service = NaepService()
