from collections import defaultdict
from typing import List, Optional

from sqlmodel import Session, select

from app.model.census_finance import CensusRevenueItem, CensusStateEnrollment, CensusStateRevenue
from app.model.naep import Jurisdiction
from app.service.inflation import in_dollars_of as adjust

SOURCES = ("federal", "state", "local")
# What a revenue row at each level is grouped by
LEVEL_KEYS = {"source": ("source",), "category": ("source", "category"), "item": ("source", "category", "code")}


def _place(place: Jurisdiction) -> dict:
    return {"id": place.id, "code": place.code, "name": place.name, "kind": place.kind}


def _share(part: int, whole: int) -> Optional[float]:
    return round(100 * part / whole, 2) if whole else None


def _figures(amount: int, year: int, enrollment: Optional[int], to_year: Optional[int]) -> dict:
    """An amount in dollars, per pupil, and in another year's dollars when asked"""
    figures = {"amount": amount, "per_pupil": round(amount / enrollment, 2) if enrollment else None}
    if to_year is not None:
        adjusted = adjust(amount, year, to_year)
        figures["amount_adjusted"] = adjusted
        figures["per_pupil_adjusted"] = round(adjusted / enrollment, 2) if enrollment else None
    return figures


class CensusFinanceService:
    def get_items(self, session: Session) -> List[CensusRevenueItem]:
        return session.exec(select(CensusRevenueItem).order_by(CensusRevenueItem.display_order)).all()

    def get_enrollment(self, session: Session, year: Optional[int] = None, jurisdiction: Optional[str] = None) -> List[dict]:
        statement = (
            select(CensusStateEnrollment, Jurisdiction)
            .join(Jurisdiction, Jurisdiction.id == CensusStateEnrollment.jurisdiction_id_fk)
            .order_by(CensusStateEnrollment.year, Jurisdiction.id)
        )
        if year is not None:
            statement = statement.where(CensusStateEnrollment.year == year)
        if jurisdiction is not None:
            statement = statement.where(Jurisdiction.code == jurisdiction.upper())
        return [{"id": row.id, "year": row.year, "jurisdiction": _place(place), "enrollment": row.enrollment}
                for row, place in session.exec(statement).all()]

    def _amounts(self, session: Session, year: Optional[int], jurisdiction: Optional[str]) -> tuple:
        """Every item's amount for the places and years asked for, in display order, with each place and
        year's enrollment."""
        statement = (
            select(CensusStateRevenue, Jurisdiction, CensusRevenueItem)
            .join(Jurisdiction, Jurisdiction.id == CensusStateRevenue.jurisdiction_id_fk)
            .join(CensusRevenueItem, CensusRevenueItem.id == CensusStateRevenue.census_revenue_item_id_fk)
            .order_by(CensusStateRevenue.year, Jurisdiction.id, CensusRevenueItem.display_order)
        )
        if year is not None:
            statement = statement.where(CensusStateRevenue.year == year)
        if jurisdiction is not None:
            statement = statement.where(Jurisdiction.code == jurisdiction.upper())
        enrollment = {(row["year"], row["jurisdiction"]["id"]): row["enrollment"]
                      for row in self.get_enrollment(session, year, jurisdiction)}
        return session.exec(statement).all(), enrollment

    def get_revenue(self, session: Session, year: Optional[int] = None, jurisdiction: Optional[str] = None,
                    source: Optional[str] = None, category: Optional[str] = None, level: str = "item",
                    in_dollars_of: Optional[int] = None) -> List[dict]:
        """Revenue grouped by source, category or item, with each group's share of its source and of all
        revenue, and its amount per pupil. Shares are of the full totals, whatever is filtered."""
        rows, enrollment = self._amounts(session, year, jurisdiction)
        totals, source_totals = defaultdict(int), defaultdict(int)
        groups = {}
        for revenue, place, item in rows:
            dollars = revenue.amount_thousands * 1000
            totals[(revenue.year, place.id)] += dollars
            source_totals[(revenue.year, place.id, item.source)] += dollars
            if (source is not None and item.source != source) or (category is not None and item.category != category):
                continue
            fields = {"source": item.source, "category": item.category, "code": item.code}
            key = (revenue.year, place.id, *(fields[name] for name in LEVEL_KEYS[level]))
            group = groups.setdefault(key, {"year": revenue.year, "place": place, "item": item, "amount": 0})
            group["amount"] += dollars

        results = []
        for group in sorted(groups.values(), key=lambda g: (g["year"], g["place"].id, SOURCES.index(g["item"].source), g["item"].display_order)):
            year_, place, item = group["year"], group["place"], group["item"]
            students = enrollment.get((year_, place.id))
            results.append({
                "year": year_,
                "jurisdiction": _place(place),
                "level": level,
                "source": item.source,
                "category": item.category if level != "source" else None,
                "item": {"id": item.id, "code": item.code, "name": item.name} if level == "item" else None,
                "share_of_source": _share(group["amount"], source_totals[(year_, place.id, item.source)]) if level != "source" else None,
                "share_of_total": _share(group["amount"], totals[(year_, place.id)]),
                "enrollment": students,
                "in_dollars_of": in_dollars_of,
                **_figures(group["amount"], year_, students, in_dollars_of),
            })
        return results

    def get_summary(self, session: Session, year: Optional[int] = None, jurisdiction: Optional[str] = None,
                    in_dollars_of: Optional[int] = None) -> List[dict]:
        """Each place and year's total revenue and its federal, state and local parts."""
        rows, enrollment = self._amounts(session, year, jurisdiction)
        places, amounts = {}, defaultdict(lambda: dict.fromkeys(SOURCES, 0))
        for revenue, place, item in rows:
            places[(revenue.year, place.id)] = place
            amounts[(revenue.year, place.id)][item.source] += revenue.amount_thousands * 1000
        results = []
        for (year_, place_id), by_source in amounts.items():
            students = enrollment.get((year_, place_id))
            total = sum(by_source.values())
            summary = {"year": year_, "jurisdiction": _place(places[(year_, place_id)]), "enrollment": students,
                       "in_dollars_of": in_dollars_of,
                       "total": {"share_of_total": 100.0 if total else None, **_figures(total, year_, students, in_dollars_of)}}
            for name, amount in by_source.items():
                summary[name] = {"share_of_total": _share(amount, total), **_figures(amount, year_, students, in_dollars_of)}
            results.append(summary)
        return results


census_finance_service = CensusFinanceService()
