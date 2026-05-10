DROP TABLE IF EXISTS stock_flow_scenarios;
DROP TABLE IF EXISTS resource_use_constraints;
DROP TABLE IF EXISTS sector_resource_pressure;
DROP TABLE IF EXISTS ecosystem_functions;
DROP TABLE IF EXISTS governance_regimes;
DROP TABLE IF EXISTS justice_burdens;
DROP TABLE IF EXISTS resilience_dependency;
DROP TABLE IF EXISTS substitution_efficiency;

CREATE TABLE stock_flow_scenarios (
    system TEXT PRIMARY KEY,
    natural_capital_t REAL,
    regeneration REAL,
    degradation REAL,
    threshold REAL,
    life_support_importance REAL,
    irreversibility REAL
);

CREATE TABLE resource_use_constraints (
    resource TEXT PRIMARY KEY,
    resource_use REAL,
    regenerative_capacity REAL,
    emissions REAL,
    absorptive_capacity REAL,
    social_necessity REAL,
    substitutability REAL
);

CREATE TABLE sector_resource_pressure (
    sector TEXT PRIMARY KEY,
    material_intensity REAL,
    energy_intensity REAL,
    water_intensity REAL,
    land_intensity REAL,
    waste_intensity REAL,
    import_dependence REAL,
    social_necessity REAL
);

CREATE TABLE ecosystem_functions (
    ecosystem TEXT PRIMARY KEY,
    water_filtration REAL,
    flood_buffering REAL,
    carbon_storage REAL,
    habitat_support REAL,
    soil_protection REAL,
    pollination_support REAL,
    market_visibility REAL
);

CREATE TABLE governance_regimes (
    regime TEXT PRIMARY KEY,
    secure_tenure REAL,
    monitoring REAL,
    participation REAL,
    enforcement REAL,
    adaptive_rules REAL,
    equity REAL,
    regeneration_alignment REAL
);

CREATE TABLE justice_burdens (
    "group" TEXT PRIMARY KEY,
    exposure REAL,
    income_buffer REAL,
    public_infrastructure REAL,
    adaptive_capacity REAL,
    political_voice REAL,
    benefit_capture REAL
);

CREATE TABLE resilience_dependency (
    system TEXT PRIMARY KEY,
    diversity REAL,
    regeneration REAL,
    redundancy REAL,
    governance REAL,
    strategic_reserve REAL,
    import_dependence REAL,
    shock_exposure REAL
);

CREATE TABLE substitution_efficiency (
    scenario TEXT PRIMARY KEY,
    efficiency_gain REAL,
    rebound_effect REAL,
    substitution_feasibility REAL,
    ecological_irreplaceability REAL,
    absolute_reduction REAL,
    innovation_quality REAL
);
