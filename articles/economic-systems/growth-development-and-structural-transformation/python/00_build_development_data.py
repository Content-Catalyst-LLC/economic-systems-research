"""
Build stylized datasets for growth, development, and structural transformation.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_growth_path_scenarios() -> pd.DataFrame:
    rows = []
    paths = {
        "extractive_growth_without_development": [100, 108, 116, 122, 120, 114],
        "broad_based_productivity_growth": [100, 105, 111, 118, 126, 135],
        "debt_fueled_consumption_growth": [100, 106, 113, 119, 117, 110],
        "industrial_upgrading_path": [100, 104, 111, 121, 134, 150],
        "premature_deindustrialization_path": [100, 103, 106, 108, 108, 107],
        "sustainable_transformation_path": [100, 104, 110, 117, 125, 134],
    }
    labor_paths = {
        "extractive_growth_without_development": [100, 101, 102, 103, 103, 102],
        "broad_based_productivity_growth": [100, 102, 104, 106, 108, 110],
        "debt_fueled_consumption_growth": [100, 102, 104, 105, 104, 102],
        "industrial_upgrading_path": [100, 101, 103, 106, 109, 112],
        "premature_deindustrialization_path": [100, 103, 106, 109, 111, 112],
        "sustainable_transformation_path": [100, 102, 104, 106, 108, 110],
    }
    for scenario, outputs in paths.items():
        for period, output in enumerate(outputs):
            rows.append({"scenario": scenario, "period": period, "output": output, "labor": labor_paths[scenario][period]})
    return pd.DataFrame(rows)


def build_sector_transformation_scenarios() -> pd.DataFrame:
    rows = []
    scenarios = {
        "agrarian_low_productivity": {
            "agriculture": (260, 520),
            "industry": (210, 145),
            "services": (310, 260),
            "knowledge_services": (40, 25),
        },
        "industrializing_transition": {
            "agriculture": (210, 390),
            "industry": (420, 255),
            "services": (380, 285),
            "knowledge_services": (95, 55),
        },
        "premature_service_shift": {
            "agriculture": (170, 280),
            "industry": (260, 170),
            "services": (520, 470),
            "knowledge_services": (80, 65),
        },
        "industrial_upgrading": {
            "agriculture": (135, 205),
            "industry": (560, 265),
            "services": (470, 300),
            "knowledge_services": (190, 85),
        },
        "knowledge_resilience_path": {
            "agriculture": (145, 185),
            "industry": (470, 220),
            "services": (520, 300),
            "knowledge_services": (280, 115),
        },
    }
    for scenario, sectors in scenarios.items():
        for sector, values in sectors.items():
            output, labor = values
            rows.append({"scenario": scenario, "sector": sector, "sector_output": output, "sector_labor": labor})
    return pd.DataFrame(rows)


def build_development_capability_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "growth_without_public_capacity", "income_index": 0.62, "health_index": 0.48, "education_index": 0.50, "infrastructure_index": 0.44, "security_index": 0.46},
        {"scenario": "human_capability_buildout", "income_index": 0.66, "health_index": 0.74, "education_index": 0.78, "infrastructure_index": 0.68, "security_index": 0.70},
        {"scenario": "industrial_upgrading_with_inclusion", "income_index": 0.72, "health_index": 0.70, "education_index": 0.76, "infrastructure_index": 0.78, "security_index": 0.72},
        {"scenario": "commodity_boom_weak_institutions", "income_index": 0.70, "health_index": 0.52, "education_index": 0.48, "infrastructure_index": 0.50, "security_index": 0.44},
        {"scenario": "sustainable_capability_path", "income_index": 0.74, "health_index": 0.78, "education_index": 0.82, "infrastructure_index": 0.84, "security_index": 0.78},
    ])


def build_urban_infrastructure_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "unplanned_urbanization", "urbanization_rate": 0.62, "infrastructure_depth": 0.42, "housing_access": 0.38, "transit_access": 0.34, "spatial_inclusion": 0.36},
        {"scenario": "infrastructure_led_integration", "urbanization_rate": 0.58, "infrastructure_depth": 0.76, "housing_access": 0.68, "transit_access": 0.72, "spatial_inclusion": 0.74},
        {"scenario": "metro_core_concentration", "urbanization_rate": 0.70, "infrastructure_depth": 0.64, "housing_access": 0.44, "transit_access": 0.60, "spatial_inclusion": 0.46},
        {"scenario": "secondary_city_network", "urbanization_rate": 0.56, "infrastructure_depth": 0.70, "housing_access": 0.66, "transit_access": 0.64, "spatial_inclusion": 0.76},
        {"scenario": "rural_urban_disconnect", "urbanization_rate": 0.48, "infrastructure_depth": 0.40, "housing_access": 0.52, "transit_access": 0.28, "spatial_inclusion": 0.34},
    ])


def build_trade_export_diversification_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "commodity_dependence", "export_concentration": 0.82, "manufacturing_export_share": 0.14, "technology_depth": 0.22, "terms_of_trade_volatility": 0.70, "foreign_exchange_resilience": 0.30},
        {"scenario": "basic_manufacturing_export_path", "export_concentration": 0.48, "manufacturing_export_share": 0.46, "technology_depth": 0.42, "terms_of_trade_volatility": 0.42, "foreign_exchange_resilience": 0.52},
        {"scenario": "industrial_diversification", "export_concentration": 0.32, "manufacturing_export_share": 0.56, "technology_depth": 0.66, "terms_of_trade_volatility": 0.28, "foreign_exchange_resilience": 0.70},
        {"scenario": "knowledge_service_exports", "export_concentration": 0.36, "manufacturing_export_share": 0.34, "technology_depth": 0.74, "terms_of_trade_volatility": 0.24, "foreign_exchange_resilience": 0.68},
        {"scenario": "low_value_assembly_lock_in", "export_concentration": 0.54, "manufacturing_export_share": 0.52, "technology_depth": 0.30, "terms_of_trade_volatility": 0.46, "foreign_exchange_resilience": 0.44},
    ])


def build_inequality_inclusion_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "elite_growth_mass_precarity", "gini_index": 0.58, "informal_labor_share": 0.54, "education_access": 0.44, "health_access": 0.50, "regional_inclusion": 0.36},
        {"scenario": "inclusive_productivity_path", "gini_index": 0.34, "informal_labor_share": 0.22, "education_access": 0.78, "health_access": 0.80, "regional_inclusion": 0.72},
        {"scenario": "urban_dualism", "gini_index": 0.50, "informal_labor_share": 0.46, "education_access": 0.58, "health_access": 0.62, "regional_inclusion": 0.40},
        {"scenario": "social_capability_state", "gini_index": 0.30, "informal_labor_share": 0.18, "education_access": 0.84, "health_access": 0.86, "regional_inclusion": 0.78},
        {"scenario": "growth_without_labor_absorption", "gini_index": 0.52, "informal_labor_share": 0.50, "education_access": 0.60, "health_access": 0.64, "regional_inclusion": 0.46},
    ])


def build_energy_ecology_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "fossil_intensive_growth", "output": 1250, "energy_use": 840, "emissions": 620, "renewable_share": 0.18, "resource_stress": 0.72},
        {"scenario": "efficiency_led_growth", "output": 1220, "energy_use": 610, "emissions": 390, "renewable_share": 0.42, "resource_stress": 0.44},
        {"scenario": "industrial_upgrade_high_energy", "output": 1360, "energy_use": 760, "emissions": 500, "renewable_share": 0.32, "resource_stress": 0.58},
        {"scenario": "green_structural_transformation", "output": 1320, "energy_use": 560, "emissions": 260, "renewable_share": 0.68, "resource_stress": 0.30},
        {"scenario": "extractive_export_path", "output": 1180, "energy_use": 720, "emissions": 540, "renewable_share": 0.20, "resource_stress": 0.78},
    ])


def build_debt_fragility_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "domestic_long_term_finance", "external_debt_ratio": 0.22, "fx_debt_share": 0.16, "short_term_debt_share": 0.18, "export_concentration": 0.34, "reserve_buffer": 0.72, "productivity_momentum": 0.70},
        {"scenario": "external_debt_growth_model", "external_debt_ratio": 0.62, "fx_debt_share": 0.58, "short_term_debt_share": 0.42, "export_concentration": 0.62, "reserve_buffer": 0.38, "productivity_momentum": 0.44},
        {"scenario": "commodity_debt_cycle", "external_debt_ratio": 0.54, "fx_debt_share": 0.52, "short_term_debt_share": 0.36, "export_concentration": 0.82, "reserve_buffer": 0.42, "productivity_momentum": 0.34},
        {"scenario": "middle_income_productivity_slowdown", "external_debt_ratio": 0.38, "fx_debt_share": 0.32, "short_term_debt_share": 0.30, "export_concentration": 0.46, "reserve_buffer": 0.50, "productivity_momentum": 0.24},
        {"scenario": "resilient_developmental_finance", "external_debt_ratio": 0.28, "fx_debt_share": 0.20, "short_term_debt_share": 0.16, "export_concentration": 0.28, "reserve_buffer": 0.76, "productivity_momentum": 0.78},
    ])


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "growth_development_structural_transformation.sqlite"
    names = [
        "growth_path_scenarios",
        "sector_transformation_scenarios",
        "development_capability_scenarios",
        "urban_infrastructure_scenarios",
        "trade_export_diversification_scenarios",
        "inequality_inclusion_scenarios",
        "energy_ecology_scenarios",
        "debt_fragility_scenarios",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_growth_path_scenarios(),
        build_sector_transformation_scenarios(),
        build_development_capability_scenarios(),
        build_urban_infrastructure_scenarios(),
        build_trade_export_diversification_scenarios(),
        build_inequality_inclusion_scenarios(),
        build_energy_ecology_scenarios(),
        build_debt_fragility_scenarios(),
    ]
    filenames = [
        "growth_path_scenarios.csv",
        "sector_transformation_scenarios.csv",
        "development_capability_scenarios.csv",
        "urban_infrastructure_scenarios.csv",
        "trade_export_diversification_scenarios.csv",
        "inequality_inclusion_scenarios.csv",
        "energy_ecology_scenarios.csv",
        "debt_fragility_scenarios.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created growth, development, and structural transformation base data.")


if __name__ == "__main__":
    main()
