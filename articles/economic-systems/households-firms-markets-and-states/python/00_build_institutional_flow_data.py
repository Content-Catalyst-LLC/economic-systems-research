"""
Build stylized institutional-flow data for households, firms, markets, and states.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_actors() -> pd.DataFrame:
    rows = [
        {
            "actor": "Households",
            "core_role": "Consumption, labor supply, saving, borrowing, care, and social reproduction",
            "main_inputs": "Wages, transfers, assets, public services, credit, time, care capacity",
            "main_outputs": "Labor, consumption demand, savings, caregiving, intergenerational support",
            "risk_absorption_role": "Absorbs income shocks, price shocks, care burdens, debt stress, and insecurity",
        },
        {
            "actor": "Firms",
            "core_role": "Production, investment, employment, innovation, and supply-chain organization",
            "main_inputs": "Labor, capital, credit, materials, infrastructure, technology, legal order",
            "main_outputs": "Goods, services, wages, profits, investment, innovation, market supply",
            "risk_absorption_role": "Absorbs or shifts demand risk, input-cost risk, financing risk, and competitive risk",
        },
        {
            "actor": "Markets",
            "core_role": "Exchange coordination through prices, contracts, competition, and information",
            "main_inputs": "Money, law, trust, infrastructure, standards, purchasing power, tradable goods",
            "main_outputs": "Prices, exchange flows, allocation signals, competition, liquidity, access channels",
            "risk_absorption_role": "Transmits price volatility, credit conditions, market power, and exclusion by purchasing power",
        },
        {
            "actor": "States",
            "core_role": "Legal order, public goods, regulation, taxation, redistribution, and stabilization",
            "main_inputs": "Tax revenue, borrowing capacity, legitimacy, administrative capacity, public trust",
            "main_outputs": "Infrastructure, public services, transfers, regulation, stabilization, collective insurance",
            "risk_absorption_role": "Absorbs systemic risk through public finance, social insurance, emergency response, and regulation",
        },
    ]
    return pd.DataFrame(rows)


def build_flow_scenarios() -> pd.DataFrame:
    rows = [
        {
            "scenario": "baseline",
            "household_wages": 500,
            "household_transfers": 120,
            "asset_income": 80,
            "taxes_paid": 140,
            "debt_service": 60,
            "household_consumption": 380,
            "firm_revenue": 900,
            "labor_cost": 500,
            "capital_cost": 120,
            "input_cost": 180,
            "public_spending": 260,
            "public_transfers": 120,
            "public_debt_interest": 40,
            "tax_revenue": 140,
        },
        {
            "scenario": "household_stress",
            "household_wages": 455,
            "household_transfers": 130,
            "asset_income": 55,
            "taxes_paid": 118,
            "debt_service": 85,
            "household_consumption": 380,
            "firm_revenue": 850,
            "labor_cost": 455,
            "capital_cost": 125,
            "input_cost": 185,
            "public_spending": 280,
            "public_transfers": 130,
            "public_debt_interest": 45,
            "tax_revenue": 118,
        },
        {
            "scenario": "public_stabilization",
            "household_wages": 480,
            "household_transfers": 165,
            "asset_income": 60,
            "taxes_paid": 125,
            "debt_service": 70,
            "household_consumption": 400,
            "firm_revenue": 890,
            "labor_cost": 480,
            "capital_cost": 115,
            "input_cost": 175,
            "public_spending": 330,
            "public_transfers": 165,
            "public_debt_interest": 48,
            "tax_revenue": 125,
        },
        {
            "scenario": "firm_margin_pressure",
            "household_wages": 510,
            "household_transfers": 115,
            "asset_income": 75,
            "taxes_paid": 145,
            "debt_service": 65,
            "household_consumption": 390,
            "firm_revenue": 880,
            "labor_cost": 510,
            "capital_cost": 145,
            "input_cost": 215,
            "public_spending": 260,
            "public_transfers": 115,
            "public_debt_interest": 42,
            "tax_revenue": 145,
        },
        {
            "scenario": "high_capacity_public_goods",
            "household_wages": 535,
            "household_transfers": 135,
            "asset_income": 85,
            "taxes_paid": 175,
            "debt_service": 55,
            "household_consumption": 410,
            "firm_revenue": 980,
            "labor_cost": 535,
            "capital_cost": 130,
            "input_cost": 190,
            "public_spending": 340,
            "public_transfers": 135,
            "public_debt_interest": 42,
            "tax_revenue": 175,
        },
    ]
    return pd.DataFrame(rows)


def build_market_access_scenarios() -> pd.DataFrame:
    rows = [
        {"group": "asset_secure_households", "need_index": 0.45, "income_command": 0.92, "price_burden": 0.45, "institutional_access": 0.82, "population_weight": 0.16},
        {"group": "stable_wage_households", "need_index": 0.60, "income_command": 0.68, "price_burden": 0.62, "institutional_access": 0.70, "population_weight": 0.28},
        {"group": "rent_burdened_workers", "need_index": 0.82, "income_command": 0.42, "price_burden": 0.85, "institutional_access": 0.52, "population_weight": 0.24},
        {"group": "care_constrained_households", "need_index": 0.86, "income_command": 0.38, "price_burden": 0.78, "institutional_access": 0.44, "population_weight": 0.16},
        {"group": "informal_or_precarious_workers", "need_index": 0.88, "income_command": 0.30, "price_burden": 0.82, "institutional_access": 0.34, "population_weight": 0.10},
        {"group": "climate_exposed_low_access", "need_index": 0.92, "income_command": 0.28, "price_burden": 0.88, "institutional_access": 0.30, "population_weight": 0.06},
    ]
    return pd.DataFrame(rows)


def build_risk_distribution_scenarios() -> pd.DataFrame:
    rows = [
        {"scenario": "baseline", "household_risk": 0.30, "firm_risk": 0.24, "market_risk": 0.20, "state_risk": 0.26},
        {"scenario": "privatized_risk", "household_risk": 0.48, "firm_risk": 0.24, "market_risk": 0.18, "state_risk": 0.10},
        {"scenario": "public_insurance", "household_risk": 0.22, "firm_risk": 0.20, "market_risk": 0.18, "state_risk": 0.40},
        {"scenario": "firm_and_market_power", "household_risk": 0.40, "firm_risk": 0.15, "market_risk": 0.32, "state_risk": 0.13},
        {"scenario": "balanced_resilience", "household_risk": 0.24, "firm_risk": 0.24, "market_risk": 0.22, "state_risk": 0.30},
    ]
    return pd.DataFrame(rows)


def save_sqlite(actors, flows, access, risk) -> None:
    db_path = PROCESSED_DIR / "households_firms_markets_states.sqlite"
    with sqlite3.connect(db_path) as conn:
        actors.to_sql("institutional_actors", conn, if_exists="replace", index=False)
        flows.to_sql("institutional_flow_scenarios", conn, if_exists="replace", index=False)
        access.to_sql("market_access_scenarios", conn, if_exists="replace", index=False)
        risk.to_sql("risk_distribution_scenarios", conn, if_exists="replace", index=False)


def main() -> None:
    actors = build_actors()
    flows = build_flow_scenarios()
    access = build_market_access_scenarios()
    risk = build_risk_distribution_scenarios()

    actors.to_csv(PROCESSED_DIR / "institutional_actors.csv", index=False)
    flows.to_csv(PROCESSED_DIR / "institutional_flow_scenarios.csv", index=False)
    access.to_csv(PROCESSED_DIR / "market_access_scenarios.csv", index=False)
    risk.to_csv(PROCESSED_DIR / "risk_distribution_scenarios.csv", index=False)

    save_sqlite(actors, flows, access, risk)
    print("Created households-firms-markets-states base data.")


if __name__ == "__main__":
    main()
