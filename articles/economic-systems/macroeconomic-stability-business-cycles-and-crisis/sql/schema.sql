DROP TABLE IF EXISTS aggregate_demand_scenarios;
DROP TABLE IF EXISTS business_cycle_phase_scenarios;
DROP TABLE IF EXISTS household_balance_sheet_scenarios;
DROP TABLE IF EXISTS credit_contraction_scenarios;
DROP TABLE IF EXISTS fiscal_stabilization_scenarios;
DROP TABLE IF EXISTS open_economy_shock_scenarios;
DROP TABLE IF EXISTS inflation_unemployment_policy_scenarios;
DROP TABLE IF EXISTS crisis_recovery_path_scenarios;

CREATE TABLE aggregate_demand_scenarios (
    scenario TEXT PRIMARY KEY,
    consumption REAL,
    investment REAL,
    government_spending REAL,
    net_exports REAL,
    potential_output REAL
);

CREATE TABLE business_cycle_phase_scenarios (
    year INTEGER PRIMARY KEY,
    cycle_phase TEXT,
    output_index REAL,
    employment_index REAL,
    expectations_index REAL,
    credit_growth REAL,
    inventory_pressure REAL
);

CREATE TABLE household_balance_sheet_scenarios (
    household_group TEXT PRIMARY KEY,
    income REAL,
    debt_service REAL,
    liquid_savings REAL,
    job_loss_income_shock REAL,
    price_shock REAL
);

CREATE TABLE credit_contraction_scenarios (
    scenario TEXT PRIMARY KEY,
    credit_growth REAL,
    nominal_debt REAL,
    price_level REAL,
    asset_price_change REAL,
    default_pressure REAL
);

CREATE TABLE fiscal_stabilization_scenarios (
    scenario TEXT PRIMARY KEY,
    delta_g REAL,
    fiscal_multiplier REAL,
    automatic_stabilizer_strength REAL,
    initial_output_gap REAL,
    public_capacity_score REAL
);

CREATE TABLE open_economy_shock_scenarios (
    external_shock TEXT PRIMARY KEY,
    shock_intensity REAL,
    export_exposure REAL,
    import_price_exposure REAL,
    capital_flow_exposure REAL,
    fx_debt_exposure REAL
);

CREATE TABLE inflation_unemployment_policy_scenarios (
    scenario TEXT PRIMARY KEY,
    inflation_pressure REAL,
    unemployment_gap REAL,
    supply_shock_intensity REAL,
    policy_rate_response REAL
);

CREATE TABLE crisis_recovery_path_scenarios (
    recovery_path TEXT,
    period INTEGER,
    output_index REAL,
    employment_index REAL,
    public_capacity_index REAL
);
