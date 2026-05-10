DROP TABLE IF EXISTS regime_scenarios;
DROP TABLE IF EXISTS financialization_scenarios;
DROP TABLE IF EXISTS labor_skill_systems;
DROP TABLE IF EXISTS corporate_governance;
DROP TABLE IF EXISTS housing_household_vulnerability;
DROP TABLE IF EXISTS globalization_hybrids;
DROP TABLE IF EXISTS crisis_sustainability;

CREATE TABLE regime_scenarios (
    regime TEXT PRIMARY KEY,
    revenue REAL,
    cost REAL,
    wages REAL,
    output REAL,
    shareholder_claims REAL,
    labor_coordination REAL,
    welfare_buffer REAL,
    finance_patience REAL,
    state_coordination REAL,
    innovation_radical REAL,
    innovation_incremental REAL
);

CREATE TABLE financialization_scenarios (
    scenario TEXT PRIMARY KEY,
    asset_price_intensity REAL,
    household_debt REAL,
    corporate_leverage REAL,
    shareholder_payout_pressure REAL,
    buyback_intensity REAL,
    productive_investment REAL,
    speculative_pressure REAL
);

CREATE TABLE labor_skill_systems (
    system TEXT PRIMARY KEY,
    employment_protection REAL,
    collective_bargaining REAL,
    union_density REAL,
    general_skills REAL,
    vocational_training REAL,
    firm_specific_skills REAL,
    wage_compression REAL
);

CREATE TABLE corporate_governance (
    governance TEXT PRIMARY KEY,
    short_term_pressure REAL,
    stakeholder_voice REAL,
    worker_representation REAL,
    patient_capital REAL,
    reinvestment_orientation REAL,
    supplier_coordination REAL,
    community_accountability REAL
);

CREATE TABLE housing_household_vulnerability (
    housing_regime TEXT PRIMARY KEY,
    rent_burden REAL,
    mortgage_debt REAL,
    asset_price_volatility REAL,
    tenant_protection REAL,
    public_housing_capacity REAL,
    household_resilience REAL,
    wealth_concentration_pressure REAL
);

CREATE TABLE globalization_hybrids (
    scenario TEXT PRIMARY KEY,
    value_chain_dependence REAL,
    domestic_supplier_depth REAL,
    foreign_currency_exposure REAL,
    technology_sovereignty REAL,
    labor_standards REAL,
    industrial_policy_capacity REAL,
    external_vulnerability REAL
);

CREATE TABLE crisis_sustainability (
    scenario TEXT PRIMARY KEY,
    automatic_stabilizers REAL,
    public_investment_capacity REAL,
    household_buffer REAL,
    financial_regulation REAL,
    industrial_adaptation REAL,
    ecological_constraint REAL,
    democratic_legitimacy REAL
);
