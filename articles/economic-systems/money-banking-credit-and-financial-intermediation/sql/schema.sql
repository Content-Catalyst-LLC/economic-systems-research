DROP TABLE IF EXISTS money_aggregate_scenarios;
DROP TABLE IF EXISTS bank_balance_sheet_scenarios;
DROP TABLE IF EXISTS debt_service_scenarios;
DROP TABLE IF EXISTS liquidity_stress_scenarios;
DROP TABLE IF EXISTS credit_allocation_scenarios;
DROP TABLE IF EXISTS monetary_hierarchy_scenarios;
DROP TABLE IF EXISTS sustainable_finance_scenarios;

CREATE TABLE money_aggregate_scenarios (
    scenario TEXT PRIMARY KEY,
    currency REAL,
    deposits REAL,
    near_money_claims REAL,
    central_bank_reserves REAL
);

CREATE TABLE bank_balance_sheet_scenarios (
    bank TEXT PRIMARY KEY,
    assets REAL,
    equity REAL,
    loans REAL,
    bank_deposits REAL,
    liquid_assets REAL,
    wholesale_funding REAL
);

CREATE TABLE debt_service_scenarios (
    borrower_group TEXT PRIMARY KEY,
    income_or_ebit REAL,
    interest_payment REAL,
    principal_payment REAL,
    rate_shock_bps REAL
);

CREATE TABLE liquidity_stress_scenarios (
    institution TEXT PRIMARY KEY,
    hqla REAL,
    net_cash_outflows REAL,
    deposit_outflow_rate REAL,
    market_funding_rollover_rate REAL
);

CREATE TABLE credit_allocation_scenarios (
    credit_channel TEXT PRIMARY KEY,
    flow_share REAL,
    productive_score REAL,
    speculation_score REAL,
    resilience_score REAL,
    inclusion_score REAL
);

CREATE TABLE monetary_hierarchy_scenarios (
    claim TEXT PRIMARY KEY,
    safety_score REAL,
    liquidity_score REAL,
    public_backstop_score REAL,
    collateral_acceptance_score REAL
);

CREATE TABLE sustainable_finance_scenarios (
    finance_use TEXT PRIMARY KEY,
    financial_return_score REAL,
    resilience_score REAL,
    ecological_alignment_score REAL,
    inclusion_score REAL,
    systemic_risk_score REAL
);
