"""
Build stylized datasets for ecological economics and the embedded economy.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_throughput_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "fossil_growth_high_throughput", "energy_input": 620, "material_input": 540, "recovered_throughput": 160, "economic_scale": 1.18, "ecological_capacity": 0.74, "wellbeing_index": 0.62},
        {"scenario": "efficiency_rebound_growth", "energy_input": 520, "material_input": 470, "recovered_throughput": 210, "economic_scale": 1.08, "ecological_capacity": 0.78, "wellbeing_index": 0.66},
        {"scenario": "renewable_transition_material_intensive", "energy_input": 450, "material_input": 610, "recovered_throughput": 260, "economic_scale": 0.96, "ecological_capacity": 0.82, "wellbeing_index": 0.70},
        {"scenario": "circular_economy_high_recovery", "energy_input": 380, "material_input": 340, "recovered_throughput": 280, "economic_scale": 0.82, "ecological_capacity": 0.86, "wellbeing_index": 0.76},
        {"scenario": "steady_state_sufficiency", "energy_input": 310, "material_input": 270, "recovered_throughput": 210, "economic_scale": 0.70, "ecological_capacity": 0.88, "wellbeing_index": 0.78},
        {"scenario": "austerity_low_throughput_low_wellbeing", "energy_input": 260, "material_input": 240, "recovered_throughput": 110, "economic_scale": 0.58, "ecological_capacity": 0.80, "wellbeing_index": 0.42},
    ])


def build_sector_footprints() -> pd.DataFrame:
    return pd.DataFrame([
        {"sector": "food_systems", "domestic_extraction": 180, "imports": 90, "exports": 40, "energy_intensity": 0.58, "water_pressure": 0.72, "land_pressure": 0.84, "waste_intensity": 0.46, "social_necessity": 0.94},
        {"sector": "housing_built_environment", "domestic_extraction": 260, "imports": 140, "exports": 20, "energy_intensity": 0.70, "water_pressure": 0.38, "land_pressure": 0.76, "waste_intensity": 0.64, "social_necessity": 0.88},
        {"sector": "transport_mobility", "domestic_extraction": 150, "imports": 180, "exports": 50, "energy_intensity": 0.86, "water_pressure": 0.22, "land_pressure": 0.58, "waste_intensity": 0.50, "social_necessity": 0.76},
        {"sector": "manufacturing_industry", "domestic_extraction": 320, "imports": 260, "exports": 210, "energy_intensity": 0.82, "water_pressure": 0.54, "land_pressure": 0.40, "waste_intensity": 0.72, "social_necessity": 0.64},
        {"sector": "digital_infrastructure", "domestic_extraction": 80, "imports": 210, "exports": 35, "energy_intensity": 0.74, "water_pressure": 0.46, "land_pressure": 0.22, "waste_intensity": 0.58, "social_necessity": 0.68},
        {"sector": "care_public_services", "domestic_extraction": 55, "imports": 45, "exports": 5, "energy_intensity": 0.28, "water_pressure": 0.20, "land_pressure": 0.18, "waste_intensity": 0.22, "social_necessity": 0.92},
    ])


def build_ecological_burdens() -> pd.DataFrame:
    return pd.DataFrame([
        {"group": "low_income_urban_households", "exposure": 0.78, "income_buffer": 0.22, "infrastructure": 0.38, "adaptive_capacity": 0.26, "historical_responsibility": 0.18, "political_voice": 0.30},
        {"group": "rural_smallholders", "exposure": 0.72, "income_buffer": 0.28, "infrastructure": 0.34, "adaptive_capacity": 0.32, "historical_responsibility": 0.14, "political_voice": 0.34},
        {"group": "coastal_communities", "exposure": 0.84, "income_buffer": 0.36, "infrastructure": 0.44, "adaptive_capacity": 0.38, "historical_responsibility": 0.20, "political_voice": 0.42},
        {"group": "industrial_workers_transition_region", "exposure": 0.62, "income_buffer": 0.40, "infrastructure": 0.52, "adaptive_capacity": 0.44, "historical_responsibility": 0.34, "political_voice": 0.46},
        {"group": "high_income_asset_owners", "exposure": 0.32, "income_buffer": 0.86, "infrastructure": 0.78, "adaptive_capacity": 0.82, "historical_responsibility": 0.76, "political_voice": 0.72},
        {"group": "future_generations_proxy", "exposure": 0.90, "income_buffer": 0.00, "infrastructure": 0.00, "adaptive_capacity": 0.00, "historical_responsibility": 0.00, "political_voice": 0.00},
    ])


def build_embeddedness_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "disembedded_market_order", "ecology_integrity": 0.32, "care_capacity": 0.28, "public_institutions": 0.34, "infrastructure_maintenance": 0.30, "cultural_reciprocity": 0.26, "market_dependence": 0.84, "community_resilience": 0.28},
        {"scenario": "welfare_embedded_economy", "ecology_integrity": 0.58, "care_capacity": 0.72, "public_institutions": 0.76, "infrastructure_maintenance": 0.70, "cultural_reciprocity": 0.62, "market_dependence": 0.48, "community_resilience": 0.68},
        {"scenario": "commons_oriented_localism", "ecology_integrity": 0.74, "care_capacity": 0.68, "public_institutions": 0.58, "infrastructure_maintenance": 0.54, "cultural_reciprocity": 0.82, "market_dependence": 0.36, "community_resilience": 0.78},
        {"scenario": "extractive_growth_regime", "ecology_integrity": 0.24, "care_capacity": 0.34, "public_institutions": 0.38, "infrastructure_maintenance": 0.36, "cultural_reciprocity": 0.30, "market_dependence": 0.78, "community_resilience": 0.32},
        {"scenario": "just_transition_embedded_system", "ecology_integrity": 0.76, "care_capacity": 0.78, "public_institutions": 0.80, "infrastructure_maintenance": 0.76, "cultural_reciprocity": 0.70, "market_dependence": 0.42, "community_resilience": 0.78},
    ])


def build_resilience_commons() -> pd.DataFrame:
    return pd.DataFrame([
        {"system": "unmanaged_open_access", "diversity": 0.32, "redundancy": 0.24, "regeneration": 0.22, "governance": 0.18, "maintenance": 0.20, "learning": 0.22, "monitoring": 0.16, "participation": 0.18},
        {"system": "privatized_extraction", "diversity": 0.28, "redundancy": 0.30, "regeneration": 0.24, "governance": 0.36, "maintenance": 0.32, "learning": 0.34, "monitoring": 0.42, "participation": 0.22},
        {"system": "state_protected_conservation", "diversity": 0.70, "redundancy": 0.62, "regeneration": 0.72, "governance": 0.66, "maintenance": 0.68, "learning": 0.56, "monitoring": 0.72, "participation": 0.44},
        {"system": "community_commons_governance", "diversity": 0.76, "redundancy": 0.70, "regeneration": 0.78, "governance": 0.80, "maintenance": 0.74, "learning": 0.76, "monitoring": 0.70, "participation": 0.84},
        {"system": "polycentric_adaptive_governance", "diversity": 0.82, "redundancy": 0.78, "regeneration": 0.80, "governance": 0.86, "maintenance": 0.78, "learning": 0.84, "monitoring": 0.82, "participation": 0.78},
    ])


def build_postgrowth_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "business_as_usual_growth", "gdp_growth": 0.032, "throughput_growth": 0.026, "efficiency_gain": 0.010, "rebound_effect": 0.018, "wellbeing_change": 0.006, "inequality_pressure": 0.62, "public_services": 0.46},
        {"scenario": "green_growth_efficiency", "gdp_growth": 0.026, "throughput_growth": 0.004, "efficiency_gain": 0.030, "rebound_effect": 0.014, "wellbeing_change": 0.012, "inequality_pressure": 0.48, "public_services": 0.58},
        {"scenario": "steady_state_high_welfare", "gdp_growth": 0.004, "throughput_growth": -0.010, "efficiency_gain": 0.018, "rebound_effect": 0.006, "wellbeing_change": 0.014, "inequality_pressure": 0.30, "public_services": 0.76},
        {"scenario": "planned_degrowth_sufficiency", "gdp_growth": -0.008, "throughput_growth": -0.038, "efficiency_gain": 0.016, "rebound_effect": 0.002, "wellbeing_change": 0.010, "inequality_pressure": 0.26, "public_services": 0.82},
        {"scenario": "austerity_contraction", "gdp_growth": -0.020, "throughput_growth": -0.018, "efficiency_gain": 0.004, "rebound_effect": 0.000, "wellbeing_change": -0.036, "inequality_pressure": 0.74, "public_services": 0.28},
    ])


def build_strong_sustainability() -> pd.DataFrame:
    return pd.DataFrame([
        {"system": "climate_stability", "substitutability": 0.08, "threshold_risk": 0.92, "irreversibility": 0.86, "regeneration_rate": 0.18, "life_support_importance": 0.96},
        {"system": "freshwater_aquifers", "substitutability": 0.18, "threshold_risk": 0.76, "irreversibility": 0.72, "regeneration_rate": 0.26, "life_support_importance": 0.92},
        {"system": "pollinator_systems", "substitutability": 0.24, "threshold_risk": 0.78, "irreversibility": 0.68, "regeneration_rate": 0.34, "life_support_importance": 0.86},
        {"system": "fertile_soils", "substitutability": 0.22, "threshold_risk": 0.74, "irreversibility": 0.62, "regeneration_rate": 0.30, "life_support_importance": 0.90},
        {"system": "critical_minerals", "substitutability": 0.44, "threshold_risk": 0.54, "irreversibility": 0.42, "regeneration_rate": 0.04, "life_support_importance": 0.58},
        {"system": "urban_green_space", "substitutability": 0.50, "threshold_risk": 0.42, "irreversibility": 0.32, "regeneration_rate": 0.58, "life_support_importance": 0.54},
    ])


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "ecological_economics_embedded_economy.sqlite"
    names = [
        "throughput_scenarios",
        "sector_footprints",
        "ecological_burdens",
        "embeddedness_scenarios",
        "resilience_commons",
        "postgrowth_scenarios",
        "strong_sustainability",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_throughput_scenarios(),
        build_sector_footprints(),
        build_ecological_burdens(),
        build_embeddedness_scenarios(),
        build_resilience_commons(),
        build_postgrowth_scenarios(),
        build_strong_sustainability(),
    ]

    filenames = [
        "throughput_scenarios.csv",
        "sector_footprints.csv",
        "ecological_burdens.csv",
        "embeddedness_scenarios.csv",
        "resilience_commons.csv",
        "postgrowth_scenarios.csv",
        "strong_sustainability.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created ecological economics and embedded economy base data.")


if __name__ == "__main__":
    main()
