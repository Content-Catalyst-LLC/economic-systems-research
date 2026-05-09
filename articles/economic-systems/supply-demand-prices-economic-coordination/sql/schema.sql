DROP TABLE IF EXISTS market_parameter_scenarios;
DROP TABLE IF EXISTS market_access_groups;
DROP TABLE IF EXISTS external_cost_scenarios;

CREATE TABLE market_parameter_scenarios (
    market TEXT,
    scenario TEXT PRIMARY KEY,
    a REAL,
    b REAL,
    c REAL,
    d REAL,
    external_cost REAL,
    markup_rate REAL,
    description TEXT
);

CREATE TABLE market_access_groups (
    group_name TEXT PRIMARY KEY,
    need_index REAL,
    income_command REAL,
    credit_access REAL,
    institutional_access REAL,
    price_burden REAL,
    population_weight REAL
);

CREATE TABLE external_cost_scenarios (
    sector TEXT PRIMARY KEY,
    private_price REAL,
    marginal_external_cost REAL,
    public_good_benefit REAL
);
