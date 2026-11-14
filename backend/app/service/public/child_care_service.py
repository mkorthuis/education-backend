import logging
from datetime import date
from functools import lru_cache
from typing import List, Optional

from fastapi import HTTPException
from sqlalchemy import func, or_
from sqlmodel import Session, select

from app.etl.core import load_config
from app.model.child_care import (
    ChildCareAvailability, ChildCareFeature, ChildCareFeatureCategory, ChildCareInspection, ChildCareLicenseStatus,
    ChildCareProgram, ChildCareProgramFeatureLink, ChildCareProgramHours, ChildCareProgramRate,
    ChildCareProgramSnapshot, ChildCareProgramType, ChildCareQualityRating, ChildCareRegion, ChildCareReviewType,
    DistrictChildCare, StateChildCare, TownChildCare,
)
from app.model.location import County, District, Town, TownDistrictLink
from app.schema.child_care_schema import (
    ChildCareProgramDetailGet, ChildCareProgramGet, DistrictChildCareGet, StateChildCareGet, TownChildCareGet,
)

logger = logging.getLogger(__name__)

AGE_GROUPS = {"infant": "Infant", "toddler": "Toddler", "preschool": "Preschool", "school_age": "School Age"}
DAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
PERIODS = ("hourly", "daily", "weekly", "monthly")
TOTALS = ("programs", "capacity", "licensed_programs", "licensed_capacity", "infant_capacity", "toddler_capacity",
          "infant_programs", "toddler_programs", "preschool_programs", "school_age_programs",
          "infant_vacancies", "toddler_vacancies", "preschool_vacancies", "school_age_vacancies")
SNAPSHOT = ("capacity", "infant_capacity", "toddler_capacity", "infant_vacancies", "toddler_vacancies",
            "preschool_vacancies", "school_age_vacancies", "vacancies_updated")
PROGRAM = ("id", "provider_number", "name", "license_issue_date", "license_expiration_date", "issued_to", "main_contact",
           "phone", "email_hidden", "street", "city", "zip", "latitude", "longitude", "min_age_months", "max_age_months",
           "infant", "toddler", "preschool", "school_age", "age_groups_source", "head_start", "early_head_start",
           "accepts_scholarship", "preventive_protective_care", "gsq_step", "details_updated", "is_current")


@lru_cache
def _detail_url() -> str:
    return load_config("child_care_config.yaml")["detail_url"]


def _as_of(value: Optional[str]) -> Optional[date]:
    try:
        return date.fromisoformat(value) if value else None
    except ValueError:
        raise HTTPException(status_code=422, detail=f"as_of {value!r} isn't a date (YYYY-MM-DD)")


def _names(session: Session, model) -> dict:
    return {row.id: row.name for row in session.exec(select(model)).all()}


def _district_towns(district_id: int):
    return select(TownDistrictLink.town_id_fk).where(TownDistrictLink.district_id_fk == district_id)


class ChildCareService:
    def get_state_totals(self, session: Session, *, as_of: Optional[str] = None) -> List[StateChildCareGet]:
        """Each download's programs added up statewide, oldest first"""
        try:
            stmt = select(StateChildCare).order_by(StateChildCare.as_of)
            if as_of:
                stmt = stmt.where(StateChildCare.as_of == _as_of(as_of))
            return [StateChildCareGet(as_of=row.as_of, **{field: getattr(row, field) for field in TOTALS})
                    for row in session.exec(stmt).all()]
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error fetching state child care totals: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch state child care totals")

    def get_town_totals(self, session: Session, *, as_of: Optional[str] = None, town_id: Optional[int] = None,
                        district_id: Optional[int] = None) -> List[TownChildCareGet]:
        """Each download's programs added up by town, by download and then town name; district_id gives that
        district's towns"""
        try:
            stmt = select(TownChildCare, Town.name).join(Town, TownChildCare.town_id_fk == Town.id)
            if as_of:
                stmt = stmt.where(TownChildCare.as_of == _as_of(as_of))
            if town_id is not None:
                stmt = stmt.where(TownChildCare.town_id_fk == town_id)
            if district_id is not None:
                stmt = stmt.where(TownChildCare.town_id_fk.in_(_district_towns(district_id)))
            stmt = stmt.order_by(TownChildCare.as_of, Town.name)
            return [TownChildCareGet(town_id=row.town_id_fk, town_name=name, as_of=row.as_of,
                                     **{field: getattr(row, field) for field in TOTALS})
                    for row, name in session.exec(stmt).all()]
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error fetching town child care totals: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch town child care totals")

    def get_district_totals(self, session: Session, *, as_of: Optional[str] = None,
                            district_id: Optional[int] = None) -> List[DistrictChildCareGet]:
        """Each download's programs added up by the district that teaches each town's kindergarten, by
        download and then district name"""
        try:
            stmt = select(DistrictChildCare, District.name).join(District, DistrictChildCare.district_id_fk == District.id)
            if as_of:
                stmt = stmt.where(DistrictChildCare.as_of == _as_of(as_of))
            if district_id is not None:
                stmt = stmt.where(DistrictChildCare.district_id_fk == district_id)
            stmt = stmt.order_by(DistrictChildCare.as_of, District.name)
            return [DistrictChildCareGet(district_id=row.district_id_fk, district_name=name, as_of=row.as_of,
                                         **{field: getattr(row, field) for field in TOTALS})
                    for row, name in session.exec(stmt).all()]
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error fetching district child care totals: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch district child care totals")

    def _program(self, program: ChildCareProgram, snapshot: ChildCareProgramSnapshot,
                 town_name: Optional[str], hide_hidden_email: bool, names: dict) -> dict:
        program_type, is_licensed = names["type"][program.program_type_id_fk]
        return {
            **{field: getattr(program, field) for field in PROGRAM},
            "program_type": program_type,
            "is_licensed": is_licensed,
            "email": None if program.email_hidden and hide_hidden_email else program.email,
            "town_id": program.town_id_fk,
            "town_name": town_name,
            "county": names["county"].get(program.county_id_fk),
            "region": names["region"].get(program.region_id_fk),
            "quality_rating": names["quality"].get(program.quality_rating_id_fk),
            "as_of": snapshot.as_of,
            "license_status": names["status"].get(snapshot.license_status_id_fk),
            "availability": names["availability"].get(snapshot.availability_id_fk),
            **{field: getattr(snapshot, field) for field in SNAPSHOT},
            "source_url": _detail_url().format(id=program.source_id),
        }

    def _lookups(self, session: Session) -> dict:
        return {
            "type": {row.id: (row.name, row.is_licensed) for row in session.exec(select(ChildCareProgramType)).all()},
            "county": _names(session, County),
            "region": _names(session, ChildCareRegion),
            "quality": _names(session, ChildCareQualityRating),
            "status": _names(session, ChildCareLicenseStatus),
            "availability": _names(session, ChildCareAvailability),
        }

    def get_programs(
        self,
        session: Session,
        *,
        town_id: Optional[int] = None,
        district_id: Optional[int] = None,
        program_type_id: Optional[int] = None,
        age_group: Optional[str] = None,
        availability_id: Optional[int] = None,
        has_vacancies: Optional[bool] = None,
        accepts_scholarship: Optional[bool] = None,
        is_current: Optional[bool] = True,
        hide_hidden_email: bool = False,
    ) -> List[ChildCareProgramGet]:
        """Programs with their latest download's license status, capacity and vacancies, by town and then name"""
        try:
            latest = (select(ChildCareProgramSnapshot.program_id_fk, func.max(ChildCareProgramSnapshot.as_of).label("as_of"))
                      .group_by(ChildCareProgramSnapshot.program_id_fk).subquery())
            stmt = (select(ChildCareProgram, ChildCareProgramSnapshot, Town.name)
                    .join(latest, latest.c.program_id_fk == ChildCareProgram.id)
                    .join(ChildCareProgramSnapshot, (ChildCareProgramSnapshot.program_id_fk == ChildCareProgram.id)
                          & (ChildCareProgramSnapshot.as_of == latest.c.as_of))
                    .outerjoin(Town, Town.id == ChildCareProgram.town_id_fk))
            if town_id is not None:
                stmt = stmt.where(ChildCareProgram.town_id_fk == town_id)
            if district_id is not None:
                stmt = stmt.where(ChildCareProgram.town_id_fk.in_(_district_towns(district_id)))
            if program_type_id is not None:
                stmt = stmt.where(ChildCareProgram.program_type_id_fk == program_type_id)
            if age_group:
                stmt = stmt.where(getattr(ChildCareProgram, age_group).is_(True))
            if availability_id is not None:
                stmt = stmt.where(ChildCareProgramSnapshot.availability_id_fk == availability_id)
            if has_vacancies is not None:
                groups = [age_group] if age_group else list(AGE_GROUPS)
                vacancies = or_(*(func.coalesce(getattr(ChildCareProgramSnapshot, f"{group}_vacancies"), 0) > 0
                                  for group in groups))
                stmt = stmt.where(vacancies if has_vacancies else ~vacancies)
            if accepts_scholarship is not None:
                stmt = stmt.where(ChildCareProgram.accepts_scholarship == accepts_scholarship)
            if is_current is not None:
                stmt = stmt.where(ChildCareProgram.is_current == is_current)
            stmt = stmt.order_by(Town.name, ChildCareProgram.name)
            names = self._lookups(session)
            return [ChildCareProgramGet(**self._program(program, snapshot, town_name, hide_hidden_email, names))
                    for program, snapshot, town_name in session.exec(stmt).all()]
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error fetching child care programs: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch child care programs")

    def get_program(self, session: Session, program_id: int, hide_hidden_email: bool = False) -> ChildCareProgramDetailGet:
        """One program with its hours, rates, features, licensing visits and every download's snapshot"""
        try:
            program = session.get(ChildCareProgram, program_id)
            if program is None:
                raise HTTPException(status_code=404, detail=f"No child care program {program_id}")
            snapshots = session.exec(select(ChildCareProgramSnapshot)
                                     .where(ChildCareProgramSnapshot.program_id_fk == program_id)
                                     .order_by(ChildCareProgramSnapshot.as_of)).all()
            town = session.get(Town, program.town_id_fk) if program.town_id_fk else None
            names = self._lookups(session)
            hours = session.exec(select(ChildCareProgramHours).where(ChildCareProgramHours.program_id_fk == program_id)
                                 .order_by(ChildCareProgramHours.schedule, ChildCareProgramHours.day_of_week,
                                           ChildCareProgramHours.opens)).all()
            rates = sorted(session.exec(select(ChildCareProgramRate).where(ChildCareProgramRate.program_id_fk == program_id)).all(),
                           key=lambda rate: (rate.schedule, list(AGE_GROUPS.values()).index(rate.age_group), PERIODS.index(rate.period)))
            features = {}
            for code, category_name, value in session.exec(
                    select(ChildCareFeatureCategory.code, ChildCareFeatureCategory.name, ChildCareFeature.name)
                    .join(ChildCareFeature, ChildCareFeature.category_id_fk == ChildCareFeatureCategory.id)
                    .join(ChildCareProgramFeatureLink, ChildCareProgramFeatureLink.feature_id_fk == ChildCareFeature.id)
                    .where(ChildCareProgramFeatureLink.program_id_fk == program_id)
                    .order_by(ChildCareFeatureCategory.id, ChildCareFeature.name)).all():
                features.setdefault(code, {"category": code, "category_name": category_name, "values": []})["values"].append(value)
            review_types = _names(session, ChildCareReviewType)
            inspections = session.exec(select(ChildCareInspection).where(ChildCareInspection.program_id_fk == program_id)
                                       .order_by(ChildCareInspection.review_date.desc())).all()
            return ChildCareProgramDetailGet(
                **self._program(program, snapshots[-1], town.name if town else None, hide_hidden_email, names),
                mailing_street=program.mailing_street,
                mailing_city=program.mailing_city,
                mailing_zip=program.mailing_zip,
                hours=[{"schedule": h.schedule, "day_of_week": h.day_of_week, "day": DAYS[h.day_of_week - 1],
                        "opens": h.opens, "closes": h.closes} for h in hours],
                rates=[{"schedule": r.schedule, "age_group": r.age_group, "period": r.period, "amount": r.amount} for r in rates],
                features=list(features.values()),
                inspections=[{"review_date": i.review_date, "review_type": review_types.get(i.review_type_id_fk),
                              "items_reviewed": i.items_reviewed, "items_compliant": i.items_compliant,
                              "document_url": i.document_url} for i in inspections],
                snapshots=[{"as_of": s.as_of, "license_status": names["status"].get(s.license_status_id_fk),
                            "availability": names["availability"].get(s.availability_id_fk),
                            **{field: getattr(s, field) for field in SNAPSHOT}} for s in snapshots],
            )
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error fetching child care program {program_id}: {e}")
            raise HTTPException(status_code=500, detail="Failed to fetch the child care program")


child_care_service = ChildCareService()
