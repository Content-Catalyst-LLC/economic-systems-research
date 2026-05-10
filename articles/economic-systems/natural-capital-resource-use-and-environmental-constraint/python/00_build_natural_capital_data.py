"""
Build stylized datasets for natural capital, resource use, and environmental constraint.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_stock_flow_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"system": "old_growth_forest", "natural_capital_t": 100, "regeneration": 2.5, "degradation": 6.8, "threshold": 62, "life_support_importance": 0.90, "irreversibility": 0.74},
        {"system": "managed_forest_regenerative", "natural_capital_t": 100, "regeneration": 5.8, "degradation": 4.2, "threshold": 58, "life_support_importance": 0.78, "irreversibility": 0.42},
        {"system": "groundwater_aquifer_overdrawn", "natural_capital_t": 100, "regeneration": 1.8, "degradation": 7.4, "threshold": 70, "life_support_importance": 0.94, "irreversibility": 0.82},
        {"system": "fishery_with_quota", "natural_capital_t": 100, "regeneration": 6.2, "degradation": 5.0, "threshold": 54, "life_support_importance": 0.70, "irreversibility": 0.46},
        {"system": "soil_fertility_depletion", "natural_capital_t": 100, "regeneration": 2.0, "degradation": 5.6, "threshold": 66, "life_support_importance": 0.92, "irreversibility": 0.66},
        {"system": "wetland_restoration", "natural_capital_t": 100, "regeneration": 6.8, "degradation": 3.2, "threshold": 60, "life_support_importance": 0.86, "irreversibility": 0.48},
    ])


def build_resource_use_constraints() -> pd.DataFrame:
    return pd.DataFrame([
        {"resource": "freshwater_withdrawal", "resource_use": 82, "regenerative_capacity": 64, "emissions": 18, "absorptive_capacity": 22, "social_necessity": 0.94, "substitutability": 0.12},
        {"resource": "timber_harvest", "resource_use": 58, "regenerative_capacity": 52, "emissions": 12, "absorptive_capacity": 18, "social_necessity": 0.58, "substitutability": 0.42},
        {"resource": "wild_fish_harvest", "resource_use": 48, "regenerative_capacity": 44, "emissions": 8, "absorptive_capacity": 12, "social_necessity": 0.64, "substitutability": 0.38},
        {"resource": "fossil_fuel_combustion", "resource_use": 96, "regenerative_capacity": 0.0, "emissions": 92, "absorptive_capacity": 36, "social_necessity": 0.72, "substitutability": 0.58},
        {"resource": "critical_minerals", "resource_use": 70, "regenerative_capacity": 0.0, "emissions": 30, "absorptive_capacity": 28, "social_necessity": 0.76, "substitutability": 0.34},
        {"resource": "soil_nutrient_drawdown", "resource_use": 62, "regenerative_capacity": 38, "emissions": 20, "absorptive_capacity": 18, "social_necessity": 0.90, "substitutability": 0.18},
    ])


def build_sector_resource_pressure() -> pd.DataFrame:
    return pd.DataFrame([
        {"sector": "agriculture_food", "material_intensity": 0.70, "energy_intensity": 0.54, "water_intensity": 0.86, "land_intensity": 0.92, "waste_intensity": 0.48, "import_dependence": 0.34, "social_necessity": 0.96},
        {"sector": "construction_housing", "material_intensity": 0.88, "energy_intensity": 0.66, "water_intensity": 0.38, "land_intensity": 0.72, "waste_intensity": 0.70, "import_dependence": 0.46, "social_necessity": 0.88},
        {"sector": "transport", "material_intensity": 0.60, "energy_intensity": 0.88, "water_intensity": 0.20, "land_intensity": 0.58, "waste_intensity": 0.52, "import_dependence": 0.62, "social_necessity": 0.78},
        {"sector": "mining_minerals", "material_intensity": 0.92, "energy_intensity": 0.82, "water_intensity": 0.64, "land_intensity": 0.76, "waste_intensity": 0.90, "import_dependence": 0.72, "social_necessity": 0.68},
        {"sector": "energy_systems", "material_intensity": 0.74, "energy_intensity": 0.94, "water_intensity": 0.58, "land_intensity": 0.54, "waste_intensity": 0.68, "import_dependence": 0.58, "social_necessity": 0.92},
        {"sector": "care_public_services", "material_intensity": 0.24, "energy_intensity": 0.30, "water_intensity": 0.26, "land_intensity": 0.20, "waste_intensity": 0.24, "import_dependence": 0.18, "social_necessity": 0.92},
    ])


def build_ecosystem_functions() -> pd.DataFrame:
    return pd.DataFrame([
        {"ecosystem": "wetland", "water_filtration": 0.92, "flood_buffering": 0.90, "carbon_storage": 0.68, "habitat_support": 0.86, "soil_protection": 0.62, "pollination_support": 0.48, "market_visibility": 0.22},
        {"ecosystem": "old_growth_forest", "water_filtration": 0.72, "flood_buffering": 0.64, "carbon_storage": 0.94, "habitat_support": 0.96, "soil_protection": 0.84, "pollination_support": 0.62, "market_visibility": 0.34},
        {"ecosystem": "healthy_soil", "water_filtration": 0.70, "flood_buffering": 0.58, "carbon_storage": 0.62, "habitat_support": 0.70, "soil_protection": 0.96, "pollination_support": 0.76, "market_visibility": 0.28},
        {"ecosystem": "river_corridor", "water_filtration": 0.84, "flood_buffering": 0.78, "carbon_storage": 0.42, "habitat_support": 0.82, "soil_protection": 0.64, "pollination_support": 0.44, "market_visibility": 0.30},
        {"ecosystem": "urban_green_space", "water_filtration": 0.50, "flood_buffering": 0.54, "carbon_storage": 0.38, "habitat_support": 0.46, "soil_protection": 0.44, "pollination_support": 0.52, "market_visibility": 0.40},
    ])


def build_governance_regimes() -> pd.DataFrame:
    return pd.DataFrame([
        {"regime": "open_access_extraction", "secure_tenure": 0.18, "monitoring": 0.14, "participation": 0.16, "enforcement": 0.18, "adaptive_rules": 0.16, "equity": 0.20, "regeneration_alignment": 0.18},
        {"regime": "private_property_short_horizon", "secure_tenure": 0.72, "monitoring": 0.50, "participation": 0.22, "enforcement": 0.62, "adaptive_rules": 0.34, "equity": 0.26, "regeneration_alignment": 0.34},
        {"regime": "state_protected_resource", "secure_tenure": 0.70, "monitoring": 0.72, "participation": 0.42, "enforcement": 0.74, "adaptive_rules": 0.56, "equity": 0.48, "regeneration_alignment": 0.68},
        {"regime": "community_commons_governance", "secure_tenure": 0.78, "monitoring": 0.76, "participation": 0.88, "enforcement": 0.70, "adaptive_rules": 0.78, "equity": 0.82, "regeneration_alignment": 0.80},
        {"regime": "polycentric_resource_governance", "secure_tenure": 0.80, "monitoring": 0.84, "participation": 0.76, "enforcement": 0.78, "adaptive_rules": 0.86, "equity": 0.72, "regeneration_alignment": 0.84},
    ])


def build_justice_burdens() -> pd.DataFrame:
    return pd.DataFrame([
        {"group": "extractive_frontier_community", "exposure": 0.86, "income_buffer": 0.24, "public_infrastructure": 0.28, "adaptive_capacity": 0.26, "political_voice": 0.24, "benefit_capture": 0.18},
        {"group": "indigenous_stewardship_territory", "exposure": 0.72, "income_buffer": 0.30, "public_infrastructure": 0.34, "adaptive_capacity": 0.38, "political_voice": 0.34, "benefit_capture": 0.16},
        {"group": "urban_pollution_corridor", "exposure": 0.80, "income_buffer": 0.28, "public_infrastructure": 0.42, "adaptive_capacity": 0.32, "political_voice": 0.30, "benefit_capture": 0.20},
        {"group": "resource_consuming_high_income_group", "exposure": 0.30, "income_buffer": 0.86, "public_infrastructure": 0.78, "adaptive_capacity": 0.82, "political_voice": 0.76, "benefit_capture": 0.84},
        {"group": "future_generations_proxy", "exposure": 0.92, "income_buffer": 0.00, "public_infrastructure": 0.00, "adaptive_capacity": 0.00, "political_voice": 0.00, "benefit_capture": 0.00},
    ])


def build_resilience_dependency() -> pd.DataFrame:
    return pd.DataFrame([
        {"system": "water_security", "diversity": 0.50, "regeneration": 0.38, "redundancy": 0.42, "governance": 0.48, "strategic_reserve": 0.36, "import_dependence": 0.12, "shock_exposure": 0.74},
        {"system": "critical_minerals_supply", "diversity": 0.28, "regeneration": 0.04, "redundancy": 0.32, "governance": 0.46, "strategic_reserve": 0.38, "import_dependence": 0.82, "shock_exposure": 0.70},
        {"system": "regional_food_system", "diversity": 0.58, "regeneration": 0.52, "redundancy": 0.48, "governance": 0.54, "strategic_reserve": 0.42, "import_dependence": 0.46, "shock_exposure": 0.62},
        {"system": "energy_transition_system", "diversity": 0.46, "regeneration": 0.28, "redundancy": 0.44, "governance": 0.58, "strategic_reserve": 0.48, "import_dependence": 0.68, "shock_exposure": 0.66},
        {"system": "forest_watershed_system", "diversity": 0.72, "regeneration": 0.68, "redundancy": 0.64, "governance": 0.70, "strategic_reserve": 0.60, "import_dependence": 0.08, "shock_exposure": 0.48},
    ])


def build_substitution_efficiency() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "efficiency_with_rebound", "efficiency_gain": 0.24, "rebound_effect": 0.18, "substitution_feasibility": 0.60, "ecological_irreplaceability": 0.52, "absolute_reduction": 0.08, "innovation_quality": 0.58},
        {"scenario": "absolute_demand_reduction", "efficiency_gain": 0.16, "rebound_effect": 0.02, "substitution_feasibility": 0.48, "ecological_irreplaceability": 0.70, "absolute_reduction": 0.34, "innovation_quality": 0.56},
        {"scenario": "material_substitution_shifted_burden", "efficiency_gain": 0.18, "rebound_effect": 0.10, "substitution_feasibility": 0.72, "ecological_irreplaceability": 0.58, "absolute_reduction": 0.04, "innovation_quality": 0.44},
        {"scenario": "repair_reuse_sufficiency", "efficiency_gain": 0.20, "rebound_effect": 0.04, "substitution_feasibility": 0.54, "ecological_irreplaceability": 0.64, "absolute_reduction": 0.30, "innovation_quality": 0.70},
        {"scenario": "techno_optimist_no_scale_governance", "efficiency_gain": 0.26, "rebound_effect": 0.22, "substitution_feasibility": 0.78, "ecological_irreplaceability": 0.66, "absolute_reduction": 0.02, "innovation_quality": 0.52},
    ])


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "natural_capital_resource_constraint.sqlite"
    names = [
        "stock_flow_scenarios",
        "resource_use_constraints",
        "sector_resource_pressure",
        "ecosystem_functions",
        "governance_regimes",
        "justice_burdens",
        "resilience_dependency",
        "substitution_efficiency",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_stock_flow_scenarios(),
        build_resource_use_constraints(),
        build_sector_resource_pressure(),
        build_ecosystem_functions(),
        build_governance_regimes(),
        build_justice_burdens(),
        build_resilience_dependency(),
        build_substitution_efficiency(),
    ]

    filenames = [
        "stock_flow_scenarios.csv",
        "resource_use_constraints.csv",
        "sector_resource_pressure.csv",
        "ecosystem_functions.csv",
        "governance_regimes.csv",
        "justice_burdens.csv",
        "resilience_dependency.csv",
        "substitution_efficiency.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created natural capital, resource use, and environmental constraint base data.")


if __name__ == "__main__":
    main()
