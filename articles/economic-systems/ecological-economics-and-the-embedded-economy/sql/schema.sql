DROP TABLE IF EXISTS throughput_scenarios;
DROP TABLE IF EXISTS sector_footprints;
DROP TABLE IF EXISTS ecological_burdens;
DROP TABLE IF EXISTS embeddedness_scenarios;
DROP TABLE IF EXISTS resilience_commons;
DROP TABLE IF EXISTS postgrowth_scenarios;
DROP TABLE IF EXISTS strong_sustainability;

CREATE TABLE throughput_scenarios (
    scenario TEXT PRIMARY KEY,
    energy_input REAL,
    material_input REAL,
    recovered_throughput REAL,
    economic_scale REAL,
    ecological_capacity REAL,
    wellbeing_index REAL
);

CREATE TABLE sector_footprints (
    sector TEXT PRIMARY KEY,
    domestic_extraction REAL,
    imports REAL,
    exports REAL,
    energy_intensity REAL,
    water_pressure REAL,
    land_pressure REAL,
    waste_intensity REAL,
    social_necessity REAL
);

CREATE TABLE ecological_burdens (
    "group" TEXT PRIMARY KEY,
    exposure REAL,
    income_buffer REAL,
    infrastructure REAL,
    adaptive_capacity REAL,
    historical_responsibility REAL,
    political_voice REAL
);

CREATE TABLE embeddedness_scenarios (
    scenario TEXT PRIMARY KEY,
    ecology_integrity REAL,
    care_capacity REAL,
    public_institutions REAL,
    infrastructure_maintenance REAL,
    cultural_reciprocity REAL,
    market_dependence REAL,
    community_resilience REAL
);

CREATE TABLE resilience_commons (
    system TEXT PRIMARY KEY,
    diversity REAL,
    redundancy REAL,
    regeneration REAL,
    governance REAL,
    maintenance REAL,
    learning REAL,
    monitoring REAL,
    participation REAL
);

CREATE TABLE postgrowth_scenarios (
    scenario TEXT PRIMARY KEY,
    gdp_growth REAL,
    throughput_growth REAL,
    efficiency_gain REAL,
    rebound_effect REAL,
    wellbeing_change REAL,
    inequality_pressure REAL,
    public_services REAL
);

CREATE TABLE strong_sustainability (
    system TEXT PRIMARY KEY,
    substitutability REAL,
    threshold_risk REAL,
    irreversibility REAL,
    regeneration_rate REAL,
    life_support_importance REAL
);
