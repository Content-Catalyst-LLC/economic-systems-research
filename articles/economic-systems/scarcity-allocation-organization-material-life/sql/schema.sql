DROP TABLE IF EXISTS allocation_priorities;
DROP TABLE IF EXISTS allocation_scenarios;
DROP TABLE IF EXISTS access_households;
DROP TABLE IF EXISTS reproduction_constraints;

CREATE TABLE allocation_priorities (
    priority TEXT PRIMARY KEY,
    material_role TEXT,
    essentiality REAL,
    resilience_value REAL
);

CREATE TABLE allocation_scenarios (
    scenario TEXT,
    priority TEXT,
    share REAL
);

CREATE TABLE access_households (
    household_group TEXT PRIMARY KEY,
    need_index REAL,
    income_command REAL,
    price_index REAL,
    institutional_access REAL,
    population_weight REAL
);

CREATE TABLE reproduction_constraints (
    scenario TEXT PRIMARY KEY,
    periods INTEGER,
    initial_produced_capacity REAL,
    initial_ecological_capacity REAL,
    consumption REAL,
    investment REAL,
    maintenance REAL,
    ecological_restoration REAL,
    depreciation_rate REAL,
    resource_use REAL,
    regenerative_capacity REAL
);
