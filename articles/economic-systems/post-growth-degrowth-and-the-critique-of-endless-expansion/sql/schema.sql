DROP TABLE IF EXISTS growth_dependence;
DROP TABLE IF EXISTS throughput_scenarios;
DROP TABLE IF EXISTS wellbeing_dashboard;
DROP TABLE IF EXISTS sufficiency;
DROP TABLE IF EXISTS work_time_care;
DROP TABLE IF EXISTS finance_growth_dependence;
DROP TABLE IF EXISTS decoupling_rebound;
DROP TABLE IF EXISTS degrowth_transition;
DROP TABLE IF EXISTS global_justice;

CREATE TABLE growth_dependence (
    scenario TEXT PRIMARY KEY,
    employment_dependency REAL,
    debt_service_dependency REAL,
    fiscal_dependency REAL,
    asset_dependency REAL,
    pension_dependency REAL,
    housing_market_dependency REAL,
    political_legitimacy_dependency REAL
);

CREATE TABLE throughput_scenarios (
    scenario TEXT PRIMARY KEY,
    population REAL,
    affluence REAL,
    intensity REAL,
    wellbeing_index REAL,
    distribution_quality REAL
);

CREATE TABLE wellbeing_dashboard (
    scenario TEXT PRIMARY KEY,
    health REAL,
    time_balance REAL,
    security REAL,
    equality REAL,
    public_goods REAL,
    ecological_quality REAL,
    care_support REAL,
    social_trust REAL
);

CREATE TABLE sufficiency (
    system TEXT PRIMARY KEY,
    needs_met REAL,
    throughput_required REAL,
    time_security REAL,
    public_access REAL,
    care_capacity REAL,
    dignity REAL
);

CREATE TABLE work_time_care (
    scenario TEXT PRIMARY KEY,
    paid_work_hours REAL,
    unpaid_care_hours REAL,
    leisure_hours REAL,
    labor_security REAL,
    care_support REAL,
    time_sovereignty REAL
);

CREATE TABLE finance_growth_dependence (
    system TEXT PRIMARY KEY,
    private_debt REAL,
    public_debt_pressure REAL,
    asset_valuation_pressure REAL,
    pension_return_dependency REAL,
    housing_speculation REAL,
    real_investment_alignment REAL
);

CREATE TABLE decoupling_rebound (
    scenario TEXT PRIMARY KEY,
    output_growth REAL,
    intensity_reduction REAL,
    additional_demand REAL,
    absolute_throughput_change REAL,
    wellbeing_gain REAL
);

CREATE TABLE degrowth_transition (
    scenario TEXT PRIMARY KEY,
    throughput_reduction REAL,
    redistribution REAL,
    public_services REAL,
    democratic_legitimacy REAL,
    macro_stabilization REAL,
    employment_security REAL
);

CREATE TABLE global_justice (
    country_group TEXT PRIMARY KEY,
    material_footprint REAL,
    historic_responsibility REAL,
    development_need REAL,
    adaptive_capacity REAL,
    basic_needs_gap REAL,
    transition_finance_obligation REAL
);
