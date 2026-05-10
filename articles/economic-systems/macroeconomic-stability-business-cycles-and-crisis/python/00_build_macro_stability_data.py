"""
Build stylized datasets for macroeconomic stability, business cycles, and crisis.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_aggregate_demand_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "stable_expansion", "consumption": 560, "investment": 180, "government_spending": 230, "net_exports": -20, "potential_output": 940},
        {"scenario": "investment_slowdown", "consumption": 535, "investment": 120, "government_spending": 230, "net_exports": -25, "potential_output": 945},
        {"scenario": "credit_recession", "consumption": 495, "investment": 85, "government_spending": 238, "net_exports": -18, "potential_output": 950},
        {"scenario": "fiscal_stabilized_recovery", "consumption": 525, "investment": 115, "government_spending": 285, "net_exports": -15, "potential_output": 955},
        {"scenario": "external_export_shock", "consumption": 545, "investment": 150, "government_spending": 235, "net_exports": -85, "potential_output": 960},
        {"scenario": "public_investment_recovery", "consumption": 555, "investment": 155, "government_spending": 310, "net_exports": -30, "potential_output": 970},
    ])


def build_business_cycle_phase_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"year": 1, "cycle_phase": "expansion", "output_index": 100, "employment_index": 100, "expectations_index": 0.68, "credit_growth": 0.06, "inventory_pressure": -0.02},
        {"year": 2, "cycle_phase": "late_expansion", "output_index": 104, "employment_index": 103, "expectations_index": 0.78, "credit_growth": 0.09, "inventory_pressure": 0.01},
        {"year": 3, "cycle_phase": "overextension", "output_index": 107, "employment_index": 104, "expectations_index": 0.82, "credit_growth": 0.12, "inventory_pressure": 0.05},
        {"year": 4, "cycle_phase": "slowdown", "output_index": 105, "employment_index": 103, "expectations_index": 0.55, "credit_growth": 0.02, "inventory_pressure": 0.09},
        {"year": 5, "cycle_phase": "recession", "output_index": 99, "employment_index": 97, "expectations_index": 0.34, "credit_growth": -0.05, "inventory_pressure": 0.08},
        {"year": 6, "cycle_phase": "crisis", "output_index": 93, "employment_index": 90, "expectations_index": 0.22, "credit_growth": -0.09, "inventory_pressure": 0.02},
        {"year": 7, "cycle_phase": "stabilization", "output_index": 96, "employment_index": 92, "expectations_index": 0.40, "credit_growth": -0.01, "inventory_pressure": -0.03},
        {"year": 8, "cycle_phase": "recovery", "output_index": 101, "employment_index": 96, "expectations_index": 0.58, "credit_growth": 0.04, "inventory_pressure": -0.04},
        {"year": 9, "cycle_phase": "renewed_expansion", "output_index": 105, "employment_index": 100, "expectations_index": 0.66, "credit_growth": 0.06, "inventory_pressure": -0.01},
    ])


def build_household_balance_sheet_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"household_group": "secure_median_household", "income": 6200, "debt_service": 720, "liquid_savings": 840, "job_loss_income_shock": 0.12, "price_shock": 0.04},
        {"household_group": "high_debt_low_savings", "income": 4200, "debt_service": 980, "liquid_savings": 180, "job_loss_income_shock": 0.28, "price_shock": 0.07},
        {"household_group": "renter_cost_pressure", "income": 3600, "debt_service": 420, "liquid_savings": 140, "job_loss_income_shock": 0.22, "price_shock": 0.09},
        {"household_group": "asset_rich_high_income", "income": 11800, "debt_service": 1100, "liquid_savings": 3600, "job_loss_income_shock": 0.06, "price_shock": 0.04},
        {"household_group": "precarious_worker_household", "income": 2900, "debt_service": 520, "liquid_savings": 60, "job_loss_income_shock": 0.35, "price_shock": 0.08},
        {"household_group": "retired_fixed_income", "income": 3100, "debt_service": 260, "liquid_savings": 950, "job_loss_income_shock": 0.02, "price_shock": 0.10},
    ])


def build_credit_contraction_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "normal_credit", "credit_growth": 0.05, "nominal_debt": 1000, "price_level": 1.00, "asset_price_change": 0.03, "default_pressure": 0.04},
        {"scenario": "credit_tightening", "credit_growth": -0.03, "nominal_debt": 1000, "price_level": 0.99, "asset_price_change": -0.04, "default_pressure": 0.10},
        {"scenario": "balance_sheet_recession", "credit_growth": -0.08, "nominal_debt": 1000, "price_level": 0.96, "asset_price_change": -0.12, "default_pressure": 0.20},
        {"scenario": "debt_deflation", "credit_growth": -0.12, "nominal_debt": 1000, "price_level": 0.92, "asset_price_change": -0.20, "default_pressure": 0.32},
        {"scenario": "liquidity_backstop", "credit_growth": -0.02, "nominal_debt": 1000, "price_level": 0.985, "asset_price_change": -0.05, "default_pressure": 0.09},
        {"scenario": "public_credit_support", "credit_growth": 0.02, "nominal_debt": 1000, "price_level": 0.995, "asset_price_change": -0.02, "default_pressure": 0.06},
    ])


def build_fiscal_stabilization_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "austerity_downturn", "delta_g": -35, "fiscal_multiplier": 1.25, "automatic_stabilizer_strength": 0.22, "initial_output_gap": -0.045, "public_capacity_score": 0.42},
        {"scenario": "neutral_policy", "delta_g": 0, "fiscal_multiplier": 1.20, "automatic_stabilizer_strength": 0.35, "initial_output_gap": -0.045, "public_capacity_score": 0.56},
        {"scenario": "temporary_transfer_stabilization", "delta_g": 35, "fiscal_multiplier": 1.15, "automatic_stabilizer_strength": 0.62, "initial_output_gap": -0.045, "public_capacity_score": 0.62},
        {"scenario": "public_investment_recovery", "delta_g": 60, "fiscal_multiplier": 1.55, "automatic_stabilizer_strength": 0.58, "initial_output_gap": -0.045, "public_capacity_score": 0.82},
        {"scenario": "resilience_oriented_recovery", "delta_g": 75, "fiscal_multiplier": 1.65, "automatic_stabilizer_strength": 0.72, "initial_output_gap": -0.045, "public_capacity_score": 0.90},
    ])


def build_open_economy_shock_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"external_shock": "export_demand_decline", "shock_intensity": 0.30, "export_exposure": 0.42, "import_price_exposure": 0.12, "capital_flow_exposure": 0.20, "fx_debt_exposure": 0.16},
        {"external_shock": "energy_import_price_spike", "shock_intensity": 0.40, "export_exposure": 0.10, "import_price_exposure": 0.72, "capital_flow_exposure": 0.14, "fx_debt_exposure": 0.10},
        {"external_shock": "capital_flow_reversal", "shock_intensity": 0.35, "export_exposure": 0.16, "import_price_exposure": 0.18, "capital_flow_exposure": 0.78, "fx_debt_exposure": 0.52},
        {"external_shock": "global_supply_chain_disruption", "shock_intensity": 0.32, "export_exposure": 0.36, "import_price_exposure": 0.48, "capital_flow_exposure": 0.22, "fx_debt_exposure": 0.18},
        {"external_shock": "reserve_currency_tightening", "shock_intensity": 0.28, "export_exposure": 0.18, "import_price_exposure": 0.25, "capital_flow_exposure": 0.64, "fx_debt_exposure": 0.68},
    ])


def build_inflation_unemployment_policy_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "demand_overheating", "inflation_pressure": 0.70, "unemployment_gap": -0.025, "supply_shock_intensity": 0.10, "policy_rate_response": 0.55},
        {"scenario": "supply_shock_stagflation", "inflation_pressure": 0.78, "unemployment_gap": 0.020, "supply_shock_intensity": 0.72, "policy_rate_response": 0.45},
        {"scenario": "weak_demand_low_inflation", "inflation_pressure": 0.22, "unemployment_gap": 0.045, "supply_shock_intensity": 0.08, "policy_rate_response": -0.35},
        {"scenario": "profit_margin_price_pressure", "inflation_pressure": 0.58, "unemployment_gap": 0.010, "supply_shock_intensity": 0.34, "policy_rate_response": 0.32},
        {"scenario": "balanced_soft_landing", "inflation_pressure": 0.36, "unemployment_gap": 0.005, "supply_shock_intensity": 0.16, "policy_rate_response": 0.10},
    ])


def build_crisis_recovery_path_scenarios() -> pd.DataFrame:
    rows = []
    recovery_paths = {
        "austerity_recovery": [100, 96, 93, 92, 93, 94, 95, 96],
        "neutral_recovery": [100, 96, 93, 94, 96, 98, 100, 102],
        "liquidity_only_recovery": [100, 96, 93, 95, 97, 99, 101, 103],
        "public_investment_recovery": [100, 96, 93, 96, 100, 104, 108, 111],
        "resilience_recovery": [100, 96, 93, 97, 102, 107, 112, 116],
    }

    for path, values in recovery_paths.items():
        for period, output_index in enumerate(values):
            rows.append({
                "recovery_path": path,
                "period": period,
                "output_index": output_index,
                "employment_index": 100 - (100 - output_index) * 0.72,
                "public_capacity_index": output_index if "public" in path or "resilience" in path else output_index - 3,
            })

    return pd.DataFrame(rows)


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "macroeconomic_stability_business_cycles_crisis.sqlite"
    names = [
        "aggregate_demand_scenarios",
        "business_cycle_phase_scenarios",
        "household_balance_sheet_scenarios",
        "credit_contraction_scenarios",
        "fiscal_stabilization_scenarios",
        "open_economy_shock_scenarios",
        "inflation_unemployment_policy_scenarios",
        "crisis_recovery_path_scenarios",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_aggregate_demand_scenarios(),
        build_business_cycle_phase_scenarios(),
        build_household_balance_sheet_scenarios(),
        build_credit_contraction_scenarios(),
        build_fiscal_stabilization_scenarios(),
        build_open_economy_shock_scenarios(),
        build_inflation_unemployment_policy_scenarios(),
        build_crisis_recovery_path_scenarios(),
    ]

    filenames = [
        "aggregate_demand_scenarios.csv",
        "business_cycle_phase_scenarios.csv",
        "household_balance_sheet_scenarios.csv",
        "credit_contraction_scenarios.csv",
        "fiscal_stabilization_scenarios.csv",
        "open_economy_shock_scenarios.csv",
        "inflation_unemployment_policy_scenarios.csv",
        "crisis_recovery_path_scenarios.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created macroeconomic stability, business cycles, and crisis base data.")


if __name__ == "__main__":
    main()
