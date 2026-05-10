DROP TABLE IF EXISTS income_distribution;
DROP TABLE IF EXISTS wealth_distribution;
DROP TABLE IF EXISTS mobility_scenarios;
DROP TABLE IF EXISTS labor_market_scenarios;
DROP TABLE IF EXISTS housing_place_scenarios;
DROP TABLE IF EXISTS public_services_scenarios;

CREATE TABLE income_distribution (
    group_name TEXT PRIMARY KEY,
    population_share REAL,
    market_income REAL,
    taxes REAL,
    transfers REAL,
    public_service_value REAL,
    housing_cost REAL,
    debt_service REAL
);

CREATE TABLE wealth_distribution (
    group_name TEXT PRIMARY KEY,
    population_share REAL,
    wealth REAL,
    debt REAL,
    inheritance_receipts REAL,
    asset_return REAL,
    housing_ownership REAL
);

CREATE TABLE mobility_scenarios (
    scenario TEXT PRIMARY KEY,
    parent_outcome REAL,
    persistence_b REAL,
    baseline_a REAL,
    education_access REAL,
    health_access REAL,
    place_advantage REAL,
    network_access REAL,
    family_wealth_buffer REAL
);

CREATE TABLE labor_market_scenarios (
    sector TEXT PRIMARY KEY,
    median_wage REAL,
    top_wage REAL,
    bottom_wage REAL,
    bargaining_power REAL,
    union_strength REAL,
    employment_security REAL,
    schedule_stability REAL,
    benefit_access REAL
);

CREATE TABLE housing_place_scenarios (
    place TEXT PRIMARY KEY,
    median_income REAL,
    housing_cost REAL,
    school_quality REAL,
    transit_access REAL,
    environmental_quality REAL,
    job_access REAL,
    homeownership_rate REAL
);

CREATE TABLE public_services_scenarios (
    scenario TEXT PRIMARY KEY,
    healthcare_access REAL,
    education_quality REAL,
    childcare_support REAL,
    transit_quality REAL,
    income_support REAL,
    unemployment_insurance REAL,
    pension_security REAL
);
