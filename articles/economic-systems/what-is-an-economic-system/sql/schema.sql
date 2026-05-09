-- Economic System SQL Schema
-- Designed for SQLite-compatible systems analysis.

DROP TABLE IF EXISTS sectors;
DROP TABLE IF EXISTS input_output_requirements;
DROP TABLE IF EXISTS final_demand_scenarios;
DROP TABLE IF EXISTS allocation_profiles;
DROP TABLE IF EXISTS reproduction_parameters;
DROP TABLE IF EXISTS economic_system_results;

CREATE TABLE sectors (
    sector_code TEXT PRIMARY KEY,
    sector TEXT,
    institutional_role TEXT,
    wage_share REAL,
    profit_share REAL,
    public_or_mixed_share REAL,
    ecological_intensity REAL,
    employment_intensity REAL
);

CREATE TABLE input_output_requirements (
    supplying_sector TEXT,
    purchasing_sector TEXT,
    input_requirement REAL
);

CREATE TABLE final_demand_scenarios (
    scenario TEXT PRIMARY KEY,
    energy REAL,
    manufacturing REAL,
    services REAL,
    public_care REAL,
    restoration REAL
);

CREATE TABLE allocation_profiles (
    scenario TEXT PRIMARY KEY,
    consumption_share REAL,
    investment_share REAL,
    public_provision_share REAL,
    restoration_share REAL
);

CREATE TABLE reproduction_parameters (
    scenario TEXT PRIMARY KEY,
    initial_produced_capital REAL,
    initial_natural_capital REAL,
    investment REAL,
    depreciation_rate REAL,
    regeneration REAL,
    depletion REAL,
    periods INTEGER
);

CREATE TABLE economic_system_results (
    scenario TEXT,
    sector_code TEXT,
    final_demand REAL,
    total_output REAL,
    indirect_output_requirement REAL,
    output_multiplier REAL,
    baseline_output REAL,
    output_change_from_baseline REAL
);
