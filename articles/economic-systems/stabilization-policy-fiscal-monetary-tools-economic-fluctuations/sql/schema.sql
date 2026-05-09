-- Stabilization Policy SQL Schema
-- Designed for SQLite-compatible analysis.

DROP TABLE IF EXISTS monthly_policy_indicators;
DROP TABLE IF EXISTS quarterly_policy_indicators;

CREATE TABLE monthly_policy_indicators (
    date TEXT PRIMARY KEY,
    recession_indicator INTEGER,
    policy_phase TEXT,
    unemployment_rate REAL,
    payroll_employment REAL,
    federal_funds_rate REAL,
    treasury_bill_3m REAL,
    cpi REAL,
    cpi_inflation_yoy_pct REAL,
    delta_unemployment_rate REAL,
    delta_federal_funds_rate REAL,
    payroll_growth_yoy_pct REAL
);

CREATE TABLE quarterly_policy_indicators (
    date TEXT PRIMARY KEY,
    real_gdp REAL,
    potential_gdp REAL,
    real_government_consumption_investment REAL,
    unemployment_rate REAL,
    payroll_employment REAL,
    federal_funds_rate REAL,
    treasury_bill_3m REAL,
    cpi REAL,
    recession_indicator INTEGER,
    policy_phase TEXT,
    real_gdp_growth_annualized REAL,
    output_gap_pct REAL,
    cpi_inflation_yoy_pct REAL,
    delta_unemployment_rate REAL,
    delta_federal_funds_rate REAL,
    payroll_growth_yoy_pct REAL,
    gov_spending_growth_yoy_pct REAL,
    taylor_rule_rate REAL,
    policy_rate_gap REAL
);
