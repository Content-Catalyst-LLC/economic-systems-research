DROP TABLE IF EXISTS production_sectors;
DROP TABLE IF EXISTS input_output_requirements;
DROP TABLE IF EXISTS final_demand_exchange_scenarios;
DROP TABLE IF EXISTS production_distribution_exchange_results;

CREATE TABLE production_sectors (
    sector_code TEXT PRIMARY KEY,
    sector TEXT,
    institutional_role TEXT,
    labor_share REAL,
    non_labor_share REAL,
    public_or_mixed_share REAL,
    public_goods_dependence REAL,
    ecological_intensity REAL,
    employment_intensity REAL,
    trade_exposure REAL
);

CREATE TABLE input_output_requirements (
    supplying_sector TEXT,
    purchasing_sector TEXT,
    input_requirement REAL
);

CREATE TABLE final_demand_exchange_scenarios (
    scenario TEXT PRIMARY KEY,
    agriculture REAL,
    manufacturing REAL,
    services REAL,
    public_goods REAL,
    care_reproduction REAL,
    ecological_repair REAL
);

CREATE TABLE production_distribution_exchange_results (
    scenario TEXT,
    sector_code TEXT,
    final_demand REAL,
    total_output REAL,
    indirect_output_requirement REAL,
    output_multiplier REAL,
    labor_income REAL,
    non_labor_income REAL,
    public_or_mixed_income REAL,
    ecological_throughput REAL,
    employment_requirement REAL,
    exchange_dependency REAL
);
