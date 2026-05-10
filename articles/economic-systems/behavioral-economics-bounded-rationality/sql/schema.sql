DROP TABLE IF EXISTS choice_options;
DROP TABLE IF EXISTS present_bias_scenarios;
DROP TABLE IF EXISTS framing_default_scenarios;
DROP TABLE IF EXISTS risk_probability_scenarios;
DROP TABLE IF EXISTS social_norm_scenarios;
DROP TABLE IF EXISTS admin_burden_scenarios;

CREATE TABLE choice_options (
    option_id INTEGER PRIMARY KEY,
    option_label TEXT,
    utility REAL,
    complexity REAL,
    salience REAL,
    search_order INTEGER,
    satisficing_threshold REAL
);

CREATE TABLE present_bias_scenarios (
    scenario TEXT,
    beta REAL,
    delta REAL,
    period INTEGER,
    future_value REAL
);

CREATE TABLE framing_default_scenarios (
    scenario TEXT PRIMARY KEY,
    frame TEXT,
    default_status INTEGER,
    benefit_value REAL,
    admin_burden REAL,
    trust_index REAL,
    salience REAL
);

CREATE TABLE risk_probability_scenarios (
    risk_case TEXT PRIMARY KEY,
    probability REAL,
    outcome_value REAL,
    salience REAL,
    ambiguity REAL
);

CREATE TABLE social_norm_scenarios (
    scenario TEXT PRIMARY KEY,
    peer_cooperation_rate REAL,
    institutional_trust REAL,
    fairness_perception REAL,
    private_cost REAL,
    collective_benefit REAL
);

CREATE TABLE admin_burden_scenarios (
    program TEXT PRIMARY KEY,
    eligible_population REAL,
    benefit_value REAL,
    admin_burden REAL,
    default_support INTEGER,
    trust_index REAL
);
