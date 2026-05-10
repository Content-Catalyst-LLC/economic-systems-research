"""
Build stylized datasets for circular economy and regenerative production.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_material_flow_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "linear_take_make_dispose", "recovered_material": 12, "total_material_input": 140, "residual_waste": 96, "total_throughput": 150, "virgin_extraction_pressure": 0.88, "leakage_risk": 0.72},
        {"scenario": "basic_recycling_improvement", "recovered_material": 36, "total_material_input": 136, "residual_waste": 70, "total_throughput": 140, "virgin_extraction_pressure": 0.70, "leakage_risk": 0.58},
        {"scenario": "repair_reuse_priority", "recovered_material": 58, "total_material_input": 122, "residual_waste": 44, "total_throughput": 128, "virgin_extraction_pressure": 0.52, "leakage_risk": 0.36},
        {"scenario": "remanufacturing_high_value_retention", "recovered_material": 72, "total_material_input": 126, "residual_waste": 38, "total_throughput": 130, "virgin_extraction_pressure": 0.44, "leakage_risk": 0.30},
        {"scenario": "circular_but_high_consumption_rebound", "recovered_material": 82, "total_material_input": 170, "residual_waste": 58, "total_throughput": 182, "virgin_extraction_pressure": 0.62, "leakage_risk": 0.44},
        {"scenario": "sufficiency_circular_system", "recovered_material": 64, "total_material_input": 96, "residual_waste": 22, "total_throughput": 102, "virgin_extraction_pressure": 0.30, "leakage_risk": 0.20},
    ])


def build_product_life_design() -> pd.DataFrame:
    return pd.DataFrame([
        {"product": "sealed_fast_cycle_electronics", "actual_product_life": 3.0, "baseline_product_life": 5.0, "durability": 0.28, "repairability": 0.14, "modularity": 0.18, "disassembly_score": 0.12, "material_separability": 0.20, "proprietary_lock_in": 0.82},
        {"product": "repairable_modular_device", "actual_product_life": 8.5, "baseline_product_life": 5.0, "durability": 0.76, "repairability": 0.82, "modularity": 0.80, "disassembly_score": 0.76, "material_separability": 0.72, "proprietary_lock_in": 0.26},
        {"product": "durable_appliance", "actual_product_life": 14.0, "baseline_product_life": 9.0, "durability": 0.84, "repairability": 0.70, "modularity": 0.58, "disassembly_score": 0.62, "material_separability": 0.64, "proprietary_lock_in": 0.30},
        {"product": "single_use_packaging", "actual_product_life": 0.1, "baseline_product_life": 0.1, "durability": 0.08, "repairability": 0.00, "modularity": 0.00, "disassembly_score": 0.12, "material_separability": 0.30, "proprietary_lock_in": 0.10},
        {"product": "standardized_reusable_container", "actual_product_life": 7.0, "baseline_product_life": 1.0, "durability": 0.78, "repairability": 0.62, "modularity": 0.44, "disassembly_score": 0.58, "material_separability": 0.74, "proprietary_lock_in": 0.12},
    ])


def build_value_retention_pathways() -> pd.DataFrame:
    return pd.DataFrame([
        {"pathway": "direct_reuse", "material_retention": 0.96, "energy_retention": 0.92, "labor_value_retention": 0.82, "functional_retention": 0.88, "processing_intensity": 0.10, "quality_loss": 0.06},
        {"pathway": "repair", "material_retention": 0.94, "energy_retention": 0.88, "labor_value_retention": 0.86, "functional_retention": 0.90, "processing_intensity": 0.16, "quality_loss": 0.08},
        {"pathway": "remanufacturing", "material_retention": 0.78, "energy_retention": 0.70, "labor_value_retention": 0.68, "functional_retention": 0.82, "processing_intensity": 0.38, "quality_loss": 0.14},
        {"pathway": "high_quality_recycling", "material_retention": 0.62, "energy_retention": 0.40, "labor_value_retention": 0.28, "functional_retention": 0.34, "processing_intensity": 0.56, "quality_loss": 0.28},
        {"pathway": "downcycling", "material_retention": 0.44, "energy_retention": 0.24, "labor_value_retention": 0.16, "functional_retention": 0.18, "processing_intensity": 0.50, "quality_loss": 0.48},
        {"pathway": "landfill_incineration", "material_retention": 0.04, "energy_retention": 0.06, "labor_value_retention": 0.02, "functional_retention": 0.00, "processing_intensity": 0.26, "quality_loss": 0.96},
    ])


def build_regenerative_production() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "extractive_land_use", "ecological_restoration": 6, "ecological_degradation": 24, "soil_health": 0.22, "water_retention": 0.24, "biodiversity": 0.20, "local_capability": 0.28, "stewardship_labor": 0.22},
        {"scenario": "reduced_impact_production", "ecological_restoration": 12, "ecological_degradation": 16, "soil_health": 0.42, "water_retention": 0.44, "biodiversity": 0.40, "local_capability": 0.44, "stewardship_labor": 0.38},
        {"scenario": "regenerative_agriculture", "ecological_restoration": 24, "ecological_degradation": 10, "soil_health": 0.76, "water_retention": 0.78, "biodiversity": 0.72, "local_capability": 0.66, "stewardship_labor": 0.74},
        {"scenario": "industrial_symbiosis_with_restoration", "ecological_restoration": 20, "ecological_degradation": 11, "soil_health": 0.60, "water_retention": 0.62, "biodiversity": 0.58, "local_capability": 0.70, "stewardship_labor": 0.62},
        {"scenario": "community_regeneration_system", "ecological_restoration": 26, "ecological_degradation": 8, "soil_health": 0.80, "water_retention": 0.82, "biodiversity": 0.78, "local_capability": 0.82, "stewardship_labor": 0.80},
    ])


def build_infrastructure_policy() -> pd.DataFrame:
    return pd.DataFrame([
        {"policy_system": "weak_recycling_only_policy", "collection_systems": 0.42, "sorting_capacity": 0.38, "repair_hubs": 0.16, "reverse_logistics": 0.24, "product_standards": 0.30, "public_procurement": 0.28, "digital_product_passports": 0.14, "right_to_repair": 0.20},
        {"policy_system": "extended_producer_responsibility", "collection_systems": 0.72, "sorting_capacity": 0.66, "repair_hubs": 0.42, "reverse_logistics": 0.68, "product_standards": 0.64, "public_procurement": 0.54, "digital_product_passports": 0.56, "right_to_repair": 0.52},
        {"policy_system": "right_to_repair_local_infrastructure", "collection_systems": 0.66, "sorting_capacity": 0.58, "repair_hubs": 0.82, "reverse_logistics": 0.62, "product_standards": 0.70, "public_procurement": 0.60, "digital_product_passports": 0.54, "right_to_repair": 0.86},
        {"policy_system": "circular_industrial_strategy", "collection_systems": 0.78, "sorting_capacity": 0.76, "repair_hubs": 0.70, "reverse_logistics": 0.82, "product_standards": 0.84, "public_procurement": 0.80, "digital_product_passports": 0.78, "right_to_repair": 0.74},
        {"policy_system": "regenerative_public_procurement", "collection_systems": 0.72, "sorting_capacity": 0.68, "repair_hubs": 0.76, "reverse_logistics": 0.70, "product_standards": 0.82, "public_procurement": 0.90, "digital_product_passports": 0.72, "right_to_repair": 0.78},
    ])


def build_labor_business_models() -> pd.DataFrame:
    return pd.DataFrame([
        {"model": "sales_volume_replacement_model", "repair_jobs": 0.18, "remanufacturing_jobs": 0.14, "maintenance_capacity": 0.20, "worker_skill_depth": 0.24, "producer_responsibility": 0.16, "durability_incentive": 0.18, "local_value_capture": 0.22},
        {"model": "repair_service_network", "repair_jobs": 0.78, "remanufacturing_jobs": 0.46, "maintenance_capacity": 0.82, "worker_skill_depth": 0.76, "producer_responsibility": 0.52, "durability_incentive": 0.68, "local_value_capture": 0.76},
        {"model": "remanufacturing_cluster", "repair_jobs": 0.54, "remanufacturing_jobs": 0.84, "maintenance_capacity": 0.68, "worker_skill_depth": 0.80, "producer_responsibility": 0.66, "durability_incentive": 0.62, "local_value_capture": 0.70},
        {"model": "product_service_system", "repair_jobs": 0.62, "remanufacturing_jobs": 0.64, "maintenance_capacity": 0.76, "worker_skill_depth": 0.70, "producer_responsibility": 0.86, "durability_incentive": 0.84, "local_value_capture": 0.58},
        {"model": "platformized_low_wage_repair", "repair_jobs": 0.62, "remanufacturing_jobs": 0.34, "maintenance_capacity": 0.58, "worker_skill_depth": 0.46, "producer_responsibility": 0.34, "durability_incentive": 0.42, "local_value_capture": 0.30},
    ])


def build_rebound_scale_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "efficiency_rebound_high_consumption", "efficiency_gain": 0.28, "induced_additional_use": 0.22, "absolute_throughput_change": 0.08, "scale_discipline": 0.20, "circularity_ratio": 0.48, "wellbeing_gain": 0.08},
        {"scenario": "circularity_without_scale_control", "efficiency_gain": 0.22, "induced_additional_use": 0.18, "absolute_throughput_change": 0.04, "scale_discipline": 0.28, "circularity_ratio": 0.62, "wellbeing_gain": 0.10},
        {"scenario": "sufficiency_plus_circularity", "efficiency_gain": 0.18, "induced_additional_use": 0.04, "absolute_throughput_change": -0.22, "scale_discipline": 0.82, "circularity_ratio": 0.70, "wellbeing_gain": 0.14},
        {"scenario": "public_procurement_durability_shift", "efficiency_gain": 0.16, "induced_additional_use": 0.03, "absolute_throughput_change": -0.14, "scale_discipline": 0.74, "circularity_ratio": 0.58, "wellbeing_gain": 0.12},
        {"scenario": "austerity_low_throughput_no_regeneration", "efficiency_gain": 0.04, "induced_additional_use": 0.00, "absolute_throughput_change": -0.16, "scale_discipline": 0.54, "circularity_ratio": 0.26, "wellbeing_gain": -0.18},
    ])


def build_circular_justice() -> pd.DataFrame:
    return pd.DataFrame([
        {"group": "waste_processing_community", "pollution_reduction": 0.34, "job_quality": 0.30, "local_value_capture": 0.22, "decision_voice": 0.26, "hazard_exposure": 0.78, "access_to_repair": 0.38},
        {"group": "repair_workers", "pollution_reduction": 0.58, "job_quality": 0.64, "local_value_capture": 0.70, "decision_voice": 0.52, "hazard_exposure": 0.38, "access_to_repair": 0.72},
        {"group": "low_income_consumers", "pollution_reduction": 0.46, "job_quality": 0.34, "local_value_capture": 0.38, "decision_voice": 0.32, "hazard_exposure": 0.56, "access_to_repair": 0.44},
        {"group": "extractive_frontier_region", "pollution_reduction": 0.26, "job_quality": 0.28, "local_value_capture": 0.18, "decision_voice": 0.24, "hazard_exposure": 0.82, "access_to_repair": 0.28},
        {"group": "circular_innovation_cluster", "pollution_reduction": 0.72, "job_quality": 0.74, "local_value_capture": 0.82, "decision_voice": 0.64, "hazard_exposure": 0.22, "access_to_repair": 0.78},
    ])


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "circular_economy_regenerative_production.sqlite"
    names = [
        "material_flow_scenarios",
        "product_life_design",
        "value_retention_pathways",
        "regenerative_production",
        "infrastructure_policy",
        "labor_business_models",
        "rebound_scale_scenarios",
        "circular_justice",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_material_flow_scenarios(),
        build_product_life_design(),
        build_value_retention_pathways(),
        build_regenerative_production(),
        build_infrastructure_policy(),
        build_labor_business_models(),
        build_rebound_scale_scenarios(),
        build_circular_justice(),
    ]

    filenames = [
        "material_flow_scenarios.csv",
        "product_life_design.csv",
        "value_retention_pathways.csv",
        "regenerative_production.csv",
        "infrastructure_policy.csv",
        "labor_business_models.csv",
        "rebound_scale_scenarios.csv",
        "circular_justice.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created circular economy and regenerative production base data.")


if __name__ == "__main__":
    main()
