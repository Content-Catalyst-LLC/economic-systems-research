"""
Build stylized datasets for capital, investment, and accumulation.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_capital_stock_scenarios() -> pd.DataFrame:
    rows = [
        {"scenario": "steady_replacement", "initial_capital": 1000, "annual_investment": 85, "depreciation_rate": 0.08, "labor": 210, "output": 1200},
        {"scenario": "capital_deepening", "initial_capital": 1000, "annual_investment": 145, "depreciation_rate": 0.07, "labor": 215, "output": 1320},
        {"scenario": "underinvestment", "initial_capital": 1000, "annual_investment": 55, "depreciation_rate": 0.085, "labor": 208, "output": 1100},
        {"scenario": "resilient_public_investment", "initial_capital": 1000, "annual_investment": 160, "depreciation_rate": 0.055, "labor": 218, "output": 1300},
        {"scenario": "extractive_run_down", "initial_capital": 1000, "annual_investment": 45, "depreciation_rate": 0.105, "labor": 205, "output": 1160},
        {"scenario": "intangible_capital_expansion", "initial_capital": 1000, "annual_investment": 135, "depreciation_rate": 0.095, "labor": 190, "output": 1420},
    ]
    return pd.DataFrame(rows)


def build_investment_project_scenarios() -> pd.DataFrame:
    rows = [
        {"project": "short_term_private_return", "cashflow_year_0": -300, "cashflow_year_1": 110, "cashflow_year_2": 105, "cashflow_year_3": 90, "cashflow_year_4": 55, "cashflow_year_5": 30, "private_discount_rate": 0.10, "public_discount_rate": 0.035},
        {"project": "public_transit_resilience", "cashflow_year_0": -300, "cashflow_year_1": 30, "cashflow_year_2": 55, "cashflow_year_3": 85, "cashflow_year_4": 115, "cashflow_year_5": 145, "private_discount_rate": 0.10, "public_discount_rate": 0.035},
        {"project": "ecological_restoration", "cashflow_year_0": -300, "cashflow_year_1": 20, "cashflow_year_2": 45, "cashflow_year_3": 75, "cashflow_year_4": 120, "cashflow_year_5": 170, "private_discount_rate": 0.10, "public_discount_rate": 0.025},
        {"project": "speculative_asset_turnover", "cashflow_year_0": -300, "cashflow_year_1": 170, "cashflow_year_2": 80, "cashflow_year_3": 30, "cashflow_year_4": 10, "cashflow_year_5": -20, "private_discount_rate": 0.12, "public_discount_rate": 0.035},
        {"project": "grid_hardening_and_storage", "cashflow_year_0": -300, "cashflow_year_1": 45, "cashflow_year_2": 70, "cashflow_year_3": 100, "cashflow_year_4": 130, "cashflow_year_5": 160, "private_discount_rate": 0.09, "public_discount_rate": 0.03},
    ]
    return pd.DataFrame(rows)


def build_maintenance_scenarios() -> pd.DataFrame:
    rows = []
    for scenario, initial_backlog, needs, maintenance in [
        ("routine_maintenance", 20, [28, 30, 32, 34, 36, 38], [28, 30, 32, 34, 36, 38]),
        ("deferred_maintenance", 20, [28, 30, 32, 34, 36, 38], [18, 20, 22, 24, 25, 26]),
        ("catch_up_repair", 60, [30, 32, 34, 36, 38, 40], [45, 50, 55, 55, 50, 45]),
        ("austerity_run_down", 30, [28, 31, 35, 38, 42, 46], [15, 15, 16, 17, 18, 18]),
    ]:
        for period, (need, actual) in enumerate(zip(needs, maintenance), start=1):
            rows.append({
                "scenario": scenario,
                "period": period,
                "initial_backlog": initial_backlog,
                "new_maintenance_need": need,
                "actual_maintenance": actual,
            })
    return pd.DataFrame(rows)


def build_ownership_distribution_scenarios() -> pd.DataFrame:
    rows = [
        {"scenario": "labor_broad_share", "wage_share": 0.58, "profit_share": 0.20, "tax_public_share": 0.16, "rent_share": 0.06, "public_reinvestment_share": 0.10},
        {"scenario": "asset_holder_capture", "wage_share": 0.44, "profit_share": 0.30, "tax_public_share": 0.12, "rent_share": 0.14, "public_reinvestment_share": 0.05},
        {"scenario": "public_investment_model", "wage_share": 0.52, "profit_share": 0.18, "tax_public_share": 0.22, "rent_share": 0.08, "public_reinvestment_share": 0.16},
        {"scenario": "rentier_accumulation", "wage_share": 0.40, "profit_share": 0.24, "tax_public_share": 0.10, "rent_share": 0.26, "public_reinvestment_share": 0.04},
        {"scenario": "cooperative_patient_capital", "wage_share": 0.56, "profit_share": 0.18, "tax_public_share": 0.14, "rent_share": 0.04, "public_reinvestment_share": 0.18},
    ]
    return pd.DataFrame(rows)


def build_finance_direction_scenarios() -> pd.DataFrame:
    rows = [
        {"finance_channel": "productive_capacity", "flow_share": 0.28, "productive_capacity_score": 0.84, "speculation_score": 0.10, "extraction_score": 0.12, "resilience_score": 0.58},
        {"finance_channel": "public_infrastructure", "flow_share": 0.18, "productive_capacity_score": 0.76, "speculation_score": 0.04, "extraction_score": 0.08, "resilience_score": 0.82},
        {"finance_channel": "maintenance_and_repair", "flow_share": 0.10, "productive_capacity_score": 0.68, "speculation_score": 0.02, "extraction_score": 0.04, "resilience_score": 0.86},
        {"finance_channel": "asset_speculation", "flow_share": 0.24, "productive_capacity_score": 0.22, "speculation_score": 0.92, "extraction_score": 0.62, "resilience_score": 0.18},
        {"finance_channel": "leveraged_acquisition", "flow_share": 0.12, "productive_capacity_score": 0.28, "speculation_score": 0.70, "extraction_score": 0.78, "resilience_score": 0.20},
        {"finance_channel": "ecological_transition", "flow_share": 0.08, "productive_capacity_score": 0.70, "speculation_score": 0.08, "extraction_score": 0.06, "resilience_score": 0.90},
    ]
    return pd.DataFrame(rows)


def build_sustainable_investment_scenarios() -> pd.DataFrame:
    rows = [
        {"project": "fossil_lock_in_expansion", "financial_return_score": 0.78, "resilience_score": 0.24, "ecological_alignment_score": 0.08, "public_value_score": 0.22, "maintenance_score": 0.36},
        {"project": "public_transit_network", "financial_return_score": 0.48, "resilience_score": 0.82, "ecological_alignment_score": 0.86, "public_value_score": 0.92, "maintenance_score": 0.78},
        {"project": "grid_resilience_and_storage", "financial_return_score": 0.60, "resilience_score": 0.90, "ecological_alignment_score": 0.84, "public_value_score": 0.86, "maintenance_score": 0.82},
        {"project": "speculative_real_estate", "financial_return_score": 0.82, "resilience_score": 0.22, "ecological_alignment_score": 0.18, "public_value_score": 0.20, "maintenance_score": 0.30},
        {"project": "water_system_renewal", "financial_return_score": 0.42, "resilience_score": 0.88, "ecological_alignment_score": 0.76, "public_value_score": 0.94, "maintenance_score": 0.92},
        {"project": "research_and_public_knowledge", "financial_return_score": 0.36, "resilience_score": 0.74, "ecological_alignment_score": 0.64, "public_value_score": 0.90, "maintenance_score": 0.70},
    ]
    return pd.DataFrame(rows)


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "capital_investment_accumulation.sqlite"
    names = [
        "capital_stock_scenarios",
        "investment_project_scenarios",
        "maintenance_scenarios",
        "ownership_distribution_scenarios",
        "finance_direction_scenarios",
        "sustainable_investment_scenarios",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_capital_stock_scenarios(),
        build_investment_project_scenarios(),
        build_maintenance_scenarios(),
        build_ownership_distribution_scenarios(),
        build_finance_direction_scenarios(),
        build_sustainable_investment_scenarios(),
    ]

    filenames = [
        "capital_stock_scenarios.csv",
        "investment_project_scenarios.csv",
        "maintenance_scenarios.csv",
        "ownership_distribution_scenarios.csv",
        "finance_direction_scenarios.csv",
        "sustainable_investment_scenarios.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created capital, investment, and accumulation base data.")


if __name__ == "__main__":
    main()
