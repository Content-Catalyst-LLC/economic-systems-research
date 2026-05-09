-- Limits of Stabilization Policy SQL Schema
-- Designed for SQLite-compatible analysis.

DROP TABLE IF EXISTS monthly_constraint_indicators;
DROP TABLE IF EXISTS quarterly_constraint_indicators;

CREATE TABLE monthly_constraint_indicators (
    date TEXT PRIMARY KEY,
    recession_indicator INTEGER,
    constraint_phase TEXT,
    unemployment_rate REAL,
    federal_funds_rate REAL,
    treasury_bill_3m REAL,
    treasury_10y REAL,
    cpi REAL,
    cpi_inflation_yoy_pct REAL,
    delta_unemployment_rate REAL,
    real_interest_rate_proxy REAL,
    lower_bound_constraint_flag INTEGER
);

CREATE TABLE quarterly_constraint_indicators (
    date TEXT PRIMARY KEY,
    real_gdp REAL,
    potential_gdp REAL,
    debt_to_gdp REAL,
    unemployment_rate REAL,
    federal_funds_rate REAL,
    treasury_bill_3m REAL,
    treasury_10y REAL,
    cpi REAL,
    recession_indicator INTEGER,
    constraint_phase TEXT,
    real_gdp_growth_annualized REAL,
    output_gap_pct REAL,
    cpi_inflation_yoy_pct REAL,
    delta_unemployment_rate REAL,
    real_interest_rate_proxy REAL,
    nominal_growth_proxy REAL,
    interest_growth_gap REAL,
    debt_stabilizing_primary_balance_pct_gdp REAL,
    lower_bound_constraint_flag INTEGER,
    inflation_constraint_flag INTEGER,
    fiscal_space_constraint_flag INTEGER,
    crowding_out_proxy REAL
);
