DROP TABLE IF EXISTS sector_emissions;
DROP TABLE IF EXISTS policy_packages;
DROP TABLE IF EXISTS transition_investment;
DROP TABLE IF EXISTS carbon_lock_in;
DROP TABLE IF EXISTS damage_adaptation;
DROP TABLE IF EXISTS just_transition;
DROP TABLE IF EXISTS hard_to_abate;
DROP TABLE IF EXISTS global_equity;
DROP TABLE IF EXISTS implementation_credibility;

CREATE TABLE sector_emissions (
    sector TEXT PRIMARY KEY,
    output REAL,
    energy_intensity REAL,
    carbon_intensity REAL,
    old_emissions_intensity REAL,
    new_emissions_intensity REAL,
    years REAL,
    abatement_readiness REAL
);

CREATE TABLE policy_packages (
    package TEXT PRIMARY KEY,
    carbon_price_strength REAL,
    regulatory_strength REAL,
    public_investment REAL,
    industrial_policy REAL,
    social_protection REAL,
    implementation_capacity REAL
);

CREATE TABLE transition_investment (
    scenario TEXT PRIMARY KEY,
    public_investment REAL,
    private_capital REAL,
    policy_credibility REAL,
    cost_of_capital_support REAL,
    permitting_capacity REAL,
    grid_readiness REAL
);

CREATE TABLE carbon_lock_in (
    system TEXT PRIMARY KEY,
    capital_stock_life REAL,
    infrastructure_dependence REAL,
    incumbent_power REAL,
    consumer_switching_barrier REAL,
    replacement_readiness REAL,
    stranded_asset_risk REAL
);

CREATE TABLE damage_adaptation (
    region TEXT PRIMARY KEY,
    temperature_stress REAL,
    flood_exposure REAL,
    wildfire_smoke REAL,
    economic_exposure REAL,
    vulnerability REAL,
    adaptation_capacity REAL,
    public_health_capacity REAL
);

CREATE TABLE just_transition (
    community TEXT PRIMARY KEY,
    worker_exposure REAL,
    retraining REAL,
    regional_investment REAL,
    income_support REAL,
    public_services REAL,
    new_industry_pipeline REAL,
    labor_standards REAL
);

CREATE TABLE hard_to_abate (
    sector TEXT PRIMARY KEY,
    process_emissions REAL,
    temperature_requirement REAL,
    technology_readiness REAL,
    procurement_leverage REAL,
    demand_reduction_potential REAL,
    carbon_capture_relevance REAL
);

CREATE TABLE global_equity (
    country_group TEXT PRIMARY KEY,
    historic_responsibility REAL,
    current_emissions REAL,
    fiscal_capacity REAL,
    climate_vulnerability REAL,
    development_need REAL,
    technology_capacity REAL
);

CREATE TABLE implementation_credibility (
    scenario TEXT PRIMARY KEY,
    target_clarity REAL,
    administrative_capacity REAL,
    fiscal_commitment REAL,
    policy_durability REAL,
    public_trust REAL,
    coordination_capacity REAL
);
