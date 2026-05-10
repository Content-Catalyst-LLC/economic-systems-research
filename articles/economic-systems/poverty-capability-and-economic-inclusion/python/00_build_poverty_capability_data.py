"""
Build stylized datasets for poverty, capability, and economic inclusion.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_household_poverty_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"household": "h01", "income": 18, "poverty_line": 30, "savings": 1, "debt_service": 6, "housing_cost": 14, "health_cost": 5, "shock_exposure": 0.82},
        {"household": "h02", "income": 22, "poverty_line": 30, "savings": 2, "debt_service": 4, "housing_cost": 15, "health_cost": 4, "shock_exposure": 0.76},
        {"household": "h03", "income": 27, "poverty_line": 30, "savings": 3, "debt_service": 5, "housing_cost": 16, "health_cost": 2, "shock_exposure": 0.70},
        {"household": "h04", "income": 34, "poverty_line": 30, "savings": 4, "debt_service": 7, "housing_cost": 18, "health_cost": 3, "shock_exposure": 0.68},
        {"household": "h05", "income": 42, "poverty_line": 30, "savings": 6, "debt_service": 6, "housing_cost": 20, "health_cost": 4, "shock_exposure": 0.54},
        {"household": "h06", "income": 55, "poverty_line": 30, "savings": 12, "debt_service": 8, "housing_cost": 24, "health_cost": 5, "shock_exposure": 0.42},
        {"household": "h07", "income": 72, "poverty_line": 30, "savings": 22, "debt_service": 9, "housing_cost": 28, "health_cost": 6, "shock_exposure": 0.30},
        {"household": "h08", "income": 96, "poverty_line": 30, "savings": 40, "debt_service": 10, "housing_cost": 34, "health_cost": 7, "shock_exposure": 0.22},
    ])


def build_multidimensional_deprivation() -> pd.DataFrame:
    return pd.DataFrame([
        {"community": "informal_urban_settlement", "health_deprivation": 0.62, "education_deprivation": 0.52, "housing_deprivation": 0.78, "sanitation_deprivation": 0.74, "food_deprivation": 0.56, "transport_deprivation": 0.48, "digital_deprivation": 0.66, "safety_deprivation": 0.58, "institutional_exclusion": 0.60},
        {"community": "rural_service_gap_region", "health_deprivation": 0.70, "education_deprivation": 0.60, "housing_deprivation": 0.42, "sanitation_deprivation": 0.52, "food_deprivation": 0.46, "transport_deprivation": 0.78, "digital_deprivation": 0.72, "safety_deprivation": 0.34, "institutional_exclusion": 0.66},
        {"community": "post_industrial_low_work_area", "health_deprivation": 0.48, "education_deprivation": 0.44, "housing_deprivation": 0.38, "sanitation_deprivation": 0.20, "food_deprivation": 0.34, "transport_deprivation": 0.54, "digital_deprivation": 0.42, "safety_deprivation": 0.40, "institutional_exclusion": 0.50},
        {"community": "capability_investment_zone", "health_deprivation": 0.18, "education_deprivation": 0.16, "housing_deprivation": 0.22, "sanitation_deprivation": 0.10, "food_deprivation": 0.14, "transport_deprivation": 0.20, "digital_deprivation": 0.18, "safety_deprivation": 0.18, "institutional_exclusion": 0.16},
        {"community": "climate_exposed_low_income_area", "health_deprivation": 0.54, "education_deprivation": 0.46, "housing_deprivation": 0.66, "sanitation_deprivation": 0.58, "food_deprivation": 0.60, "transport_deprivation": 0.56, "digital_deprivation": 0.50, "safety_deprivation": 0.70, "institutional_exclusion": 0.52},
    ])


def build_capability_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "cash_support_weak_services", "income_score": 0.58, "health_score": 0.40, "education_score": 0.46, "mobility_score": 0.36, "safety_score": 0.42, "time_score": 0.38, "institutional_access": 0.44},
        {"scenario": "universal_services_capability_path", "income_score": 0.62, "health_score": 0.82, "education_score": 0.80, "mobility_score": 0.72, "safety_score": 0.70, "time_score": 0.66, "institutional_access": 0.78},
        {"scenario": "precarious_work_low_capability", "income_score": 0.48, "health_score": 0.44, "education_score": 0.42, "mobility_score": 0.40, "safety_score": 0.46, "time_score": 0.24, "institutional_access": 0.38},
        {"scenario": "inclusive_infrastructure_strategy", "income_score": 0.60, "health_score": 0.70, "education_score": 0.68, "mobility_score": 0.82, "safety_score": 0.66, "time_score": 0.64, "institutional_access": 0.70},
        {"scenario": "territorial_exclusion", "income_score": 0.42, "health_score": 0.34, "education_score": 0.36, "mobility_score": 0.22, "safety_score": 0.38, "time_score": 0.30, "institutional_access": 0.28},
    ])


def build_inclusion_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "formal_but_fragile_inclusion", "work_access": 0.62, "finance_access": 0.54, "service_access": 0.42, "infrastructure_access": 0.48, "digital_access": 0.50, "legal_recognition": 0.72, "participation_security": 0.34},
        {"scenario": "deep_inclusion_public_capacity", "work_access": 0.76, "finance_access": 0.68, "service_access": 0.82, "infrastructure_access": 0.80, "digital_access": 0.78, "legal_recognition": 0.88, "participation_security": 0.76},
        {"scenario": "informal_survival_economy", "work_access": 0.58, "finance_access": 0.28, "service_access": 0.32, "infrastructure_access": 0.36, "digital_access": 0.34, "legal_recognition": 0.44, "participation_security": 0.22},
        {"scenario": "digital_gatekeeping_exclusion", "work_access": 0.54, "finance_access": 0.46, "service_access": 0.50, "infrastructure_access": 0.54, "digital_access": 0.22, "legal_recognition": 0.58, "participation_security": 0.36},
        {"scenario": "place_based_inclusion_strategy", "work_access": 0.70, "finance_access": 0.60, "service_access": 0.72, "infrastructure_access": 0.82, "digital_access": 0.70, "legal_recognition": 0.78, "participation_security": 0.68},
    ])


def build_work_informality_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"sector": "informal_street_services", "wage_adequacy": 0.32, "hours_stability": 0.22, "legal_protection": 0.18, "benefit_access": 0.10, "skill_progression": 0.20, "workplace_safety": 0.30, "recognition": 0.24},
        {"sector": "low_wage_formal_services", "wage_adequacy": 0.44, "hours_stability": 0.40, "legal_protection": 0.52, "benefit_access": 0.34, "skill_progression": 0.34, "workplace_safety": 0.52, "recognition": 0.44},
        {"sector": "protected_public_service_work", "wage_adequacy": 0.72, "hours_stability": 0.80, "legal_protection": 0.84, "benefit_access": 0.86, "skill_progression": 0.68, "workplace_safety": 0.76, "recognition": 0.74},
        {"sector": "gig_platform_work", "wage_adequacy": 0.40, "hours_stability": 0.30, "legal_protection": 0.24, "benefit_access": 0.18, "skill_progression": 0.26, "workplace_safety": 0.38, "recognition": 0.30},
        {"sector": "inclusive_apprenticeship_path", "wage_adequacy": 0.58, "hours_stability": 0.66, "legal_protection": 0.70, "benefit_access": 0.62, "skill_progression": 0.80, "workplace_safety": 0.70, "recognition": 0.68},
    ])


def build_housing_infrastructure_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"community": "overcrowded_urban_rent_burden", "housing_security": 0.28, "water_sanitation": 0.54, "electricity_reliability": 0.62, "transport_access": 0.60, "digital_connectivity": 0.54, "environmental_safety": 0.34, "rent_burden": 0.72},
        {"community": "rural_infrastructure_gap", "housing_security": 0.46, "water_sanitation": 0.42, "electricity_reliability": 0.40, "transport_access": 0.22, "digital_connectivity": 0.26, "environmental_safety": 0.58, "rent_burden": 0.34},
        {"community": "stable_social_housing_services", "housing_security": 0.82, "water_sanitation": 0.86, "electricity_reliability": 0.84, "transport_access": 0.76, "digital_connectivity": 0.74, "environmental_safety": 0.78, "rent_burden": 0.24},
        {"community": "climate_exposed_informal_settlement", "housing_security": 0.20, "water_sanitation": 0.34, "electricity_reliability": 0.38, "transport_access": 0.42, "digital_connectivity": 0.40, "environmental_safety": 0.18, "rent_burden": 0.56},
        {"community": "inclusive_transit_connected_area", "housing_security": 0.68, "water_sanitation": 0.78, "electricity_reliability": 0.80, "transport_access": 0.86, "digital_connectivity": 0.76, "environmental_safety": 0.70, "rent_burden": 0.36},
    ])


def build_finance_care_digital_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "fair_financial_inclusion", "affordable_credit": 0.72, "savings_access": 0.70, "fee_burden": 0.20, "debt_stress": 0.24, "digital_literacy": 0.66, "device_access": 0.70, "platform_accessibility": 0.68},
        {"scenario": "predatory_credit_inclusion", "affordable_credit": 0.26, "savings_access": 0.34, "fee_burden": 0.72, "debt_stress": 0.78, "digital_literacy": 0.48, "device_access": 0.52, "platform_accessibility": 0.42},
        {"scenario": "care_burden_exclusion", "affordable_credit": 0.44, "savings_access": 0.38, "fee_burden": 0.44, "debt_stress": 0.58, "digital_literacy": 0.50, "device_access": 0.48, "platform_accessibility": 0.46},
        {"scenario": "digital_exclusion_barrier", "affordable_credit": 0.46, "savings_access": 0.42, "fee_burden": 0.38, "debt_stress": 0.46, "digital_literacy": 0.20, "device_access": 0.22, "platform_accessibility": 0.24},
        {"scenario": "integrated_inclusion_system", "affordable_credit": 0.78, "savings_access": 0.76, "fee_burden": 0.16, "debt_stress": 0.20, "digital_literacy": 0.82, "device_access": 0.84, "platform_accessibility": 0.80},
    ])


def build_public_service_vulnerability_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "thin_services_high_vulnerability", "healthcare_access": 0.34, "education_quality": 0.40, "childcare_support": 0.20, "food_support": 0.26, "unemployment_protection": 0.28, "disability_support": 0.24, "low_savings": 0.82, "high_debt": 0.68, "insecure_work": 0.76, "shock_exposure": 0.80},
        {"scenario": "basic_transfer_system", "healthcare_access": 0.52, "education_quality": 0.56, "childcare_support": 0.40, "food_support": 0.62, "unemployment_protection": 0.48, "disability_support": 0.44, "low_savings": 0.66, "high_debt": 0.52, "insecure_work": 0.58, "shock_exposure": 0.62},
        {"scenario": "universal_capability_services", "healthcare_access": 0.84, "education_quality": 0.82, "childcare_support": 0.76, "food_support": 0.72, "unemployment_protection": 0.74, "disability_support": 0.78, "low_savings": 0.36, "high_debt": 0.28, "insecure_work": 0.34, "shock_exposure": 0.32},
        {"scenario": "austerity_service_erosion", "healthcare_access": 0.38, "education_quality": 0.42, "childcare_support": 0.28, "food_support": 0.34, "unemployment_protection": 0.32, "disability_support": 0.30, "low_savings": 0.78, "high_debt": 0.62, "insecure_work": 0.70, "shock_exposure": 0.76},
        {"scenario": "place_based_social_protection", "healthcare_access": 0.72, "education_quality": 0.70, "childcare_support": 0.66, "food_support": 0.68, "unemployment_protection": 0.64, "disability_support": 0.66, "low_savings": 0.44, "high_debt": 0.36, "insecure_work": 0.42, "shock_exposure": 0.40},
    ])


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "poverty_capability_economic_inclusion.sqlite"
    names = [
        "household_poverty_scenarios",
        "multidimensional_deprivation",
        "capability_scenarios",
        "inclusion_scenarios",
        "work_informality_scenarios",
        "housing_infrastructure_scenarios",
        "finance_care_digital_scenarios",
        "public_service_vulnerability_scenarios",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_household_poverty_scenarios(),
        build_multidimensional_deprivation(),
        build_capability_scenarios(),
        build_inclusion_scenarios(),
        build_work_informality_scenarios(),
        build_housing_infrastructure_scenarios(),
        build_finance_care_digital_scenarios(),
        build_public_service_vulnerability_scenarios(),
    ]

    filenames = [
        "household_poverty_scenarios.csv",
        "multidimensional_deprivation.csv",
        "capability_scenarios.csv",
        "inclusion_scenarios.csv",
        "work_informality_scenarios.csv",
        "housing_infrastructure_scenarios.csv",
        "finance_care_digital_scenarios.csv",
        "public_service_vulnerability_scenarios.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created poverty, capability, and economic inclusion base data.")


if __name__ == "__main__":
    main()
