"""
Build stylized datasets for economic systems within planetary boundaries.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_boundary_pressure() -> pd.DataFrame:
    return pd.DataFrame([
        {"boundary": "climate_change", "economic_pressure": 1.42, "earth_system_capacity": 1.00, "irreversibility": 0.84, "system_connectivity": 0.92, "policy_response": 0.56},
        {"boundary": "biosphere_integrity", "economic_pressure": 1.68, "earth_system_capacity": 1.00, "irreversibility": 0.90, "system_connectivity": 0.94, "policy_response": 0.38},
        {"boundary": "land_system_change", "economic_pressure": 1.25, "earth_system_capacity": 1.00, "irreversibility": 0.70, "system_connectivity": 0.82, "policy_response": 0.42},
        {"boundary": "freshwater_change", "economic_pressure": 1.22, "earth_system_capacity": 1.00, "irreversibility": 0.68, "system_connectivity": 0.78, "policy_response": 0.44},
        {"boundary": "biogeochemical_flows", "economic_pressure": 1.80, "earth_system_capacity": 1.00, "irreversibility": 0.74, "system_connectivity": 0.86, "policy_response": 0.32},
        {"boundary": "novel_entities", "economic_pressure": 1.55, "earth_system_capacity": 1.00, "irreversibility": 0.82, "system_connectivity": 0.76, "policy_response": 0.26},
        {"boundary": "ocean_acidification", "economic_pressure": 0.86, "earth_system_capacity": 1.00, "irreversibility": 0.72, "system_connectivity": 0.80, "policy_response": 0.48},
        {"boundary": "stratospheric_ozone", "economic_pressure": 0.42, "earth_system_capacity": 1.00, "irreversibility": 0.62, "system_connectivity": 0.54, "policy_response": 0.84},
        {"boundary": "atmospheric_aerosol_loading", "economic_pressure": 0.78, "earth_system_capacity": 1.00, "irreversibility": 0.56, "system_connectivity": 0.70, "policy_response": 0.46},
    ])


def build_resource_use_identity() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "high_income_high_intensity", "population": 100, "affluence": 2.6, "resource_intensity": 0.82, "wellbeing_index": 0.74, "distribution_quality": 0.42},
        {"scenario": "high_income_efficiency_only", "population": 100, "affluence": 2.8, "resource_intensity": 0.58, "wellbeing_index": 0.76, "distribution_quality": 0.46},
        {"scenario": "sufficiency_high_wellbeing", "population": 100, "affluence": 1.8, "resource_intensity": 0.42, "wellbeing_index": 0.80, "distribution_quality": 0.76},
        {"scenario": "low_income_development_need", "population": 100, "affluence": 0.8, "resource_intensity": 0.52, "wellbeing_index": 0.46, "distribution_quality": 0.50},
        {"scenario": "inclusive_green_development", "population": 100, "affluence": 1.3, "resource_intensity": 0.36, "wellbeing_index": 0.70, "distribution_quality": 0.72},
    ])


def build_sector_pressure() -> pd.DataFrame:
    return pd.DataFrame([
        {"sector": "energy_systems", "climate": 0.90, "biosphere": 0.42, "land": 0.46, "freshwater": 0.40, "nutrients": 0.24, "novel_entities": 0.36, "social_necessity": 0.92, "transition_readiness": 0.62},
        {"sector": "food_agriculture", "climate": 0.62, "biosphere": 0.86, "land": 0.88, "freshwater": 0.78, "nutrients": 0.90, "novel_entities": 0.54, "social_necessity": 0.96, "transition_readiness": 0.46},
        {"sector": "materials_industry", "climate": 0.76, "biosphere": 0.58, "land": 0.62, "freshwater": 0.54, "nutrients": 0.34, "novel_entities": 0.76, "social_necessity": 0.78, "transition_readiness": 0.42},
        {"sector": "transport_mobility", "climate": 0.78, "biosphere": 0.36, "land": 0.50, "freshwater": 0.22, "nutrients": 0.10, "novel_entities": 0.32, "social_necessity": 0.74, "transition_readiness": 0.56},
        {"sector": "housing_built_environment", "climate": 0.66, "biosphere": 0.44, "land": 0.70, "freshwater": 0.40, "nutrients": 0.18, "novel_entities": 0.46, "social_necessity": 0.88, "transition_readiness": 0.52},
        {"sector": "public_health_and_care", "climate": 0.24, "biosphere": 0.18, "land": 0.16, "freshwater": 0.20, "nutrients": 0.08, "novel_entities": 0.20, "social_necessity": 0.94, "transition_readiness": 0.70},
    ])


def build_coupled_systems() -> pd.DataFrame:
    return pd.DataFrame([
        {"system": "energy_food_land_water", "energy_pressure": 0.72, "food_pressure": 0.86, "land_pressure": 0.82, "water_pressure": 0.78, "governance_integration": 0.38, "adaptation_capacity": 0.44},
        {"system": "urban_growth_transport_heat", "energy_pressure": 0.68, "food_pressure": 0.28, "land_pressure": 0.70, "water_pressure": 0.52, "governance_integration": 0.46, "adaptation_capacity": 0.50},
        {"system": "industrial_minerals_energy_waste", "energy_pressure": 0.82, "food_pressure": 0.12, "land_pressure": 0.58, "water_pressure": 0.56, "governance_integration": 0.42, "adaptation_capacity": 0.48},
        {"system": "regenerative_regional_system", "energy_pressure": 0.34, "food_pressure": 0.42, "land_pressure": 0.38, "water_pressure": 0.36, "governance_integration": 0.76, "adaptation_capacity": 0.74},
        {"system": "fragmented_policy_transition", "energy_pressure": 0.58, "food_pressure": 0.64, "land_pressure": 0.66, "water_pressure": 0.60, "governance_integration": 0.28, "adaptation_capacity": 0.36},
    ])


def build_ecological_space_justice() -> pd.DataFrame:
    return pd.DataFrame([
        {"group": "high_income_high_throughput", "resource_claim": 0.90, "historic_pressure": 0.86, "development_need": 0.24, "adaptive_capacity": 0.82, "harm_exposure": 0.32, "voice": 0.78},
        {"group": "middle_income_transitioning", "resource_claim": 0.58, "historic_pressure": 0.42, "development_need": 0.60, "adaptive_capacity": 0.54, "harm_exposure": 0.58, "voice": 0.52},
        {"group": "low_income_development_priority", "resource_claim": 0.20, "historic_pressure": 0.10, "development_need": 0.88, "adaptive_capacity": 0.24, "harm_exposure": 0.82, "voice": 0.30},
        {"group": "indigenous_and_local_stewards", "resource_claim": 0.22, "historic_pressure": 0.08, "development_need": 0.62, "adaptive_capacity": 0.46, "harm_exposure": 0.70, "voice": 0.26},
        {"group": "future_generations_proxy", "resource_claim": 0.00, "historic_pressure": 0.00, "development_need": 0.92, "adaptive_capacity": 0.00, "harm_exposure": 0.94, "voice": 0.00},
    ])


def build_transition_capacity() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "target_rich_capacity_poor", "state_capacity": 0.38, "public_investment": 0.36, "social_legitimacy": 0.34, "technological_capability": 0.62, "coordination": 0.30, "adaptive_governance": 0.28},
        {"scenario": "market_led_efficiency", "state_capacity": 0.44, "public_investment": 0.32, "social_legitimacy": 0.42, "technological_capability": 0.74, "coordination": 0.38, "adaptive_governance": 0.36},
        {"scenario": "public_transition_compact", "state_capacity": 0.78, "public_investment": 0.82, "social_legitimacy": 0.76, "technological_capability": 0.72, "coordination": 0.80, "adaptive_governance": 0.74},
        {"scenario": "local_resilience_polycentric", "state_capacity": 0.66, "public_investment": 0.62, "social_legitimacy": 0.82, "technological_capability": 0.58, "coordination": 0.70, "adaptive_governance": 0.84},
        {"scenario": "fragmented_low_trust_transition", "state_capacity": 0.34, "public_investment": 0.38, "social_legitimacy": 0.24, "technological_capability": 0.52, "coordination": 0.24, "adaptive_governance": 0.30},
    ])


def build_finance_direction() -> pd.DataFrame:
    return pd.DataFrame([
        {"portfolio": "legacy_extraction_reinforcement", "fossil_exposure": 0.82, "restoration_investment": 0.12, "resilience_investment": 0.18, "circular_materials": 0.14, "public_goods_alignment": 0.18, "short_term_return_pressure": 0.88},
        {"portfolio": "green_growth_without_scale", "fossil_exposure": 0.42, "restoration_investment": 0.36, "resilience_investment": 0.42, "circular_materials": 0.48, "public_goods_alignment": 0.34, "short_term_return_pressure": 0.70},
        {"portfolio": "boundary_aware_development", "fossil_exposure": 0.18, "restoration_investment": 0.74, "resilience_investment": 0.78, "circular_materials": 0.72, "public_goods_alignment": 0.80, "short_term_return_pressure": 0.30},
        {"portfolio": "adaptation_and_public_infrastructure", "fossil_exposure": 0.24, "restoration_investment": 0.62, "resilience_investment": 0.84, "circular_materials": 0.58, "public_goods_alignment": 0.86, "short_term_return_pressure": 0.38},
        {"portfolio": "speculative_transition_bubble", "fossil_exposure": 0.30, "restoration_investment": 0.28, "resilience_investment": 0.34, "circular_materials": 0.40, "public_goods_alignment": 0.24, "short_term_return_pressure": 0.82},
    ])


def build_boundary_accounting() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "gdp_growth_high_overshoot", "gdp_growth": 0.034, "wellbeing": 0.62, "material_throughput": 0.86, "ecological_pressure": 0.88, "natural_capital": 0.38, "inclusion": 0.44},
        {"scenario": "low_growth_high_wellbeing", "gdp_growth": 0.012, "wellbeing": 0.78, "material_throughput": 0.44, "ecological_pressure": 0.36, "natural_capital": 0.74, "inclusion": 0.76},
        {"scenario": "green_efficiency_rebound", "gdp_growth": 0.028, "wellbeing": 0.68, "material_throughput": 0.72, "ecological_pressure": 0.66, "natural_capital": 0.54, "inclusion": 0.58},
        {"scenario": "inclusive_boundary_aware_transition", "gdp_growth": 0.020, "wellbeing": 0.80, "material_throughput": 0.40, "ecological_pressure": 0.32, "natural_capital": 0.78, "inclusion": 0.80},
        {"scenario": "austerity_low_output_weak_resilience", "gdp_growth": -0.006, "wellbeing": 0.46, "material_throughput": 0.38, "ecological_pressure": 0.42, "natural_capital": 0.60, "inclusion": 0.34},
    ])


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "economic_systems_within_planetary_boundaries.sqlite"
    names = [
        "boundary_pressure",
        "resource_use_identity",
        "sector_pressure",
        "coupled_systems",
        "ecological_space_justice",
        "transition_capacity",
        "finance_direction",
        "boundary_accounting",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_boundary_pressure(),
        build_resource_use_identity(),
        build_sector_pressure(),
        build_coupled_systems(),
        build_ecological_space_justice(),
        build_transition_capacity(),
        build_finance_direction(),
        build_boundary_accounting(),
    ]

    filenames = [
        "boundary_pressure.csv",
        "resource_use_identity.csv",
        "sector_pressure.csv",
        "coupled_systems.csv",
        "ecological_space_justice.csv",
        "transition_capacity.csv",
        "finance_direction.csv",
        "boundary_accounting.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created economic systems within planetary boundaries base data.")


if __name__ == "__main__":
    main()
