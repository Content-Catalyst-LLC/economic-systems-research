"""
Build stylized datasets for money, banking, credit, and financial intermediation.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_money_aggregate_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "baseline_deposit_money_system", "currency": 220, "deposits": 880, "near_money_claims": 420, "central_bank_reserves": 160},
        {"scenario": "cash_preference_stress", "currency": 310, "deposits": 760, "near_money_claims": 360, "central_bank_reserves": 220},
        {"scenario": "credit_expansion", "currency": 230, "deposits": 1120, "near_money_claims": 580, "central_bank_reserves": 210},
        {"scenario": "deposit_outflow_pressure", "currency": 260, "deposits": 720, "near_money_claims": 430, "central_bank_reserves": 190},
        {"scenario": "safe_liquidity_preference", "currency": 280, "deposits": 840, "near_money_claims": 300, "central_bank_reserves": 260},
    ])


def build_bank_balance_sheet_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"bank": "community_bank_stable", "assets": 1000, "equity": 115, "loans": 690, "bank_deposits": 760, "liquid_assets": 190, "wholesale_funding": 80},
        {"bank": "fast_growth_lender", "assets": 1300, "equity": 95, "loans": 1040, "bank_deposits": 820, "liquid_assets": 110, "wholesale_funding": 360},
        {"bank": "high_liquidity_bank", "assets": 1100, "equity": 125, "loans": 610, "bank_deposits": 800, "liquid_assets": 330, "wholesale_funding": 90},
        {"bank": "commercial_real_estate_exposed", "assets": 1250, "equity": 90, "loans": 980, "bank_deposits": 740, "liquid_assets": 120, "wholesale_funding": 390},
        {"bank": "public_development_bank", "assets": 1450, "equity": 180, "loans": 980, "bank_deposits": 650, "liquid_assets": 280, "wholesale_funding": 300},
    ])


def build_debt_service_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"borrower_group": "median_household_mortgage", "income_or_ebit": 6200, "interest_payment": 980, "principal_payment": 1320, "rate_shock_bps": 100},
        {"borrower_group": "low_income_household_high_cost_credit", "income_or_ebit": 2800, "interest_payment": 520, "principal_payment": 460, "rate_shock_bps": 250},
        {"borrower_group": "small_business_working_capital", "income_or_ebit": 950, "interest_payment": 180, "principal_payment": 210, "rate_shock_bps": 200},
        {"borrower_group": "leveraged_corporate", "income_or_ebit": 1600, "interest_payment": 520, "principal_payment": 420, "rate_shock_bps": 175},
        {"borrower_group": "public_infrastructure_authority", "income_or_ebit": 2400, "interest_payment": 430, "principal_payment": 360, "rate_shock_bps": 125},
        {"borrower_group": "precarious_renter_consumer_debt", "income_or_ebit": 2400, "interest_payment": 380, "principal_payment": 540, "rate_shock_bps": 300},
    ])


def build_liquidity_stress_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"institution": "community_bank_stable", "hqla": 190, "net_cash_outflows": 130, "deposit_outflow_rate": 0.12, "market_funding_rollover_rate": 0.82},
        {"institution": "fast_growth_lender", "hqla": 110, "net_cash_outflows": 190, "deposit_outflow_rate": 0.22, "market_funding_rollover_rate": 0.54},
        {"institution": "high_liquidity_bank", "hqla": 330, "net_cash_outflows": 150, "deposit_outflow_rate": 0.10, "market_funding_rollover_rate": 0.88},
        {"institution": "shadow_credit_vehicle", "hqla": 80, "net_cash_outflows": 170, "deposit_outflow_rate": 0.00, "market_funding_rollover_rate": 0.42},
        {"institution": "public_development_bank", "hqla": 280, "net_cash_outflows": 155, "deposit_outflow_rate": 0.08, "market_funding_rollover_rate": 0.86},
    ])


def build_credit_allocation_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"credit_channel": "productive_business_investment", "flow_share": 0.22, "productive_score": 0.86, "speculation_score": 0.10, "resilience_score": 0.58, "inclusion_score": 0.54},
        {"credit_channel": "mortgage_housing_access", "flow_share": 0.24, "productive_score": 0.52, "speculation_score": 0.38, "resilience_score": 0.50, "inclusion_score": 0.62},
        {"credit_channel": "property_speculation", "flow_share": 0.18, "productive_score": 0.22, "speculation_score": 0.90, "resilience_score": 0.16, "inclusion_score": 0.20},
        {"credit_channel": "public_infrastructure", "flow_share": 0.14, "productive_score": 0.78, "speculation_score": 0.05, "resilience_score": 0.86, "inclusion_score": 0.78},
        {"credit_channel": "consumer_high_cost_credit", "flow_share": 0.08, "productive_score": 0.18, "speculation_score": 0.52, "resilience_score": 0.12, "inclusion_score": 0.18},
        {"credit_channel": "green_transition_finance", "flow_share": 0.09, "productive_score": 0.74, "speculation_score": 0.12, "resilience_score": 0.90, "inclusion_score": 0.64},
        {"credit_channel": "small_business_community_credit", "flow_share": 0.05, "productive_score": 0.72, "speculation_score": 0.08, "resilience_score": 0.66, "inclusion_score": 0.82},
    ])


def build_monetary_hierarchy_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"claim": "central_bank_reserves", "safety_score": 1.00, "liquidity_score": 1.00, "public_backstop_score": 1.00, "collateral_acceptance_score": 1.00},
        {"claim": "insured_bank_deposits", "safety_score": 0.88, "liquidity_score": 0.92, "public_backstop_score": 0.90, "collateral_acceptance_score": 0.70},
        {"claim": "uninsured_large_deposits", "safety_score": 0.68, "liquidity_score": 0.82, "public_backstop_score": 0.58, "collateral_acceptance_score": 0.55},
        {"claim": "treasury_securities", "safety_score": 0.96, "liquidity_score": 0.94, "public_backstop_score": 0.86, "collateral_acceptance_score": 0.98},
        {"claim": "repo_claims", "safety_score": 0.64, "liquidity_score": 0.78, "public_backstop_score": 0.45, "collateral_acceptance_score": 0.75},
        {"claim": "private_asset_backed_paper", "safety_score": 0.44, "liquidity_score": 0.46, "public_backstop_score": 0.24, "collateral_acceptance_score": 0.38},
        {"claim": "informal_high_cost_credit", "safety_score": 0.18, "liquidity_score": 0.30, "public_backstop_score": 0.05, "collateral_acceptance_score": 0.10},
    ])


def build_sustainable_finance_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"finance_use": "fossil_asset_expansion", "financial_return_score": 0.78, "resilience_score": 0.20, "ecological_alignment_score": 0.06, "inclusion_score": 0.24, "systemic_risk_score": 0.72},
        {"finance_use": "public_transit_finance", "financial_return_score": 0.42, "resilience_score": 0.82, "ecological_alignment_score": 0.88, "inclusion_score": 0.86, "systemic_risk_score": 0.22},
        {"finance_use": "grid_resilience_credit", "financial_return_score": 0.56, "resilience_score": 0.90, "ecological_alignment_score": 0.84, "inclusion_score": 0.72, "systemic_risk_score": 0.26},
        {"finance_use": "affordable_housing_credit", "financial_return_score": 0.46, "resilience_score": 0.72, "ecological_alignment_score": 0.62, "inclusion_score": 0.92, "systemic_risk_score": 0.30},
        {"finance_use": "leveraged_asset_buyouts", "financial_return_score": 0.82, "resilience_score": 0.18, "ecological_alignment_score": 0.22, "inclusion_score": 0.16, "systemic_risk_score": 0.78},
        {"finance_use": "water_infrastructure_renewal", "financial_return_score": 0.38, "resilience_score": 0.92, "ecological_alignment_score": 0.78, "inclusion_score": 0.88, "systemic_risk_score": 0.20},
    ])


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "money_banking_credit_intermediation.sqlite"
    names = [
        "money_aggregate_scenarios",
        "bank_balance_sheet_scenarios",
        "debt_service_scenarios",
        "liquidity_stress_scenarios",
        "credit_allocation_scenarios",
        "monetary_hierarchy_scenarios",
        "sustainable_finance_scenarios",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_money_aggregate_scenarios(),
        build_bank_balance_sheet_scenarios(),
        build_debt_service_scenarios(),
        build_liquidity_stress_scenarios(),
        build_credit_allocation_scenarios(),
        build_monetary_hierarchy_scenarios(),
        build_sustainable_finance_scenarios(),
    ]

    filenames = [
        "money_aggregate_scenarios.csv",
        "bank_balance_sheet_scenarios.csv",
        "debt_service_scenarios.csv",
        "liquidity_stress_scenarios.csv",
        "credit_allocation_scenarios.csv",
        "monetary_hierarchy_scenarios.csv",
        "sustainable_finance_scenarios.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created money, banking, credit, and intermediation base data.")


if __name__ == "__main__":
    main()
