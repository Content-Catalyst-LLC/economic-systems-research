DROP TABLE IF EXISTS household_tax_transfer;
DROP TABLE IF EXISTS social_spending_scenarios;
DROP TABLE IF EXISTS program_coverage;
DROP TABLE IF EXISTS welfare_regime_scenarios;
DROP TABLE IF EXISTS life_course_risk;
DROP TABLE IF EXISTS care_family_policy;
DROP TABLE IF EXISTS fiscal_capacity;
DROP TABLE IF EXISTS digital_administration;
DROP TABLE IF EXISTS adaptive_protection;

CREATE TABLE household_tax_transfer (
    household TEXT PRIMARY KEY,
    market_income REAL,
    taxes REAL,
    transfers REAL,
    service_value REAL,
    housing_cost REAL,
    care_cost REAL
);

CREATE TABLE social_spending_scenarios (
    scenario TEXT PRIMARY KEY,
    social_spending REAL,
    output REAL,
    healthcare_spending REAL,
    pensions REAL,
    unemployment REAL,
    family_policy REAL,
    housing_support REAL,
    disability_support REAL,
    administration_quality REAL
);

CREATE TABLE program_coverage (
    program TEXT PRIMARY KEY,
    covered_population REAL,
    target_population REAL,
    benefit REAL,
    previous_earnings REAL,
    take_up_rate REAL,
    administrative_burden REAL,
    stigma_cost REAL
);

CREATE TABLE welfare_regime_scenarios (
    regime TEXT PRIMARY KEY,
    universalism REAL,
    targeting_precision REAL,
    benefit_adequacy REAL,
    service_quality REAL,
    labor_market_security REAL,
    dignity_score REAL,
    political_durability REAL
);

CREATE TABLE life_course_risk (
    risk TEXT PRIMARY KEY,
    baseline_vulnerability REAL,
    protected_vulnerability REAL,
    coverage REAL,
    adequacy REAL,
    duration_support REAL,
    service_integration REAL
);

CREATE TABLE care_family_policy (
    scenario TEXT PRIMARY KEY,
    childcare_support REAL,
    paid_leave REAL,
    eldercare_support REAL,
    disability_care_support REAL,
    care_worker_protection REAL,
    female_labor_participation_support REAL,
    child_development_support REAL
);

CREATE TABLE fiscal_capacity (
    scenario TEXT PRIMARY KEY,
    tax_revenue REAL,
    output REAL,
    administrative_capacity REAL,
    compliance_strength REAL,
    progressivity REAL,
    benefit_delivery_quality REAL,
    automatic_stabilizer_strength REAL
);

CREATE TABLE digital_administration (
    scenario TEXT PRIMARY KEY,
    digital_access REAL,
    identity_coverage REAL,
    application_simplicity REAL,
    appeal_access REAL,
    automation_error_risk REAL,
    data_protection REAL,
    human_support REAL
);

CREATE TABLE adaptive_protection (
    shock TEXT PRIMARY KEY,
    baseline_exposure REAL,
    scale_up_capacity REAL,
    payment_speed REAL,
    registry_quality REAL,
    local_delivery_capacity REAL,
    benefit_adequacy REAL,
    post_shock_vulnerability REAL
);
