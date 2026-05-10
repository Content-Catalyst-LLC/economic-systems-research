"""
Build stylized datasets for the future of economic systems in an age of limits.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_future_viability() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "fossil_extractivist_continuity", "ecological_pressure": 0.88, "institutional_capacity": 0.44, "social_inclusion": 0.38, "resilience": 0.34, "public_trust": 0.36, "adaptive_learning": 0.28},
        {"scenario": "green_growth_technology_push", "ecological_pressure": 0.60, "institutional_capacity": 0.62, "social_inclusion": 0.50, "resilience": 0.54, "public_trust": 0.50, "adaptive_learning": 0.58},
        {"scenario": "boundary_aware_social_democracy", "ecological_pressure": 0.38, "institutional_capacity": 0.78, "social_inclusion": 0.76, "resilience": 0.74, "public_trust": 0.72, "adaptive_learning": 0.76},
        {"scenario": "austerity_under_limits", "ecological_pressure": 0.48, "institutional_capacity": 0.36, "social_inclusion": 0.28, "resilience": 0.30, "public_trust": 0.24, "adaptive_learning": 0.30},
        {"scenario": "regenerative_public_goods_transition", "ecological_pressure": 0.30, "institutional_capacity": 0.82, "social_inclusion": 0.80, "resilience": 0.82, "public_trust": 0.78, "adaptive_learning": 0.84},
    ])


def build_throughput_pressure() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "high_growth_high_intensity", "population": 100, "affluence": 2.4, "material_intensity": 0.78, "wellbeing": 0.68, "inclusion": 0.42},
        {"scenario": "efficiency_led_transition", "population": 100, "affluence": 2.1, "material_intensity": 0.46, "wellbeing": 0.72, "inclusion": 0.54},
        {"scenario": "sufficiency_public_goods", "population": 100, "affluence": 1.5, "material_intensity": 0.34, "wellbeing": 0.80, "inclusion": 0.78},
        {"scenario": "low_income_development_priority", "population": 100, "affluence": 0.9, "material_intensity": 0.52, "wellbeing": 0.48, "inclusion": 0.46},
        {"scenario": "circular_regenerative_system", "population": 100, "affluence": 1.6, "material_intensity": 0.28, "wellbeing": 0.82, "inclusion": 0.80},
    ])


def build_transition_capacity() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "market_signals_only", "public_investment": 0.34, "policy_credibility": 0.40, "technology": 0.66, "social_trust": 0.42, "implementation_capacity": 0.36, "coordination": 0.30},
        {"scenario": "industrial_policy_compact", "public_investment": 0.76, "policy_credibility": 0.72, "technology": 0.78, "social_trust": 0.66, "implementation_capacity": 0.70, "coordination": 0.76},
        {"scenario": "fragmented_transition", "public_investment": 0.48, "policy_credibility": 0.32, "technology": 0.64, "social_trust": 0.28, "implementation_capacity": 0.36, "coordination": 0.30},
        {"scenario": "local_polycentric_transition", "public_investment": 0.62, "policy_credibility": 0.62, "technology": 0.58, "social_trust": 0.78, "implementation_capacity": 0.66, "coordination": 0.72},
        {"scenario": "regenerative_state_capacity", "public_investment": 0.82, "policy_credibility": 0.80, "technology": 0.74, "social_trust": 0.76, "implementation_capacity": 0.84, "coordination": 0.82},
    ])


def build_wellbeing_measurement() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "gdp_growth_low_legitimacy", "health": 0.62, "security": 0.48, "inclusion": 0.38, "ecological_quality": 0.32, "public_goods": 0.46, "care": 0.36, "time_balance": 0.34},
        {"scenario": "beyond_gdp_dashboard_state", "health": 0.76, "security": 0.70, "inclusion": 0.68, "ecological_quality": 0.66, "public_goods": 0.74, "care": 0.72, "time_balance": 0.66},
        {"scenario": "green_growth_distribution_gap", "health": 0.70, "security": 0.58, "inclusion": 0.48, "ecological_quality": 0.58, "public_goods": 0.60, "care": 0.54, "time_balance": 0.48},
        {"scenario": "public_goods_sufficiency_model", "health": 0.82, "security": 0.76, "inclusion": 0.78, "ecological_quality": 0.76, "public_goods": 0.84, "care": 0.80, "time_balance": 0.78},
        {"scenario": "austerity_low_output_model", "health": 0.48, "security": 0.34, "inclusion": 0.30, "ecological_quality": 0.58, "public_goods": 0.28, "care": 0.26, "time_balance": 0.42},
    ])


def build_finance_direction() -> pd.DataFrame:
    return pd.DataFrame([
        {"portfolio": "stranded_asset_continuity", "fossil_exposure": 0.86, "resilience_investment": 0.16, "restoration": 0.10, "public_goods_alignment": 0.16, "short_termism": 0.86, "adaptation_finance": 0.14},
        {"portfolio": "green_growth_private_capital", "fossil_exposure": 0.42, "resilience_investment": 0.48, "restoration": 0.34, "public_goods_alignment": 0.36, "short_termism": 0.68, "adaptation_finance": 0.38},
        {"portfolio": "public_resilience_investment", "fossil_exposure": 0.22, "resilience_investment": 0.78, "restoration": 0.62, "public_goods_alignment": 0.84, "short_termism": 0.34, "adaptation_finance": 0.80},
        {"portfolio": "speculative_transition_bubble", "fossil_exposure": 0.34, "resilience_investment": 0.36, "restoration": 0.26, "public_goods_alignment": 0.24, "short_termism": 0.82, "adaptation_finance": 0.30},
        {"portfolio": "regenerative_finance_compact", "fossil_exposure": 0.14, "resilience_investment": 0.84, "restoration": 0.82, "public_goods_alignment": 0.80, "short_termism": 0.26, "adaptation_finance": 0.78},
    ])


def build_circular_repair_systems() -> pd.DataFrame:
    return pd.DataFrame([
        {"system": "linear_high_waste_model", "repairability": 0.18, "reuse": 0.16, "remanufacturing": 0.14, "material_recovery": 0.28, "maintenance_culture": 0.22, "regeneration": 0.12},
        {"system": "recycling_only_model", "repairability": 0.34, "reuse": 0.30, "remanufacturing": 0.26, "material_recovery": 0.62, "maintenance_culture": 0.36, "regeneration": 0.22},
        {"system": "circular_industrial_redesign", "repairability": 0.72, "reuse": 0.70, "remanufacturing": 0.76, "material_recovery": 0.78, "maintenance_culture": 0.68, "regeneration": 0.50},
        {"system": "repair_oriented_public_infrastructure", "repairability": 0.80, "reuse": 0.66, "remanufacturing": 0.62, "material_recovery": 0.70, "maintenance_culture": 0.84, "regeneration": 0.62},
        {"system": "regenerative_circular_system", "repairability": 0.82, "reuse": 0.78, "remanufacturing": 0.80, "material_recovery": 0.82, "maintenance_culture": 0.86, "regeneration": 0.84},
    ])


def build_technology_governance() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "automation_for_private_output", "productivity": 0.82, "distribution": 0.32, "public_purpose": 0.28, "energy_demand_control": 0.30, "labor_transition_support": 0.24, "capability_expansion": 0.44},
        {"scenario": "ai_for_public_capability", "productivity": 0.74, "distribution": 0.70, "public_purpose": 0.82, "energy_demand_control": 0.58, "labor_transition_support": 0.72, "capability_expansion": 0.80},
        {"scenario": "digital_fragility_model", "productivity": 0.68, "distribution": 0.38, "public_purpose": 0.34, "energy_demand_control": 0.26, "labor_transition_support": 0.28, "capability_expansion": 0.42},
        {"scenario": "technology_for_repair_and_resilience", "productivity": 0.66, "distribution": 0.64, "public_purpose": 0.76, "energy_demand_control": 0.70, "labor_transition_support": 0.68, "capability_expansion": 0.74},
        {"scenario": "platform_concentration_model", "productivity": 0.76, "distribution": 0.26, "public_purpose": 0.24, "energy_demand_control": 0.34, "labor_transition_support": 0.20, "capability_expansion": 0.38},
    ])


def build_global_asymmetry() -> pd.DataFrame:
    return pd.DataFrame([
        {"country_group": "high_income_high_footprint", "material_footprint": 0.90, "historic_responsibility": 0.86, "development_need": 0.22, "adaptive_capacity": 0.82, "finance_obligation": 0.86, "basic_needs_gap": 0.12},
        {"country_group": "upper_middle_transitioning", "material_footprint": 0.62, "historic_responsibility": 0.44, "development_need": 0.58, "adaptive_capacity": 0.56, "finance_obligation": 0.46, "basic_needs_gap": 0.38},
        {"country_group": "low_income_development_priority", "material_footprint": 0.18, "historic_responsibility": 0.08, "development_need": 0.90, "adaptive_capacity": 0.24, "finance_obligation": 0.08, "basic_needs_gap": 0.78},
        {"country_group": "climate_vulnerable_low_emitters", "material_footprint": 0.12, "historic_responsibility": 0.04, "development_need": 0.86, "adaptive_capacity": 0.20, "finance_obligation": 0.04, "basic_needs_gap": 0.74},
        {"country_group": "resource_exporting_transition_states", "material_footprint": 0.50, "historic_responsibility": 0.34, "development_need": 0.62, "adaptive_capacity": 0.42, "finance_obligation": 0.34, "basic_needs_gap": 0.46},
    ])


def build_democratic_legitimacy() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "technocratic_transition_without_voice", "fairness": 0.36, "affordability": 0.42, "voice": 0.20, "trust": 0.30, "visible_benefit": 0.34, "policy_stability": 0.44},
        {"scenario": "just_transition_compact", "fairness": 0.78, "affordability": 0.74, "voice": 0.72, "trust": 0.70, "visible_benefit": 0.78, "policy_stability": 0.76},
        {"scenario": "austerity_under_green_targets", "fairness": 0.24, "affordability": 0.28, "voice": 0.30, "trust": 0.22, "visible_benefit": 0.26, "policy_stability": 0.30},
        {"scenario": "local_participatory_transition", "fairness": 0.70, "affordability": 0.68, "voice": 0.84, "trust": 0.76, "visible_benefit": 0.72, "policy_stability": 0.68},
        {"scenario": "polarized_backlash_transition", "fairness": 0.34, "affordability": 0.36, "voice": 0.38, "trust": 0.24, "visible_benefit": 0.28, "policy_stability": 0.22},
    ])


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "future_economic_systems_age_of_limits.sqlite"
    names = [
        "future_viability",
        "throughput_pressure",
        "transition_capacity",
        "wellbeing_measurement",
        "finance_direction",
        "circular_repair_systems",
        "technology_governance",
        "global_asymmetry",
        "democratic_legitimacy",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_future_viability(),
        build_throughput_pressure(),
        build_transition_capacity(),
        build_wellbeing_measurement(),
        build_finance_direction(),
        build_circular_repair_systems(),
        build_technology_governance(),
        build_global_asymmetry(),
        build_democratic_legitimacy(),
    ]

    filenames = [
        "future_viability.csv",
        "throughput_pressure.csv",
        "transition_capacity.csv",
        "wellbeing_measurement.csv",
        "finance_direction.csv",
        "circular_repair_systems.csv",
        "technology_governance.csv",
        "global_asymmetry.csv",
        "democratic_legitimacy.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created future economic systems in an age of limits base data.")


if __name__ == "__main__":
    main()
