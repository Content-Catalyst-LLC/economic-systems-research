"""
Build stylized datasets for monetary policy, central banking, and financial conditions.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_policy_rate_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "low_inflation_slack", "nominal_rate": 0.020, "expected_inflation": 0.018, "neutral_rate": 0.025, "inflation_gap": -0.005, "output_gap": -0.025, "a_inflation": 1.20, "b_output": 0.50},
        {"scenario": "balanced_soft_landing", "nominal_rate": 0.040, "expected_inflation": 0.024, "neutral_rate": 0.028, "inflation_gap": 0.003, "output_gap": -0.003, "a_inflation": 1.20, "b_output": 0.50},
        {"scenario": "demand_overheating", "nominal_rate": 0.060, "expected_inflation": 0.036, "neutral_rate": 0.030, "inflation_gap": 0.018, "output_gap": 0.020, "a_inflation": 1.30, "b_output": 0.60},
        {"scenario": "supply_shock_stagflation", "nominal_rate": 0.055, "expected_inflation": 0.044, "neutral_rate": 0.030, "inflation_gap": 0.022, "output_gap": -0.015, "a_inflation": 1.15, "b_output": 0.40},
        {"scenario": "financial_stress_easing", "nominal_rate": 0.025, "expected_inflation": 0.020, "neutral_rate": 0.030, "inflation_gap": -0.002, "output_gap": -0.035, "a_inflation": 1.00, "b_output": 0.75},
        {"scenario": "credibility_tightening", "nominal_rate": 0.070, "expected_inflation": 0.040, "neutral_rate": 0.030, "inflation_gap": 0.025, "output_gap": 0.000, "a_inflation": 1.50, "b_output": 0.40},
    ])


def build_debt_service_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"borrower_group": "fixed_rate_household", "income": 6200, "debt_service": 1350, "repricing_share": 0.05, "rate_shock": 0.020, "debt_stock": 320000},
        {"borrower_group": "floating_rate_household", "income": 5600, "debt_service": 1450, "repricing_share": 0.80, "rate_shock": 0.020, "debt_stock": 280000},
        {"borrower_group": "small_business_bank_dependent", "income": 22000, "debt_service": 4100, "repricing_share": 0.65, "rate_shock": 0.025, "debt_stock": 460000},
        {"borrower_group": "large_firm_bond_financed", "income": 180000, "debt_service": 21000, "repricing_share": 0.20, "rate_shock": 0.018, "debt_stock": 2900000},
        {"borrower_group": "local_government_short_duration", "income": 95000, "debt_service": 12500, "repricing_share": 0.45, "rate_shock": 0.018, "debt_stock": 1300000},
        {"borrower_group": "public_infrastructure_authority", "income": 125000, "debt_service": 14200, "repricing_share": 0.28, "rate_shock": 0.016, "debt_stock": 2100000},
    ])


def build_financial_conditions_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "easy_credit_conditions", "policy_rate": 0.025, "credit_spread": 0.010, "equity_price_change": 0.12, "exchange_rate_pressure": -0.010, "lending_tightness": 0.10, "market_liquidity_stress": 0.10},
        {"scenario": "neutral_conditions", "policy_rate": 0.040, "credit_spread": 0.020, "equity_price_change": 0.00, "exchange_rate_pressure": 0.000, "lending_tightness": 0.25, "market_liquidity_stress": 0.20},
        {"scenario": "rate_tightening", "policy_rate": 0.060, "credit_spread": 0.030, "equity_price_change": -0.08, "exchange_rate_pressure": 0.020, "lending_tightness": 0.45, "market_liquidity_stress": 0.32},
        {"scenario": "market_stress_without_rate_hike", "policy_rate": 0.040, "credit_spread": 0.070, "equity_price_change": -0.18, "exchange_rate_pressure": 0.050, "lending_tightness": 0.70, "market_liquidity_stress": 0.68},
        {"scenario": "crisis_liquidity_freeze", "policy_rate": 0.030, "credit_spread": 0.110, "equity_price_change": -0.32, "exchange_rate_pressure": 0.080, "lending_tightness": 0.88, "market_liquidity_stress": 0.92},
        {"scenario": "resilience_oriented_stabilization", "policy_rate": 0.035, "credit_spread": 0.025, "equity_price_change": -0.02, "exchange_rate_pressure": 0.010, "lending_tightness": 0.32, "market_liquidity_stress": 0.24},
    ])


def build_asset_valuation_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"asset_class": "short_duration_bond", "cash_flow": 105, "discount_rate": 0.035, "duration_years": 2, "rate_shock": 0.015},
        {"asset_class": "long_duration_bond", "cash_flow": 105, "discount_rate": 0.035, "duration_years": 12, "rate_shock": 0.015},
        {"asset_class": "growth_equity", "cash_flow": 12, "discount_rate": 0.070, "duration_years": 20, "rate_shock": 0.020},
        {"asset_class": "income_equity", "cash_flow": 18, "discount_rate": 0.075, "duration_years": 10, "rate_shock": 0.018},
        {"asset_class": "commercial_real_estate", "cash_flow": 45, "discount_rate": 0.060, "duration_years": 15, "rate_shock": 0.025},
        {"asset_class": "public_infrastructure_cash_flow", "cash_flow": 28, "discount_rate": 0.045, "duration_years": 25, "rate_shock": 0.012},
    ])


def build_bank_liquidity_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"institution": "stable_retail_bank", "liquid_assets": 240, "short_term_outflows": 150, "deposit_outflow_shock": 0.10, "collateral_quality": 0.90, "central_bank_access": 0.80},
        {"institution": "regional_duration_mismatch_bank", "liquid_assets": 120, "short_term_outflows": 180, "deposit_outflow_shock": 0.28, "collateral_quality": 0.64, "central_bank_access": 0.70},
        {"institution": "wholesale_funded_bank", "liquid_assets": 160, "short_term_outflows": 260, "deposit_outflow_shock": 0.34, "collateral_quality": 0.72, "central_bank_access": 0.65},
        {"institution": "shadow_credit_vehicle", "liquid_assets": 45, "short_term_outflows": 140, "deposit_outflow_shock": 0.42, "collateral_quality": 0.55, "central_bank_access": 0.18},
        {"institution": "systemically_important_bank", "liquid_assets": 420, "short_term_outflows": 360, "deposit_outflow_shock": 0.22, "collateral_quality": 0.82, "central_bank_access": 0.92},
    ])


def build_open_economy_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "reserve_currency_stable", "domestic_rate": 0.045, "world_rate": 0.040, "risk_premium": 0.010, "capital_flow_pressure": -0.02, "fx_debt_exposure": 0.10, "import_price_exposure": 0.20},
        {"scenario": "capital_outflow_pressure", "domestic_rate": 0.050, "world_rate": 0.060, "risk_premium": 0.035, "capital_flow_pressure": 0.18, "fx_debt_exposure": 0.38, "import_price_exposure": 0.42},
        {"scenario": "energy_import_currency_stress", "domestic_rate": 0.055, "world_rate": 0.050, "risk_premium": 0.030, "capital_flow_pressure": 0.12, "fx_debt_exposure": 0.22, "import_price_exposure": 0.70},
        {"scenario": "dominant_currency_tightening_spillover", "domestic_rate": 0.045, "world_rate": 0.065, "risk_premium": 0.040, "capital_flow_pressure": 0.22, "fx_debt_exposure": 0.46, "import_price_exposure": 0.36},
        {"scenario": "capital_controls_buffer", "domestic_rate": 0.040, "world_rate": 0.055, "risk_premium": 0.022, "capital_flow_pressure": 0.06, "fx_debt_exposure": 0.18, "import_price_exposure": 0.30},
    ])


def build_public_debt_interaction_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "long_maturity_low_rate", "public_debt": 1200, "average_interest_rate": 0.025, "share_rolling_over": 0.12, "rate_shock": 0.015, "output": 1800, "public_investment_need": 130},
        {"scenario": "short_maturity_rate_shock", "public_debt": 1200, "average_interest_rate": 0.032, "share_rolling_over": 0.42, "rate_shock": 0.025, "output": 1760, "public_investment_need": 150},
        {"scenario": "high_debt_tightening", "public_debt": 1600, "average_interest_rate": 0.040, "share_rolling_over": 0.34, "rate_shock": 0.022, "output": 1820, "public_investment_need": 170},
        {"scenario": "resilience_investment_priority", "public_debt": 1350, "average_interest_rate": 0.035, "share_rolling_over": 0.22, "rate_shock": 0.014, "output": 1900, "public_investment_need": 210},
        {"scenario": "fiscal_space_constrained", "public_debt": 1500, "average_interest_rate": 0.052, "share_rolling_over": 0.48, "rate_shock": 0.020, "output": 1700, "public_investment_need": 190},
    ])


def build_sustainable_investment_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"investment_area": "grid_modernization", "expected_social_return": 0.095, "financing_cost": 0.045, "rate_shock": 0.015, "investment_scale": 180, "strategic_priority": 0.92},
        {"investment_area": "public_transit", "expected_social_return": 0.080, "financing_cost": 0.044, "rate_shock": 0.014, "investment_scale": 130, "strategic_priority": 0.86},
        {"investment_area": "water_resilience", "expected_social_return": 0.088, "financing_cost": 0.043, "rate_shock": 0.012, "investment_scale": 115, "strategic_priority": 0.90},
        {"investment_area": "housing_supply", "expected_social_return": 0.075, "financing_cost": 0.050, "rate_shock": 0.020, "investment_scale": 220, "strategic_priority": 0.84},
        {"investment_area": "climate_adaptation", "expected_social_return": 0.092, "financing_cost": 0.046, "rate_shock": 0.016, "investment_scale": 155, "strategic_priority": 0.94},
        {"investment_area": "speculative_real_estate", "expected_social_return": 0.040, "financing_cost": 0.055, "rate_shock": 0.025, "investment_scale": 250, "strategic_priority": 0.22},
    ])


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "monetary_policy_central_banking_financial_conditions.sqlite"
    names = [
        "policy_rate_scenarios",
        "debt_service_scenarios",
        "financial_conditions_scenarios",
        "asset_valuation_scenarios",
        "bank_liquidity_scenarios",
        "open_economy_scenarios",
        "public_debt_interaction_scenarios",
        "sustainable_investment_scenarios",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_policy_rate_scenarios(),
        build_debt_service_scenarios(),
        build_financial_conditions_scenarios(),
        build_asset_valuation_scenarios(),
        build_bank_liquidity_scenarios(),
        build_open_economy_scenarios(),
        build_public_debt_interaction_scenarios(),
        build_sustainable_investment_scenarios(),
    ]

    filenames = [
        "policy_rate_scenarios.csv",
        "debt_service_scenarios.csv",
        "financial_conditions_scenarios.csv",
        "asset_valuation_scenarios.csv",
        "bank_liquidity_scenarios.csv",
        "open_economy_scenarios.csv",
        "public_debt_interaction_scenarios.csv",
        "sustainable_investment_scenarios.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created monetary policy, central banking, and financial conditions base data.")


if __name__ == "__main__":
    main()
