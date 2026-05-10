DROP TABLE IF EXISTS material_flow_scenarios;
DROP TABLE IF EXISTS product_life_design;
DROP TABLE IF EXISTS value_retention_pathways;
DROP TABLE IF EXISTS regenerative_production;
DROP TABLE IF EXISTS infrastructure_policy;
DROP TABLE IF EXISTS labor_business_models;
DROP TABLE IF EXISTS rebound_scale_scenarios;
DROP TABLE IF EXISTS circular_justice;

CREATE TABLE material_flow_scenarios (
    scenario TEXT PRIMARY KEY,
    recovered_material REAL,
    total_material_input REAL,
    residual_waste REAL,
    total_throughput REAL,
    virgin_extraction_pressure REAL,
    leakage_risk REAL
);

CREATE TABLE product_life_design (
    product TEXT PRIMARY KEY,
    actual_product_life REAL,
    baseline_product_life REAL,
    durability REAL,
    repairability REAL,
    modularity REAL,
    disassembly_score REAL,
    material_separability REAL,
    proprietary_lock_in REAL
);

CREATE TABLE value_retention_pathways (
    pathway TEXT PRIMARY KEY,
    material_retention REAL,
    energy_retention REAL,
    labor_value_retention REAL,
    functional_retention REAL,
    processing_intensity REAL,
    quality_loss REAL
);

CREATE TABLE regenerative_production (
    scenario TEXT PRIMARY KEY,
    ecological_restoration REAL,
    ecological_degradation REAL,
    soil_health REAL,
    water_retention REAL,
    biodiversity REAL,
    local_capability REAL,
    stewardship_labor REAL
);

CREATE TABLE infrastructure_policy (
    policy_system TEXT PRIMARY KEY,
    collection_systems REAL,
    sorting_capacity REAL,
    repair_hubs REAL,
    reverse_logistics REAL,
    product_standards REAL,
    public_procurement REAL,
    digital_product_passports REAL,
    right_to_repair REAL
);

CREATE TABLE labor_business_models (
    model TEXT PRIMARY KEY,
    repair_jobs REAL,
    remanufacturing_jobs REAL,
    maintenance_capacity REAL,
    worker_skill_depth REAL,
    producer_responsibility REAL,
    durability_incentive REAL,
    local_value_capture REAL
);

CREATE TABLE rebound_scale_scenarios (
    scenario TEXT PRIMARY KEY,
    efficiency_gain REAL,
    induced_additional_use REAL,
    absolute_throughput_change REAL,
    scale_discipline REAL,
    circularity_ratio REAL,
    wellbeing_gain REAL
);

CREATE TABLE circular_justice (
    "group" TEXT PRIMARY KEY,
    pollution_reduction REAL,
    job_quality REAL,
    local_value_capture REAL,
    decision_voice REAL,
    hazard_exposure REAL,
    access_to_repair REAL
);
