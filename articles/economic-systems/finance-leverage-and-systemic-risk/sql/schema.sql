DROP TABLE IF EXISTS institution_balance_sheets;
DROP TABLE IF EXISTS asset_shock_scenarios;
DROP TABLE IF EXISTS collateral_haircut_scenarios;
DROP TABLE IF EXISTS funding_gap_scenarios;
DROP TABLE IF EXISTS network_exposure_matrix;
DROP TABLE IF EXISTS household_leverage_scenarios;
DROP TABLE IF EXISTS macroprudential_buffer_scenarios;
DROP TABLE IF EXISTS sustainability_shock_scenarios;

CREATE TABLE institution_balance_sheets (
    institution TEXT PRIMARY KEY,
    assets REAL,
    debt REAL,
    liquid_assets REAL,
    short_term_liabilities REAL,
    common_exposure_share REAL
);

CREATE TABLE asset_shock_scenarios (
    shock_name TEXT PRIMARY KEY,
    asset_shock REAL
);

CREATE TABLE collateral_haircut_scenarios (
    scenario TEXT PRIMARY KEY,
    collateral_value REAL,
    haircut_before REAL,
    haircut_after REAL,
    outstanding_borrowing REAL
);

CREATE TABLE funding_gap_scenarios (
    institution TEXT PRIMARY KEY,
    short_term_liabilities REAL,
    liquid_assets REAL,
    rollover_rate REAL,
    emergency_liquidity_access REAL
);

CREATE TABLE network_exposure_matrix (
    from_institution TEXT,
    to_institution TEXT,
    exposure REAL
);

CREATE TABLE household_leverage_scenarios (
    household_group TEXT PRIMARY KEY,
    housing_value REAL,
    mortgage_debt REAL,
    liquid_savings REAL,
    income REAL,
    debt_service REAL
);

CREATE TABLE macroprudential_buffer_scenarios (
    scenario TEXT PRIMARY KEY,
    capital_buffer REAL,
    liquidity_buffer REAL,
    countercyclical_buffer REAL,
    loan_to_value_limit REAL,
    stress_test_strength REAL
);

CREATE TABLE sustainability_shock_scenarios (
    shock TEXT PRIMARY KEY,
    portfolio_exposure REAL,
    loss_given_shock REAL,
    liquidity_impact REAL,
    public_backstop_need REAL
);
