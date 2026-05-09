DROP TABLE IF EXISTS household_profiles;
DROP TABLE IF EXISTS inflation_scenarios;
DROP TABLE IF EXISTS public_goods_scenarios;
DROP TABLE IF EXISTS expense_categories;

CREATE TABLE household_profiles (
    household_group TEXT PRIMARY KEY,
    income REAL,
    transfers REAL,
    liquid_assets REAL,
    debt_service REAL,
    other_fixed_burdens REAL,
    rent REAL,
    food REAL,
    transport REAL,
    utilities REAL,
    health REAL,
    other REAL,
    paid_labor_hours REAL,
    care_hours REAL,
    commute_hours REAL,
    household_admin_hours REAL,
    population_weight REAL
);

CREATE TABLE inflation_scenarios (
    scenario TEXT PRIMARY KEY,
    rent_multiplier REAL,
    food_multiplier REAL,
    transport_multiplier REAL,
    utilities_multiplier REAL,
    health_multiplier REAL,
    other_multiplier REAL
);

CREATE TABLE public_goods_scenarios (
    scenario TEXT PRIMARY KEY,
    transport_private_cost_reduction REAL,
    health_private_cost_reduction REAL,
    childcare_private_cost_reduction REAL,
    time_savings_hours REAL,
    institutional_support_index REAL
);

CREATE TABLE expense_categories (
    category TEXT PRIMARY KEY,
    is_essential INTEGER,
    is_fixed INTEGER,
    welfare_domain TEXT
);
