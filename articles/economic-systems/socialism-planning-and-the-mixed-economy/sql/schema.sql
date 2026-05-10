DROP TABLE IF EXISTS mixed_economy_scenarios;
DROP TABLE IF EXISTS planning_capacity;
DROP TABLE IF EXISTS decommodification_scenarios;
DROP TABLE IF EXISTS sector_coordination;
DROP TABLE IF EXISTS public_utilities;
DROP TABLE IF EXISTS industrial_policy;
DROP TABLE IF EXISTS crisis_transition_globalization;

CREATE TABLE mixed_economy_scenarios (
    scenario TEXT PRIMARY KEY,
    market_allocation REAL,
    public_planning REAL,
    public_provision REAL,
    regulation_rights REAL,
    public_ownership_share REAL,
    social_rights_strength REAL,
    private_profit_weight REAL,
    social_need_weight REAL
);

CREATE TABLE planning_capacity (
    scenario TEXT PRIMARY KEY,
    state_capacity REAL,
    data_quality REAL,
    institutional_reach REAL,
    feedback_quality REAL,
    democratic_accountability REAL,
    coordination_authority REAL,
    implementation_speed REAL
);

CREATE TABLE decommodification_scenarios (
    scenario TEXT PRIMARY KEY,
    healthcare_access REAL,
    education_access REAL,
    housing_security REAL,
    childcare_support REAL,
    public_transport REAL,
    social_insurance REAL,
    guaranteed_access REAL
);

CREATE TABLE sector_coordination (
    sector TEXT PRIMARY KEY,
    market_fit REAL,
    planning_fit REAL,
    public_ownership_fit REAL,
    regulation_need REAL,
    social_rights_need REAL,
    network_interdependence REAL,
    public_good_character REAL
);

CREATE TABLE public_utilities (
    utility TEXT PRIMARY KEY,
    universal_access REAL,
    affordability REAL,
    maintenance_investment REAL,
    democratic_accountability REAL,
    service_reliability REAL,
    profit_extraction_pressure REAL,
    regional_equity REAL
);

CREATE TABLE industrial_policy (
    scenario TEXT PRIMARY KEY,
    public_investment REAL,
    sector_targeting REAL,
    learning_policy REAL,
    supplier_development REAL,
    public_procurement REAL,
    performance_discipline REAL,
    green_transition_alignment REAL
);

CREATE TABLE crisis_transition_globalization (
    scenario TEXT PRIMARY KEY,
    public_planning REAL,
    infrastructure_depth REAL,
    fiscal_capacity REAL,
    administrative_speed REAL,
    social_protection REAL,
    ecological_targets REAL,
    democratic_legitimacy REAL,
    external_finance_constraint REAL
);
