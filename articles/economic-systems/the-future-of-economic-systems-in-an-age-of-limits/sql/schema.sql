DROP TABLE IF EXISTS future_viability;
DROP TABLE IF EXISTS throughput_pressure;
DROP TABLE IF EXISTS transition_capacity;
DROP TABLE IF EXISTS wellbeing_measurement;
DROP TABLE IF EXISTS finance_direction;
DROP TABLE IF EXISTS circular_repair_systems;
DROP TABLE IF EXISTS technology_governance;
DROP TABLE IF EXISTS global_asymmetry;
DROP TABLE IF EXISTS democratic_legitimacy;

CREATE TABLE future_viability (
    scenario TEXT PRIMARY KEY,
    ecological_pressure REAL,
    institutional_capacity REAL,
    social_inclusion REAL,
    resilience REAL,
    public_trust REAL,
    adaptive_learning REAL
);

CREATE TABLE throughput_pressure (
    scenario TEXT PRIMARY KEY,
    population REAL,
    affluence REAL,
    material_intensity REAL,
    wellbeing REAL,
    inclusion REAL
);

CREATE TABLE transition_capacity (
    scenario TEXT PRIMARY KEY,
    public_investment REAL,
    policy_credibility REAL,
    technology REAL,
    social_trust REAL,
    implementation_capacity REAL,
    coordination REAL
);

CREATE TABLE wellbeing_measurement (
    scenario TEXT PRIMARY KEY,
    health REAL,
    security REAL,
    inclusion REAL,
    ecological_quality REAL,
    public_goods REAL,
    care REAL,
    time_balance REAL
);

CREATE TABLE finance_direction (
    portfolio TEXT PRIMARY KEY,
    fossil_exposure REAL,
    resilience_investment REAL,
    restoration REAL,
    public_goods_alignment REAL,
    short_termism REAL,
    adaptation_finance REAL
);

CREATE TABLE circular_repair_systems (
    system TEXT PRIMARY KEY,
    repairability REAL,
    reuse REAL,
    remanufacturing REAL,
    material_recovery REAL,
    maintenance_culture REAL,
    regeneration REAL
);

CREATE TABLE technology_governance (
    scenario TEXT PRIMARY KEY,
    productivity REAL,
    distribution REAL,
    public_purpose REAL,
    energy_demand_control REAL,
    labor_transition_support REAL,
    capability_expansion REAL
);

CREATE TABLE global_asymmetry (
    country_group TEXT PRIMARY KEY,
    material_footprint REAL,
    historic_responsibility REAL,
    development_need REAL,
    adaptive_capacity REAL,
    finance_obligation REAL,
    basic_needs_gap REAL
);

CREATE TABLE democratic_legitimacy (
    scenario TEXT PRIMARY KEY,
    fairness REAL,
    affordability REAL,
    voice REAL,
    trust REAL,
    visible_benefit REAL,
    policy_stability REAL
);
