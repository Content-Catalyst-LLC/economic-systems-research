DROP TABLE IF EXISTS trade_position_scenarios;
DROP TABLE IF EXISTS export_basket_scenarios;
DROP TABLE IF EXISTS value_chain_scenarios;
DROP TABLE IF EXISTS terms_of_trade_scenarios;
DROP TABLE IF EXISTS finance_currency_scenarios;
DROP TABLE IF EXISTS regional_inequality_scenarios;
DROP TABLE IF EXISTS labor_exposure_scenarios;
DROP TABLE IF EXISTS ecological_trade_scenarios;
DROP TABLE IF EXISTS strategic_resilience_scenarios;

CREATE TABLE trade_position_scenarios (
    scenario TEXT PRIMARY KEY,
    exports REAL,
    imports REAL,
    output REAL,
    strategic_import_dependence REAL,
    intermediate_import_share REAL,
    energy_import_share REAL
);

CREATE TABLE export_basket_scenarios (
    scenario TEXT,
    export_category TEXT,
    export_value REAL
);

CREATE TABLE value_chain_scenarios (
    scenario TEXT PRIMARY KEY,
    gross_exports REAL,
    domestic_value_added REAL,
    lead_firm_control REAL,
    technology_control REAL,
    branding_control REAL,
    assembly_dependence REAL,
    upgrading_potential REAL
);

CREATE TABLE terms_of_trade_scenarios (
    scenario TEXT PRIMARY KEY,
    export_price_index REAL,
    import_price_index REAL,
    commodity_share REAL,
    imported_food_energy_share REAL,
    stabilization_fund_strength REAL
);

CREATE TABLE finance_currency_scenarios (
    scenario TEXT PRIMARY KEY,
    foreign_currency_debt REAL,
    capital_flow_volatility REAL,
    reserve_buffer REAL,
    current_account_pressure REAL,
    external_financing_need REAL,
    policy_space REAL
);

CREATE TABLE regional_inequality_scenarios (
    region TEXT PRIMARY KEY,
    export_linkage REAL,
    productivity REAL,
    infrastructure_depth REAL,
    capital_access REAL,
    market_access REAL,
    institutional_capacity REAL
);

CREATE TABLE labor_exposure_scenarios (
    sector TEXT PRIMARY KEY,
    import_competition REAL,
    offshoring_risk REAL,
    wage_bargaining_strength REAL,
    skills_transferability REAL,
    employment_security REAL,
    adjustment_support REAL
);

CREATE TABLE ecological_trade_scenarios (
    scenario TEXT PRIMARY KEY,
    embodied_emissions_imports REAL,
    domestic_emissions_intensity REAL,
    resource_extraction_burden REAL,
    waste_displacement REAL,
    supply_chain_traceability REAL,
    ecological_regulation_alignment REAL
);

CREATE TABLE strategic_resilience_scenarios (
    scenario TEXT PRIMARY KEY,
    supplier_diversification REAL,
    domestic_capability REAL,
    strategic_stock_buffer REAL,
    regional_redundancy REAL,
    import_substitution_capacity REAL,
    cooperative_trade_access REAL
);
