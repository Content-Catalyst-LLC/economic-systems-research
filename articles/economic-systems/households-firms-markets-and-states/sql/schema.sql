DROP TABLE IF EXISTS institutional_actors;
DROP TABLE IF EXISTS institutional_flow_scenarios;
DROP TABLE IF EXISTS market_access_scenarios;
DROP TABLE IF EXISTS risk_distribution_scenarios;

CREATE TABLE institutional_actors (
    actor TEXT PRIMARY KEY,
    core_role TEXT,
    main_inputs TEXT,
    main_outputs TEXT,
    risk_absorption_role TEXT
);

CREATE TABLE institutional_flow_scenarios (
    scenario TEXT PRIMARY KEY,
    household_wages REAL,
    household_transfers REAL,
    asset_income REAL,
    taxes_paid REAL,
    debt_service REAL,
    household_consumption REAL,
    firm_revenue REAL,
    labor_cost REAL,
    capital_cost REAL,
    input_cost REAL,
    public_spending REAL,
    public_transfers REAL,
    public_debt_interest REAL,
    tax_revenue REAL
);

CREATE TABLE market_access_scenarios (
    group_name TEXT PRIMARY KEY,
    need_index REAL,
    income_command REAL,
    price_burden REAL,
    institutional_access REAL,
    population_weight REAL
);

CREATE TABLE risk_distribution_scenarios (
    scenario TEXT PRIMARY KEY,
    household_risk REAL,
    firm_risk REAL,
    market_risk REAL,
    state_risk REAL
);
