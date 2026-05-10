"""
Build stylized datasets for political economy, power, and distributional conflict.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_income_distribution() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "labor_strong_shared_growth", "wages": 360, "profits": 105, "rents": 35, "taxes_paid": 72, "benefits_received": 88, "public_goods_value": 64},
        {"scenario": "finance_asset_led_growth", "wages": 285, "profits": 145, "rents": 90, "taxes_paid": 62, "benefits_received": 38, "public_goods_value": 42},
        {"scenario": "rentier_housing_pressure", "wages": 300, "profits": 110, "rents": 120, "taxes_paid": 54, "benefits_received": 46, "public_goods_value": 40},
        {"scenario": "austerity_wage_compression", "wages": 270, "profits": 140, "rents": 70, "taxes_paid": 58, "benefits_received": 28, "public_goods_value": 30},
        {"scenario": "welfare_buffered_distribution", "wages": 335, "profits": 115, "rents": 55, "taxes_paid": 82, "benefits_received": 96, "public_goods_value": 74},
        {"scenario": "crisis_loss_socialized_upward", "wages": 255, "profits": 155, "rents": 85, "taxes_paid": 64, "benefits_received": 26, "public_goods_value": 34},
    ])


def build_power_groups() -> pd.DataFrame:
    return pd.DataFrame([
        {"group": "organized_labor", "ownership_power": 0.22, "organization_power": 0.72, "access_power": 0.48, "mobility_power": 0.28, "voice_power": 0.66, "media_influence": 0.34, "legal_position": 0.56},
        {"group": "large_firms", "ownership_power": 0.82, "organization_power": 0.70, "access_power": 0.78, "mobility_power": 0.76, "voice_power": 0.58, "media_influence": 0.64, "legal_position": 0.74},
        {"group": "creditors_finance", "ownership_power": 0.78, "organization_power": 0.76, "access_power": 0.82, "mobility_power": 0.84, "voice_power": 0.56, "media_influence": 0.62, "legal_position": 0.82},
        {"group": "landlords_asset_owners", "ownership_power": 0.74, "organization_power": 0.54, "access_power": 0.62, "mobility_power": 0.52, "voice_power": 0.48, "media_influence": 0.50, "legal_position": 0.76},
        {"group": "precarious_workers", "ownership_power": 0.08, "organization_power": 0.20, "access_power": 0.18, "mobility_power": 0.24, "voice_power": 0.22, "media_influence": 0.12, "legal_position": 0.28},
        {"group": "tenants_indebted_households", "ownership_power": 0.10, "organization_power": 0.24, "access_power": 0.20, "mobility_power": 0.18, "voice_power": 0.26, "media_influence": 0.14, "legal_position": 0.30},
    ])


def build_fiscal_incidence() -> pd.DataFrame:
    return pd.DataFrame([
        {"group": "low_income_households", "market_income": 28, "taxes_paid": 4, "cash_transfers": 18, "services_received": 20, "debt_service": 6, "housing_cost": 15},
        {"group": "working_households", "market_income": 55, "taxes_paid": 10, "cash_transfers": 8, "services_received": 18, "debt_service": 12, "housing_cost": 20},
        {"group": "middle_income_households", "market_income": 92, "taxes_paid": 22, "cash_transfers": 5, "services_received": 16, "debt_service": 16, "housing_cost": 28},
        {"group": "high_income_professionals", "market_income": 190, "taxes_paid": 52, "cash_transfers": 1, "services_received": 10, "debt_service": 22, "housing_cost": 48},
        {"group": "asset_owning_households", "market_income": 260, "taxes_paid": 64, "cash_transfers": 0, "services_received": 8, "debt_service": 18, "housing_cost": 42},
        {"group": "large_corporate_sector", "market_income": 420, "taxes_paid": 46, "cash_transfers": 8, "services_received": 32, "debt_service": 38, "housing_cost": 0},
    ])


def build_inflation_labor_conflict() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "labor_protected_real_wages", "price_inflation": 0.06, "nominal_wage_growth": 0.07, "profit_margin_change": 0.01, "interest_rate_shock": 0.02, "unemployment_pressure": 0.32, "bargaining_strength": 0.72},
        {"scenario": "profit_margin_preservation", "price_inflation": 0.08, "nominal_wage_growth": 0.04, "profit_margin_change": 0.04, "interest_rate_shock": 0.04, "unemployment_pressure": 0.46, "bargaining_strength": 0.36},
        {"scenario": "creditor_disinflation_path", "price_inflation": 0.05, "nominal_wage_growth": 0.03, "profit_margin_change": 0.01, "interest_rate_shock": 0.07, "unemployment_pressure": 0.68, "bargaining_strength": 0.28},
        {"scenario": "price_controls_subsidy_buffer", "price_inflation": 0.04, "nominal_wage_growth": 0.05, "profit_margin_change": -0.01, "interest_rate_shock": 0.02, "unemployment_pressure": 0.30, "bargaining_strength": 0.58},
        {"scenario": "energy_food_shock_regressive", "price_inflation": 0.09, "nominal_wage_growth": 0.04, "profit_margin_change": 0.02, "interest_rate_shock": 0.05, "unemployment_pressure": 0.55, "bargaining_strength": 0.30},
    ])


def build_debt_rent_conflict() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "household_debt_stress", "debt_stock": 140, "income": 70, "interest_rate": 0.07, "rent_burden": 0.36, "asset_owner_gain": 0.62, "debtor_relief_access": 0.24, "legal_enforcement_strength": 0.78},
        {"scenario": "student_debt_obligation", "debt_stock": 80, "income": 48, "interest_rate": 0.05, "rent_burden": 0.32, "asset_owner_gain": 0.30, "debtor_relief_access": 0.34, "legal_enforcement_strength": 0.70},
        {"scenario": "sovereign_austerity_pressure", "debt_stock": 620, "income": 480, "interest_rate": 0.06, "rent_burden": 0.00, "asset_owner_gain": 0.58, "debtor_relief_access": 0.20, "legal_enforcement_strength": 0.86},
        {"scenario": "housing_rentier_pressure", "debt_stock": 110, "income": 60, "interest_rate": 0.06, "rent_burden": 0.48, "asset_owner_gain": 0.78, "debtor_relief_access": 0.18, "legal_enforcement_strength": 0.80},
        {"scenario": "debt_restructuring_social_buffer", "debt_stock": 100, "income": 70, "interest_rate": 0.035, "rent_burden": 0.26, "asset_owner_gain": 0.34, "debtor_relief_access": 0.72, "legal_enforcement_strength": 0.46},
    ])


def build_welfare_globalization_crisis() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "strong_welfare_social_compromise", "welfare_buffer": 0.82, "tax_progressivity": 0.72, "labor_voice": 0.70, "capital_mobility": 0.42, "trade_exposure": 0.52, "austerity_pressure": 0.24, "public_trust": 0.72},
        {"scenario": "capital_mobility_exit_threat", "welfare_buffer": 0.42, "tax_progressivity": 0.34, "labor_voice": 0.32, "capital_mobility": 0.82, "trade_exposure": 0.70, "austerity_pressure": 0.68, "public_trust": 0.38},
        {"scenario": "export_winners_import_losers", "welfare_buffer": 0.48, "tax_progressivity": 0.40, "labor_voice": 0.38, "capital_mobility": 0.64, "trade_exposure": 0.82, "austerity_pressure": 0.46, "public_trust": 0.44},
        {"scenario": "crisis_bailout_public_losses", "welfare_buffer": 0.36, "tax_progressivity": 0.32, "labor_voice": 0.30, "capital_mobility": 0.76, "trade_exposure": 0.58, "austerity_pressure": 0.74, "public_trust": 0.30},
        {"scenario": "inclusive_transition_compact", "welfare_buffer": 0.76, "tax_progressivity": 0.68, "labor_voice": 0.66, "capital_mobility": 0.44, "trade_exposure": 0.60, "austerity_pressure": 0.28, "public_trust": 0.70},
    ])


def build_legitimacy_conflict() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "credible_social_settlement", "inequality_pressure": 0.30, "inflation_pressure": 0.34, "unemployment_pressure": 0.28, "representation_gap": 0.24, "shock_exposure": 0.30, "fairness": 0.74, "security": 0.78, "voice": 0.72, "institutional_trust": 0.76},
        {"scenario": "oligarchic_capture", "inequality_pressure": 0.82, "inflation_pressure": 0.48, "unemployment_pressure": 0.42, "representation_gap": 0.78, "shock_exposure": 0.62, "fairness": 0.24, "security": 0.34, "voice": 0.22, "institutional_trust": 0.26},
        {"scenario": "austerity_legitimacy_crisis", "inequality_pressure": 0.68, "inflation_pressure": 0.42, "unemployment_pressure": 0.64, "representation_gap": 0.60, "shock_exposure": 0.58, "fairness": 0.32, "security": 0.28, "voice": 0.36, "institutional_trust": 0.30},
        {"scenario": "inflation_distributional_spiral", "inequality_pressure": 0.56, "inflation_pressure": 0.84, "unemployment_pressure": 0.46, "representation_gap": 0.50, "shock_exposure": 0.66, "fairness": 0.38, "security": 0.34, "voice": 0.42, "institutional_trust": 0.36},
        {"scenario": "green_transition_burden_conflict", "inequality_pressure": 0.52, "inflation_pressure": 0.38, "unemployment_pressure": 0.44, "representation_gap": 0.48, "shock_exposure": 0.72, "fairness": 0.46, "security": 0.50, "voice": 0.52, "institutional_trust": 0.48},
        {"scenario": "participatory_resilience_compact", "inequality_pressure": 0.36, "inflation_pressure": 0.32, "unemployment_pressure": 0.30, "representation_gap": 0.26, "shock_exposure": 0.38, "fairness": 0.70, "security": 0.74, "voice": 0.76, "institutional_trust": 0.72},
    ])


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "political_economy_power_distributional_conflict.sqlite"
    names = [
        "income_distribution",
        "power_groups",
        "fiscal_incidence",
        "inflation_labor_conflict",
        "debt_rent_conflict",
        "welfare_globalization_crisis",
        "legitimacy_conflict",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_income_distribution(),
        build_power_groups(),
        build_fiscal_incidence(),
        build_inflation_labor_conflict(),
        build_debt_rent_conflict(),
        build_welfare_globalization_crisis(),
        build_legitimacy_conflict(),
    ]

    filenames = [
        "income_distribution.csv",
        "power_groups.csv",
        "fiscal_incidence.csv",
        "inflation_labor_conflict.csv",
        "debt_rent_conflict.csv",
        "welfare_globalization_crisis.csv",
        "legitimacy_conflict.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created political economy, power, and distributional conflict base data.")


if __name__ == "__main__":
    main()
