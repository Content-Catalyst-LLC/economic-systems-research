DROP TABLE IF EXISTS fiscal_position_scenarios;
DROP TABLE IF EXISTS tax_distribution_scenarios;
DROP TABLE IF EXISTS spending_composition_scenarios;
DROP TABLE IF EXISTS fiscal_multiplier_scenarios;
DROP TABLE IF EXISTS infrastructure_maintenance_scenarios;
DROP TABLE IF EXISTS local_fiscal_capacity_scenarios;
DROP TABLE IF EXISTS public_investment_resilience_scenarios;

CREATE TABLE fiscal_position_scenarios (
    scenario TEXT PRIMARY KEY,
    tax_revenue REAL,
    public_spending REAL,
    primary_spending REAL,
    interest_rate REAL,
    debt_stock REAL,
    output REAL
);

CREATE TABLE tax_distribution_scenarios (
    income_group TEXT PRIMARY KEY,
    income REAL,
    tax_paid REAL,
    transfer_received REAL,
    consumption_tax_paid REAL,
    wealth_tax_paid REAL
);

CREATE TABLE spending_composition_scenarios (
    spending_category TEXT PRIMARY KEY,
    spending_amount REAL,
    public_investment_component REAL,
    current_service_component REAL,
    resilience_score REAL
);

CREATE TABLE fiscal_multiplier_scenarios (
    instrument TEXT PRIMARY KEY,
    delta_g REAL,
    fiscal_multiplier REAL,
    slack_index REAL,
    speed_score REAL,
    long_run_capacity_score REAL
);

CREATE TABLE infrastructure_maintenance_scenarios (
    asset_class TEXT PRIMARY KEY,
    maintenance_needed REAL,
    maintenance_actual REAL,
    failure_risk_index REAL,
    replacement_cost_if_deferred REAL
);

CREATE TABLE local_fiscal_capacity_scenarios (
    locality TEXT PRIMARY KEY,
    tax_base_per_capita REAL,
    service_need_index REAL,
    infrastructure_age_index REAL,
    intergovernmental_transfer_per_capita REAL
);

CREATE TABLE public_investment_resilience_scenarios (
    investment_area TEXT PRIMARY KEY,
    public_investment REAL,
    avoided_future_losses REAL,
    productivity_gain REAL,
    equity_score REAL,
    climate_resilience_score REAL
);
