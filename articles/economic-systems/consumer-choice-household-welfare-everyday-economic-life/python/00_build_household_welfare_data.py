"""
Build stylized household welfare, expense, inflation, and public-goods datasets.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_household_profiles() -> pd.DataFrame:
    rows = [
        {
            "household_group": "asset_secure_high_income",
            "income": 9800,
            "transfers": 0,
            "liquid_assets": 25000,
            "debt_service": 750,
            "other_fixed_burdens": 450,
            "rent": 2600,
            "food": 950,
            "transport": 650,
            "utilities": 380,
            "health": 450,
            "other": 1800,
            "paid_labor_hours": 8.5,
            "care_hours": 1.0,
            "commute_hours": 0.8,
            "household_admin_hours": 1.0,
            "population_weight": 0.12,
        },
        {
            "household_group": "middle_income_stable",
            "income": 5600,
            "transfers": 150,
            "liquid_assets": 6500,
            "debt_service": 520,
            "other_fixed_burdens": 300,
            "rent": 1750,
            "food": 780,
            "transport": 420,
            "utilities": 310,
            "health": 320,
            "other": 850,
            "paid_labor_hours": 8.7,
            "care_hours": 1.6,
            "commute_hours": 1.2,
            "household_admin_hours": 1.4,
            "population_weight": 0.26,
        },
        {
            "household_group": "rent_burdened_workers",
            "income": 3900,
            "transfers": 250,
            "liquid_assets": 1400,
            "debt_service": 430,
            "other_fixed_burdens": 260,
            "rent": 1650,
            "food": 680,
            "transport": 360,
            "utilities": 290,
            "health": 240,
            "other": 520,
            "paid_labor_hours": 9.0,
            "care_hours": 2.2,
            "commute_hours": 1.6,
            "household_admin_hours": 1.6,
            "population_weight": 0.24,
        },
        {
            "household_group": "care_constrained_households",
            "income": 4300,
            "transfers": 450,
            "liquid_assets": 1800,
            "debt_service": 380,
            "other_fixed_burdens": 420,
            "rent": 1500,
            "food": 760,
            "transport": 410,
            "utilities": 320,
            "health": 390,
            "other": 540,
            "paid_labor_hours": 8.2,
            "care_hours": 4.2,
            "commute_hours": 1.1,
            "household_admin_hours": 1.8,
            "population_weight": 0.18,
        },
        {
            "household_group": "precarious_low_income",
            "income": 2600,
            "transfers": 500,
            "liquid_assets": 350,
            "debt_service": 260,
            "other_fixed_burdens": 180,
            "rent": 1150,
            "food": 540,
            "transport": 280,
            "utilities": 230,
            "health": 180,
            "other": 320,
            "paid_labor_hours": 8.8,
            "care_hours": 2.6,
            "commute_hours": 1.8,
            "household_admin_hours": 1.7,
            "population_weight": 0.14,
        },
        {
            "household_group": "climate_energy_exposed",
            "income": 3100,
            "transfers": 350,
            "liquid_assets": 600,
            "debt_service": 310,
            "other_fixed_burdens": 220,
            "rent": 1250,
            "food": 620,
            "transport": 420,
            "utilities": 410,
            "health": 240,
            "other": 360,
            "paid_labor_hours": 8.6,
            "care_hours": 2.0,
            "commute_hours": 2.1,
            "household_admin_hours": 1.5,
            "population_weight": 0.06,
        },
    ]
    return pd.DataFrame(rows)


def build_inflation_scenarios() -> pd.DataFrame:
    rows = [
        {"scenario": "baseline", "rent_multiplier": 1.00, "food_multiplier": 1.00, "transport_multiplier": 1.00, "utilities_multiplier": 1.00, "health_multiplier": 1.00, "other_multiplier": 1.00},
        {"scenario": "essentials_inflation", "rent_multiplier": 1.09, "food_multiplier": 1.14, "transport_multiplier": 1.08, "utilities_multiplier": 1.12, "health_multiplier": 1.07, "other_multiplier": 1.03},
        {"scenario": "housing_shock", "rent_multiplier": 1.18, "food_multiplier": 1.04, "transport_multiplier": 1.02, "utilities_multiplier": 1.03, "health_multiplier": 1.02, "other_multiplier": 1.01},
        {"scenario": "energy_transport_shock", "rent_multiplier": 1.02, "food_multiplier": 1.06, "transport_multiplier": 1.18, "utilities_multiplier": 1.22, "health_multiplier": 1.02, "other_multiplier": 1.02},
        {"scenario": "health_care_shock", "rent_multiplier": 1.02, "food_multiplier": 1.04, "transport_multiplier": 1.03, "utilities_multiplier": 1.03, "health_multiplier": 1.28, "other_multiplier": 1.02},
        {"scenario": "public_goods_support", "rent_multiplier": 0.98, "food_multiplier": 0.98, "transport_multiplier": 0.82, "utilities_multiplier": 0.90, "health_multiplier": 0.78, "other_multiplier": 1.00},
    ]
    return pd.DataFrame(rows)


def build_public_goods_scenarios() -> pd.DataFrame:
    rows = [
        {
            "scenario": "weak_public_goods",
            "transport_private_cost_reduction": 0.00,
            "health_private_cost_reduction": 0.00,
            "childcare_private_cost_reduction": 0.00,
            "time_savings_hours": 0.00,
            "institutional_support_index": 0.35,
        },
        {
            "scenario": "baseline_public_goods",
            "transport_private_cost_reduction": 0.08,
            "health_private_cost_reduction": 0.10,
            "childcare_private_cost_reduction": 0.08,
            "time_savings_hours": 0.30,
            "institutional_support_index": 0.55,
        },
        {
            "scenario": "strong_public_goods",
            "transport_private_cost_reduction": 0.22,
            "health_private_cost_reduction": 0.30,
            "childcare_private_cost_reduction": 0.25,
            "time_savings_hours": 0.90,
            "institutional_support_index": 0.78,
        },
        {
            "scenario": "universal_basic_services",
            "transport_private_cost_reduction": 0.32,
            "health_private_cost_reduction": 0.48,
            "childcare_private_cost_reduction": 0.40,
            "time_savings_hours": 1.30,
            "institutional_support_index": 0.88,
        },
    ]
    return pd.DataFrame(rows)


def build_expense_categories() -> pd.DataFrame:
    rows = [
        {"category": "rent", "is_essential": 1, "is_fixed": 1, "welfare_domain": "housing_security"},
        {"category": "food", "is_essential": 1, "is_fixed": 0, "welfare_domain": "nutrition"},
        {"category": "transport", "is_essential": 1, "is_fixed": 0, "welfare_domain": "mobility"},
        {"category": "utilities", "is_essential": 1, "is_fixed": 1, "welfare_domain": "energy_and_water_security"},
        {"category": "health", "is_essential": 1, "is_fixed": 0, "welfare_domain": "health_security"},
        {"category": "other", "is_essential": 0, "is_fixed": 0, "welfare_domain": "discretionary_and_household_misc"},
        {"category": "debt_service", "is_essential": 1, "is_fixed": 1, "welfare_domain": "financial_obligation"},
        {"category": "other_fixed_burdens", "is_essential": 1, "is_fixed": 1, "welfare_domain": "fixed_obligations"},
    ]
    return pd.DataFrame(rows)


def save_sqlite(households, inflation, public_goods, categories) -> None:
    db_path = PROCESSED_DIR / "consumer_choice_household_welfare.sqlite"
    with sqlite3.connect(db_path) as conn:
        households.to_sql("household_profiles", conn, if_exists="replace", index=False)
        inflation.to_sql("inflation_scenarios", conn, if_exists="replace", index=False)
        public_goods.to_sql("public_goods_scenarios", conn, if_exists="replace", index=False)
        categories.to_sql("expense_categories", conn, if_exists="replace", index=False)


def main() -> None:
    households = build_household_profiles()
    inflation = build_inflation_scenarios()
    public_goods = build_public_goods_scenarios()
    categories = build_expense_categories()

    households.to_csv(PROCESSED_DIR / "household_profiles.csv", index=False)
    inflation.to_csv(PROCESSED_DIR / "inflation_scenarios.csv", index=False)
    public_goods.to_csv(PROCESSED_DIR / "public_goods_scenarios.csv", index=False)
    categories.to_csv(PROCESSED_DIR / "expense_categories.csv", index=False)

    save_sqlite(households, inflation, public_goods, categories)
    print("Created consumer choice and household welfare base data.")


if __name__ == "__main__":
    main()
