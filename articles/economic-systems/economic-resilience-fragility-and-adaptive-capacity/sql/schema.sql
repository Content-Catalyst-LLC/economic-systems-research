DROP TABLE IF EXISTS resilience_scenarios;
DROP TABLE IF EXISTS fragility_scenarios;
DROP TABLE IF EXISTS adaptive_capacity;
DROP TABLE IF EXISTS shock_scenarios;
DROP TABLE IF EXISTS household_resilience;
DROP TABLE IF EXISTS firm_supply_chain;
DROP TABLE IF EXISTS financial_fragility;
DROP TABLE IF EXISTS labor_adaptation;
DROP TABLE IF EXISTS ecological_energy_risk;
DROP TABLE IF EXISTS recovery_learning;

CREATE TABLE resilience_scenarios (
    scenario TEXT PRIMARY KEY,
    buffers REAL,
    redundancy REAL,
    coordination REAL,
    trust REAL,
    learning REAL,
    recovery_capacity REAL
);

CREATE TABLE fragility_scenarios (
    scenario TEXT PRIMARY KEY,
    leverage REAL,
    concentration REAL,
    exposure REAL,
    underinvestment REAL,
    inequality REAL,
    political_fragmentation REAL
);

CREATE TABLE adaptive_capacity (
    scenario TEXT PRIMARY KEY,
    information REAL,
    fiscal_space REAL,
    skills REAL,
    flexibility REAL,
    legitimacy REAL,
    implementation_capacity REAL
);

CREATE TABLE shock_scenarios (
    shock TEXT PRIMARY KEY,
    shock_magnitude REAL,
    household_vulnerability REAL,
    firm_vulnerability REAL,
    public_capacity REAL,
    infrastructure_integrity REAL,
    recovery_speed REAL
);

CREATE TABLE household_resilience (
    household_group TEXT PRIMARY KEY,
    income_security REAL,
    savings REAL,
    care_access REAL,
    housing_stability REAL,
    social_protection REAL,
    mobility REAL
);

CREATE TABLE firm_supply_chain (
    firm_type TEXT PRIMARY KEY,
    supplier_concentration REAL,
    inventory_buffer REAL,
    credit_access REAL,
    demand_diversification REAL,
    digital_continuity REAL,
    adaptation_capability REAL
);

CREATE TABLE financial_fragility (
    system TEXT PRIMARY KEY,
    leverage REAL,
    refinancing_risk REAL,
    asset_price_dependence REAL,
    liquidity_buffer REAL,
    regulatory_capacity REAL,
    contagion_channels REAL
);

CREATE TABLE labor_adaptation (
    region TEXT PRIMARY KEY,
    skill_transferability REAL,
    training_capacity REAL,
    income_support REAL,
    mobility_support REAL,
    place_based_investment REAL,
    employer_diversity REAL
);

CREATE TABLE ecological_energy_risk (
    system TEXT PRIMARY KEY,
    energy_volatility REAL,
    water_stress REAL,
    climate_hazard REAL,
    material_dependency REAL,
    adaptation_investment REAL,
    ecosystem_integrity REAL
);

CREATE TABLE recovery_learning (
    scenario TEXT PRIMARY KEY,
    response_speed REAL,
    public_capacity REAL,
    household_stability REAL,
    infrastructure_integrity REAL,
    institutional_learning REAL,
    transformational_adaptation REAL
);
