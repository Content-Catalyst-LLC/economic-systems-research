DROP TABLE IF EXISTS externality_scenarios;
DROP TABLE IF EXISTS public_good_scenarios;
DROP TABLE IF EXISTS contribution_scenarios;
DROP TABLE IF EXISTS collective_finance_scenarios;
DROP TABLE IF EXISTS burden_distribution_groups;

CREATE TABLE externality_scenarios (
    scenario TEXT PRIMARY KEY,
    mpc_intercept REAL,
    mpc_slope REAL,
    mec_intercept REAL,
    mec_slope REAL,
    mpb_intercept REAL,
    mpb_slope REAL,
    meb_intercept REAL,
    meb_slope REAL,
    critical_threshold REAL
);

CREATE TABLE public_good_scenarios (
    public_good TEXT PRIMARY KEY,
    private_benefit REAL,
    external_benefit REAL,
    private_cost REAL,
    social_need REAL,
    voluntary_provision REAL
);

CREATE TABLE contribution_scenarios (
    scenario TEXT,
    contributor_group TEXT,
    contribution REAL,
    benefit_share REAL
);

CREATE TABLE collective_finance_scenarios (
    scenario TEXT PRIMARY KEY,
    tax_revenue REAL,
    borrowing_capacity REAL,
    pooled_funds REAL,
    maintenance_need REAL,
    preparedness_need REAL
);

CREATE TABLE burden_distribution_groups (
    group_name TEXT PRIMARY KEY,
    income_index REAL,
    exposure_index REAL,
    political_voice_index REAL,
    population_weight REAL
);
