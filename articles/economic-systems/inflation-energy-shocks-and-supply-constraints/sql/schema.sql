DROP TABLE IF EXISTS price_index_scenarios;
DROP TABLE IF EXISTS sector_energy_pass_through_scenarios;
DROP TABLE IF EXISTS household_energy_burden_scenarios;
DROP TABLE IF EXISTS import_price_transmission_scenarios;
DROP TABLE IF EXISTS supply_bottleneck_scenarios;
DROP TABLE IF EXISTS market_power_price_amplification_scenarios;
DROP TABLE IF EXISTS resilience_policy_scenarios;

CREATE TABLE price_index_scenarios (
    scenario TEXT,
    period INTEGER,
    price_level REAL
);

CREATE TABLE sector_energy_pass_through_scenarios (
    sector TEXT PRIMARY KEY,
    energy_cost_change REAL,
    wage_cost_change REAL,
    materials_cost_change REAL,
    alpha_energy REAL,
    beta_wage REAL,
    gamma_materials REAL
);

CREATE TABLE household_energy_burden_scenarios (
    household_group TEXT PRIMARY KEY,
    income REAL,
    energy_spending REAL,
    transport_fuel_spending REAL,
    nominal_wage REAL,
    price_level_relative REAL
);

CREATE TABLE import_price_transmission_scenarios (
    scenario TEXT PRIMARY KEY,
    world_price_change REAL,
    exchange_rate_effect REAL,
    import_dependence REAL,
    energy_share_of_imports REAL
);

CREATE TABLE supply_bottleneck_scenarios (
    scenario TEXT PRIMARY KEY,
    capital_capacity REAL,
    labor_capacity REAL,
    energy_capacity REAL,
    logistics_capacity REAL,
    supply_availability REAL
);

CREATE TABLE market_power_price_amplification_scenarios (
    sector TEXT PRIMARY KEY,
    cost_shock REAL,
    market_concentration_index REAL,
    margin_expansion REAL,
    demand_necessity_score REAL
);

CREATE TABLE resilience_policy_scenarios (
    policy TEXT PRIMARY KEY,
    energy_resilience REAL,
    supply_diversification REAL,
    household_protection REAL,
    infrastructure_capacity REAL,
    public_buffer_capacity REAL,
    near_term_disinflation REAL
);
