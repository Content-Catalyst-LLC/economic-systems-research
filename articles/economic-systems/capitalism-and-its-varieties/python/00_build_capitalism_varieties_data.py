"""
Build stylized datasets for capitalism and its varieties.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_regime_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"regime": "liberal_market_economy", "revenue": 560, "cost": 430, "wages": 255, "output": 560, "shareholder_claims": 0.78, "labor_coordination": 0.28, "welfare_buffer": 0.36, "finance_patience": 0.30, "state_coordination": 0.32, "innovation_radical": 0.78, "innovation_incremental": 0.46},
        {"regime": "coordinated_market_economy", "revenue": 540, "cost": 420, "wages": 305, "output": 540, "shareholder_claims": 0.42, "labor_coordination": 0.76, "welfare_buffer": 0.70, "finance_patience": 0.72, "state_coordination": 0.62, "innovation_radical": 0.48, "innovation_incremental": 0.80},
        {"regime": "developmental_capitalism", "revenue": 590, "cost": 455, "wages": 285, "output": 590, "shareholder_claims": 0.38, "labor_coordination": 0.52, "welfare_buffer": 0.50, "finance_patience": 0.68, "state_coordination": 0.84, "innovation_radical": 0.62, "innovation_incremental": 0.72},
        {"regime": "finance_led_capitalism", "revenue": 610, "cost": 470, "wages": 250, "output": 610, "shareholder_claims": 0.90, "labor_coordination": 0.22, "welfare_buffer": 0.32, "finance_patience": 0.22, "state_coordination": 0.28, "innovation_radical": 0.66, "innovation_incremental": 0.40},
        {"regime": "welfare_capitalism", "revenue": 525, "cost": 415, "wages": 310, "output": 525, "shareholder_claims": 0.44, "labor_coordination": 0.70, "welfare_buffer": 0.84, "finance_patience": 0.62, "state_coordination": 0.70, "innovation_radical": 0.52, "innovation_incremental": 0.68},
        {"regime": "resource_dependent_capitalism", "revenue": 575, "cost": 405, "wages": 220, "output": 575, "shareholder_claims": 0.64, "labor_coordination": 0.34, "welfare_buffer": 0.38, "finance_patience": 0.42, "state_coordination": 0.50, "innovation_radical": 0.34, "innovation_incremental": 0.38},
        {"regime": "hybrid_global_value_chain_capitalism", "revenue": 550, "cost": 430, "wages": 245, "output": 550, "shareholder_claims": 0.58, "labor_coordination": 0.40, "welfare_buffer": 0.44, "finance_patience": 0.46, "state_coordination": 0.54, "innovation_radical": 0.50, "innovation_incremental": 0.58},
    ])


def build_financialization_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "patient_banking_productive_investment", "asset_price_intensity": 0.38, "household_debt": 0.36, "corporate_leverage": 0.42, "shareholder_payout_pressure": 0.30, "buyback_intensity": 0.18, "productive_investment": 0.78, "speculative_pressure": 0.24},
        {"scenario": "shareholder_primacy_finance_led", "asset_price_intensity": 0.82, "household_debt": 0.70, "corporate_leverage": 0.76, "shareholder_payout_pressure": 0.88, "buyback_intensity": 0.82, "productive_investment": 0.42, "speculative_pressure": 0.76},
        {"scenario": "developmental_credit_guidance", "asset_price_intensity": 0.44, "household_debt": 0.38, "corporate_leverage": 0.56, "shareholder_payout_pressure": 0.32, "buyback_intensity": 0.20, "productive_investment": 0.82, "speculative_pressure": 0.30},
        {"scenario": "housing_finance_expansion", "asset_price_intensity": 0.74, "household_debt": 0.82, "corporate_leverage": 0.54, "shareholder_payout_pressure": 0.54, "buyback_intensity": 0.46, "productive_investment": 0.46, "speculative_pressure": 0.70},
        {"scenario": "regulated_stakeholder_finance", "asset_price_intensity": 0.46, "household_debt": 0.42, "corporate_leverage": 0.44, "shareholder_payout_pressure": 0.36, "buyback_intensity": 0.24, "productive_investment": 0.72, "speculative_pressure": 0.34},
    ])


def build_labor_skill_systems() -> pd.DataFrame:
    return pd.DataFrame([
        {"system": "flexible_liberal_labor", "employment_protection": 0.28, "collective_bargaining": 0.22, "union_density": 0.20, "general_skills": 0.76, "vocational_training": 0.34, "firm_specific_skills": 0.32, "wage_compression": 0.24},
        {"system": "coordinated_sectoral_bargaining", "employment_protection": 0.68, "collective_bargaining": 0.78, "union_density": 0.64, "general_skills": 0.62, "vocational_training": 0.82, "firm_specific_skills": 0.74, "wage_compression": 0.76},
        {"system": "developmental_export_labor", "employment_protection": 0.52, "collective_bargaining": 0.48, "union_density": 0.36, "general_skills": 0.58, "vocational_training": 0.66, "firm_specific_skills": 0.62, "wage_compression": 0.46},
        {"system": "precarious_dual_labor_market", "employment_protection": 0.34, "collective_bargaining": 0.26, "union_density": 0.22, "general_skills": 0.48, "vocational_training": 0.38, "firm_specific_skills": 0.36, "wage_compression": 0.22},
        {"system": "stakeholder_skill_formation", "employment_protection": 0.72, "collective_bargaining": 0.70, "union_density": 0.58, "general_skills": 0.68, "vocational_training": 0.78, "firm_specific_skills": 0.72, "wage_compression": 0.68},
    ])


def build_corporate_governance() -> pd.DataFrame:
    return pd.DataFrame([
        {"governance": "shareholder_value", "short_term_pressure": 0.86, "stakeholder_voice": 0.20, "worker_representation": 0.12, "patient_capital": 0.24, "reinvestment_orientation": 0.38, "supplier_coordination": 0.34, "community_accountability": 0.20},
        {"governance": "stakeholder_codetermination", "short_term_pressure": 0.34, "stakeholder_voice": 0.78, "worker_representation": 0.82, "patient_capital": 0.70, "reinvestment_orientation": 0.72, "supplier_coordination": 0.74, "community_accountability": 0.66},
        {"governance": "developmental_state_guided", "short_term_pressure": 0.30, "stakeholder_voice": 0.52, "worker_representation": 0.44, "patient_capital": 0.78, "reinvestment_orientation": 0.82, "supplier_coordination": 0.68, "community_accountability": 0.54},
        {"governance": "family_bank_network", "short_term_pressure": 0.42, "stakeholder_voice": 0.58, "worker_representation": 0.42, "patient_capital": 0.74, "reinvestment_orientation": 0.70, "supplier_coordination": 0.72, "community_accountability": 0.56},
        {"governance": "platform_asset_light", "short_term_pressure": 0.76, "stakeholder_voice": 0.24, "worker_representation": 0.10, "patient_capital": 0.38, "reinvestment_orientation": 0.50, "supplier_coordination": 0.28, "community_accountability": 0.18},
    ])


def build_housing_household_vulnerability() -> pd.DataFrame:
    return pd.DataFrame([
        {"housing_regime": "social_housing_buffer", "rent_burden": 0.26, "mortgage_debt": 0.32, "asset_price_volatility": 0.28, "tenant_protection": 0.78, "public_housing_capacity": 0.74, "household_resilience": 0.72, "wealth_concentration_pressure": 0.30},
        {"housing_regime": "financialized_homeownership", "rent_burden": 0.54, "mortgage_debt": 0.78, "asset_price_volatility": 0.70, "tenant_protection": 0.34, "public_housing_capacity": 0.22, "household_resilience": 0.38, "wealth_concentration_pressure": 0.76},
        {"housing_regime": "rental_dual_market", "rent_burden": 0.62, "mortgage_debt": 0.46, "asset_price_volatility": 0.56, "tenant_protection": 0.40, "public_housing_capacity": 0.28, "household_resilience": 0.34, "wealth_concentration_pressure": 0.58},
        {"housing_regime": "regulated_mixed_housing", "rent_burden": 0.36, "mortgage_debt": 0.42, "asset_price_volatility": 0.40, "tenant_protection": 0.66, "public_housing_capacity": 0.54, "household_resilience": 0.60, "wealth_concentration_pressure": 0.42},
        {"housing_regime": "speculative_urban_asset_market", "rent_burden": 0.72, "mortgage_debt": 0.64, "asset_price_volatility": 0.82, "tenant_protection": 0.22, "public_housing_capacity": 0.16, "household_resilience": 0.24, "wealth_concentration_pressure": 0.84},
    ])


def build_globalization_hybrids() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "embedded_export_coordinated", "value_chain_dependence": 0.56, "domestic_supplier_depth": 0.78, "foreign_currency_exposure": 0.30, "technology_sovereignty": 0.66, "labor_standards": 0.70, "industrial_policy_capacity": 0.72, "external_vulnerability": 0.34},
        {"scenario": "dependent_assembly_platform", "value_chain_dependence": 0.82, "domestic_supplier_depth": 0.34, "foreign_currency_exposure": 0.62, "technology_sovereignty": 0.28, "labor_standards": 0.34, "industrial_policy_capacity": 0.36, "external_vulnerability": 0.74},
        {"scenario": "resource_export_capitalism", "value_chain_dependence": 0.64, "domestic_supplier_depth": 0.30, "foreign_currency_exposure": 0.70, "technology_sovereignty": 0.24, "labor_standards": 0.38, "industrial_policy_capacity": 0.42, "external_vulnerability": 0.78},
        {"scenario": "developmental_upgrading_strategy", "value_chain_dependence": 0.58, "domestic_supplier_depth": 0.70, "foreign_currency_exposure": 0.44, "technology_sovereignty": 0.64, "labor_standards": 0.58, "industrial_policy_capacity": 0.82, "external_vulnerability": 0.42},
        {"scenario": "financialized_open_capital_account", "value_chain_dependence": 0.54, "domestic_supplier_depth": 0.46, "foreign_currency_exposure": 0.72, "technology_sovereignty": 0.46, "labor_standards": 0.42, "industrial_policy_capacity": 0.38, "external_vulnerability": 0.72},
    ])


def build_crisis_sustainability() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "market_adjustment_downward_pressure", "automatic_stabilizers": 0.30, "public_investment_capacity": 0.34, "household_buffer": 0.28, "financial_regulation": 0.32, "industrial_adaptation": 0.36, "ecological_constraint": 0.28, "democratic_legitimacy": 0.36},
        {"scenario": "coordinated_negotiated_adjustment", "automatic_stabilizers": 0.72, "public_investment_capacity": 0.66, "household_buffer": 0.70, "financial_regulation": 0.68, "industrial_adaptation": 0.72, "ecological_constraint": 0.58, "democratic_legitimacy": 0.70},
        {"scenario": "developmental_green_transition", "automatic_stabilizers": 0.60, "public_investment_capacity": 0.84, "household_buffer": 0.58, "financial_regulation": 0.64, "industrial_adaptation": 0.86, "ecological_constraint": 0.78, "democratic_legitimacy": 0.62},
        {"scenario": "finance_led_bailout_path", "automatic_stabilizers": 0.38, "public_investment_capacity": 0.42, "household_buffer": 0.32, "financial_regulation": 0.28, "industrial_adaptation": 0.40, "ecological_constraint": 0.30, "democratic_legitimacy": 0.34},
        {"scenario": "welfare_buffered_resilience", "automatic_stabilizers": 0.82, "public_investment_capacity": 0.72, "household_buffer": 0.84, "financial_regulation": 0.66, "industrial_adaptation": 0.68, "ecological_constraint": 0.64, "democratic_legitimacy": 0.76},
    ])


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "capitalism_and_its_varieties.sqlite"
    names = [
        "regime_scenarios",
        "financialization_scenarios",
        "labor_skill_systems",
        "corporate_governance",
        "housing_household_vulnerability",
        "globalization_hybrids",
        "crisis_sustainability",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_regime_scenarios(),
        build_financialization_scenarios(),
        build_labor_skill_systems(),
        build_corporate_governance(),
        build_housing_household_vulnerability(),
        build_globalization_hybrids(),
        build_crisis_sustainability(),
    ]

    filenames = [
        "regime_scenarios.csv",
        "financialization_scenarios.csv",
        "labor_skill_systems.csv",
        "corporate_governance.csv",
        "housing_household_vulnerability.csv",
        "globalization_hybrids.csv",
        "crisis_sustainability.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created capitalism and its varieties base data.")


if __name__ == "__main__":
    main()
