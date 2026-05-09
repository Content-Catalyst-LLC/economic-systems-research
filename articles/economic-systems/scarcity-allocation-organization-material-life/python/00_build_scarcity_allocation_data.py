"""
Build stylized scarcity, allocation, access, and reproduction datasets.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_priorities() -> pd.DataFrame:
    rows = [
        {"priority": "Housing", "material_role": "Shelter and residential stability", "essentiality": 0.95, "resilience_value": 0.85},
        {"priority": "Health", "material_role": "Public health, care access, and bodily security", "essentiality": 0.98, "resilience_value": 0.92},
        {"priority": "Education", "material_role": "Human capability and intergenerational capacity", "essentiality": 0.86, "resilience_value": 0.88},
        {"priority": "Infrastructure", "material_role": "Transport, water, energy, communications, and public systems", "essentiality": 0.90, "resilience_value": 0.95},
        {"priority": "Energy", "material_role": "Useful energy for households, firms, and public systems", "essentiality": 0.92, "resilience_value": 0.82},
        {"priority": "Care", "material_role": "Household care, elder care, disability support, and social reproduction", "essentiality": 0.96, "resilience_value": 0.90},
        {"priority": "Ecological Restoration", "material_role": "Repair, regeneration, adaptation, and ecological capacity", "essentiality": 0.88, "resilience_value": 0.97},
        {"priority": "Other", "material_role": "Residual discretionary allocation", "essentiality": 0.40, "resilience_value": 0.35},
    ]
    return pd.DataFrame(rows)


def build_allocation_scenarios() -> pd.DataFrame:
    rows = [
        {"scenario": "baseline", "priority": "Housing", "share": 0.20},
        {"scenario": "baseline", "priority": "Health", "share": 0.18},
        {"scenario": "baseline", "priority": "Education", "share": 0.15},
        {"scenario": "baseline", "priority": "Infrastructure", "share": 0.15},
        {"scenario": "baseline", "priority": "Energy", "share": 0.10},
        {"scenario": "baseline", "priority": "Care", "share": 0.12},
        {"scenario": "baseline", "priority": "Ecological Restoration", "share": 0.05},
        {"scenario": "baseline", "priority": "Other", "share": 0.05},

        {"scenario": "resilience_repair", "priority": "Housing", "share": 0.19},
        {"scenario": "resilience_repair", "priority": "Health", "share": 0.18},
        {"scenario": "resilience_repair", "priority": "Education", "share": 0.14},
        {"scenario": "resilience_repair", "priority": "Infrastructure", "share": 0.18},
        {"scenario": "resilience_repair", "priority": "Energy", "share": 0.09},
        {"scenario": "resilience_repair", "priority": "Care", "share": 0.13},
        {"scenario": "resilience_repair", "priority": "Ecological Restoration", "share": 0.08},
        {"scenario": "resilience_repair", "priority": "Other", "share": 0.01},

        {"scenario": "consumption_pressure", "priority": "Housing", "share": 0.23},
        {"scenario": "consumption_pressure", "priority": "Health", "share": 0.18},
        {"scenario": "consumption_pressure", "priority": "Education", "share": 0.13},
        {"scenario": "consumption_pressure", "priority": "Infrastructure", "share": 0.12},
        {"scenario": "consumption_pressure", "priority": "Energy", "share": 0.12},
        {"scenario": "consumption_pressure", "priority": "Care", "share": 0.10},
        {"scenario": "consumption_pressure", "priority": "Ecological Restoration", "share": 0.03},
        {"scenario": "consumption_pressure", "priority": "Other", "share": 0.09},

        {"scenario": "austerity_undermaintenance", "priority": "Housing", "share": 0.18},
        {"scenario": "austerity_undermaintenance", "priority": "Health", "share": 0.16},
        {"scenario": "austerity_undermaintenance", "priority": "Education", "share": 0.13},
        {"scenario": "austerity_undermaintenance", "priority": "Infrastructure", "share": 0.10},
        {"scenario": "austerity_undermaintenance", "priority": "Energy", "share": 0.12},
        {"scenario": "austerity_undermaintenance", "priority": "Care", "share": 0.08},
        {"scenario": "austerity_undermaintenance", "priority": "Ecological Restoration", "share": 0.02},
        {"scenario": "austerity_undermaintenance", "priority": "Other", "share": 0.21},
    ]
    return pd.DataFrame(rows)


def build_households() -> pd.DataFrame:
    rows = [
        {"household_group": "asset_secure_high_income", "need_index": 0.45, "income_command": 0.95, "price_index": 0.60, "institutional_access": 0.80, "population_weight": 0.15},
        {"household_group": "middle_income_stable", "need_index": 0.62, "income_command": 0.65, "price_index": 0.72, "institutional_access": 0.68, "population_weight": 0.30},
        {"household_group": "low_income_rent_burdened", "need_index": 0.88, "income_command": 0.35, "price_index": 0.90, "institutional_access": 0.46, "population_weight": 0.25},
        {"household_group": "care_constrained_households", "need_index": 0.82, "income_command": 0.42, "price_index": 0.82, "institutional_access": 0.40, "population_weight": 0.15},
        {"household_group": "rural_infrastructure_gap", "need_index": 0.76, "income_command": 0.45, "price_index": 0.78, "institutional_access": 0.35, "population_weight": 0.10},
        {"household_group": "climate_exposed_low_access", "need_index": 0.92, "income_command": 0.30, "price_index": 0.88, "institutional_access": 0.30, "population_weight": 0.05},
    ]
    return pd.DataFrame(rows)


def build_reproduction_constraints() -> pd.DataFrame:
    rows = [
        {"scenario": "baseline", "periods": 25, "initial_produced_capacity": 1000, "initial_ecological_capacity": 1000, "consumption": 560, "investment": 190, "maintenance": 140, "ecological_restoration": 70, "depreciation_rate": 0.050, "resource_use": 42, "regenerative_capacity": 38},
        {"scenario": "resilience_repair", "periods": 25, "initial_produced_capacity": 1000, "initial_ecological_capacity": 1000, "consumption": 520, "investment": 220, "maintenance": 170, "ecological_restoration": 110, "depreciation_rate": 0.045, "resource_use": 36, "regenerative_capacity": 48},
        {"scenario": "consumption_pressure", "periods": 25, "initial_produced_capacity": 1000, "initial_ecological_capacity": 1000, "consumption": 650, "investment": 150, "maintenance": 100, "ecological_restoration": 40, "depreciation_rate": 0.060, "resource_use": 48, "regenerative_capacity": 32},
        {"scenario": "austerity_undermaintenance", "periods": 25, "initial_produced_capacity": 1000, "initial_ecological_capacity": 1000, "consumption": 520, "investment": 130, "maintenance": 70, "ecological_restoration": 25, "depreciation_rate": 0.070, "resource_use": 45, "regenerative_capacity": 25},
    ]
    return pd.DataFrame(rows)


def save_sqlite(priorities, scenarios, households, reproduction) -> None:
    db_path = PROCESSED_DIR / "scarcity_allocation.sqlite"
    with sqlite3.connect(db_path) as conn:
        priorities.to_sql("allocation_priorities", conn, if_exists="replace", index=False)
        scenarios.to_sql("allocation_scenarios", conn, if_exists="replace", index=False)
        households.to_sql("access_households", conn, if_exists="replace", index=False)
        reproduction.to_sql("reproduction_constraints", conn, if_exists="replace", index=False)


def main() -> None:
    priorities = build_priorities()
    scenarios = build_allocation_scenarios()
    households = build_households()
    reproduction = build_reproduction_constraints()

    priorities.to_csv(PROCESSED_DIR / "allocation_priorities.csv", index=False)
    scenarios.to_csv(PROCESSED_DIR / "allocation_scenarios.csv", index=False)
    households.to_csv(PROCESSED_DIR / "access_households.csv", index=False)
    reproduction.to_csv(PROCESSED_DIR / "reproduction_constraints.csv", index=False)

    save_sqlite(priorities, scenarios, households, reproduction)

    print("Created scarcity and allocation base data.")


if __name__ == "__main__":
    main()
