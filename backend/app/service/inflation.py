"""
The site's inflation adjustment, shared by the Ask feature and the Census school finance API.

CPI_BY_YEAR matches CPI_BY_YEAR in the frontend's src/utils/calculations.ts; keep the two the same.
"""
from typing import Optional

# BLS CPI-U annual averages, U.S. city average, looked up by the year a school or fiscal year ends.
# A year outside the table uses the nearest year's.
CPI_BY_YEAR = {
    2000: 172.2, 2001: 177.1, 2002: 179.9, 2003: 184.0, 2004: 188.9, 2005: 195.3, 2006: 201.6, 2007: 207.3,
    2008: 215.3, 2009: 214.5, 2010: 218.1, 2011: 224.9, 2012: 229.6, 2013: 233.0, 2014: 236.7, 2015: 237.0,
    2016: 240.0, 2017: 245.1, 2018: 251.1, 2019: 255.7, 2020: 258.8, 2021: 271.0, 2022: 292.7, 2023: 304.7,
    2024: 313.7, 2025: 321.9, 2026: 333.5,
}


def in_dollars_of(amount: Optional[float], from_year: int, to_year: int) -> Optional[float]:
    """An amount from one year in another year's dollars, as the site's inflation switch shows it."""
    def cpi(year: int) -> float:
        return CPI_BY_YEAR[min(max(year, min(CPI_BY_YEAR)), max(CPI_BY_YEAR))]
    return None if amount is None else round(amount * cpi(to_year) / cpi(from_year))
