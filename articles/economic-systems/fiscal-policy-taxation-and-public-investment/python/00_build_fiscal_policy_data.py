"""
Build stylized datasets for fiscal policy, taxation, and public investment.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_fiscal_position_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "stable_public_finance", "tax_revenue": 430, "public_spending": 455, "primary_spending": 420, "interest_rate": 0.035, "debt_stock": 780, "output": 1250},
        {"scenario": "recession_stabilization", "tax_revenue": 390, "public_spending": 510, "primary_spending": 470, "interest_rate": 0.030, "debt_stock": 820, "output": 1180},
        {"scenario": "austerity_underinvestment", "tax_revenue": 405, "public_spending": 410, "primary_spending": 382, "interest_rate": 0.040, "debt_stock": 760, "output": 1190},
        {"scenario": "public_investment_expansion", "tax_revenue": 435, "public_spending": 545, "primary_spending": 505, "interest_rate": 0.034, "debt_stock": 800, "output": 1265},
        {"scenario": "high_interest_debt_pressure", "tax_revenue": 420, "public_spending": 525, "primary_spending": 455, "interest_rate": 0.062, "debt_stock": 980, "output": 1220},
        {"scenario": "resilience_oriented_fiscal_state", "tax_revenue": 470, "public_spending": 565, "primary_spending": 520, "interest_rate": 0.032, "debt_stock": 820, "output": 1320},
    ])


def build_tax_distribution_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"income_group": "bottom_20", "income": 22000, "tax_paid": 1900, "transfer_received": 6500, "consumption_tax_paid": 1450, "wealth_tax_paid": 0},
        {"income_group": "second_20", "income": 41000, "tax_paid": 5200, "transfer_received": 3800, "consumption_tax_paid": 2650, "wealth_tax_paid": 0},
        {"income_group": "middle_20", "income": 68000, "tax_paid": 11200, "transfer_received": 1900, "consumption_tax_paid": 3800, "wealth_tax_paid": 100},
        {"income_group": "fourth_20", "income": 112000, "tax_paid": 24500, "transfer_received": 800, "consumption_tax_paid": 5200, "wealth_tax_paid": 450},
        {"income_group": "top_10", "income": 245000, "tax_paid": 69000, "transfer_received": 200, "consumption_tax_paid": 8800, "wealth_tax_paid": 4200},
        {"income_group": "top_1", "income": 1250000, "tax_paid": 385000, "transfer_received": 0, "consumption_tax_paid": 24000, "wealth_tax_paid": 42000},
    ])


def build_spending_composition_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"spending_category": "health_and_public_health", "spending_amount": 145, "public_investment_component": 28, "current_service_component": 117, "resilience_score": 0.82},
        {"spending_category": "education_and_research", "spending_amount": 132, "public_investment_component": 46, "current_service_component": 86, "resilience_score": 0.86},
        {"spending_category": "transport_and_infrastructure", "spending_amount": 118, "public_investment_component": 82, "current_service_component": 36, "resilience_score": 0.88},
        {"spending_category": "social_insurance_and_transfers", "spending_amount": 168, "public_investment_component": 8, "current_service_component": 160, "resilience_score": 0.74},
        {"spending_category": "climate_adaptation_and_energy", "spending_amount": 92, "public_investment_component": 76, "current_service_component": 16, "resilience_score": 0.93},
        {"spending_category": "administration_and_courts", "spending_amount": 64, "public_investment_component": 14, "current_service_component": 50, "resilience_score": 0.68},
        {"spending_category": "debt_service", "spending_amount": 45, "public_investment_component": 0, "current_service_component": 45, "resilience_score": 0.22},
    ])


def build_fiscal_multiplier_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"instrument": "high_income_tax_cut", "delta_g": 45, "fiscal_multiplier": 0.35, "slack_index": 0.30, "speed_score": 0.48, "long_run_capacity_score": 0.20},
        {"instrument": "low_income_transfer", "delta_g": 45, "fiscal_multiplier": 1.15, "slack_index": 0.74, "speed_score": 0.86, "long_run_capacity_score": 0.45},
        {"instrument": "unemployment_insurance_expansion", "delta_g": 45, "fiscal_multiplier": 1.25, "slack_index": 0.82, "speed_score": 0.92, "long_run_capacity_score": 0.55},
        {"instrument": "transport_infrastructure", "delta_g": 45, "fiscal_multiplier": 1.55, "slack_index": 0.70, "speed_score": 0.42, "long_run_capacity_score": 0.88},
        {"instrument": "grid_resilience_investment", "delta_g": 45, "fiscal_multiplier": 1.45, "slack_index": 0.66, "speed_score": 0.38, "long_run_capacity_score": 0.94},
        {"instrument": "maintenance_backlog_repair", "delta_g": 45, "fiscal_multiplier": 1.35, "slack_index": 0.68, "speed_score": 0.62, "long_run_capacity_score": 0.86},
    ])


def build_infrastructure_maintenance_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"asset_class": "bridges_and_roads", "maintenance_needed": 95, "maintenance_actual": 66, "failure_risk_index": 0.62, "replacement_cost_if_deferred": 210},
        {"asset_class": "water_systems", "maintenance_needed": 82, "maintenance_actual": 49, "failure_risk_index": 0.70, "replacement_cost_if_deferred": 240},
        {"asset_class": "public_schools", "maintenance_needed": 68, "maintenance_actual": 44, "failure_risk_index": 0.54, "replacement_cost_if_deferred": 155},
        {"asset_class": "electric_grid", "maintenance_needed": 110, "maintenance_actual": 72, "failure_risk_index": 0.76, "replacement_cost_if_deferred": 310},
        {"asset_class": "public_health_systems", "maintenance_needed": 78, "maintenance_actual": 58, "failure_risk_index": 0.58, "replacement_cost_if_deferred": 185},
        {"asset_class": "public_transit", "maintenance_needed": 74, "maintenance_actual": 46, "failure_risk_index": 0.66, "replacement_cost_if_deferred": 170},
    ])


def build_local_fiscal_capacity_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"locality": "high_income_metro_core", "tax_base_per_capita": 88000, "service_need_index": 0.58, "infrastructure_age_index": 0.38, "intergovernmental_transfer_per_capita": 1400},
        {"locality": "inner_suburb_under_stress", "tax_base_per_capita": 52000, "service_need_index": 0.76, "infrastructure_age_index": 0.62, "intergovernmental_transfer_per_capita": 1850},
        {"locality": "rural_low_tax_base", "tax_base_per_capita": 36000, "service_need_index": 0.72, "infrastructure_age_index": 0.74, "intergovernmental_transfer_per_capita": 2100},
        {"locality": "postindustrial_city", "tax_base_per_capita": 42000, "service_need_index": 0.88, "infrastructure_age_index": 0.82, "intergovernmental_transfer_per_capita": 2400},
        {"locality": "wealthy_suburb", "tax_base_per_capita": 112000, "service_need_index": 0.42, "infrastructure_age_index": 0.34, "intergovernmental_transfer_per_capita": 900},
        {"locality": "climate_exposed_coastal_county", "tax_base_per_capita": 61000, "service_need_index": 0.68, "infrastructure_age_index": 0.70, "intergovernmental_transfer_per_capita": 1700},
    ])


def build_public_investment_resilience_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"investment_area": "flood_control_and_water_resilience", "public_investment": 120, "avoided_future_losses": 420, "productivity_gain": 0.10, "equity_score": 0.78, "climate_resilience_score": 0.92},
        {"investment_area": "grid_modernization", "public_investment": 150, "avoided_future_losses": 480, "productivity_gain": 0.14, "equity_score": 0.64, "climate_resilience_score": 0.88},
        {"investment_area": "public_transit_expansion", "public_investment": 110, "avoided_future_losses": 260, "productivity_gain": 0.12, "equity_score": 0.86, "climate_resilience_score": 0.82},
        {"investment_area": "school_retrofit_and_cooling", "public_investment": 80, "avoided_future_losses": 190, "productivity_gain": 0.08, "equity_score": 0.90, "climate_resilience_score": 0.76},
        {"investment_area": "public_health_preparedness", "public_investment": 95, "avoided_future_losses": 360, "productivity_gain": 0.11, "equity_score": 0.82, "climate_resilience_score": 0.72},
        {"investment_area": "ecosystem_restoration", "public_investment": 70, "avoided_future_losses": 220, "productivity_gain": 0.06, "equity_score": 0.70, "climate_resilience_score": 0.90},
    ])


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "fiscal_policy_taxation_public_investment.sqlite"
    names = [
        "fiscal_position_scenarios",
        "tax_distribution_scenarios",
        "spending_composition_scenarios",
        "fiscal_multiplier_scenarios",
        "infrastructure_maintenance_scenarios",
        "local_fiscal_capacity_scenarios",
        "public_investment_resilience_scenarios",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_fiscal_position_scenarios(),
        build_tax_distribution_scenarios(),
        build_spending_composition_scenarios(),
        build_fiscal_multiplier_scenarios(),
        build_infrastructure_maintenance_scenarios(),
        build_local_fiscal_capacity_scenarios(),
        build_public_investment_resilience_scenarios(),
    ]

    filenames = [
        "fiscal_position_scenarios.csv",
        "tax_distribution_scenarios.csv",
        "spending_composition_scenarios.csv",
        "fiscal_multiplier_scenarios.csv",
        "infrastructure_maintenance_scenarios.csv",
        "local_fiscal_capacity_scenarios.csv",
        "public_investment_resilience_scenarios.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created fiscal policy, taxation, and public investment base data.")


if __name__ == "__main__":
    main()
