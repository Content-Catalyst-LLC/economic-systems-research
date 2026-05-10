"""
Build stylized datasets for debt, dependency, and global financial order.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_debt_position_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "domestic_currency_development_debt", "debt_stock": 680, "output": 1500, "external_debt_service": 55, "export_earnings": 320, "foreign_currency_debt": 120, "exchange_rate": 1.00, "effective_interest_rate": 0.045, "growth_rate": 0.050, "primary_deficit": 18, "reserves": 260, "short_term_external_obligations": 120},
        {"scenario": "foreign_currency_debt_stress", "debt_stock": 760, "output": 1420, "external_debt_service": 125, "export_earnings": 280, "foreign_currency_debt": 430, "exchange_rate": 1.35, "effective_interest_rate": 0.075, "growth_rate": 0.018, "primary_deficit": 30, "reserves": 145, "short_term_external_obligations": 210},
        {"scenario": "commodity_boom_borrowing", "debt_stock": 620, "output": 1350, "external_debt_service": 82, "export_earnings": 410, "foreign_currency_debt": 310, "exchange_rate": 1.10, "effective_interest_rate": 0.060, "growth_rate": 0.055, "primary_deficit": 26, "reserves": 220, "short_term_external_obligations": 150},
        {"scenario": "commodity_bust_debt_pressure", "debt_stock": 700, "output": 1260, "external_debt_service": 118, "export_earnings": 210, "foreign_currency_debt": 340, "exchange_rate": 1.45, "effective_interest_rate": 0.085, "growth_rate": -0.012, "primary_deficit": 35, "reserves": 110, "short_term_external_obligations": 190},
        {"scenario": "sustainable_development_finance", "debt_stock": 720, "output": 1600, "external_debt_service": 70, "export_earnings": 390, "foreign_currency_debt": 180, "exchange_rate": 1.05, "effective_interest_rate": 0.048, "growth_rate": 0.058, "primary_deficit": 22, "reserves": 310, "short_term_external_obligations": 135},
        {"scenario": "sudden_stop_crisis", "debt_stock": 820, "output": 1380, "external_debt_service": 150, "export_earnings": 260, "foreign_currency_debt": 500, "exchange_rate": 1.60, "effective_interest_rate": 0.095, "growth_rate": -0.025, "primary_deficit": 40, "reserves": 95, "short_term_external_obligations": 250},
    ])


def build_currency_hierarchy_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "reserve_currency_issuer", "own_currency_borrowing_share": 0.92, "foreign_currency_debt_share": 0.08, "market_depth": 0.90, "safe_asset_status": 0.88, "policy_space": 0.84, "external_discipline": 0.18},
        {"scenario": "upper_middle_currency", "own_currency_borrowing_share": 0.64, "foreign_currency_debt_share": 0.28, "market_depth": 0.62, "safe_asset_status": 0.42, "policy_space": 0.58, "external_discipline": 0.42},
        {"scenario": "dependent_foreign_currency_borrower", "own_currency_borrowing_share": 0.24, "foreign_currency_debt_share": 0.62, "market_depth": 0.28, "safe_asset_status": 0.14, "policy_space": 0.30, "external_discipline": 0.76},
        {"scenario": "commodity_currency_constraint", "own_currency_borrowing_share": 0.38, "foreign_currency_debt_share": 0.50, "market_depth": 0.34, "safe_asset_status": 0.18, "policy_space": 0.36, "external_discipline": 0.70},
        {"scenario": "managed_debt_sovereignty_path", "own_currency_borrowing_share": 0.70, "foreign_currency_debt_share": 0.22, "market_depth": 0.66, "safe_asset_status": 0.36, "policy_space": 0.68, "external_discipline": 0.34},
    ])


def build_external_account_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "diversified_export_base", "export_concentration": 0.28, "import_dependence": 0.34, "external_finance_reliance": 0.30, "capital_flow_volatility": 0.28, "reserve_buffer": 0.76, "domestic_capability": 0.70},
        {"scenario": "narrow_export_dependency", "export_concentration": 0.72, "import_dependence": 0.58, "external_finance_reliance": 0.62, "capital_flow_volatility": 0.54, "reserve_buffer": 0.36, "domestic_capability": 0.34},
        {"scenario": "energy_import_constraint", "export_concentration": 0.40, "import_dependence": 0.70, "external_finance_reliance": 0.54, "capital_flow_volatility": 0.42, "reserve_buffer": 0.44, "domestic_capability": 0.48},
        {"scenario": "external_credit_rollover_model", "export_concentration": 0.52, "import_dependence": 0.50, "external_finance_reliance": 0.78, "capital_flow_volatility": 0.66, "reserve_buffer": 0.32, "domestic_capability": 0.42},
        {"scenario": "resilient_external_position", "export_concentration": 0.24, "import_dependence": 0.32, "external_finance_reliance": 0.26, "capital_flow_volatility": 0.24, "reserve_buffer": 0.82, "domestic_capability": 0.76},
    ])


def build_credit_discipline_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "investment_grade_market_access", "spread": 0.018, "rating_pressure": 0.20, "rollover_need": 0.26, "foreign_investor_share": 0.36, "legal_constraint": 0.30, "market_access_score": 0.78},
        {"scenario": "downgrade_pressure_cycle", "spread": 0.062, "rating_pressure": 0.72, "rollover_need": 0.58, "foreign_investor_share": 0.62, "legal_constraint": 0.56, "market_access_score": 0.38},
        {"scenario": "high_yield_debt_dependence", "spread": 0.085, "rating_pressure": 0.82, "rollover_need": 0.70, "foreign_investor_share": 0.68, "legal_constraint": 0.66, "market_access_score": 0.28},
        {"scenario": "domestic_market_deepening", "spread": 0.030, "rating_pressure": 0.34, "rollover_need": 0.36, "foreign_investor_share": 0.28, "legal_constraint": 0.34, "market_access_score": 0.64},
        {"scenario": "crisis_market_exclusion", "spread": 0.125, "rating_pressure": 0.90, "rollover_need": 0.76, "foreign_investor_share": 0.72, "legal_constraint": 0.76, "market_access_score": 0.16},
    ])


def build_conditionality_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"program": "liquidity_support_with_investment_floor", "fiscal_compression": 0.28, "social_spending_protection": 0.72, "public_investment_protection": 0.68, "privatization_pressure": 0.24, "policy_space": 0.60, "developmental_alignment": 0.66},
        {"program": "procyclical_austerity_program", "fiscal_compression": 0.78, "social_spending_protection": 0.22, "public_investment_protection": 0.18, "privatization_pressure": 0.64, "policy_space": 0.24, "developmental_alignment": 0.20},
        {"program": "stabilization_without_transformation", "fiscal_compression": 0.58, "social_spending_protection": 0.42, "public_investment_protection": 0.34, "privatization_pressure": 0.46, "policy_space": 0.34, "developmental_alignment": 0.36},
        {"program": "development_finance_reform_path", "fiscal_compression": 0.34, "social_spending_protection": 0.66, "public_investment_protection": 0.72, "privatization_pressure": 0.28, "policy_space": 0.62, "developmental_alignment": 0.74},
        {"program": "creditor_priority_adjustment", "fiscal_compression": 0.70, "social_spending_protection": 0.30, "public_investment_protection": 0.24, "privatization_pressure": 0.58, "policy_space": 0.28, "developmental_alignment": 0.26},
    ])


def build_austerity_adjustment_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "front_loaded_austerity", "austerity_intensity": 0.82, "health_spending_cut": 0.30, "education_spending_cut": 0.26, "infrastructure_cut": 0.42, "wage_compression": 0.36, "growth_damage": 0.44, "poverty_pressure": 0.50},
        {"scenario": "protected_social_adjustment", "austerity_intensity": 0.38, "health_spending_cut": 0.06, "education_spending_cut": 0.08, "infrastructure_cut": 0.18, "wage_compression": 0.12, "growth_damage": 0.20, "poverty_pressure": 0.18},
        {"scenario": "investment_sacrificed_repayment", "austerity_intensity": 0.64, "health_spending_cut": 0.16, "education_spending_cut": 0.18, "infrastructure_cut": 0.54, "wage_compression": 0.28, "growth_damage": 0.48, "poverty_pressure": 0.36},
        {"scenario": "restructuring_with_capacity_protection", "austerity_intensity": 0.30, "health_spending_cut": 0.04, "education_spending_cut": 0.04, "infrastructure_cut": 0.12, "wage_compression": 0.10, "growth_damage": 0.16, "poverty_pressure": 0.14},
        {"scenario": "delayed_default_social_erosion", "austerity_intensity": 0.72, "health_spending_cut": 0.28, "education_spending_cut": 0.24, "infrastructure_cut": 0.46, "wage_compression": 0.34, "growth_damage": 0.52, "poverty_pressure": 0.56},
    ])


def build_commodity_debt_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "commodity_boom", "commodity_export_share": 0.72, "commodity_price_index": 125, "export_earnings": 410, "external_debt_service": 82, "stabilization_fund": 0.62, "diversification_effort": 0.34},
        {"scenario": "commodity_bust", "commodity_export_share": 0.74, "commodity_price_index": 82, "export_earnings": 210, "external_debt_service": 118, "stabilization_fund": 0.34, "diversification_effort": 0.26},
        {"scenario": "rent_stabilized_transformation", "commodity_export_share": 0.48, "commodity_price_index": 110, "export_earnings": 360, "external_debt_service": 78, "stabilization_fund": 0.76, "diversification_effort": 0.70},
        {"scenario": "extractive_debt_cycle", "commodity_export_share": 0.80, "commodity_price_index": 90, "export_earnings": 245, "external_debt_service": 130, "stabilization_fund": 0.24, "diversification_effort": 0.18},
        {"scenario": "post_commodity_diversification", "commodity_export_share": 0.34, "commodity_price_index": 105, "export_earnings": 390, "external_debt_service": 72, "stabilization_fund": 0.68, "diversification_effort": 0.78},
    ])


def build_capital_flow_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "stable_long_term_inflows", "portfolio_share": 0.22, "fdi_share": 0.52, "short_term_debt_share": 0.18, "capital_flow_reversal": 0.16, "reserve_loss": 0.14, "currency_depreciation": 0.10},
        {"scenario": "portfolio_surge_reversal", "portfolio_share": 0.62, "fdi_share": 0.22, "short_term_debt_share": 0.38, "capital_flow_reversal": 0.66, "reserve_loss": 0.46, "currency_depreciation": 0.34},
        {"scenario": "sudden_stop_crisis", "portfolio_share": 0.56, "fdi_share": 0.18, "short_term_debt_share": 0.52, "capital_flow_reversal": 0.82, "reserve_loss": 0.62, "currency_depreciation": 0.48},
        {"scenario": "managed_capital_flow_buffers", "portfolio_share": 0.30, "fdi_share": 0.46, "short_term_debt_share": 0.20, "capital_flow_reversal": 0.24, "reserve_loss": 0.20, "currency_depreciation": 0.16},
        {"scenario": "external_credit_rollover_failure", "portfolio_share": 0.44, "fdi_share": 0.26, "short_term_debt_share": 0.58, "capital_flow_reversal": 0.72, "reserve_loss": 0.54, "currency_depreciation": 0.42},
    ])


def build_restructuring_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "maturity_extension_only", "initial_debt": 780, "restructuring_haircut": 0.00, "maturity_extension": 0.42, "interest_relief": 0.10, "social_spending_floor": 0.42, "growth_recovery": 0.36, "creditor_acceptance": 0.72},
        {"scenario": "moderate_haircut_capacity_protection", "initial_debt": 780, "restructuring_haircut": 0.25, "maturity_extension": 0.52, "interest_relief": 0.22, "social_spending_floor": 0.68, "growth_recovery": 0.62, "creditor_acceptance": 0.56},
        {"scenario": "deep_haircut_long_delay", "initial_debt": 780, "restructuring_haircut": 0.45, "maturity_extension": 0.60, "interest_relief": 0.34, "social_spending_floor": 0.60, "growth_recovery": 0.52, "creditor_acceptance": 0.30},
        {"scenario": "liquidity_rollover_no_relief", "initial_debt": 780, "restructuring_haircut": 0.00, "maturity_extension": 0.18, "interest_relief": 0.02, "social_spending_floor": 0.30, "growth_recovery": 0.22, "creditor_acceptance": 0.86},
        {"scenario": "development_linked_restructuring", "initial_debt": 780, "restructuring_haircut": 0.20, "maturity_extension": 0.58, "interest_relief": 0.26, "social_spending_floor": 0.74, "growth_recovery": 0.70, "creditor_acceptance": 0.60},
    ])


def build_sustainable_finance_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "repayment_first_compression", "productive_investment": 0.22, "domestic_capability": 0.28, "export_resilience": 0.30, "social_protection": 0.24, "ecological_resilience": 0.26, "debt_manageability": 0.42},
        {"scenario": "infrastructure_capacity_finance", "productive_investment": 0.76, "domestic_capability": 0.66, "export_resilience": 0.58, "social_protection": 0.56, "ecological_resilience": 0.54, "debt_manageability": 0.62},
        {"scenario": "green_development_finance", "productive_investment": 0.72, "domestic_capability": 0.68, "export_resilience": 0.62, "social_protection": 0.64, "ecological_resilience": 0.82, "debt_manageability": 0.66},
        {"scenario": "speculative_external_borrowing", "productive_investment": 0.24, "domestic_capability": 0.22, "export_resilience": 0.26, "social_protection": 0.34, "ecological_resilience": 0.24, "debt_manageability": 0.28},
        {"scenario": "sovereign_capacity_path", "productive_investment": 0.80, "domestic_capability": 0.78, "export_resilience": 0.74, "social_protection": 0.72, "ecological_resilience": 0.70, "debt_manageability": 0.76},
    ])


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "debt_dependency_global_financial_order.sqlite"
    names = [
        "debt_position_scenarios",
        "currency_hierarchy_scenarios",
        "external_account_scenarios",
        "credit_discipline_scenarios",
        "conditionality_scenarios",
        "austerity_adjustment_scenarios",
        "commodity_debt_scenarios",
        "capital_flow_scenarios",
        "restructuring_scenarios",
        "sustainable_finance_scenarios",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_debt_position_scenarios(),
        build_currency_hierarchy_scenarios(),
        build_external_account_scenarios(),
        build_credit_discipline_scenarios(),
        build_conditionality_scenarios(),
        build_austerity_adjustment_scenarios(),
        build_commodity_debt_scenarios(),
        build_capital_flow_scenarios(),
        build_restructuring_scenarios(),
        build_sustainable_finance_scenarios(),
    ]
    filenames = [
        "debt_position_scenarios.csv",
        "currency_hierarchy_scenarios.csv",
        "external_account_scenarios.csv",
        "credit_discipline_scenarios.csv",
        "conditionality_scenarios.csv",
        "austerity_adjustment_scenarios.csv",
        "commodity_debt_scenarios.csv",
        "capital_flow_scenarios.csv",
        "restructuring_scenarios.csv",
        "sustainable_finance_scenarios.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created debt, dependency, and global financial order base data.")


if __name__ == "__main__":
    main()
