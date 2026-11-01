from typing import List, Optional
from sqlmodel import Session

from app.model.outcome import (
    PostGraduationType,
    SchoolPostGraduation,
    StatePostGraduation,
    SchoolEarlyExit,
    StateEarlyExit,
    DistrictPostGraduation,
    DistrictEarlyExit,
    SchoolGraduationCohort,
    StateGraduationCohort,
    DistrictGraduationCohort,
)
from app.service.dataset_query import Dataset, fetch_dataset, list_types

# The district tables are views keyed by district (no id), and their queries don't join District
POST_GRADUATION = Dataset(
    {"school": SchoolPostGraduation, "district": DistrictPostGraduation, "state": StatePostGraduation},
    ("value",), "post graduation",
    type_model=PostGraduationType, type_fk="post_graduation_type_id_fk", type_key="post_graduation_type",
    type_fields=("id", "name", "description"), type_join_first=True, join_district=False)
EARLY_EXIT = Dataset(
    {"school": SchoolEarlyExit, "district": DistrictEarlyExit, "state": StateEarlyExit},
    ("adjusted_fall_enrollment", "earned_hiset", "enrolled_in_college", "dropped_out", "missing",
     "annual_early_exit_percentage", "four_year_early_exit_percentage",
     "annual_dropout_percentage", "four_year_dropout_percentage"),
    "early exit", join_district=False)
GRADUATION_COHORT = Dataset(
    {"school": SchoolGraduationCohort, "district": DistrictGraduationCohort, "state": StateGraduationCohort},
    ("cohort_size", "graduate", "earned_hiset", "dropped_out"),
    "graduation cohort", join_district=False)


class OutcomeService:
    # Post-graduation type
    def get_post_graduation_types(self, session: Session) -> List[dict]:
        return list_types(session, PostGraduationType, "post graduation types", ("id", "name", "description"))

    # Post-graduation
    def get_school_post_graduation(self, session: Session, year: Optional[int] = None,
                                   school_id: Optional[int] = None, district_id: Optional[int] = None,
                                   pg_type_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, POST_GRADUATION, "school", year, school_id, district_id, pg_type_id)

    def get_district_post_graduation(self, session: Session, year: Optional[int] = None,
                                     district_id: Optional[int] = None,
                                     pg_type_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, POST_GRADUATION, "district", year, district_id=district_id, type_id=pg_type_id)

    def get_state_post_graduation(self, session: Session, year: Optional[int] = None,
                                  pg_type_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, POST_GRADUATION, "state", year, type_id=pg_type_id)

    # Early exit
    def get_school_early_exit(self, session: Session, year: Optional[int] = None, school_id: Optional[int] = None,
                              district_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, EARLY_EXIT, "school", year, school_id, district_id)

    def get_district_early_exit(self, session: Session, year: Optional[int] = None,
                                district_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, EARLY_EXIT, "district", year, district_id=district_id)

    def get_state_early_exit(self, session: Session, year: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, EARLY_EXIT, "state", year)

    # Graduation cohort
    def get_school_graduation_cohort(self, session: Session, year: Optional[int] = None,
                                     school_id: Optional[int] = None,
                                     district_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, GRADUATION_COHORT, "school", year, school_id, district_id)

    def get_district_graduation_cohort(self, session: Session, year: Optional[int] = None,
                                       district_id: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, GRADUATION_COHORT, "district", year, district_id=district_id)

    def get_state_graduation_cohort(self, session: Session, year: Optional[int] = None) -> List[dict]:
        return fetch_dataset(session, GRADUATION_COHORT, "state", year)


outcome_service = OutcomeService()
