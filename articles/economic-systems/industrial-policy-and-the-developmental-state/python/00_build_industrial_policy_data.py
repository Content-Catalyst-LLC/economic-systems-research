"""
Build stylized datasets for industrial policy and the developmental state.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_strategic_sector_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"sector": "clean_energy_equipment", "sector_output": 220, "total_output": 1800, "sector_labor": 62, "sector_exports": 88, "technology_depth": 0.72, "learning_potential": 0.86, "domestic_linkage_potential": 0.78},
        {"sector": "semiconductors_and_components", "sector_output": 180, "total_output": 1800, "sector_labor": 38, "sector_exports": 112, "technology_depth": 0.92, "learning_potential": 0.94, "domestic_linkage_potential": 0.64},
        {"sector": "food_processing_and_cold_chain", "sector_output": 260, "total_output": 1800, "sector_labor": 95, "sector_exports": 52, "technology_depth": 0.48, "learning_potential": 0.60, "domestic_linkage_potential": 0.88},
        {"sector": "advanced_materials", "sector_output": 140, "total_output": 1800, "sector_labor": 30, "sector_exports": 70, "technology_depth": 0.84, "learning_potential": 0.88, "domestic_linkage_potential": 0.70},
        {"sector": "public_transit_manufacturing", "sector_output": 120, "total_output": 1800, "sector_labor": 42, "sector_exports": 24, "technology_depth": 0.64, "learning_potential": 0.76, "domestic_linkage_potential": 0.82},
        {"sector": "low_value_assembly", "sector_output": 310, "total_output": 1800, "sector_labor": 210, "sector_exports": 180, "technology_depth": 0.26, "learning_potential": 0.34, "domestic_linkage_potential": 0.38},
    ])


def build_support_conditionality_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"sector": "clean_energy_equipment", "public_support": 55, "productivity_gain": 0.16, "employment_gain": 1450, "export_growth": 0.18, "local_supplier_share": 0.62, "emissions_reduction": 0.34, "support_duration_years": 5},
        {"sector": "semiconductors_and_components", "public_support": 90, "productivity_gain": 0.20, "employment_gain": 900, "export_growth": 0.22, "local_supplier_share": 0.42, "emissions_reduction": 0.18, "support_duration_years": 7},
        {"sector": "food_processing_and_cold_chain", "public_support": 38, "productivity_gain": 0.12, "employment_gain": 2100, "export_growth": 0.10, "local_supplier_share": 0.74, "emissions_reduction": 0.16, "support_duration_years": 4},
        {"sector": "advanced_materials", "public_support": 46, "productivity_gain": 0.18, "employment_gain": 620, "export_growth": 0.17, "local_supplier_share": 0.56, "emissions_reduction": 0.22, "support_duration_years": 6},
        {"sector": "public_transit_manufacturing", "public_support": 44, "productivity_gain": 0.13, "employment_gain": 1500, "export_growth": 0.07, "local_supplier_share": 0.66, "emissions_reduction": 0.46, "support_duration_years": 6},
        {"sector": "low_value_assembly", "public_support": 40, "productivity_gain": 0.04, "employment_gain": 1800, "export_growth": 0.06, "local_supplier_share": 0.32, "emissions_reduction": 0.02, "support_duration_years": 10},
    ])


def build_development_finance_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "short_term_commercial_credit", "patient_credit_share": 0.18, "industrial_credit_share": 0.26, "speculative_credit_share": 0.46, "fx_debt_exposure": 0.36, "development_bank_capacity": 0.24, "credit_monitoring_quality": 0.34},
        {"scenario": "directed_credit_without_discipline", "patient_credit_share": 0.48, "industrial_credit_share": 0.54, "speculative_credit_share": 0.26, "fx_debt_exposure": 0.28, "development_bank_capacity": 0.52, "credit_monitoring_quality": 0.26},
        {"scenario": "development_bank_learning_model", "patient_credit_share": 0.66, "industrial_credit_share": 0.68, "speculative_credit_share": 0.14, "fx_debt_exposure": 0.18, "development_bank_capacity": 0.76, "credit_monitoring_quality": 0.74},
        {"scenario": "green_development_finance", "patient_credit_share": 0.70, "industrial_credit_share": 0.62, "speculative_credit_share": 0.12, "fx_debt_exposure": 0.16, "development_bank_capacity": 0.80, "credit_monitoring_quality": 0.78},
        {"scenario": "external_debt_dependency", "patient_credit_share": 0.34, "industrial_credit_share": 0.38, "speculative_credit_share": 0.30, "fx_debt_exposure": 0.62, "development_bank_capacity": 0.30, "credit_monitoring_quality": 0.42},
    ])


def build_infrastructure_energy_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"region": "core_export_corridor", "transport_reliability": 0.82, "port_access": 0.86, "energy_reliability": 0.78, "water_reliability": 0.70, "digital_connectivity": 0.76, "industrial_land_readiness": 0.72},
        {"region": "secondary_city_cluster", "transport_reliability": 0.66, "port_access": 0.58, "energy_reliability": 0.70, "water_reliability": 0.66, "digital_connectivity": 0.68, "industrial_land_readiness": 0.74},
        {"region": "rural_processing_zone", "transport_reliability": 0.48, "port_access": 0.36, "energy_reliability": 0.52, "water_reliability": 0.62, "digital_connectivity": 0.44, "industrial_land_readiness": 0.58},
        {"region": "energy_transition_hub", "transport_reliability": 0.72, "port_access": 0.64, "energy_reliability": 0.88, "water_reliability": 0.68, "digital_connectivity": 0.78, "industrial_land_readiness": 0.80},
        {"region": "postindustrial_reinvestment_region", "transport_reliability": 0.62, "port_access": 0.60, "energy_reliability": 0.64, "water_reliability": 0.58, "digital_connectivity": 0.70, "industrial_land_readiness": 0.66},
    ])


def build_skills_labor_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "low_wage_assembly_model", "technical_training_depth": 0.30, "apprenticeship_capacity": 0.22, "engineering_depth": 0.28, "labor_security": 0.26, "wage_progression": 0.22, "learning_retention": 0.34},
        {"scenario": "vocational_upgrading_model", "technical_training_depth": 0.68, "apprenticeship_capacity": 0.72, "engineering_depth": 0.58, "labor_security": 0.54, "wage_progression": 0.50, "learning_retention": 0.68},
        {"scenario": "engineering_research_model", "technical_training_depth": 0.76, "apprenticeship_capacity": 0.62, "engineering_depth": 0.86, "labor_security": 0.60, "wage_progression": 0.58, "learning_retention": 0.78},
        {"scenario": "inclusive_skills_state", "technical_training_depth": 0.82, "apprenticeship_capacity": 0.78, "engineering_depth": 0.78, "labor_security": 0.74, "wage_progression": 0.72, "learning_retention": 0.82},
        {"scenario": "precarious_platform_industrialization", "technical_training_depth": 0.42, "apprenticeship_capacity": 0.24, "engineering_depth": 0.38, "labor_security": 0.18, "wage_progression": 0.24, "learning_retention": 0.30},
    ])


def build_capture_risk_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"program": "transparent_export_conditioned_support", "market_concentration": 0.34, "lobbying_intensity": 0.28, "evaluation_strength": 0.82, "open_ended_support": 0.18, "performance_shortfall": 0.22, "public_disclosure": 0.78},
        {"program": "incumbent_protection_subsidy", "market_concentration": 0.76, "lobbying_intensity": 0.72, "evaluation_strength": 0.26, "open_ended_support": 0.82, "performance_shortfall": 0.64, "public_disclosure": 0.24},
        {"program": "strategic_procurement_with_audit", "market_concentration": 0.46, "lobbying_intensity": 0.40, "evaluation_strength": 0.72, "open_ended_support": 0.34, "performance_shortfall": 0.30, "public_disclosure": 0.70},
        {"program": "regional_patronage_industrial_park", "market_concentration": 0.58, "lobbying_intensity": 0.66, "evaluation_strength": 0.22, "open_ended_support": 0.70, "performance_shortfall": 0.58, "public_disclosure": 0.28},
        {"program": "sunset_clause_learning_fund", "market_concentration": 0.38, "lobbying_intensity": 0.32, "evaluation_strength": 0.76, "open_ended_support": 0.20, "performance_shortfall": 0.26, "public_disclosure": 0.74},
    ])


def build_regional_cluster_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"cluster": "battery_supply_chain_cluster", "supplier_density": 0.76, "skills_depth": 0.70, "infrastructure_quality": 0.78, "research_linkage": 0.68, "regional_inclusion": 0.62, "export_connectivity": 0.72},
        {"cluster": "food_processing_cluster", "supplier_density": 0.66, "skills_depth": 0.54, "infrastructure_quality": 0.62, "research_linkage": 0.42, "regional_inclusion": 0.78, "export_connectivity": 0.52},
        {"cluster": "semiconductor_cluster", "supplier_density": 0.54, "skills_depth": 0.82, "infrastructure_quality": 0.86, "research_linkage": 0.88, "regional_inclusion": 0.46, "export_connectivity": 0.84},
        {"cluster": "public_transit_equipment_cluster", "supplier_density": 0.62, "skills_depth": 0.64, "infrastructure_quality": 0.72, "research_linkage": 0.56, "regional_inclusion": 0.74, "export_connectivity": 0.48},
        {"cluster": "industrial_park_without_ecosystem", "supplier_density": 0.26, "skills_depth": 0.32, "infrastructure_quality": 0.54, "research_linkage": 0.20, "regional_inclusion": 0.30, "export_connectivity": 0.28},
    ])


def build_green_industrial_policy_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"sector": "grid_storage", "productivity_gain": 0.16, "emissions_reduction": 0.42, "domestic_linkage": 0.66, "employment_quality": 0.68, "resilience_value": 0.86, "material_risk": 0.42},
        {"sector": "solar_manufacturing", "productivity_gain": 0.12, "emissions_reduction": 0.36, "domestic_linkage": 0.58, "employment_quality": 0.54, "resilience_value": 0.76, "material_risk": 0.46},
        {"sector": "green_steel", "productivity_gain": 0.18, "emissions_reduction": 0.52, "domestic_linkage": 0.72, "employment_quality": 0.70, "resilience_value": 0.82, "material_risk": 0.54},
        {"sector": "building_retrofit_supply_chain", "productivity_gain": 0.10, "emissions_reduction": 0.44, "domestic_linkage": 0.78, "employment_quality": 0.66, "resilience_value": 0.80, "material_risk": 0.28},
        {"sector": "fossil_input_substitution", "productivity_gain": 0.08, "emissions_reduction": 0.20, "domestic_linkage": 0.42, "employment_quality": 0.46, "resilience_value": 0.48, "material_risk": 0.62},
    ])


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "industrial_policy_developmental_state.sqlite"
    names = [
        "strategic_sector_scenarios",
        "support_conditionality_scenarios",
        "development_finance_scenarios",
        "infrastructure_energy_scenarios",
        "skills_labor_scenarios",
        "capture_risk_scenarios",
        "regional_cluster_scenarios",
        "green_industrial_policy_scenarios",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_strategic_sector_scenarios(),
        build_support_conditionality_scenarios(),
        build_development_finance_scenarios(),
        build_infrastructure_energy_scenarios(),
        build_skills_labor_scenarios(),
        build_capture_risk_scenarios(),
        build_regional_cluster_scenarios(),
        build_green_industrial_policy_scenarios(),
    ]

    filenames = [
        "strategic_sector_scenarios.csv",
        "support_conditionality_scenarios.csv",
        "development_finance_scenarios.csv",
        "infrastructure_energy_scenarios.csv",
        "skills_labor_scenarios.csv",
        "capture_risk_scenarios.csv",
        "regional_cluster_scenarios.csv",
        "green_industrial_policy_scenarios.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created industrial policy and developmental state base data.")


if __name__ == "__main__":
    main()
