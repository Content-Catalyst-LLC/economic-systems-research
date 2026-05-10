DROP TABLE IF EXISTS income_distribution;
DROP TABLE IF EXISTS power_groups;
DROP TABLE IF EXISTS fiscal_incidence;
DROP TABLE IF EXISTS inflation_labor_conflict;
DROP TABLE IF EXISTS debt_rent_conflict;
DROP TABLE IF EXISTS welfare_globalization_crisis;
DROP TABLE IF EXISTS legitimacy_conflict;

CREATE TABLE income_distribution (
    scenario TEXT PRIMARY KEY,
    wages REAL,
    profits REAL,
    rents REAL,
    taxes_paid REAL,
    benefits_received REAL,
    public_goods_value REAL
);

CREATE TABLE power_groups (
    "group" TEXT PRIMARY KEY,
    ownership_power REAL,
    organization_power REAL,
    access_power REAL,
    mobility_power REAL,
    voice_power REAL,
    media_influence REAL,
    legal_position REAL
);

CREATE TABLE fiscal_incidence (
    "group" TEXT PRIMARY KEY,
    market_income REAL,
    taxes_paid REAL,
    cash_transfers REAL,
    services_received REAL,
    debt_service REAL,
    housing_cost REAL
);

CREATE TABLE inflation_labor_conflict (
    scenario TEXT PRIMARY KEY,
    price_inflation REAL,
    nominal_wage_growth REAL,
    profit_margin_change REAL,
    interest_rate_shock REAL,
    unemployment_pressure REAL,
    bargaining_strength REAL
);

CREATE TABLE debt_rent_conflict (
    scenario TEXT PRIMARY KEY,
    debt_stock REAL,
    income REAL,
    interest_rate REAL,
    rent_burden REAL,
    asset_owner_gain REAL,
    debtor_relief_access REAL,
    legal_enforcement_strength REAL
);

CREATE TABLE welfare_globalization_crisis (
    scenario TEXT PRIMARY KEY,
    welfare_buffer REAL,
    tax_progressivity REAL,
    labor_voice REAL,
    capital_mobility REAL,
    trade_exposure REAL,
    austerity_pressure REAL,
    public_trust REAL
);

CREATE TABLE legitimacy_conflict (
    scenario TEXT PRIMARY KEY,
    inequality_pressure REAL,
    inflation_pressure REAL,
    unemployment_pressure REAL,
    representation_gap REAL,
    shock_exposure REAL,
    fairness REAL,
    security REAL,
    voice REAL,
    institutional_trust REAL
);
