DROP TABLE IF EXISTS household_poverty_scenarios;
DROP TABLE IF EXISTS multidimensional_deprivation;
DROP TABLE IF EXISTS capability_scenarios;
DROP TABLE IF EXISTS inclusion_scenarios;
DROP TABLE IF EXISTS work_informality_scenarios;
DROP TABLE IF EXISTS housing_infrastructure_scenarios;
DROP TABLE IF EXISTS finance_care_digital_scenarios;
DROP TABLE IF EXISTS public_service_vulnerability_scenarios;

CREATE TABLE household_poverty_scenarios (
    household TEXT PRIMARY KEY,
    income REAL,
    poverty_line REAL,
    savings REAL,
    debt_service REAL,
    housing_cost REAL,
    health_cost REAL,
    shock_exposure REAL
);

CREATE TABLE multidimensional_deprivation (
    community TEXT PRIMARY KEY,
    health_deprivation REAL,
    education_deprivation REAL,
    housing_deprivation REAL,
    sanitation_deprivation REAL,
    food_deprivation REAL,
    transport_deprivation REAL,
    digital_deprivation REAL,
    safety_deprivation REAL,
    institutional_exclusion REAL
);

CREATE TABLE capability_scenarios (
    scenario TEXT PRIMARY KEY,
    income_score REAL,
    health_score REAL,
    education_score REAL,
    mobility_score REAL,
    safety_score REAL,
    time_score REAL,
    institutional_access REAL
);

CREATE TABLE inclusion_scenarios (
    scenario TEXT PRIMARY KEY,
    work_access REAL,
    finance_access REAL,
    service_access REAL,
    infrastructure_access REAL,
    digital_access REAL,
    legal_recognition REAL,
    participation_security REAL
);

CREATE TABLE work_informality_scenarios (
    sector TEXT PRIMARY KEY,
    wage_adequacy REAL,
    hours_stability REAL,
    legal_protection REAL,
    benefit_access REAL,
    skill_progression REAL,
    workplace_safety REAL,
    recognition REAL
);

CREATE TABLE housing_infrastructure_scenarios (
    community TEXT PRIMARY KEY,
    housing_security REAL,
    water_sanitation REAL,
    electricity_reliability REAL,
    transport_access REAL,
    digital_connectivity REAL,
    environmental_safety REAL,
    rent_burden REAL
);

CREATE TABLE finance_care_digital_scenarios (
    scenario TEXT PRIMARY KEY,
    affordable_credit REAL,
    savings_access REAL,
    fee_burden REAL,
    debt_stress REAL,
    digital_literacy REAL,
    device_access REAL,
    platform_accessibility REAL
);

CREATE TABLE public_service_vulnerability_scenarios (
    scenario TEXT PRIMARY KEY,
    healthcare_access REAL,
    education_quality REAL,
    childcare_support REAL,
    food_support REAL,
    unemployment_protection REAL,
    disability_support REAL,
    low_savings REAL,
    high_debt REAL,
    insecure_work REAL,
    shock_exposure REAL
);
