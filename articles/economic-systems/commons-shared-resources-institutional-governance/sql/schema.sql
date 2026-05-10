DROP TABLE IF EXISTS resource_scenarios;
DROP TABLE IF EXISTS user_extraction_profiles;
DROP TABLE IF EXISTS governance_scenarios;
DROP TABLE IF EXISTS access_justice_scenarios;

CREATE TABLE resource_scenarios (
    resource TEXT PRIMARY KEY,
    initial_stock REAL,
    carrying_capacity REAL,
    regeneration_rate REAL,
    critical_stock_threshold REAL
);

CREATE TABLE user_extraction_profiles (
    user_group TEXT PRIMARY KEY,
    baseline_extraction REAL,
    governed_extraction REAL,
    access_rights_index REAL,
    compliance_tendency REAL,
    population_weight REAL
);

CREATE TABLE governance_scenarios (
    scenario TEXT PRIMARY KEY,
    monitoring_capacity REAL,
    rule_clarity REAL,
    legitimacy REAL,
    sanction_capacity REAL,
    capture_risk REAL,
    local_knowledge_use REAL,
    polycentric_coordination REAL,
    institutional_upkeep REAL,
    institutional_erosion REAL,
    extraction_multiplier REAL
);

CREATE TABLE access_justice_scenarios (
    regime TEXT PRIMARY KEY,
    preservation_score REAL,
    access_score REAL,
    justice_score REAL,
    maintenance_score REAL
);
