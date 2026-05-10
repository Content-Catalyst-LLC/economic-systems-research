DROP TABLE IF EXISTS policy_rate_scenarios;
DROP TABLE IF EXISTS debt_service_scenarios;
DROP TABLE IF EXISTS financial_conditions_scenarios;
DROP TABLE IF EXISTS asset_valuation_scenarios;
DROP TABLE IF EXISTS bank_liquidity_scenarios;
DROP TABLE IF EXISTS open_economy_scenarios;
DROP TABLE IF EXISTS public_debt_interaction_scenarios;
DROP TABLE IF EXISTS sustainable_investment_scenarios;

CREATE TABLE policy_rate_scenarios (
    scenario TEXT PRIMARY KEY,
    nominal_rate REAL,
    expected_inflation REAL,
    neutral_rate REAL,
    inflation_gap REAL,
    output_gap REAL,
    a_inflation REAL,
    b_output REAL
);

CREATE TABLE debt_service_scenarios (
    borrower_group TEXT PRIMARY KEY,
    income REAL,
    debt_service REAL,
    repricing_share REAL,
    rate_shock REAL,
    debt_stock REAL
);

CREATE TABLE financial_conditions_scenarios (
    scenario TEXT PRIMARY KEY,
    policy_rate REAL,
    credit_spread REAL,
    equity_price_change REAL,
    exchange_rate_pressure REAL,
    lending_tightness REAL,
    market_liquidity_stress REAL
);

CREATE TABLE asset_valuation_scenarios (
    asset_class TEXT PRIMARY KEY,
    cash_flow REAL,
    discount_rate REAL,
    duration_years INTEGER,
    rate_shock REAL
);

CREATE TABLE bank_liquidity_scenarios (
    institution TEXT PRIMARY KEY,
    liquid_assets REAL,
    short_term_outflows REAL,
    deposit_outflow_shock REAL,
    collateral_quality REAL,
    central_bank_access REAL
);

CREATE TABLE open_economy_scenarios (
    scenario TEXT PRIMARY KEY,
    domestic_rate REAL,
    world_rate REAL,
    risk_premium REAL,
    capital_flow_pressure REAL,
    fx_debt_exposure REAL,
    import_price_exposure REAL
);

CREATE TABLE public_debt_interaction_scenarios (
    scenario TEXT PRIMARY KEY,
    public_debt REAL,
    average_interest_rate REAL,
    share_rolling_over REAL,
    rate_shock REAL,
    output REAL,
    public_investment_need REAL
);

CREATE TABLE sustainable_investment_scenarios (
    investment_area TEXT PRIMARY KEY,
    expected_social_return REAL,
    financing_cost REAL,
    rate_shock REAL,
    investment_scale REAL,
    strategic_priority REAL
);
