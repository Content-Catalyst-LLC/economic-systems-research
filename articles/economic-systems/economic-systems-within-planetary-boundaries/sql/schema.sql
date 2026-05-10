DROP TABLE IF EXISTS boundary_pressure;
DROP TABLE IF EXISTS resource_use_identity;
DROP TABLE IF EXISTS sector_pressure;
DROP TABLE IF EXISTS coupled_systems;
DROP TABLE IF EXISTS ecological_space_justice;
DROP TABLE IF EXISTS transition_capacity;
DROP TABLE IF EXISTS finance_direction;
DROP TABLE IF EXISTS boundary_accounting;

CREATE TABLE boundary_pressure (
    boundary TEXT PRIMARY KEY,
    economic_pressure REAL,
    earth_system_capacity REAL,
    irreversibility REAL,
    system_connectivity REAL,
    policy_response REAL
);

CREATE TABLE resource_use_identity (
    scenario TEXT PRIMARY KEY,
    population REAL,
    affluence REAL,
    resource_intensity REAL,
    wellbeing_index REAL,
    distribution_quality REAL
);

CREATE TABLE sector_pressure (
    sector TEXT PRIMARY KEY,
    climate REAL,
    biosphere REAL,
    land REAL,
    freshwater REAL,
    nutrients REAL,
    novel_entities REAL,
    social_necessity REAL,
    transition_readiness REAL
);

CREATE TABLE coupled_systems (
    system TEXT PRIMARY KEY,
    energy_pressure REAL,
    food_pressure REAL,
    land_pressure REAL,
    water_pressure REAL,
    governance_integration REAL,
    adaptation_capacity REAL
);

CREATE TABLE ecological_space_justice (
    "group" TEXT PRIMARY KEY,
    resource_claim REAL,
    historic_pressure REAL,
    development_need REAL,
    adaptive_capacity REAL,
    harm_exposure REAL,
    voice REAL
);

CREATE TABLE transition_capacity (
    scenario TEXT PRIMARY KEY,
    state_capacity REAL,
    public_investment REAL,
    social_legitimacy REAL,
    technological_capability REAL,
    coordination REAL,
    adaptive_governance REAL
);

CREATE TABLE finance_direction (
    portfolio TEXT PRIMARY KEY,
    fossil_exposure REAL,
    restoration_investment REAL,
    resilience_investment REAL,
    circular_materials REAL,
    public_goods_alignment REAL,
    short_term_return_pressure REAL
);

CREATE TABLE boundary_accounting (
    scenario TEXT PRIMARY KEY,
    gdp_growth REAL,
    wellbeing REAL,
    material_throughput REAL,
    ecological_pressure REAL,
    natural_capital REAL,
    inclusion REAL
);
