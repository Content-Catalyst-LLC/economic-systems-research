"""
Build stylized datasets for socialism, planning, and the mixed economy.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_mixed_economy_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "market_led_residual_state", "market_allocation": 0.72, "public_planning": 0.10, "public_provision": 0.10, "regulation_rights": 0.08, "public_ownership_share": 0.08, "social_rights_strength": 0.28, "private_profit_weight": 0.82, "social_need_weight": 0.24},
        {"scenario": "social_democratic_mixed_economy", "market_allocation": 0.46, "public_planning": 0.18, "public_provision": 0.22, "regulation_rights": 0.14, "public_ownership_share": 0.18, "social_rights_strength": 0.76, "private_profit_weight": 0.52, "social_need_weight": 0.72},
        {"scenario": "developmental_mixed_economy", "market_allocation": 0.50, "public_planning": 0.26, "public_provision": 0.12, "regulation_rights": 0.12, "public_ownership_share": 0.22, "social_rights_strength": 0.52, "private_profit_weight": 0.60, "social_need_weight": 0.58},
        {"scenario": "public_economy_expansion", "market_allocation": 0.34, "public_planning": 0.24, "public_provision": 0.28, "regulation_rights": 0.14, "public_ownership_share": 0.34, "social_rights_strength": 0.82, "private_profit_weight": 0.38, "social_need_weight": 0.82},
        {"scenario": "centralized_planning_model", "market_allocation": 0.12, "public_planning": 0.62, "public_provision": 0.18, "regulation_rights": 0.08, "public_ownership_share": 0.72, "social_rights_strength": 0.66, "private_profit_weight": 0.16, "social_need_weight": 0.76},
        {"scenario": "green_transition_mixed_economy", "market_allocation": 0.42, "public_planning": 0.28, "public_provision": 0.18, "regulation_rights": 0.12, "public_ownership_share": 0.26, "social_rights_strength": 0.74, "private_profit_weight": 0.48, "social_need_weight": 0.84},
    ])


def build_planning_capacity() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "thin_state_low_reach", "state_capacity": 0.34, "data_quality": 0.38, "institutional_reach": 0.32, "feedback_quality": 0.30, "democratic_accountability": 0.42, "coordination_authority": 0.30, "implementation_speed": 0.34},
        {"scenario": "technocratic_high_capacity_low_accountability", "state_capacity": 0.78, "data_quality": 0.74, "institutional_reach": 0.76, "feedback_quality": 0.54, "democratic_accountability": 0.32, "coordination_authority": 0.80, "implementation_speed": 0.72},
        {"scenario": "democratic_planning_capacity", "state_capacity": 0.74, "data_quality": 0.72, "institutional_reach": 0.70, "feedback_quality": 0.76, "democratic_accountability": 0.82, "coordination_authority": 0.70, "implementation_speed": 0.66},
        {"scenario": "bureaucratic_rigid_planning", "state_capacity": 0.66, "data_quality": 0.54, "institutional_reach": 0.68, "feedback_quality": 0.28, "democratic_accountability": 0.24, "coordination_authority": 0.84, "implementation_speed": 0.58},
        {"scenario": "adaptive_mission_oriented_state", "state_capacity": 0.82, "data_quality": 0.80, "institutional_reach": 0.78, "feedback_quality": 0.82, "democratic_accountability": 0.74, "coordination_authority": 0.78, "implementation_speed": 0.76},
    ])


def build_decommodification_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "commodified_basic_needs", "healthcare_access": 0.32, "education_access": 0.44, "housing_security": 0.28, "childcare_support": 0.18, "public_transport": 0.30, "social_insurance": 0.26, "guaranteed_access": 0.22},
        {"scenario": "targeted_social_assistance", "healthcare_access": 0.54, "education_access": 0.58, "housing_security": 0.40, "childcare_support": 0.36, "public_transport": 0.42, "social_insurance": 0.48, "guaranteed_access": 0.46},
        {"scenario": "universal_public_services", "healthcare_access": 0.86, "education_access": 0.84, "housing_security": 0.66, "childcare_support": 0.78, "public_transport": 0.74, "social_insurance": 0.78, "guaranteed_access": 0.82},
        {"scenario": "worker_owned_social_rights_model", "healthcare_access": 0.74, "education_access": 0.78, "housing_security": 0.60, "childcare_support": 0.64, "public_transport": 0.62, "social_insurance": 0.70, "guaranteed_access": 0.72},
        {"scenario": "austerity_public_service_erosion", "healthcare_access": 0.42, "education_access": 0.46, "housing_security": 0.32, "childcare_support": 0.28, "public_transport": 0.34, "social_insurance": 0.36, "guaranteed_access": 0.34},
    ])


def build_sector_coordination() -> pd.DataFrame:
    return pd.DataFrame([
        {"sector": "consumer_goods", "market_fit": 0.82, "planning_fit": 0.30, "public_ownership_fit": 0.22, "regulation_need": 0.40, "social_rights_need": 0.24, "network_interdependence": 0.22, "public_good_character": 0.20},
        {"sector": "healthcare", "market_fit": 0.28, "planning_fit": 0.78, "public_ownership_fit": 0.68, "regulation_need": 0.82, "social_rights_need": 0.90, "network_interdependence": 0.70, "public_good_character": 0.82},
        {"sector": "housing", "market_fit": 0.42, "planning_fit": 0.72, "public_ownership_fit": 0.58, "regulation_need": 0.84, "social_rights_need": 0.82, "network_interdependence": 0.66, "public_good_character": 0.70},
        {"sector": "energy_grid", "market_fit": 0.24, "planning_fit": 0.90, "public_ownership_fit": 0.78, "regulation_need": 0.92, "social_rights_need": 0.74, "network_interdependence": 0.96, "public_good_character": 0.84},
        {"sector": "digital_platforms", "market_fit": 0.54, "planning_fit": 0.56, "public_ownership_fit": 0.34, "regulation_need": 0.82, "social_rights_need": 0.56, "network_interdependence": 0.88, "public_good_character": 0.62},
        {"sector": "public_transport", "market_fit": 0.34, "planning_fit": 0.84, "public_ownership_fit": 0.72, "regulation_need": 0.78, "social_rights_need": 0.76, "network_interdependence": 0.88, "public_good_character": 0.80},
        {"sector": "basic_water_sanitation", "market_fit": 0.18, "planning_fit": 0.88, "public_ownership_fit": 0.86, "regulation_need": 0.90, "social_rights_need": 0.92, "network_interdependence": 0.92, "public_good_character": 0.90},
    ])


def build_public_utilities() -> pd.DataFrame:
    return pd.DataFrame([
        {"utility": "water_public_utility", "universal_access": 0.88, "affordability": 0.80, "maintenance_investment": 0.74, "democratic_accountability": 0.70, "service_reliability": 0.78, "profit_extraction_pressure": 0.18, "regional_equity": 0.82},
        {"utility": "privatized_energy_distribution", "universal_access": 0.72, "affordability": 0.44, "maintenance_investment": 0.52, "democratic_accountability": 0.26, "service_reliability": 0.62, "profit_extraction_pressure": 0.78, "regional_equity": 0.40},
        {"utility": "regulated_private_telecom", "universal_access": 0.64, "affordability": 0.48, "maintenance_investment": 0.62, "democratic_accountability": 0.34, "service_reliability": 0.68, "profit_extraction_pressure": 0.66, "regional_equity": 0.42},
        {"utility": "public_transport_authority", "universal_access": 0.76, "affordability": 0.72, "maintenance_investment": 0.70, "democratic_accountability": 0.66, "service_reliability": 0.74, "profit_extraction_pressure": 0.20, "regional_equity": 0.76},
        {"utility": "underfunded_public_system", "universal_access": 0.66, "affordability": 0.70, "maintenance_investment": 0.36, "democratic_accountability": 0.56, "service_reliability": 0.42, "profit_extraction_pressure": 0.12, "regional_equity": 0.58},
    ])


def build_industrial_policy() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "laissez_faire_industrial_structure", "public_investment": 0.28, "sector_targeting": 0.18, "learning_policy": 0.20, "supplier_development": 0.22, "public_procurement": 0.24, "performance_discipline": 0.18, "green_transition_alignment": 0.20},
        {"scenario": "developmental_industrial_policy", "public_investment": 0.76, "sector_targeting": 0.82, "learning_policy": 0.78, "supplier_development": 0.74, "public_procurement": 0.68, "performance_discipline": 0.76, "green_transition_alignment": 0.54},
        {"scenario": "mission_oriented_green_transition", "public_investment": 0.84, "sector_targeting": 0.76, "learning_policy": 0.82, "supplier_development": 0.76, "public_procurement": 0.82, "performance_discipline": 0.72, "green_transition_alignment": 0.90},
        {"scenario": "captured_subsidy_regime", "public_investment": 0.54, "sector_targeting": 0.60, "learning_policy": 0.32, "supplier_development": 0.34, "public_procurement": 0.46, "performance_discipline": 0.20, "green_transition_alignment": 0.30},
        {"scenario": "regional_resilience_strategy", "public_investment": 0.70, "sector_targeting": 0.64, "learning_policy": 0.66, "supplier_development": 0.72, "public_procurement": 0.70, "performance_discipline": 0.62, "green_transition_alignment": 0.76},
    ])


def build_crisis_transition_globalization() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "market_only_crisis_response", "public_planning": 0.22, "infrastructure_depth": 0.36, "fiscal_capacity": 0.34, "administrative_speed": 0.30, "social_protection": 0.28, "ecological_targets": 0.24, "democratic_legitimacy": 0.36, "external_finance_constraint": 0.70},
        {"scenario": "wartime_mobilization_style_planning", "public_planning": 0.86, "infrastructure_depth": 0.78, "fiscal_capacity": 0.72, "administrative_speed": 0.82, "social_protection": 0.58, "ecological_targets": 0.42, "democratic_legitimacy": 0.46, "external_finance_constraint": 0.42},
        {"scenario": "pandemic_public_health_coordination", "public_planning": 0.76, "infrastructure_depth": 0.70, "fiscal_capacity": 0.68, "administrative_speed": 0.66, "social_protection": 0.72, "ecological_targets": 0.44, "democratic_legitimacy": 0.62, "external_finance_constraint": 0.48},
        {"scenario": "green_transition_planning", "public_planning": 0.82, "infrastructure_depth": 0.84, "fiscal_capacity": 0.74, "administrative_speed": 0.64, "social_protection": 0.76, "ecological_targets": 0.92, "democratic_legitimacy": 0.72, "external_finance_constraint": 0.46},
        {"scenario": "globally_constrained_development", "public_planning": 0.62, "infrastructure_depth": 0.54, "fiscal_capacity": 0.46, "administrative_speed": 0.50, "social_protection": 0.44, "ecological_targets": 0.58, "democratic_legitimacy": 0.54, "external_finance_constraint": 0.82},
    ])


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "socialism_planning_mixed_economy.sqlite"
    names = [
        "mixed_economy_scenarios",
        "planning_capacity",
        "decommodification_scenarios",
        "sector_coordination",
        "public_utilities",
        "industrial_policy",
        "crisis_transition_globalization",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_mixed_economy_scenarios(),
        build_planning_capacity(),
        build_decommodification_scenarios(),
        build_sector_coordination(),
        build_public_utilities(),
        build_industrial_policy(),
        build_crisis_transition_globalization(),
    ]

    filenames = [
        "mixed_economy_scenarios.csv",
        "planning_capacity.csv",
        "decommodification_scenarios.csv",
        "sector_coordination.csv",
        "public_utilities.csv",
        "industrial_policy.csv",
        "crisis_transition_globalization.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created socialism, planning, and mixed economy base data.")


if __name__ == "__main__":
    main()
