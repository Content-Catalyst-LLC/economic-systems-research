DROP TABLE IF EXISTS strategic_sector_scenarios;
DROP TABLE IF EXISTS support_conditionality_scenarios;
DROP TABLE IF EXISTS development_finance_scenarios;
DROP TABLE IF EXISTS infrastructure_energy_scenarios;
DROP TABLE IF EXISTS skills_labor_scenarios;
DROP TABLE IF EXISTS capture_risk_scenarios;
DROP TABLE IF EXISTS regional_cluster_scenarios;
DROP TABLE IF EXISTS green_industrial_policy_scenarios;

CREATE TABLE strategic_sector_scenarios (
    sector TEXT PRIMARY KEY,
    sector_output REAL,
    total_output REAL,
    sector_labor REAL,
    sector_exports REAL,
    technology_depth REAL,
    learning_potential REAL,
    domestic_linkage_potential REAL
);

CREATE TABLE support_conditionality_scenarios (
    sector TEXT PRIMARY KEY,
    public_support REAL,
    productivity_gain REAL,
    employment_gain REAL,
    export_growth REAL,
    local_supplier_share REAL,
    emissions_reduction REAL,
    support_duration_years REAL
);

CREATE TABLE development_finance_scenarios (
    scenario TEXT PRIMARY KEY,
    patient_credit_share REAL,
    industrial_credit_share REAL,
    speculative_credit_share REAL,
    fx_debt_exposure REAL,
    development_bank_capacity REAL,
    credit_monitoring_quality REAL
);

CREATE TABLE infrastructure_energy_scenarios (
    region TEXT PRIMARY KEY,
    transport_reliability REAL,
    port_access REAL,
    energy_reliability REAL,
    water_reliability REAL,
    digital_connectivity REAL,
    industrial_land_readiness REAL
);

CREATE TABLE skills_labor_scenarios (
    scenario TEXT PRIMARY KEY,
    technical_training_depth REAL,
    apprenticeship_capacity REAL,
    engineering_depth REAL,
    labor_security REAL,
    wage_progression REAL,
    learning_retention REAL
);

CREATE TABLE capture_risk_scenarios (
    program TEXT PRIMARY KEY,
    market_concentration REAL,
    lobbying_intensity REAL,
    evaluation_strength REAL,
    open_ended_support REAL,
    performance_shortfall REAL,
    public_disclosure REAL
);

CREATE TABLE regional_cluster_scenarios (
    cluster TEXT PRIMARY KEY,
    supplier_density REAL,
    skills_depth REAL,
    infrastructure_quality REAL,
    research_linkage REAL,
    regional_inclusion REAL,
    export_connectivity REAL
);

CREATE TABLE green_industrial_policy_scenarios (
    sector TEXT PRIMARY KEY,
    productivity_gain REAL,
    emissions_reduction REAL,
    domestic_linkage REAL,
    employment_quality REAL,
    resilience_value REAL,
    material_risk REAL
);
