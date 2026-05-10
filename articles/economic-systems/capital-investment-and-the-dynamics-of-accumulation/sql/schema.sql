DROP TABLE IF EXISTS capital_stock_scenarios;
DROP TABLE IF EXISTS investment_project_scenarios;
DROP TABLE IF EXISTS maintenance_scenarios;
DROP TABLE IF EXISTS ownership_distribution_scenarios;
DROP TABLE IF EXISTS finance_direction_scenarios;
DROP TABLE IF EXISTS sustainable_investment_scenarios;

CREATE TABLE capital_stock_scenarios (
    scenario TEXT PRIMARY KEY,
    initial_capital REAL,
    annual_investment REAL,
    depreciation_rate REAL,
    labor REAL,
    output REAL
);

CREATE TABLE investment_project_scenarios (
    project TEXT PRIMARY KEY,
    cashflow_year_0 REAL,
    cashflow_year_1 REAL,
    cashflow_year_2 REAL,
    cashflow_year_3 REAL,
    cashflow_year_4 REAL,
    cashflow_year_5 REAL,
    private_discount_rate REAL,
    public_discount_rate REAL
);

CREATE TABLE maintenance_scenarios (
    scenario TEXT,
    period INTEGER,
    initial_backlog REAL,
    new_maintenance_need REAL,
    actual_maintenance REAL
);

CREATE TABLE ownership_distribution_scenarios (
    scenario TEXT PRIMARY KEY,
    wage_share REAL,
    profit_share REAL,
    tax_public_share REAL,
    rent_share REAL,
    public_reinvestment_share REAL
);

CREATE TABLE finance_direction_scenarios (
    finance_channel TEXT PRIMARY KEY,
    flow_share REAL,
    productive_capacity_score REAL,
    speculation_score REAL,
    extraction_score REAL,
    resilience_score REAL
);

CREATE TABLE sustainable_investment_scenarios (
    project TEXT PRIMARY KEY,
    financial_return_score REAL,
    resilience_score REAL,
    ecological_alignment_score REAL,
    public_value_score REAL,
    maintenance_score REAL
);
