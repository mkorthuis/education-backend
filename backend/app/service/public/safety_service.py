from dataclasses import dataclass
from sqlmodel import Session, select
from typing import List, Optional
from fastapi import HTTPException
import logging

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
from app.model.location import School, District

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class SafetyDataset:
    """One safety dataset: its table at each level and the fields it returns."""
    school: type
    district: type
    state: type
    value_fields: tuple
    label: str                          # error text: "Failed to fetch {level} {label} data"
    school_label: Optional[str] = None  # school-level error text, when it isn't just the label
    type_model: Optional[type] = None   # lookup table joined in for the type name
    type_fk: Optional[str] = None       # column on the data tables pointing at type_model
    type_key: Optional[str] = None      # response field holding the type's {id, name}


SAFETY = SafetyDataset(
    SchoolSafety, DistrictSafety, StateSafety, ("count",), "safety", school_label="school safety",
    type_model=SafetySafetyType, type_fk="school_safety_type_id_fk", type_key="safety_type")
TRUANCY = SafetyDataset(SchoolTruancy, DistrictTruancy, StateTruancy, ("count",), "truancy")
DISCIPLINE_INCIDENT = SafetyDataset(
    SchoolDisciplineIncident, DistrictDisciplineIncident, StateDisciplineIncident, ("count",), "discipline incident",
    type_model=SafetyDisciplineIncidentType, type_fk="school_discipline_incident_type_id_fk", type_key="incident_type")
DISCIPLINE_COUNT = SafetyDataset(
    SchoolDisciplineCount, DistrictDisciplineCount, StateDisciplineCount, ("count",), "discipline count",
    type_model=SafetyDisciplineCountType, type_fk="school_discipline_count_type_id_fk", type_key="count_type")
BULLYING = SafetyDataset(
    SchoolBullying, DistrictBullying, StateBullying, ("reported", "investigated_actual"), "bullying",
    type_model=SafetyBullyingType, type_fk="school_bullying_type_id_fk", type_key="bullying_type")
BULLYING_CLASSIFICATION = SafetyDataset(
    SchoolBullyingClassification, DistrictBullyingClassification, StateBullyingClassification, ("count",),
    "bullying classification",
    type_model=SafetyBullyingClassificationType, type_fk="school_bullying_classification_type_id_fk",
    type_key="classification_type")
BULLYING_IMPACT = SafetyDataset(
    SchoolBullyingImpact, DistrictBullyingImpact, StateBullyingImpact, ("count",), "bullying impact",
    type_model=SafetyBullyingImpactType, type_fk="school_bullying_impact_type_id_fk", type_key="impact_type")
HARASSMENT = SafetyDataset(
    SchoolHarassment, DistrictHarassment, StateHarassment,
    ("incident_count", "student_impact_count", "student_engaged_count"), "harassment",
    type_model=SafetyHarassmentClassification, type_fk="school_harassment_classification_id_fk",
    type_key="classification")
RESTRAINT = SafetyDataset(
    SchoolRestraint, DistrictRestraint, StateRestraint,
    ("generated", "active_investigation", "closed_investigation", "bodily_injury", "serious_injury"), "restraint")
SECLUSION = SafetyDataset(
    SchoolSeclusion, DistrictSeclusion, StateSeclusion,
    ("generated", "active_investigation", "closed_investigation"), "seclusion")


def _fail(label: str) -> HTTPException:
    logger.exception(f"Error fetching {label}")
    return HTTPException(status_code=500, detail=f"Failed to fetch {label}")


class SafetyService:
    def _list_types(self, session: Session, type_model, label: str) -> List[dict]:
        """Get all rows of a lookup table, ordered by name"""
        try:
            statement = select(type_model.id, type_model.name).order_by(type_model.name)
            return [dict(row) for row in session.exec(statement).mappings()]
        except Exception:
            raise _fail(label)

    def _fetch(
        self,
        session: Session,
        dataset: SafetyDataset,
        level: str,
        year: Optional[int] = None,
        school_id: Optional[int] = None,
        district_id: Optional[int] = None,
        type_id: Optional[int] = None
    ) -> List[dict]:
        """
        Get one dataset at one level ("school", "district" or "state") as response dicts.

        Selects only the columns the response needs, but keeps the same joins and filters
        as the original per-dataset queries, so the query plan and row order are unchanged.
        """
        model = getattr(dataset, level)
        if level == "school":
            label = f"{dataset.school_label or dataset.label} data"
        else:
            label = f"{level} {dataset.label} data"

        try:
            columns = [model.id]
            if level == "school":
                columns.append(model.school_id_fk.label("school_id"))
            elif level == "district":
                columns.append(model.district_id_fk.label("district_id"))
            columns.append(model.year)
            columns.extend(getattr(model, field) for field in dataset.value_fields)
            if dataset.type_model is not None:
                columns.extend([dataset.type_model.id.label("_type_id"), dataset.type_model.name.label("_type_name")])

            statement = select(*columns).select_from(model)
            if level == "school":
                statement = statement.join(School, model.school_id_fk == School.id)
            elif level == "district":
                statement = statement.join(District, model.district_id_fk == District.id)
            if dataset.type_model is not None:
                type_fk = getattr(model, dataset.type_fk)
                statement = statement.join(dataset.type_model, type_fk == dataset.type_model.id)

            if year is not None:
                statement = statement.where(model.year == year)
            if school_id is not None:
                statement = statement.where(model.school_id_fk == school_id)
            if district_id is not None:
                if level == "school":
                    statement = statement.where(School.district_id_fk == district_id)
                else:
                    statement = statement.where(model.district_id_fk == district_id)
            if type_id is not None:
                statement = statement.where(type_fk == type_id)

            rows = []
            for row in session.exec(statement).mappings():
                data = dict(row)
                if dataset.type_model is not None:
                    data[dataset.type_key] = {"id": data.pop("_type_id"), "name": data.pop("_type_name")}
                rows.append(data)
            return rows
        except Exception:
            raise _fail(label)

    # Lookup types
    def get_safety_types(self, session: Session) -> List[dict]:
        return self._list_types(session, SafetySafetyType, "safety types")

    def get_discipline_incident_types(self, session: Session) -> List[dict]:
        return self._list_types(session, SafetyDisciplineIncidentType, "discipline incident types")

    def get_discipline_count_types(self, session: Session) -> List[dict]:
        return self._list_types(session, SafetyDisciplineCountType, "discipline count types")

    def get_bullying_types(self, session: Session) -> List[dict]:
        return self._list_types(session, SafetyBullyingType, "bullying types")

    def get_bullying_classification_types(self, session: Session) -> List[dict]:
        return self._list_types(session, SafetyBullyingClassificationType, "bullying classification types")

    def get_bullying_impact_types(self, session: Session) -> List[dict]:
        return self._list_types(session, SafetyBullyingImpactType, "bullying impact types")

    def get_harassment_classifications(self, session: Session) -> List[dict]:
        return self._list_types(session, SafetyHarassmentClassification, "harassment classifications")

    # School-level methods
    def get_school_safety(self, session: Session, year: Optional[int] = None, school_id: Optional[int] = None,
                          district_id: Optional[int] = None, safety_type_id: Optional[int] = None) -> List[dict]:
        return self._fetch(session, SAFETY, "school", year, school_id, district_id, safety_type_id)

    def get_school_truancy(self, session: Session, year: Optional[int] = None, school_id: Optional[int] = None,
                           district_id: Optional[int] = None) -> List[dict]:
        return self._fetch(session, TRUANCY, "school", year, school_id, district_id)

    def get_school_discipline_incidents(self, session: Session, year: Optional[int] = None,
                                        school_id: Optional[int] = None, district_id: Optional[int] = None,
                                        discipline_incident_type_id: Optional[int] = None) -> List[dict]:
        return self._fetch(session, DISCIPLINE_INCIDENT, "school", year, school_id, district_id,
                           discipline_incident_type_id)

    def get_school_discipline_counts(self, session: Session, year: Optional[int] = None,
                                     school_id: Optional[int] = None, district_id: Optional[int] = None,
                                     discipline_count_type_id: Optional[int] = None) -> List[dict]:
        return self._fetch(session, DISCIPLINE_COUNT, "school", year, school_id, district_id, discipline_count_type_id)

    def get_school_bullying(self, session: Session, year: Optional[int] = None, school_id: Optional[int] = None,
                            district_id: Optional[int] = None, bullying_type_id: Optional[int] = None) -> List[dict]:
        return self._fetch(session, BULLYING, "school", year, school_id, district_id, bullying_type_id)

    def get_school_bullying_classifications(self, session: Session, year: Optional[int] = None,
                                            school_id: Optional[int] = None, district_id: Optional[int] = None,
                                            bullying_classification_type_id: Optional[int] = None) -> List[dict]:
        return self._fetch(session, BULLYING_CLASSIFICATION, "school", year, school_id, district_id,
                           bullying_classification_type_id)

    def get_school_bullying_impacts(self, session: Session, year: Optional[int] = None,
                                    school_id: Optional[int] = None, district_id: Optional[int] = None,
                                    bullying_impact_type_id: Optional[int] = None) -> List[dict]:
        return self._fetch(session, BULLYING_IMPACT, "school", year, school_id, district_id, bullying_impact_type_id)

    def get_school_harassment(self, session: Session, year: Optional[int] = None, school_id: Optional[int] = None,
                              district_id: Optional[int] = None,
                              harassment_classification_id: Optional[int] = None) -> List[dict]:
        return self._fetch(session, HARASSMENT, "school", year, school_id, district_id, harassment_classification_id)

    def get_school_restraint(self, session: Session, year: Optional[int] = None, school_id: Optional[int] = None,
                             district_id: Optional[int] = None) -> List[dict]:
        return self._fetch(session, RESTRAINT, "school", year, school_id, district_id)

    def get_school_seclusion(self, session: Session, year: Optional[int] = None, school_id: Optional[int] = None,
                             district_id: Optional[int] = None) -> List[dict]:
        return self._fetch(session, SECLUSION, "school", year, school_id, district_id)

    # State-level methods
    def get_state_safety(self, session: Session, year: Optional[int] = None,
                         safety_type_id: Optional[int] = None) -> List[dict]:
        return self._fetch(session, SAFETY, "state", year, type_id=safety_type_id)

    def get_state_truancy(self, session: Session, year: Optional[int] = None) -> List[dict]:
        return self._fetch(session, TRUANCY, "state", year)

    def get_state_discipline_incidents(self, session: Session, year: Optional[int] = None,
                                       discipline_incident_type_id: Optional[int] = None) -> List[dict]:
        return self._fetch(session, DISCIPLINE_INCIDENT, "state", year, type_id=discipline_incident_type_id)

    def get_state_discipline_counts(self, session: Session, year: Optional[int] = None,
                                    discipline_count_type_id: Optional[int] = None) -> List[dict]:
        return self._fetch(session, DISCIPLINE_COUNT, "state", year, type_id=discipline_count_type_id)

    def get_state_bullying(self, session: Session, year: Optional[int] = None,
                           bullying_type_id: Optional[int] = None) -> List[dict]:
        return self._fetch(session, BULLYING, "state", year, type_id=bullying_type_id)

    def get_state_bullying_classifications(self, session: Session, year: Optional[int] = None,
                                           bullying_classification_type_id: Optional[int] = None) -> List[dict]:
        return self._fetch(session, BULLYING_CLASSIFICATION, "state", year, type_id=bullying_classification_type_id)

    def get_state_bullying_impacts(self, session: Session, year: Optional[int] = None,
                                   bullying_impact_type_id: Optional[int] = None) -> List[dict]:
        return self._fetch(session, BULLYING_IMPACT, "state", year, type_id=bullying_impact_type_id)

    def get_state_harassment(self, session: Session, year: Optional[int] = None,
                             harassment_classification_id: Optional[int] = None) -> List[dict]:
        return self._fetch(session, HARASSMENT, "state", year, type_id=harassment_classification_id)

    def get_state_restraint(self, session: Session, year: Optional[int] = None) -> List[dict]:
        return self._fetch(session, RESTRAINT, "state", year)

    def get_state_seclusion(self, session: Session, year: Optional[int] = None) -> List[dict]:
        return self._fetch(session, SECLUSION, "state", year)

    # District-level methods
    def get_district_safety(self, session: Session, year: Optional[int] = None, district_id: Optional[int] = None,
                            safety_type_id: Optional[int] = None) -> List[dict]:
        return self._fetch(session, SAFETY, "district", year, district_id=district_id, type_id=safety_type_id)

    def get_district_truancy(self, session: Session, year: Optional[int] = None,
                             district_id: Optional[int] = None) -> List[dict]:
        return self._fetch(session, TRUANCY, "district", year, district_id=district_id)

    def get_district_discipline_incidents(self, session: Session, year: Optional[int] = None,
                                          district_id: Optional[int] = None,
                                          discipline_incident_type_id: Optional[int] = None) -> List[dict]:
        return self._fetch(session, DISCIPLINE_INCIDENT, "district", year, district_id=district_id,
                           type_id=discipline_incident_type_id)

    def get_district_discipline_counts(self, session: Session, year: Optional[int] = None,
                                       district_id: Optional[int] = None,
                                       discipline_count_type_id: Optional[int] = None) -> List[dict]:
        return self._fetch(session, DISCIPLINE_COUNT, "district", year, district_id=district_id,
                           type_id=discipline_count_type_id)

    def get_district_bullying(self, session: Session, year: Optional[int] = None, district_id: Optional[int] = None,
                              bullying_type_id: Optional[int] = None) -> List[dict]:
        return self._fetch(session, BULLYING, "district", year, district_id=district_id, type_id=bullying_type_id)

    def get_district_bullying_classifications(self, session: Session, year: Optional[int] = None,
                                              district_id: Optional[int] = None,
                                              bullying_classification_type_id: Optional[int] = None) -> List[dict]:
        return self._fetch(session, BULLYING_CLASSIFICATION, "district", year, district_id=district_id,
                           type_id=bullying_classification_type_id)

    def get_district_bullying_impacts(self, session: Session, year: Optional[int] = None,
                                      district_id: Optional[int] = None,
                                      bullying_impact_type_id: Optional[int] = None) -> List[dict]:
        return self._fetch(session, BULLYING_IMPACT, "district", year, district_id=district_id,
                           type_id=bullying_impact_type_id)

    def get_district_harassment(self, session: Session, year: Optional[int] = None,
                                district_id: Optional[int] = None,
                                harassment_classification_id: Optional[int] = None) -> List[dict]:
        return self._fetch(session, HARASSMENT, "district", year, district_id=district_id,
                           type_id=harassment_classification_id)

    def get_district_restraint(self, session: Session, year: Optional[int] = None,
                               district_id: Optional[int] = None) -> List[dict]:
        return self._fetch(session, RESTRAINT, "district", year, district_id=district_id)

    def get_district_seclusion(self, session: Session, year: Optional[int] = None,
                               district_id: Optional[int] = None) -> List[dict]:
        return self._fetch(session, SECLUSION, "district", year, district_id=district_id)

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
            raise _fail("school safety enrollment data")

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
            raise _fail("district safety enrollment data")

    def get_state_safety_enrollment(self, session: Session, year: Optional[int] = None) -> List[dict]:
        """Get state safety enrollment data with optional filters"""
        try:
            model = StateSafetyEnrollment
            statement = select(model.year, model.total_enrollment)
            if year is not None:
                statement = statement.where(model.year == year)
            return [dict(row) for row in session.exec(statement).mappings()]
        except Exception:
            raise _fail("state safety enrollment data")


safety_service = SafetyService()
