"""
Build stylized datasets for inequality, redistribution, and social mobility.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_income_distribution() -> pd.DataFrame:
    return pd.DataFrame([
        {"group": "decile_1", "population_share": 0.10, "market_income": 12, "taxes": 1, "transfers": 9, "public_service_value": 12, "housing_cost": 10, "debt_service": 2},
        {"group": "decile_2", "population_share": 0.10, "market_income": 22, "taxes": 2, "transfers": 8, "public_service_value": 11, "housing_cost": 12, "debt_service": 3},
        {"group": "decile_3", "population_share": 0.10, "market_income": 32, "taxes": 4, "transfers": 7, "public_service_value": 10, "housing_cost": 14, "debt_service": 4},
        {"group": "decile_4", "population_share": 0.10, "market_income": 43, "taxes": 6, "transfers": 5, "public_service_value": 9, "housing_cost": 16, "debt_service": 5},
        {"group": "decile_5", "population_share": 0.10, "market_income": 55, "taxes": 8, "transfers": 4, "public_service_value": 8, "housing_cost": 18, "debt_service": 5},
        {"group": "decile_6", "population_share": 0.10, "market_income": 70, "taxes": 12, "transfers": 3, "public_service_value": 7, "housing_cost": 20, "debt_service": 6},
        {"group": "decile_7", "population_share": 0.10, "market_income": 90, "taxes": 17, "transfers": 2, "public_service_value": 6, "housing_cost": 24, "debt_service": 7},
        {"group": "decile_8", "population_share": 0.10, "market_income": 120, "taxes": 26, "transfers": 1, "public_service_value": 5, "housing_cost": 30, "debt_service": 8},
        {"group": "decile_9", "population_share": 0.10, "market_income": 175, "taxes": 44, "transfers": 0, "public_service_value": 4, "housing_cost": 38, "debt_service": 10},
        {"group": "decile_10", "population_share": 0.10, "market_income": 420, "taxes": 118, "transfers": 0, "public_service_value": 3, "housing_cost": 68, "debt_service": 16},
    ])


def build_wealth_distribution() -> pd.DataFrame:
    return pd.DataFrame([
        {"group": "bottom_50", "population_share": 0.50, "wealth": 65, "debt": 48, "inheritance_receipts": 4, "asset_return": 0.02, "housing_ownership": 0.24},
        {"group": "middle_40", "population_share": 0.40, "wealth": 820, "debt": 210, "inheritance_receipts": 35, "asset_return": 0.04, "housing_ownership": 0.64},
        {"group": "top_10", "population_share": 0.10, "wealth": 3100, "debt": 260, "inheritance_receipts": 220, "asset_return": 0.06, "housing_ownership": 0.88},
        {"group": "top_1", "population_share": 0.01, "wealth": 1450, "debt": 60, "inheritance_receipts": 420, "asset_return": 0.075, "housing_ownership": 0.94},
    ])


def build_mobility_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "high_mobility_social_investment", "parent_outcome": 60, "persistence_b": 0.28, "baseline_a": 34, "education_access": 0.82, "health_access": 0.80, "place_advantage": 0.76, "network_access": 0.66, "family_wealth_buffer": 0.58},
        {"scenario": "moderate_mobility_mixed_system", "parent_outcome": 60, "persistence_b": 0.48, "baseline_a": 22, "education_access": 0.62, "health_access": 0.64, "place_advantage": 0.58, "network_access": 0.50, "family_wealth_buffer": 0.46},
        {"scenario": "low_mobility_inherited_advantage", "parent_outcome": 60, "persistence_b": 0.72, "baseline_a": 10, "education_access": 0.38, "health_access": 0.44, "place_advantage": 0.34, "network_access": 0.30, "family_wealth_buffer": 0.28},
        {"scenario": "segmented_opportunity_structure", "parent_outcome": 60, "persistence_b": 0.64, "baseline_a": 14, "education_access": 0.46, "health_access": 0.52, "place_advantage": 0.28, "network_access": 0.34, "family_wealth_buffer": 0.36},
        {"scenario": "universal_services_mobility_path", "parent_outcome": 60, "persistence_b": 0.34, "baseline_a": 30, "education_access": 0.78, "health_access": 0.84, "place_advantage": 0.68, "network_access": 0.60, "family_wealth_buffer": 0.52},
    ])


def build_labor_market_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"sector": "secure_public_services", "median_wage": 62, "top_wage": 120, "bottom_wage": 38, "bargaining_power": 0.74, "union_strength": 0.68, "employment_security": 0.78, "schedule_stability": 0.82, "benefit_access": 0.86},
        {"sector": "high_skill_platform_core", "median_wage": 125, "top_wage": 420, "bottom_wage": 72, "bargaining_power": 0.62, "union_strength": 0.18, "employment_security": 0.58, "schedule_stability": 0.66, "benefit_access": 0.72},
        {"sector": "precarious_services", "median_wage": 34, "top_wage": 62, "bottom_wage": 22, "bargaining_power": 0.22, "union_strength": 0.10, "employment_security": 0.24, "schedule_stability": 0.20, "benefit_access": 0.18},
        {"sector": "manufacturing_with_bargaining", "median_wage": 68, "top_wage": 130, "bottom_wage": 42, "bargaining_power": 0.70, "union_strength": 0.62, "employment_security": 0.66, "schedule_stability": 0.72, "benefit_access": 0.76},
        {"sector": "fissured_contract_work", "median_wage": 42, "top_wage": 95, "bottom_wage": 24, "bargaining_power": 0.28, "union_strength": 0.12, "employment_security": 0.26, "schedule_stability": 0.34, "benefit_access": 0.30},
    ])


def build_housing_place_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"place": "high_opportunity_ownership_zone", "median_income": 118, "housing_cost": 38, "school_quality": 0.86, "transit_access": 0.72, "environmental_quality": 0.80, "job_access": 0.84, "homeownership_rate": 0.76},
        {"place": "rent_burdened_metro_core", "median_income": 72, "housing_cost": 38, "school_quality": 0.62, "transit_access": 0.84, "environmental_quality": 0.58, "job_access": 0.78, "homeownership_rate": 0.28},
        {"place": "disinvested_periphery", "median_income": 44, "housing_cost": 20, "school_quality": 0.38, "transit_access": 0.24, "environmental_quality": 0.42, "job_access": 0.32, "homeownership_rate": 0.42},
        {"place": "stable_mixed_income_city", "median_income": 76, "housing_cost": 24, "school_quality": 0.70, "transit_access": 0.68, "environmental_quality": 0.66, "job_access": 0.70, "homeownership_rate": 0.54},
        {"place": "exclusionary_high_asset_suburb", "median_income": 150, "housing_cost": 52, "school_quality": 0.92, "transit_access": 0.44, "environmental_quality": 0.84, "job_access": 0.74, "homeownership_rate": 0.86},
    ])


def build_public_services_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "thin_safety_net_private_services", "healthcare_access": 0.34, "education_quality": 0.46, "childcare_support": 0.18, "transit_quality": 0.30, "income_support": 0.22, "unemployment_insurance": 0.30, "pension_security": 0.38},
        {"scenario": "targeted_transfer_system", "healthcare_access": 0.56, "education_quality": 0.58, "childcare_support": 0.42, "transit_quality": 0.44, "income_support": 0.64, "unemployment_insurance": 0.52, "pension_security": 0.56},
        {"scenario": "universal_public_services", "healthcare_access": 0.84, "education_quality": 0.82, "childcare_support": 0.78, "transit_quality": 0.70, "income_support": 0.62, "unemployment_insurance": 0.72, "pension_security": 0.80},
        {"scenario": "social_insurance_plus_services", "healthcare_access": 0.78, "education_quality": 0.76, "childcare_support": 0.66, "transit_quality": 0.62, "income_support": 0.70, "unemployment_insurance": 0.78, "pension_security": 0.82},
        {"scenario": "austerity_public_capacity_erosion", "healthcare_access": 0.40, "education_quality": 0.42, "childcare_support": 0.24, "transit_quality": 0.34, "income_support": 0.30, "unemployment_insurance": 0.36, "pension_security": 0.44},
    ])


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "inequality_redistribution_social_mobility.sqlite"
    names = [
        "income_distribution",
        "wealth_distribution",
        "mobility_scenarios",
        "labor_market_scenarios",
        "housing_place_scenarios",
        "public_services_scenarios",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_income_distribution(),
        build_wealth_distribution(),
        build_mobility_scenarios(),
        build_labor_market_scenarios(),
        build_housing_place_scenarios(),
        build_public_services_scenarios(),
    ]
    filenames = [
        "income_distribution.csv",
        "wealth_distribution.csv",
        "mobility_scenarios.csv",
        "labor_market_scenarios.csv",
        "housing_place_scenarios.csv",
        "public_services_scenarios.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created inequality, redistribution, and social mobility base data.")


if __name__ == "__main__":
    main()
