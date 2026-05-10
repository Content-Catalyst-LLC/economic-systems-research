DROP TABLE IF EXISTS sector_labor_scenarios;
DROP TABLE IF EXISTS wage_productivity_time_series;
DROP TABLE IF EXISTS household_reproduction_scenarios;
DROP TABLE IF EXISTS time_use_scenarios;
DROP TABLE IF EXISTS bargaining_institution_scenarios;
DROP TABLE IF EXISTS automation_shock_scenarios;

CREATE TABLE sector_labor_scenarios (
    sector TEXT PRIMARY KEY,
    output REAL,
    hours_worked REAL,
    total_wages REAL,
    employment_quality_index REAL,
    care_intensity REAL
);

CREATE TABLE wage_productivity_time_series (
    year INTEGER PRIMARY KEY,
    productivity_index REAL,
    wage_index REAL,
    compensation_with_strong_bargaining REAL,
    union_density_index REAL,
    labor_market_tightness REAL
);

CREATE TABLE household_reproduction_scenarios (
    household_type TEXT PRIMARY KEY,
    wage_income REAL,
    social_support REAL,
    household_cost REAL,
    care_reproduction_cost REAL,
    dependents INTEGER
);

CREATE TABLE time_use_scenarios (
    worker_group TEXT PRIMARY KEY,
    paid_work_time REAL,
    care_time REAL,
    household_time REAL,
    commute_time REAL
);

CREATE TABLE bargaining_institution_scenarios (
    scenario TEXT PRIMARY KEY,
    labor_productivity REAL,
    bargaining_power REAL,
    institutional_support REAL,
    outside_option REAL
);

CREATE TABLE automation_shock_scenarios (
    scenario TEXT PRIMARY KEY,
    automation_intensity REAL,
    productivity_gain REAL,
    employment_effect REAL,
    wage_share_effect REAL,
    quality_effect REAL
);
