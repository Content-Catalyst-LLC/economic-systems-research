"""
Build stylized supply, demand, price, access, and external-cost datasets.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_market_parameter_scenarios() -> pd.DataFrame:
    rows = [
        {
            "market": "essential_good",
            "scenario": "baseline",
            "a": 120.0,
            "b": 2.0,
            "c": 20.0,
            "d": 1.5,
            "external_cost": 0.0,
            "markup_rate": 0.0,
            "description": "Baseline competitive market with moderate demand and supply responsiveness.",
        },
        {
            "market": "essential_good",
            "scenario": "demand_expansion",
            "a": 145.0,
            "b": 2.0,
            "c": 20.0,
            "d": 1.5,
            "external_cost": 0.0,
            "markup_rate": 0.0,
            "description": "Demand shifts outward because income, population, or preference intensity rises.",
        },
        {
            "market": "essential_good",
            "scenario": "negative_supply_shock",
            "a": 120.0,
            "b": 2.0,
            "c": 5.0,
            "d": 1.5,
            "external_cost": 0.0,
            "markup_rate": 0.0,
            "description": "Supply shifts inward because input, energy, logistics, or production costs rise.",
        },
        {
            "market": "essential_good",
            "scenario": "rigid_supply",
            "a": 120.0,
            "b": 2.0,
            "c": 20.0,
            "d": 0.45,
            "external_cost": 0.0,
            "markup_rate": 0.0,
            "description": "Supply is inelastic; demand pressure shows up more strongly in prices.",
        },
        {
            "market": "essential_good",
            "scenario": "elastic_supply",
            "a": 120.0,
            "b": 2.0,
            "c": 20.0,
            "d": 3.0,
            "external_cost": 0.0,
            "markup_rate": 0.0,
            "description": "Supply is more responsive because spare capacity, logistics, or technology allow expansion.",
        },
        {
            "market": "essential_good",
            "scenario": "market_power_markup",
            "a": 120.0,
            "b": 2.0,
            "c": 20.0,
            "d": 1.5,
            "external_cost": 0.0,
            "markup_rate": 0.18,
            "description": "Market power adds a markup over competitive equilibrium price.",
        },
        {
            "market": "carbon_intensive_good",
            "scenario": "missing_external_cost",
            "a": 120.0,
            "b": 2.0,
            "c": 20.0,
            "d": 1.5,
            "external_cost": 12.0,
            "markup_rate": 0.0,
            "description": "Private market price omits marginal external ecological or social cost.",
        },
        {
            "market": "housing_like_market",
            "scenario": "high_need_rigid_supply",
            "a": 155.0,
            "b": 1.2,
            "c": 15.0,
            "d": 0.35,
            "external_cost": 0.0,
            "markup_rate": 0.05,
            "description": "Essential market with strong demand, rigid supply, and limited competitive adjustment.",
        },
    ]
    return pd.DataFrame(rows)


def build_market_access_groups() -> pd.DataFrame:
    rows = [
        {
            "group": "high_income_flexible_consumers",
            "need_index": 0.45,
            "income_command": 0.95,
            "credit_access": 0.88,
            "institutional_access": 0.80,
            "price_burden": 0.38,
            "population_weight": 0.16,
        },
        {
            "group": "middle_income_households",
            "need_index": 0.62,
            "income_command": 0.68,
            "credit_access": 0.60,
            "institutional_access": 0.66,
            "price_burden": 0.58,
            "population_weight": 0.30,
        },
        {
            "group": "low_income_essential_need",
            "need_index": 0.88,
            "income_command": 0.36,
            "credit_access": 0.34,
            "institutional_access": 0.46,
            "price_burden": 0.82,
            "population_weight": 0.24,
        },
        {
            "group": "debt_constrained_households",
            "need_index": 0.78,
            "income_command": 0.44,
            "credit_access": 0.20,
            "institutional_access": 0.44,
            "price_burden": 0.76,
            "population_weight": 0.14,
        },
        {
            "group": "public_access_dependent",
            "need_index": 0.86,
            "income_command": 0.32,
            "credit_access": 0.25,
            "institutional_access": 0.62,
            "price_burden": 0.74,
            "population_weight": 0.10,
        },
        {
            "group": "excluded_high_need",
            "need_index": 0.94,
            "income_command": 0.24,
            "credit_access": 0.15,
            "institutional_access": 0.28,
            "price_burden": 0.90,
            "population_weight": 0.06,
        },
    ]
    return pd.DataFrame(rows)


def build_external_cost_scenarios() -> pd.DataFrame:
    rows = [
        {"sector": "food", "private_price": 100, "marginal_external_cost": 8, "public_good_benefit": 4},
        {"sector": "energy", "private_price": 100, "marginal_external_cost": 22, "public_good_benefit": 3},
        {"sector": "housing", "private_price": 100, "marginal_external_cost": 5, "public_good_benefit": 12},
        {"sector": "transport", "private_price": 100, "marginal_external_cost": 16, "public_good_benefit": 7},
        {"sector": "health", "private_price": 100, "marginal_external_cost": 2, "public_good_benefit": 18},
        {"sector": "ecological_restoration", "private_price": 100, "marginal_external_cost": -20, "public_good_benefit": 24},
    ]
    return pd.DataFrame(rows)


def save_sqlite(markets, access, external_costs) -> None:
    db_path = PROCESSED_DIR / "supply_demand_coordination.sqlite"
    with sqlite3.connect(db_path) as conn:
        markets.to_sql("market_parameter_scenarios", conn, if_exists="replace", index=False)
        access.to_sql("market_access_groups", conn, if_exists="replace", index=False)
        external_costs.to_sql("external_cost_scenarios", conn, if_exists="replace", index=False)


def main() -> None:
    markets = build_market_parameter_scenarios()
    access = build_market_access_groups()
    external_costs = build_external_cost_scenarios()

    markets.to_csv(PROCESSED_DIR / "market_parameter_scenarios.csv", index=False)
    access.to_csv(PROCESSED_DIR / "market_access_groups.csv", index=False)
    external_costs.to_csv(PROCESSED_DIR / "external_cost_scenarios.csv", index=False)

    save_sqlite(markets, access, external_costs)
    print("Created supply-demand coordination base data.")


if __name__ == "__main__":
    main()
