DROP TABLE IF EXISTS growth_path_scenarios;
DROP TABLE IF EXISTS sector_transformation_scenarios;
DROP TABLE IF EXISTS development_capability_scenarios;
DROP TABLE IF EXISTS urban_infrastructure_scenarios;
DROP TABLE IF EXISTS trade_export_diversification_scenarios;
DROP TABLE IF EXISTS inequality_inclusion_scenarios;
DROP TABLE IF EXISTS energy_ecology_scenarios;
DROP TABLE IF EXISTS debt_fragility_scenarios;

CREATE TABLE growth_path_scenarios (
    scenario TEXT,
    period INTEGER,
    output REAL,
    labor REAL
);

CREATE TABLE sector_transformation_scenarios (
    scenario TEXT,
    sector TEXT,
    sector_output REAL,
    sector_labor REAL
);

CREATE TABLE development_capability_scenarios (
    scenario TEXT PRIMARY KEY,
    income_index REAL,
    health_index REAL,
    education_index REAL,
    infrastructure_index REAL,
    security_index REAL
);

CREATE TABLE urban_infrastructure_scenarios (
    scenario TEXT PRIMARY KEY,
    urbanization_rate REAL,
    infrastructure_depth REAL,
    housing_access REAL,
    transit_access REAL,
    spatial_inclusion REAL
);

CREATE TABLE trade_export_diversification_scenarios (
    scenario TEXT PRIMARY KEY,
    export_concentration REAL,
    manufacturing_export_share REAL,
    technology_depth REAL,
    terms_of_trade_volatility REAL,
    foreign_exchange_resilience REAL
);

CREATE TABLE inequality_inclusion_scenarios (
    scenario TEXT PRIMARY KEY,
    gini_index REAL,
    informal_labor_share REAL,
    education_access REAL,
    health_access REAL,
    regional_inclusion REAL
);

CREATE TABLE energy_ecology_scenarios (
    scenario TEXT PRIMARY KEY,
    output REAL,
    energy_use REAL,
    emissions REAL,
    renewable_share REAL,
    resource_stress REAL
);

CREATE TABLE debt_fragility_scenarios (
    scenario TEXT PRIMARY KEY,
    external_debt_ratio REAL,
    fx_debt_share REAL,
    short_term_debt_share REAL,
    export_concentration REAL,
    reserve_buffer REAL,
    productivity_momentum REAL
);
