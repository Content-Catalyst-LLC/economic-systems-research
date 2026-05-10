"""
Build stylized datasets for Beyond GDP: well-being, inclusion, and sustainability.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_gdp_dashboard_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "high_gdp_low_inclusion", "consumption": 720, "investment": 210, "government": 160, "net_exports": -30, "health": 0.62, "education": 0.66, "income_security": 0.48, "housing": 0.36, "safety": 0.58, "social_connection": 0.44, "environment": 0.38, "time_balance": 0.40},
        {"scenario": "moderate_gdp_high_wellbeing", "consumption": 560, "investment": 170, "government": 230, "net_exports": 10, "health": 0.80, "education": 0.78, "income_security": 0.74, "housing": 0.70, "safety": 0.76, "social_connection": 0.74, "environment": 0.72, "time_balance": 0.70},
        {"scenario": "growth_with_ecological_depletion", "consumption": 690, "investment": 240, "government": 150, "net_exports": 20, "health": 0.68, "education": 0.70, "income_security": 0.60, "housing": 0.54, "safety": 0.64, "social_connection": 0.56, "environment": 0.30, "time_balance": 0.48},
        {"scenario": "low_gdp_strong_public_goods", "consumption": 470, "investment": 140, "government": 260, "net_exports": -10, "health": 0.76, "education": 0.80, "income_security": 0.70, "housing": 0.68, "safety": 0.72, "social_connection": 0.76, "environment": 0.74, "time_balance": 0.78},
        {"scenario": "recession_with_resilience", "consumption": 500, "investment": 110, "government": 250, "net_exports": 15, "health": 0.72, "education": 0.74, "income_security": 0.66, "housing": 0.62, "safety": 0.70, "social_connection": 0.72, "environment": 0.76, "time_balance": 0.68},
    ])


def build_inclusion_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"group": "top_income_decile", "distribution": 0.88, "mobility": 0.72, "access": 0.92, "voice": 0.82, "regional_equity": 0.76, "service_reach": 0.88},
        {"group": "median_households", "distribution": 0.56, "mobility": 0.54, "access": 0.66, "voice": 0.58, "regional_equity": 0.60, "service_reach": 0.64},
        {"group": "low_income_households", "distribution": 0.26, "mobility": 0.32, "access": 0.42, "voice": 0.34, "regional_equity": 0.38, "service_reach": 0.44},
        {"group": "rural_peripheral_region", "distribution": 0.38, "mobility": 0.40, "access": 0.36, "voice": 0.42, "regional_equity": 0.28, "service_reach": 0.34},
        {"group": "marginalized_urban_community", "distribution": 0.30, "mobility": 0.34, "access": 0.40, "voice": 0.30, "regional_equity": 0.36, "service_reach": 0.42},
    ])


def build_sustainability_stocks() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "output_growth_stock_depletion", "natural_capital": 0.34, "human_capital": 0.66, "institutional_trust": 0.46, "produced_capital": 0.72, "maintenance_gap": 0.66, "ecological_pressure": 0.78},
        {"scenario": "inclusive_wealth_strategy", "natural_capital": 0.72, "human_capital": 0.78, "institutional_trust": 0.76, "produced_capital": 0.74, "maintenance_gap": 0.28, "ecological_pressure": 0.34},
        {"scenario": "austerity_undermaintenance", "natural_capital": 0.58, "human_capital": 0.52, "institutional_trust": 0.38, "produced_capital": 0.50, "maintenance_gap": 0.74, "ecological_pressure": 0.46},
        {"scenario": "green_wellbeing_investment", "natural_capital": 0.78, "human_capital": 0.80, "institutional_trust": 0.74, "produced_capital": 0.78, "maintenance_gap": 0.24, "ecological_pressure": 0.30},
        {"scenario": "market_output_without_trust", "natural_capital": 0.50, "human_capital": 0.64, "institutional_trust": 0.30, "produced_capital": 0.70, "maintenance_gap": 0.56, "ecological_pressure": 0.58},
    ])


def build_adjusted_progress() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "high_output_high_damage", "current_benefits": 1000, "social_costs": 220, "ecological_costs": 260, "defensive_expenditure": 120, "unpaid_care_value": 180, "public_goods_value": 140},
        {"scenario": "moderate_output_low_damage", "current_benefits": 860, "social_costs": 90, "ecological_costs": 80, "defensive_expenditure": 50, "unpaid_care_value": 210, "public_goods_value": 220},
        {"scenario": "growth_with_household_stress", "current_benefits": 940, "social_costs": 210, "ecological_costs": 140, "defensive_expenditure": 95, "unpaid_care_value": 240, "public_goods_value": 130},
        {"scenario": "sustainable_public_goods", "current_benefits": 900, "social_costs": 80, "ecological_costs": 60, "defensive_expenditure": 40, "unpaid_care_value": 230, "public_goods_value": 260},
        {"scenario": "low_output_high_care_resilience", "current_benefits": 760, "social_costs": 70, "ecological_costs": 50, "defensive_expenditure": 35, "unpaid_care_value": 260, "public_goods_value": 240},
    ])


def build_capability_conversion() -> pd.DataFrame:
    return pd.DataFrame([
        {"household_type": "secure_middle_income", "resources": 0.66, "public_goods": 0.72, "health_conversion": 0.76, "education_conversion": 0.74, "transport_access": 0.70, "care_support": 0.66, "discrimination_barrier": 0.18},
        {"household_type": "low_income_high_public_support", "resources": 0.38, "public_goods": 0.82, "health_conversion": 0.70, "education_conversion": 0.74, "transport_access": 0.68, "care_support": 0.72, "discrimination_barrier": 0.26},
        {"household_type": "low_income_weak_services", "resources": 0.34, "public_goods": 0.36, "health_conversion": 0.42, "education_conversion": 0.40, "transport_access": 0.32, "care_support": 0.28, "discrimination_barrier": 0.52},
        {"household_type": "disabled_household_with_support", "resources": 0.48, "public_goods": 0.78, "health_conversion": 0.62, "education_conversion": 0.66, "transport_access": 0.70, "care_support": 0.82, "discrimination_barrier": 0.36},
        {"household_type": "rural_isolated_household", "resources": 0.50, "public_goods": 0.42, "health_conversion": 0.46, "education_conversion": 0.52, "transport_access": 0.28, "care_support": 0.44, "discrimination_barrier": 0.32},
    ])


def build_care_time_use() -> pd.DataFrame:
    return pd.DataFrame([
        {"group": "unpaid_family_caregivers", "paid_work_hours": 26, "unpaid_care_hours": 34, "leisure_hours": 12, "time_stress": 0.78, "formal_recognition": 0.20, "support_services": 0.34},
        {"group": "dual_earner_parents", "paid_work_hours": 72, "unpaid_care_hours": 42, "leisure_hours": 10, "time_stress": 0.82, "formal_recognition": 0.26, "support_services": 0.42},
        {"group": "single_adult_no_dependents", "paid_work_hours": 40, "unpaid_care_hours": 8, "leisure_hours": 28, "time_stress": 0.42, "formal_recognition": 0.32, "support_services": 0.50},
        {"group": "elder_care_household", "paid_work_hours": 34, "unpaid_care_hours": 30, "leisure_hours": 14, "time_stress": 0.74, "formal_recognition": 0.22, "support_services": 0.36},
        {"group": "public_care_supported_household", "paid_work_hours": 42, "unpaid_care_hours": 18, "leisure_hours": 24, "time_stress": 0.48, "formal_recognition": 0.58, "support_services": 0.76},
    ])


def build_subjective_wellbeing() -> pd.DataFrame:
    return pd.DataFrame([
        {"community": "high_income_low_trust", "income_index": 0.82, "life_satisfaction": 0.56, "stress": 0.72, "meaning": 0.52, "social_trust": 0.34, "loneliness": 0.66},
        {"community": "moderate_income_high_connection", "income_index": 0.58, "life_satisfaction": 0.76, "stress": 0.34, "meaning": 0.78, "social_trust": 0.76, "loneliness": 0.24},
        {"community": "low_income_public_security", "income_index": 0.42, "life_satisfaction": 0.64, "stress": 0.46, "meaning": 0.70, "social_trust": 0.66, "loneliness": 0.32},
        {"community": "precarious_high_cost_region", "income_index": 0.62, "life_satisfaction": 0.48, "stress": 0.82, "meaning": 0.50, "social_trust": 0.40, "loneliness": 0.58},
        {"community": "ecologically_secure_local_region", "income_index": 0.54, "life_satisfaction": 0.74, "stress": 0.36, "meaning": 0.76, "social_trust": 0.72, "loneliness": 0.28},
    ])


def build_indicator_governance() -> pd.DataFrame:
    return pd.DataFrame([
        {"system": "single_gdp_growth_target", "clarity": 0.88, "multidimensionality": 0.12, "public_legibility": 0.82, "gaming_risk": 0.70, "policy_linkage": 0.72, "local_relevance": 0.24},
        {"system": "composite_wellbeing_index", "clarity": 0.70, "multidimensionality": 0.64, "public_legibility": 0.62, "gaming_risk": 0.52, "policy_linkage": 0.58, "local_relevance": 0.48},
        {"system": "dashboard_with_budget_link", "clarity": 0.56, "multidimensionality": 0.86, "public_legibility": 0.54, "gaming_risk": 0.34, "policy_linkage": 0.82, "local_relevance": 0.70},
        {"system": "participatory_local_dashboard", "clarity": 0.50, "multidimensionality": 0.78, "public_legibility": 0.66, "gaming_risk": 0.28, "policy_linkage": 0.64, "local_relevance": 0.88},
        {"system": "decorative_indicator_report", "clarity": 0.46, "multidimensionality": 0.70, "public_legibility": 0.38, "gaming_risk": 0.42, "policy_linkage": 0.20, "local_relevance": 0.36},
    ])


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "beyond_gdp_wellbeing_inclusion_sustainability.sqlite"
    names = [
        "gdp_dashboard_scenarios",
        "inclusion_scenarios",
        "sustainability_stocks",
        "adjusted_progress",
        "capability_conversion",
        "care_time_use",
        "subjective_wellbeing",
        "indicator_governance",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_gdp_dashboard_scenarios(),
        build_inclusion_scenarios(),
        build_sustainability_stocks(),
        build_adjusted_progress(),
        build_capability_conversion(),
        build_care_time_use(),
        build_subjective_wellbeing(),
        build_indicator_governance(),
    ]

    filenames = [
        "gdp_dashboard_scenarios.csv",
        "inclusion_scenarios.csv",
        "sustainability_stocks.csv",
        "adjusted_progress.csv",
        "capability_conversion.csv",
        "care_time_use.csv",
        "subjective_wellbeing.csv",
        "indicator_governance.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created Beyond GDP well-being, inclusion, and sustainability base data.")


if __name__ == "__main__":
    main()
