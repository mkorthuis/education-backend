from sqlmodel import Session, select
from typing import List, Optional

from app.model.safety import (
    SafetySafetyType, SchoolSafety, SchoolTruancy,
    SafetyDisciplineIncidentType, SchoolDisciplineIncident,
    SafetyDisciplineCountType, SchoolDisciplineCount,
    SafetyBullyingType, SchoolBullying,
    SafetyBullyingClassificationType, SchoolBullyingClassification,
    SafetyBullyingImpactType, SchoolBullyingImpact,
    SafetyHarassmentClassification, SchoolHarassment,
    SchoolRestraint, SchoolSeclusion,
    # State models
    StateSafety, StateTruancy,
    StateDisciplineIncident, StateDisciplineCount,
    StateBullying, StateBullyingClassification,
    StateBullyingImpact, StateHarassment,
    StateRestraint, StateSeclusion,
    # District models
    DistrictSafety, DistrictTruancy,
    DistrictDisciplineIncident, DistrictDisciplineCount,
    DistrictBullying, DistrictBullyingClassification,
    DistrictBullyingImpact, DistrictHarassment,
    DistrictRestraint, DistrictSeclusion,
    # Enrollment models
    SchoolSafetyEnrollment, StateSafetyEnrollment, DistrictSafetyEnrollment
)
from app.model.location import School
from app.service.dataset_query import Dataset, fail, fetch_dataset, list_types


# School-level error messages for safety data have no "school" prefix, except for "school safety data"
def _safety(tables, value_fields, label, **kwargs) -> Dataset:
    school_label = kwargs.pop("school_label", label)
    return Dataset(dict(zip(("school", "district", "state"), tables)), value_fields, label,
                   level_labels={"school": school_label}, **kwargs)


SAFETY = _safety(
    (SchoolSafety, DistrictSafety, StateSafety), ("count",), "safety data", school_label="school safety data",
    type_model=SafetySafetyType, type_fk="school_safety_type_id_fk", type_key="safety_type")
TRUANCY = _safety((SchoolTruancy, DistrictTruancy, StateTruancy), ("count",), "truancy data")
DISCIPLINE_INCIDENT = _safety(
    (SchoolDisciplineIncident, DistrictDisciplineIncident, StateDisciplineIncident), ("count",),
    "discipline incident data",
    type_model=SafetyDisciplineIncidentType, type_fk="school_discipline_incident_type_id_fk", type_key="incident_type")
DISCIPLINE_COUNT = _safety(
    (SchoolDisciplineCount, DistrictDisciplineCount, StateDisciplineCount), ("count",), "discipline count data",
    type_model=SafetyDisciplineCountType, type_fk="school_discipline_count_type_id_fk", type_key="count_type")
BULLYING = _safety(
    (SchoolBullying, DistrictBullying, StateBullying), ("reported", "investigated_actual"), "bullying data",
    type_model=SafetyBullyingType, type_fk="school_bullying_type_id_fk", type_key="bullying_type")
BULLYING_CLASSIFICATION = _safety(
    (SchoolBullyingClassification, DistrictBullyingClassification, StateBullyingClassification), ("count",),
    "bullying classification data",
    type_model=SafetyBullyingClassificationType, type_fk="school_bullying_classification_type_id_fk",
    type_key="classification_type")
BULLYING_IMPACT = _safety(
    (SchoolBullyingImpact, DistrictBullyingImpact, StateBullyingImpact), ("count",), "bullying impact data",
    type_model=SafetyBullyingImpactType, type_fk="school_bullying_impact_type_id_fk", type_key="impact_type")
HARASSMENT = _safety(
    (SchoolHarassment, DistrictHarassment, StateHarassment),
    ("incident_count", "student_impact_count", "student_engaged_count"), "harassment data",
    type_model=SafetyHarassmentClassification, type_fk="school_harassment_classification_id_fk",
    type_key="classification")
RESTRAINT = _safety(
    (SchoolRestraint, DistrictRestraint, StateRestraint),
    ("generated", "active_investigation", "closed_investigation", "bodily_injury", "serious_injury"), "restraint data")
SECLUSION = _safety(
    (SchoolSeclusion, DistrictSeclusion, StateSeclusion),
    ("generated", "active_investigation", "closed_investigation"), "seclusion data")


class SafetyService:
    # Lookup types
    def get_safety_types(self, session: Session) -> List[dict]:
        return list_types(session, SafetySafetyType, "safety types")

    def get_discipline_incident_types(self, session: Session) -> List[dict]:
        return list_types(session, SafetyDisciplineIncidentType, "discipline incident types")

    def get_discipline_count_types(self, session: Session) -> List[dict]:
        return list_types(session, SafetyDisciplineCountType, "discipline count types")

    def get_bullying_types(self, session: Session) -> List[dict]:
        return list_types(session, SafetyBullyingType, "bullying types")

    def get_bullying_classification_types(self, session: Session) -> List[dict]:
        return list_types(session, SafetyBullyingClassificationType, "bullying classification types")

    def get_bullying_impact_types(self, session: Session) -> List[dict]:
        return list_types(session, SafetyBullyingImpactType, "bullying impact types")

    def get_harassment_classifications(self, session: Session) -> List[dict]:
        return list_types(session, SafetyHarassmentClassification, "harassment classifications")

    # School-level methods
    def get_school_safety(self, session: Session, year: Optional[int] = None, school_id: Optional[int] = None,
                          district_id: Optional[int] = None, safety_type_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, SAFETY, "school", year, school_id, district_id, safety_type_id)

    def get_school_truancy(self, session: Session, year: Optional[int] = None, school_id: Optional[int] = None,
                           district_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, TRUANCY, "school", year, school_id, district_id)

    def get_school_discipline_incidents(self, session: Session, year: Optional[int] = None,
                                        school_id: Optional[int] = None, district_id: Optional[int] = None,
                                        discipline_incident_type_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, DISCIPLINE_INCIDENT, "school", year, school_id, district_id,
                           discipline_incident_type_id)

    def get_school_discipline_counts(self, session: Session, year: Optional[int] = None,
                                     school_id: Optional[int] = None, district_id: Optional[int] = None,
                                     discipline_count_type_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, DISCIPLINE_COUNT, "school", year, school_id, district_id, discipline_count_type_id)

    def get_school_bullying(self, session: Session, year: Optional[int] = None, school_id: Optional[int] = None,
                            district_id: Optional[int] = None, bullying_type_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, BULLYING, "school", year, school_id, district_id, bullying_type_id)

    def get_school_bullying_classifications(self, session: Session, year: Optional[int] = None,
                                            school_id: Optional[int] = None, district_id: Optional[int] = None,
                                            bullying_classification_type_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, BULLYING_CLASSIFICATION, "school", year, school_id, district_id,
                           bullying_classification_type_id)

    def get_school_bullying_impacts(self, session: Session, year: Optional[int] = None,
                                    school_id: Optional[int] = None, district_id: Optional[int] = None,
                                    bullying_impact_type_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, BULLYING_IMPACT, "school", year, school_id, district_id, bullying_impact_type_id)

    def get_school_harassment(self, session: Session, year: Optional[int] = None, school_id: Optional[int] = None,
                              district_id: Optional[int] = None,
                              harassment_classification_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, HARASSMENT, "school", year, school_id, district_id, harassment_classification_id)

    def get_school_restraint(self, session: Session, year: Optional[int] = None, school_id: Optional[int] = None,
                             district_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, RESTRAINT, "school", year, school_id, district_id)

    def get_school_seclusion(self, session: Session, year: Optional[int] = None, school_id: Optional[int] = None,
                             district_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, SECLUSION, "school", year, school_id, district_id)

    # State-level methods
    def get_state_safety(self, session: Session, year: Optional[int] = None,
                         safety_type_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, SAFETY, "state", year, type_id=safety_type_id)

    def get_state_truancy(self, session: Session, year: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, TRUANCY, "state", year)

    def get_state_discipline_incidents(self, session: Session, year: Optional[int] = None,
                                       discipline_incident_type_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, DISCIPLINE_INCIDENT, "state", year, type_id=discipline_incident_type_id)

    def get_state_discipline_counts(self, session: Session, year: Optional[int] = None,
                                    discipline_count_type_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, DISCIPLINE_COUNT, "state", year, type_id=discipline_count_type_id)

    def get_state_bullying(self, session: Session, year: Optional[int] = None,
                           bullying_type_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, BULLYING, "state", year, type_id=bullying_type_id)

    def get_state_bullying_classifications(self, session: Session, year: Optional[int] = None,
                                           bullying_classification_type_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, BULLYING_CLASSIFICATION, "state", year, type_id=bullying_classification_type_id)

    def get_state_bullying_impacts(self, session: Session, year: Optional[int] = None,
                                   bullying_impact_type_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, BULLYING_IMPACT, "state", year, type_id=bullying_impact_type_id)

    def get_state_harassment(self, session: Session, year: Optional[int] = None,
                             harassment_classification_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, HARASSMENT, "state", year, type_id=harassment_classification_id)

    def get_state_restraint(self, session: Session, year: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, RESTRAINT, "state", year)

    def get_state_seclusion(self, session: Session, year: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, SECLUSION, "state", year)

    # District-level methods
    def get_district_safety(self, session: Session, year: Optional[int] = None, district_id: Optional[int] = None,
                            safety_type_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, SAFETY, "district", year, district_id=district_id, type_id=safety_type_id)

    def get_district_truancy(self, session: Session, year: Optional[int] = None,
                             district_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, TRUANCY, "district", year, district_id=district_id)

    def get_district_discipline_incidents(self, session: Session, year: Optional[int] = None,
                                          district_id: Optional[int] = None,
                                          discipline_incident_type_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, DISCIPLINE_INCIDENT, "district", year, district_id=district_id,
                           type_id=discipline_incident_type_id)

    def get_district_discipline_counts(self, session: Session, year: Optional[int] = None,
                                       district_id: Optional[int] = None,
                                       discipline_count_type_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, DISCIPLINE_COUNT, "district", year, district_id=district_id,
                           type_id=discipline_count_type_id)

    def get_district_bullying(self, session: Session, year: Optional[int] = None, district_id: Optional[int] = None,
                              bullying_type_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, BULLYING, "district", year, district_id=district_id, type_id=bullying_type_id)

    def get_district_bullying_classifications(self, session: Session, year: Optional[int] = None,
                                              district_id: Optional[int] = None,
                                              bullying_classification_type_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, BULLYING_CLASSIFICATION, "district", year, district_id=district_id,
                           type_id=bullying_classification_type_id)

    def get_district_bullying_impacts(self, session: Session, year: Optional[int] = None,
                                      district_id: Optional[int] = None,
                                      bullying_impact_type_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, BULLYING_IMPACT, "district", year, district_id=district_id,
                           type_id=bullying_impact_type_id)

    def get_district_harassment(self, session: Session, year: Optional[int] = None,
                                district_id: Optional[int] = None,
                                harassment_classification_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, HARASSMENT, "district", year, district_id=district_id,
                           type_id=harassment_classification_id)

    def get_district_restraint(self, session: Session, year: Optional[int] = None,
                               district_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, RESTRAINT, "district", year, district_id=district_id)

    def get_district_seclusion(self, session: Session, year: Optional[int] = None,
                               district_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, SECLUSION, "district", year, district_id=district_id)

    # Enrollment (materialized views, no id column)
    def get_school_safety_enrollment(self, session: Session, year: Optional[int] = None,
                                     school_id: Optional[int] = None,
                                     district_id: Optional[int] = None) -> List[dict]:
        """Get school safety enrollment data with optional filters"""
        try:
            model = SchoolSafetyEnrollment
            statement = select(model.school_id_fk.label("school_id"), model.year, model.total_enrollment)
            # The School join is only needed (and only added) for the district filter
            if district_id is not None:
                statement = statement.join(School, model.school_id_fk == School.id).where(
                    School.district_id_fk == district_id)
            if year is not None:
                statement = statement.where(model.year == year)
            if school_id is not None:
                statement = statement.where(model.school_id_fk == school_id)
            return [dict(row) for row in session.exec(statement).mappings()]
        except Exception:
            raise fail("school safety enrollment data")

    def get_district_safety_enrollment(self, session: Session, year: Optional[int] = None,
                                       district_id: Optional[int] = None) -> List[dict]:
        """Get district safety enrollment data with optional filters"""
        try:
            model = DistrictSafetyEnrollment
            statement = select(model.district_id_fk.label("district_id"), model.year, model.total_enrollment)
            if year is not None:
                statement = statement.where(model.year == year)
            if district_id is not None:
                statement = statement.where(model.district_id_fk == district_id)
            return [dict(row) for row in session.exec(statement).mappings()]
        except Exception:
            raise fail("district safety enrollment data")

    def get_state_safety_enrollment(self, session: Session, year: Optional[int] = None) -> List[dict]:
        """Get state safety enrollment data with optional filters"""
        try:
            model = StateSafetyEnrollment
            statement = select(model.year, model.total_enrollment)
            if year is not None:
                statement = statement.where(model.year == year)
            return [dict(row) for row in session.exec(statement).mappings()]
        except Exception:
            raise fail("state safety enrollment data")


safety_service = SafetyService()
