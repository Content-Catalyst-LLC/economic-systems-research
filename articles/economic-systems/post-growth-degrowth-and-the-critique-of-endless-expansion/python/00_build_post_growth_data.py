"""
Build stylized datasets for post-growth, degrowth, and the critique of endless expansion.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_growth_dependence() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "growth_dependent_status_quo", "employment_dependency": 0.82, "debt_service_dependency": 0.78, "fiscal_dependency": 0.76, "asset_dependency": 0.84, "pension_dependency": 0.70, "housing_market_dependency": 0.86, "political_legitimacy_dependency": 0.80},
        {"scenario": "green_growth_reform", "employment_dependency": 0.70, "debt_service_dependency": 0.70, "fiscal_dependency": 0.68, "asset_dependency": 0.74, "pension_dependency": 0.66, "housing_market_dependency": 0.74, "political_legitimacy_dependency": 0.68},
        {"scenario": "post_growth_public_goods", "employment_dependency": 0.42, "debt_service_dependency": 0.46, "fiscal_dependency": 0.48, "asset_dependency": 0.40, "pension_dependency": 0.48, "housing_market_dependency": 0.36, "political_legitimacy_dependency": 0.38},
        {"scenario": "austerity_stagnation", "employment_dependency": 0.80, "debt_service_dependency": 0.82, "fiscal_dependency": 0.78, "asset_dependency": 0.66, "pension_dependency": 0.74, "housing_market_dependency": 0.58, "political_legitimacy_dependency": 0.86},
        {"scenario": "degrowth_transition_compact", "employment_dependency": 0.36, "debt_service_dependency": 0.42, "fiscal_dependency": 0.44, "asset_dependency": 0.34, "pension_dependency": 0.46, "housing_market_dependency": 0.30, "political_legitimacy_dependency": 0.34},
    ])


def build_throughput_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "high_income_expansion", "population": 100, "affluence": 2.4, "intensity": 0.78, "wellbeing_index": 0.70, "distribution_quality": 0.42},
        {"scenario": "efficiency_rebound", "population": 100, "affluence": 2.6, "intensity": 0.54, "wellbeing_index": 0.72, "distribution_quality": 0.44},
        {"scenario": "sufficiency_public_goods", "population": 100, "affluence": 1.6, "intensity": 0.38, "wellbeing_index": 0.80, "distribution_quality": 0.76},
        {"scenario": "austerity_low_wellbeing", "population": 100, "affluence": 1.1, "intensity": 0.42, "wellbeing_index": 0.46, "distribution_quality": 0.34},
        {"scenario": "degrowth_just_transition", "population": 100, "affluence": 1.4, "intensity": 0.34, "wellbeing_index": 0.76, "distribution_quality": 0.78},
    ])


def build_wellbeing_dashboard() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "consumer_growth_stress", "health": 0.62, "time_balance": 0.34, "security": 0.54, "equality": 0.38, "public_goods": 0.48, "ecological_quality": 0.32, "care_support": 0.36, "social_trust": 0.42},
        {"scenario": "wellbeing_economy", "health": 0.80, "time_balance": 0.74, "security": 0.76, "equality": 0.72, "public_goods": 0.82, "ecological_quality": 0.76, "care_support": 0.78, "social_trust": 0.74},
        {"scenario": "green_growth_mixed_outcomes", "health": 0.72, "time_balance": 0.52, "security": 0.62, "equality": 0.50, "public_goods": 0.64, "ecological_quality": 0.58, "care_support": 0.54, "social_trust": 0.56},
        {"scenario": "low_output_public_security", "health": 0.74, "time_balance": 0.78, "security": 0.70, "equality": 0.76, "public_goods": 0.78, "ecological_quality": 0.80, "care_support": 0.80, "social_trust": 0.72},
        {"scenario": "low_output_disorganized_decline", "health": 0.46, "time_balance": 0.44, "security": 0.30, "equality": 0.34, "public_goods": 0.28, "ecological_quality": 0.58, "care_support": 0.26, "social_trust": 0.24},
    ])


def build_sufficiency() -> pd.DataFrame:
    return pd.DataFrame([
        {"system": "car_dependent_private_consumption", "needs_met": 0.66, "throughput_required": 0.88, "time_security": 0.42, "public_access": 0.34, "care_capacity": 0.36, "dignity": 0.52},
        {"system": "public_transit_and_15_min_city", "needs_met": 0.80, "throughput_required": 0.46, "time_security": 0.74, "public_access": 0.82, "care_capacity": 0.68, "dignity": 0.76},
        {"system": "universal_basic_services", "needs_met": 0.84, "throughput_required": 0.52, "time_security": 0.72, "public_access": 0.86, "care_capacity": 0.78, "dignity": 0.82},
        {"system": "luxury_high_throughput_model", "needs_met": 0.78, "throughput_required": 0.96, "time_security": 0.48, "public_access": 0.42, "care_capacity": 0.38, "dignity": 0.62},
        {"system": "austerity_low_support", "needs_met": 0.42, "throughput_required": 0.34, "time_security": 0.30, "public_access": 0.24, "care_capacity": 0.22, "dignity": 0.28},
    ])


def build_work_time_care() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "long_hours_growth_norm", "paid_work_hours": 42, "unpaid_care_hours": 20, "leisure_hours": 18, "labor_security": 0.52, "care_support": 0.36, "time_sovereignty": 0.34},
        {"scenario": "shorter_work_week_public_services", "paid_work_hours": 32, "unpaid_care_hours": 18, "leisure_hours": 28, "labor_security": 0.72, "care_support": 0.78, "time_sovereignty": 0.76},
        {"scenario": "automation_without_distribution", "paid_work_hours": 38, "unpaid_care_hours": 22, "leisure_hours": 20, "labor_security": 0.34, "care_support": 0.38, "time_sovereignty": 0.42},
        {"scenario": "care_centered_economy", "paid_work_hours": 34, "unpaid_care_hours": 22, "leisure_hours": 26, "labor_security": 0.70, "care_support": 0.86, "time_sovereignty": 0.74},
        {"scenario": "precarious_low_growth", "paid_work_hours": 30, "unpaid_care_hours": 28, "leisure_hours": 16, "labor_security": 0.24, "care_support": 0.22, "time_sovereignty": 0.26},
    ])


def build_finance_growth_dependence() -> pd.DataFrame:
    return pd.DataFrame([
        {"system": "asset_inflation_growth_model", "private_debt": 0.82, "public_debt_pressure": 0.70, "asset_valuation_pressure": 0.88, "pension_return_dependency": 0.74, "housing_speculation": 0.84, "real_investment_alignment": 0.32},
        {"system": "green_investment_growth_model", "private_debt": 0.68, "public_debt_pressure": 0.62, "asset_valuation_pressure": 0.70, "pension_return_dependency": 0.68, "housing_speculation": 0.62, "real_investment_alignment": 0.58},
        {"system": "post_growth_financial_reform", "private_debt": 0.42, "public_debt_pressure": 0.44, "asset_valuation_pressure": 0.38, "pension_return_dependency": 0.48, "housing_speculation": 0.30, "real_investment_alignment": 0.78},
        {"system": "debt_deflation_austerity", "private_debt": 0.86, "public_debt_pressure": 0.82, "asset_valuation_pressure": 0.64, "pension_return_dependency": 0.76, "housing_speculation": 0.52, "real_investment_alignment": 0.26},
        {"system": "public_banking_social_investment", "private_debt": 0.36, "public_debt_pressure": 0.42, "asset_valuation_pressure": 0.34, "pension_return_dependency": 0.44, "housing_speculation": 0.26, "real_investment_alignment": 0.84},
    ])


def build_decoupling_rebound() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "relative_decoupling_only", "output_growth": 0.030, "intensity_reduction": 0.020, "additional_demand": 0.006, "absolute_throughput_change": 0.016, "wellbeing_gain": 0.04},
        {"scenario": "absolute_decoupling_weak", "output_growth": 0.018, "intensity_reduction": 0.030, "additional_demand": 0.004, "absolute_throughput_change": -0.008, "wellbeing_gain": 0.05},
        {"scenario": "sufficiency_plus_efficiency", "output_growth": 0.006, "intensity_reduction": 0.028, "additional_demand": 0.001, "absolute_throughput_change": -0.024, "wellbeing_gain": 0.10},
        {"scenario": "rebound_high_consumption", "output_growth": 0.034, "intensity_reduction": 0.026, "additional_demand": 0.014, "absolute_throughput_change": 0.022, "wellbeing_gain": 0.02},
        {"scenario": "degrowth_throughput_reduction", "output_growth": -0.004, "intensity_reduction": 0.024, "additional_demand": 0.000, "absolute_throughput_change": -0.028, "wellbeing_gain": 0.08},
    ])


def build_degrowth_transition() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "unplanned_recession", "throughput_reduction": 0.42, "redistribution": 0.18, "public_services": 0.22, "democratic_legitimacy": 0.18, "macro_stabilization": 0.16, "employment_security": 0.20},
        {"scenario": "technocratic_austerity", "throughput_reduction": 0.46, "redistribution": 0.24, "public_services": 0.20, "democratic_legitimacy": 0.22, "macro_stabilization": 0.28, "employment_security": 0.24},
        {"scenario": "post_growth_transition", "throughput_reduction": 0.54, "redistribution": 0.66, "public_services": 0.72, "democratic_legitimacy": 0.68, "macro_stabilization": 0.62, "employment_security": 0.64},
        {"scenario": "degrowth_social_compact", "throughput_reduction": 0.72, "redistribution": 0.80, "public_services": 0.82, "democratic_legitimacy": 0.76, "macro_stabilization": 0.70, "employment_security": 0.72},
        {"scenario": "elite_green_enclosure", "throughput_reduction": 0.50, "redistribution": 0.28, "public_services": 0.36, "democratic_legitimacy": 0.30, "macro_stabilization": 0.42, "employment_security": 0.34},
    ])


def build_global_justice() -> pd.DataFrame:
    return pd.DataFrame([
        {"country_group": "high_income_high_footprint", "material_footprint": 0.90, "historic_responsibility": 0.86, "development_need": 0.22, "adaptive_capacity": 0.82, "basic_needs_gap": 0.14, "transition_finance_obligation": 0.84},
        {"country_group": "upper_middle_income_industrializing", "material_footprint": 0.62, "historic_responsibility": 0.44, "development_need": 0.58, "adaptive_capacity": 0.56, "basic_needs_gap": 0.40, "transition_finance_obligation": 0.46},
        {"country_group": "low_income_development_priority", "material_footprint": 0.18, "historic_responsibility": 0.08, "development_need": 0.90, "adaptive_capacity": 0.24, "basic_needs_gap": 0.78, "transition_finance_obligation": 0.08},
        {"country_group": "climate_vulnerable_low_emitters", "material_footprint": 0.12, "historic_responsibility": 0.04, "development_need": 0.84, "adaptive_capacity": 0.20, "basic_needs_gap": 0.72, "transition_finance_obligation": 0.04},
        {"country_group": "resource_exporting_transition_states", "material_footprint": 0.50, "historic_responsibility": 0.34, "development_need": 0.62, "adaptive_capacity": 0.42, "basic_needs_gap": 0.46, "transition_finance_obligation": 0.34},
    ])


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "post_growth_degrowth_endless_expansion.sqlite"
    names = [
        "growth_dependence",
        "throughput_scenarios",
        "wellbeing_dashboard",
        "sufficiency",
        "work_time_care",
        "finance_growth_dependence",
        "decoupling_rebound",
        "degrowth_transition",
        "global_justice",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_growth_dependence(),
        build_throughput_scenarios(),
        build_wellbeing_dashboard(),
        build_sufficiency(),
        build_work_time_care(),
        build_finance_growth_dependence(),
        build_decoupling_rebound(),
        build_degrowth_transition(),
        build_global_justice(),
    ]

    filenames = [
        "growth_dependence.csv",
        "throughput_scenarios.csv",
        "wellbeing_dashboard.csv",
        "sufficiency.csv",
        "work_time_care.csv",
        "finance_growth_dependence.csv",
        "decoupling_rebound.csv",
        "degrowth_transition.csv",
        "global_justice.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created post-growth, degrowth, and endless expansion base data.")


if __name__ == "__main__":
    main()
