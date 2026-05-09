-- Business Cycles SQL Schema
-- Designed for SQLite-compatible analysis.

DROP TABLE IF EXISTS monthly_indicators;
DROP TABLE IF EXISTS quarterly_indicators;

CREATE TABLE monthly_indicators (
    date TEXT PRIMARY KEY,
    recession_indicator INTEGER,
    business_cycle_phase TEXT,
    unemployment_rate REAL,
    payroll_employment REAL,
    industrial_production REAL,
    federal_funds_rate REAL,
    cpi REAL,
    retail_sales REAL,
    real_disposable_income REAL,
    payroll_growth_yoy_pct REAL,
    industrial_production_yoy_pct REAL,
    retail_sales_yoy_pct REAL,
    real_income_yoy_pct REAL,
    cpi_inflation_yoy_pct REAL,
    delta_unemployment_rate REAL
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
    retail_sales REAL,
    real_disposable_income REAL,
    recession_indicator INTEGER,
    business_cycle_phase TEXT,
    real_gdp_growth_annualized REAL,
    output_gap_pct REAL,
    delta_unemployment_rate REAL,
    payroll_growth_yoy_pct REAL,
    industrial_production_yoy_pct REAL,
    retail_sales_yoy_pct REAL,
    real_income_yoy_pct REAL,
    cpi_inflation_yoy_pct REAL,
    rolling_gdp_volatility_12q REAL,
    rolling_unemployment_volatility_12q REAL
);
