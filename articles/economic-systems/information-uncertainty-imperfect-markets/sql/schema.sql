DROP TABLE IF EXISTS market_quality_types;
DROP TABLE IF EXISTS credit_risk_types;
DROP TABLE IF EXISTS signaling_scenarios;
DROP TABLE IF EXISTS information_search_scenarios;
DROP TABLE IF EXISTS uncertainty_scenarios;
DROP TABLE IF EXISTS consumer_complexity_scenarios;

CREATE TABLE market_quality_types (
    type TEXT PRIMARY KEY,
    share REAL,
    value REAL,
    reservation_value REAL,
    quality_verifiability REAL
);

CREATE TABLE credit_risk_types (
    borrower_type TEXT PRIMARY KEY,
    share REAL,
    default_probability REAL,
    loss_given_default REAL,
    productive_return REAL,
    screening_cost REAL
);

CREATE TABLE signaling_scenarios (
    signal TEXT PRIMARY KEY,
    signal_strength REAL,
    signal_cost_high_type REAL,
    signal_cost_low_type REAL,
    verification_strength REAL
);

CREATE TABLE information_search_scenarios (
    information_level INTEGER PRIMARY KEY,
    benefit_information REAL,
    cost_information REAL,
    time_cost REAL,
    processing_cost REAL
);

CREATE TABLE uncertainty_scenarios (
    action TEXT PRIMARY KEY,
    good_case REAL,
    moderate_case REAL,
    bad_case REAL,
    transition_case REAL,
    systemic_crisis_case REAL
);

CREATE TABLE consumer_complexity_scenarios (
    market TEXT PRIMARY KEY,
    complexity_index REAL,
    hidden_fee_index REAL,
    switching_cost_index REAL,
    trust_index REAL,
    disclosure_quality REAL
);
