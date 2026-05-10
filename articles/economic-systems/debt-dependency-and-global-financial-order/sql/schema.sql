DROP TABLE IF EXISTS debt_position_scenarios;
DROP TABLE IF EXISTS currency_hierarchy_scenarios;
DROP TABLE IF EXISTS external_account_scenarios;
DROP TABLE IF EXISTS credit_discipline_scenarios;
DROP TABLE IF EXISTS conditionality_scenarios;
DROP TABLE IF EXISTS austerity_adjustment_scenarios;
DROP TABLE IF EXISTS commodity_debt_scenarios;
DROP TABLE IF EXISTS capital_flow_scenarios;
DROP TABLE IF EXISTS restructuring_scenarios;
DROP TABLE IF EXISTS sustainable_finance_scenarios;

CREATE TABLE debt_position_scenarios (
    scenario TEXT PRIMARY KEY,
    debt_stock REAL,
    output REAL,
    external_debt_service REAL,
    export_earnings REAL,
    foreign_currency_debt REAL,
    exchange_rate REAL,
    effective_interest_rate REAL,
    growth_rate REAL,
    primary_deficit REAL,
    reserves REAL,
    short_term_external_obligations REAL
);

CREATE TABLE currency_hierarchy_scenarios (
    scenario TEXT PRIMARY KEY,
    own_currency_borrowing_share REAL,
    foreign_currency_debt_share REAL,
    market_depth REAL,
    safe_asset_status REAL,
    policy_space REAL,
    external_discipline REAL
);

CREATE TABLE external_account_scenarios (
    scenario TEXT PRIMARY KEY,
    export_concentration REAL,
    import_dependence REAL,
    external_finance_reliance REAL,
    capital_flow_volatility REAL,
    reserve_buffer REAL,
    domestic_capability REAL
);

CREATE TABLE credit_discipline_scenarios (
    scenario TEXT PRIMARY KEY,
    spread REAL,
    rating_pressure REAL,
    rollover_need REAL,
    foreign_investor_share REAL,
    legal_constraint REAL,
    market_access_score REAL
);

CREATE TABLE conditionality_scenarios (
    program TEXT PRIMARY KEY,
    fiscal_compression REAL,
    social_spending_protection REAL,
    public_investment_protection REAL,
    privatization_pressure REAL,
    policy_space REAL,
    developmental_alignment REAL
);

CREATE TABLE austerity_adjustment_scenarios (
    scenario TEXT PRIMARY KEY,
    austerity_intensity REAL,
    health_spending_cut REAL,
    education_spending_cut REAL,
    infrastructure_cut REAL,
    wage_compression REAL,
    growth_damage REAL,
    poverty_pressure REAL
);

CREATE TABLE commodity_debt_scenarios (
    scenario TEXT PRIMARY KEY,
    commodity_export_share REAL,
    commodity_price_index REAL,
    export_earnings REAL,
    external_debt_service REAL,
    stabilization_fund REAL,
    diversification_effort REAL
);

CREATE TABLE capital_flow_scenarios (
    scenario TEXT PRIMARY KEY,
    portfolio_share REAL,
    fdi_share REAL,
    short_term_debt_share REAL,
    capital_flow_reversal REAL,
    reserve_loss REAL,
    currency_depreciation REAL
);

CREATE TABLE restructuring_scenarios (
    scenario TEXT PRIMARY KEY,
    initial_debt REAL,
    restructuring_haircut REAL,
    maturity_extension REAL,
    interest_relief REAL,
    social_spending_floor REAL,
    growth_recovery REAL,
    creditor_acceptance REAL
);

CREATE TABLE sustainable_finance_scenarios (
    scenario TEXT PRIMARY KEY,
    productive_investment REAL,
    domestic_capability REAL,
    export_resilience REAL,
    social_protection REAL,
    ecological_resilience REAL,
    debt_manageability REAL
);
