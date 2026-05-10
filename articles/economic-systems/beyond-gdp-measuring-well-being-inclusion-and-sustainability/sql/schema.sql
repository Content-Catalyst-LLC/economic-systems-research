DROP TABLE IF EXISTS gdp_dashboard_scenarios;
DROP TABLE IF EXISTS inclusion_scenarios;
DROP TABLE IF EXISTS sustainability_stocks;
DROP TABLE IF EXISTS adjusted_progress;
DROP TABLE IF EXISTS capability_conversion;
DROP TABLE IF EXISTS care_time_use;
DROP TABLE IF EXISTS subjective_wellbeing;
DROP TABLE IF EXISTS indicator_governance;

CREATE TABLE gdp_dashboard_scenarios (
    scenario TEXT PRIMARY KEY,
    consumption REAL,
    investment REAL,
    government REAL,
    net_exports REAL,
    health REAL,
    education REAL,
    income_security REAL,
    housing REAL,
    safety REAL,
    social_connection REAL,
    environment REAL,
    time_balance REAL
);

CREATE TABLE inclusion_scenarios (
    "group" TEXT PRIMARY KEY,
    distribution REAL,
    mobility REAL,
    access REAL,
    voice REAL,
    regional_equity REAL,
    service_reach REAL
);

CREATE TABLE sustainability_stocks (
    scenario TEXT PRIMARY KEY,
    natural_capital REAL,
    human_capital REAL,
    institutional_trust REAL,
    produced_capital REAL,
    maintenance_gap REAL,
    ecological_pressure REAL
);

CREATE TABLE adjusted_progress (
    scenario TEXT PRIMARY KEY,
    current_benefits REAL,
    social_costs REAL,
    ecological_costs REAL,
    defensive_expenditure REAL,
    unpaid_care_value REAL,
    public_goods_value REAL
);

CREATE TABLE capability_conversion (
    household_type TEXT PRIMARY KEY,
    resources REAL,
    public_goods REAL,
    health_conversion REAL,
    education_conversion REAL,
    transport_access REAL,
    care_support REAL,
    discrimination_barrier REAL
);

CREATE TABLE care_time_use (
    "group" TEXT PRIMARY KEY,
    paid_work_hours REAL,
    unpaid_care_hours REAL,
    leisure_hours REAL,
    time_stress REAL,
    formal_recognition REAL,
    support_services REAL
);

CREATE TABLE subjective_wellbeing (
    community TEXT PRIMARY KEY,
    income_index REAL,
    life_satisfaction REAL,
    stress REAL,
    meaning REAL,
    social_trust REAL,
    loneliness REAL
);

CREATE TABLE indicator_governance (
    system TEXT PRIMARY KEY,
    clarity REAL,
    multidimensionality REAL,
    public_legibility REAL,
    gaming_risk REAL,
    policy_linkage REAL,
    local_relevance REAL
);
