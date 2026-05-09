-- Economic Resilience SQL Schema
-- Designed for SQLite-compatible analysis.

DROP TABLE IF EXISTS monthly_indicators;
DROP TABLE IF EXISTS quarterly_indicators;

CREATE TABLE monthly_indicators (
    date TEXT PRIMARY KEY,
    recession_indicator INTEGER,
    unemployment_rate REAL,
    payroll_employment REAL,
    industrial_production REAL,
    federal_funds_rate REAL,
    cpi REAL,
    unemployment_rate_12m_low REAL,
    unemployment_gap_from_12m_low REAL,
    payroll_growth_yoy_pct REAL,
    industrial_production_yoy_pct REAL,
    cpi_inflation_yoy_pct REAL
);

CREATE TABLE quarterly_indicators (
    date TEXT PRIMARY KEY,
    real_gdp REAL,
    potential_gdp REAL,
    unemployment_rate REAL,
    payroll_employment REAL,
    industrial_production REAL,
    federal_funds_rate REAL,
    cpi REAL,
    recession_indicator INTEGER,
    real_gdp_growth_annualized REAL,
    output_gap_pct REAL,
    delta_unemployment_rate REAL,
    payroll_growth_yoy_pct REAL,
    industrial_production_yoy_pct REAL,
    cpi_inflation_yoy_pct REAL
);
