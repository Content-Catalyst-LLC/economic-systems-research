"""
Build stylized datasets for finance, leverage, and systemic risk.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_institution_balance_sheets() -> pd.DataFrame:
    return pd.DataFrame([
        {"institution": "conservative_bank", "assets": 1000, "debt": 880, "liquid_assets": 230, "short_term_liabilities": 170, "common_exposure_share": 0.22},
        {"institution": "leveraged_credit_fund", "assets": 1200, "debt": 1120, "liquid_assets": 90, "short_term_liabilities": 310, "common_exposure_share": 0.62},
        {"institution": "shadow_banking_vehicle", "assets": 950, "debt": 900, "liquid_assets": 55, "short_term_liabilities": 340, "common_exposure_share": 0.74},
        {"institution": "public_development_bank", "assets": 1400, "debt": 1180, "liquid_assets": 360, "short_term_liabilities": 210, "common_exposure_share": 0.28},
        {"institution": "mortgage_lender", "assets": 1100, "debt": 1010, "liquid_assets": 120, "short_term_liabilities": 260, "common_exposure_share": 0.70},
        {"institution": "insurance_asset_manager", "assets": 1300, "debt": 1090, "liquid_assets": 260, "short_term_liabilities": 180, "common_exposure_share": 0.38},
    ])


def build_asset_shock_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"shock_name": "mild_price_decline", "asset_shock": 0.02},
        {"shock_name": "moderate_price_decline", "asset_shock": 0.05},
        {"shock_name": "severe_price_decline", "asset_shock": 0.10},
        {"shock_name": "crisis_price_decline", "asset_shock": 0.18},
        {"shock_name": "tail_price_decline", "asset_shock": 0.28},
    ])


def build_collateral_haircut_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "stable_repo_market", "collateral_value": 850, "haircut_before": 0.08, "haircut_after": 0.10, "outstanding_borrowing": 760},
        {"scenario": "haircut_jump", "collateral_value": 850, "haircut_before": 0.10, "haircut_after": 0.22, "outstanding_borrowing": 760},
        {"scenario": "collateral_price_drop", "collateral_value": 720, "haircut_before": 0.10, "haircut_after": 0.20, "outstanding_borrowing": 760},
        {"scenario": "combined_price_and_haircut_shock", "collateral_value": 650, "haircut_before": 0.10, "haircut_after": 0.30, "outstanding_borrowing": 760},
        {"scenario": "central_bank_backstop", "collateral_value": 780, "haircut_before": 0.10, "haircut_after": 0.14, "outstanding_borrowing": 760},
    ])


def build_funding_gap_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"institution": "conservative_bank", "short_term_liabilities": 170, "liquid_assets": 230, "rollover_rate": 0.86, "emergency_liquidity_access": 0.70},
        {"institution": "leveraged_credit_fund", "short_term_liabilities": 310, "liquid_assets": 90, "rollover_rate": 0.52, "emergency_liquidity_access": 0.12},
        {"institution": "shadow_banking_vehicle", "short_term_liabilities": 340, "liquid_assets": 55, "rollover_rate": 0.36, "emergency_liquidity_access": 0.08},
        {"institution": "public_development_bank", "short_term_liabilities": 210, "liquid_assets": 360, "rollover_rate": 0.90, "emergency_liquidity_access": 0.82},
        {"institution": "mortgage_lender", "short_term_liabilities": 260, "liquid_assets": 120, "rollover_rate": 0.60, "emergency_liquidity_access": 0.30},
    ])


def build_network_exposure_matrix() -> pd.DataFrame:
    rows = [
        {"from_institution": "conservative_bank", "to_institution": "leveraged_credit_fund", "exposure": 42},
        {"from_institution": "conservative_bank", "to_institution": "mortgage_lender", "exposure": 65},
        {"from_institution": "leveraged_credit_fund", "to_institution": "shadow_banking_vehicle", "exposure": 92},
        {"from_institution": "leveraged_credit_fund", "to_institution": "mortgage_lender", "exposure": 84},
        {"from_institution": "shadow_banking_vehicle", "to_institution": "leveraged_credit_fund", "exposure": 74},
        {"from_institution": "shadow_banking_vehicle", "to_institution": "insurance_asset_manager", "exposure": 55},
        {"from_institution": "mortgage_lender", "to_institution": "conservative_bank", "exposure": 58},
        {"from_institution": "mortgage_lender", "to_institution": "shadow_banking_vehicle", "exposure": 70},
        {"from_institution": "insurance_asset_manager", "to_institution": "leveraged_credit_fund", "exposure": 46},
        {"from_institution": "insurance_asset_manager", "to_institution": "public_development_bank", "exposure": 32},
        {"from_institution": "public_development_bank", "to_institution": "conservative_bank", "exposure": 28},
        {"from_institution": "public_development_bank", "to_institution": "mortgage_lender", "exposure": 35},
    ]
    return pd.DataFrame(rows)


def build_household_leverage_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"household_group": "low_ltv_stable_income", "housing_value": 420, "mortgage_debt": 220, "liquid_savings": 45, "income": 95, "debt_service": 23},
        {"household_group": "high_ltv_median_income", "housing_value": 360, "mortgage_debt": 325, "liquid_savings": 18, "income": 72, "debt_service": 26},
        {"household_group": "variable_rate_stretched", "housing_value": 330, "mortgage_debt": 310, "liquid_savings": 9, "income": 64, "debt_service": 31},
        {"household_group": "renter_consumer_debt", "housing_value": 0, "mortgage_debt": 0, "liquid_savings": 5, "income": 42, "debt_service": 12},
        {"household_group": "asset_rich_high_income", "housing_value": 880, "mortgage_debt": 360, "liquid_savings": 150, "income": 210, "debt_service": 38},
    ])


def build_macroprudential_buffer_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "thin_buffers_procyclical", "capital_buffer": 0.045, "liquidity_buffer": 0.12, "countercyclical_buffer": 0.00, "loan_to_value_limit": 0.95, "stress_test_strength": 0.35},
        {"scenario": "moderate_macroprudential", "capital_buffer": 0.075, "liquidity_buffer": 0.20, "countercyclical_buffer": 0.015, "loan_to_value_limit": 0.85, "stress_test_strength": 0.62},
        {"scenario": "strong_countercyclical", "capital_buffer": 0.095, "liquidity_buffer": 0.26, "countercyclical_buffer": 0.030, "loan_to_value_limit": 0.75, "stress_test_strength": 0.82},
        {"scenario": "shadow_gap_regulatory_arbitrage", "capital_buffer": 0.060, "liquidity_buffer": 0.16, "countercyclical_buffer": 0.010, "loan_to_value_limit": 0.90, "stress_test_strength": 0.42},
        {"scenario": "resilience_oriented", "capital_buffer": 0.105, "liquidity_buffer": 0.30, "countercyclical_buffer": 0.035, "loan_to_value_limit": 0.70, "stress_test_strength": 0.90},
    ])


def build_sustainability_shock_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"shock": "fossil_stranded_asset", "portfolio_exposure": 0.34, "loss_given_shock": 0.42, "liquidity_impact": 0.30, "public_backstop_need": 0.46},
        {"shock": "climate_insurance_withdrawal", "portfolio_exposure": 0.26, "loss_given_shock": 0.35, "liquidity_impact": 0.38, "public_backstop_need": 0.55},
        {"shock": "infrastructure_failure_credit_event", "portfolio_exposure": 0.22, "loss_given_shock": 0.28, "liquidity_impact": 0.25, "public_backstop_need": 0.60},
        {"shock": "green_bubble_repricing", "portfolio_exposure": 0.18, "loss_given_shock": 0.30, "liquidity_impact": 0.22, "public_backstop_need": 0.24},
        {"shock": "resilience_investment_buffer", "portfolio_exposure": 0.12, "loss_given_shock": 0.10, "liquidity_impact": 0.08, "public_backstop_need": 0.12},
    ])


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "finance_leverage_systemic_risk.sqlite"
    names = [
        "institution_balance_sheets",
        "asset_shock_scenarios",
        "collateral_haircut_scenarios",
        "funding_gap_scenarios",
        "network_exposure_matrix",
        "household_leverage_scenarios",
        "macroprudential_buffer_scenarios",
        "sustainability_shock_scenarios",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_institution_balance_sheets(),
        build_asset_shock_scenarios(),
        build_collateral_haircut_scenarios(),
        build_funding_gap_scenarios(),
        build_network_exposure_matrix(),
        build_household_leverage_scenarios(),
        build_macroprudential_buffer_scenarios(),
        build_sustainability_shock_scenarios(),
    ]

    filenames = [
        "institution_balance_sheets.csv",
        "asset_shock_scenarios.csv",
        "collateral_haircut_scenarios.csv",
        "funding_gap_scenarios.csv",
        "network_exposure_matrix.csv",
        "household_leverage_scenarios.csv",
        "macroprudential_buffer_scenarios.csv",
        "sustainability_shock_scenarios.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created finance, leverage, and systemic risk base data.")


if __name__ == "__main__":
    main()
