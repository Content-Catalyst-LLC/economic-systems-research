"""
Build stylized datasets for the welfare state and social protection.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_household_tax_transfer() -> pd.DataFrame:
    return pd.DataFrame([
        {"household": "low_income_single_parent", "market_income": 28, "taxes": 2, "transfers": 18, "service_value": 16, "housing_cost": 18, "care_cost": 8},
        {"household": "low_wage_worker", "market_income": 36, "taxes": 4, "transfers": 9, "service_value": 12, "housing_cost": 16, "care_cost": 2},
        {"household": "unemployed_worker", "market_income": 12, "taxes": 0.5, "transfers": 24, "service_value": 14, "housing_cost": 14, "care_cost": 3},
        {"household": "disabled_adult", "market_income": 18, "taxes": 1, "transfers": 20, "service_value": 18, "housing_cost": 12, "care_cost": 9},
        {"household": "middle_income_family", "market_income": 82, "taxes": 16, "transfers": 8, "service_value": 15, "housing_cost": 28, "care_cost": 10},
        {"household": "retired_household", "market_income": 24, "taxes": 3, "transfers": 30, "service_value": 20, "housing_cost": 10, "care_cost": 6},
        {"household": "high_income_household", "market_income": 210, "taxes": 62, "transfers": 2, "service_value": 8, "housing_cost": 52, "care_cost": 4},
    ])


def build_social_spending_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "thin_residual_system", "social_spending": 160, "output": 1500, "healthcare_spending": 44, "pensions": 50, "unemployment": 12, "family_policy": 10, "housing_support": 8, "disability_support": 12, "administration_quality": 0.42},
        {"scenario": "targeted_assistance_model", "social_spending": 240, "output": 1500, "healthcare_spending": 72, "pensions": 66, "unemployment": 18, "family_policy": 20, "housing_support": 18, "disability_support": 18, "administration_quality": 0.56},
        {"scenario": "social_insurance_model", "social_spending": 335, "output": 1500, "healthcare_spending": 98, "pensions": 112, "unemployment": 28, "family_policy": 26, "housing_support": 18, "disability_support": 26, "administration_quality": 0.70},
        {"scenario": "universal_services_model", "social_spending": 430, "output": 1500, "healthcare_spending": 132, "pensions": 118, "unemployment": 32, "family_policy": 48, "housing_support": 34, "disability_support": 30, "administration_quality": 0.82},
        {"scenario": "austerity_erosion_model", "social_spending": 205, "output": 1500, "healthcare_spending": 60, "pensions": 70, "unemployment": 10, "family_policy": 14, "housing_support": 8, "disability_support": 14, "administration_quality": 0.38},
    ])


def build_program_coverage() -> pd.DataFrame:
    return pd.DataFrame([
        {"program": "unemployment_insurance", "covered_population": 620, "target_population": 900, "benefit": 24, "previous_earnings": 44, "take_up_rate": 0.72, "administrative_burden": 0.34, "stigma_cost": 0.18},
        {"program": "basic_income_support", "covered_population": 780, "target_population": 1000, "benefit": 16, "previous_earnings": 32, "take_up_rate": 0.76, "administrative_burden": 0.42, "stigma_cost": 0.38},
        {"program": "universal_child_benefit", "covered_population": 960, "target_population": 1000, "benefit": 10, "previous_earnings": 28, "take_up_rate": 0.95, "administrative_burden": 0.12, "stigma_cost": 0.06},
        {"program": "disability_support", "covered_population": 540, "target_population": 800, "benefit": 26, "previous_earnings": 38, "take_up_rate": 0.66, "administrative_burden": 0.56, "stigma_cost": 0.30},
        {"program": "old_age_pension", "covered_population": 920, "target_population": 980, "benefit": 30, "previous_earnings": 50, "take_up_rate": 0.94, "administrative_burden": 0.18, "stigma_cost": 0.05},
        {"program": "housing_support", "covered_population": 430, "target_population": 850, "benefit": 14, "previous_earnings": 36, "take_up_rate": 0.58, "administrative_burden": 0.62, "stigma_cost": 0.36},
    ])


def build_welfare_regime_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"regime": "residual_means_tested", "universalism": 0.22, "targeting_precision": 0.70, "benefit_adequacy": 0.36, "service_quality": 0.34, "labor_market_security": 0.28, "dignity_score": 0.30, "political_durability": 0.34},
        {"regime": "employment_linked_social_insurance", "universalism": 0.52, "targeting_precision": 0.48, "benefit_adequacy": 0.64, "service_quality": 0.58, "labor_market_security": 0.62, "dignity_score": 0.58, "political_durability": 0.66},
        {"regime": "universal_social_democratic", "universalism": 0.84, "targeting_precision": 0.36, "benefit_adequacy": 0.76, "service_quality": 0.82, "labor_market_security": 0.74, "dignity_score": 0.82, "political_durability": 0.78},
        {"regime": "fragmented_dual_system", "universalism": 0.38, "targeting_precision": 0.54, "benefit_adequacy": 0.44, "service_quality": 0.42, "labor_market_security": 0.40, "dignity_score": 0.38, "political_durability": 0.42},
        {"regime": "adaptive_resilience_oriented", "universalism": 0.72, "targeting_precision": 0.62, "benefit_adequacy": 0.70, "service_quality": 0.76, "labor_market_security": 0.68, "dignity_score": 0.76, "political_durability": 0.72},
    ])


def build_life_course_risk() -> pd.DataFrame:
    return pd.DataFrame([
        {"risk": "childhood_poverty", "baseline_vulnerability": 0.78, "protected_vulnerability": 0.34, "coverage": 0.82, "adequacy": 0.68, "duration_support": 0.72, "service_integration": 0.70},
        {"risk": "unemployment", "baseline_vulnerability": 0.72, "protected_vulnerability": 0.40, "coverage": 0.68, "adequacy": 0.56, "duration_support": 0.52, "service_integration": 0.48},
        {"risk": "sickness", "baseline_vulnerability": 0.74, "protected_vulnerability": 0.28, "coverage": 0.86, "adequacy": 0.72, "duration_support": 0.66, "service_integration": 0.74},
        {"risk": "disability", "baseline_vulnerability": 0.82, "protected_vulnerability": 0.42, "coverage": 0.66, "adequacy": 0.62, "duration_support": 0.78, "service_integration": 0.58},
        {"risk": "caregiving", "baseline_vulnerability": 0.70, "protected_vulnerability": 0.44, "coverage": 0.54, "adequacy": 0.48, "duration_support": 0.42, "service_integration": 0.52},
        {"risk": "old_age", "baseline_vulnerability": 0.76, "protected_vulnerability": 0.30, "coverage": 0.92, "adequacy": 0.68, "duration_support": 0.88, "service_integration": 0.64},
    ])


def build_care_family_policy() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "private_family_care_burden", "childcare_support": 0.18, "paid_leave": 0.20, "eldercare_support": 0.16, "disability_care_support": 0.22, "care_worker_protection": 0.24, "female_labor_participation_support": 0.30, "child_development_support": 0.34},
        {"scenario": "targeted_childcare_support", "childcare_support": 0.56, "paid_leave": 0.42, "eldercare_support": 0.30, "disability_care_support": 0.36, "care_worker_protection": 0.38, "female_labor_participation_support": 0.54, "child_development_support": 0.58},
        {"scenario": "universal_care_infrastructure", "childcare_support": 0.84, "paid_leave": 0.78, "eldercare_support": 0.72, "disability_care_support": 0.76, "care_worker_protection": 0.78, "female_labor_participation_support": 0.82, "child_development_support": 0.84},
        {"scenario": "austerity_care_gap", "childcare_support": 0.30, "paid_leave": 0.26, "eldercare_support": 0.24, "disability_care_support": 0.28, "care_worker_protection": 0.26, "female_labor_participation_support": 0.34, "child_development_support": 0.36},
        {"scenario": "integrated_family_policy", "childcare_support": 0.72, "paid_leave": 0.70, "eldercare_support": 0.60, "disability_care_support": 0.66, "care_worker_protection": 0.68, "female_labor_participation_support": 0.74, "child_development_support": 0.76},
    ])


def build_fiscal_capacity() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "low_tax_weak_capacity", "tax_revenue": 240, "output": 1500, "administrative_capacity": 0.36, "compliance_strength": 0.40, "progressivity": 0.28, "benefit_delivery_quality": 0.34, "automatic_stabilizer_strength": 0.30},
        {"scenario": "payroll_insurance_capacity", "tax_revenue": 360, "output": 1500, "administrative_capacity": 0.62, "compliance_strength": 0.66, "progressivity": 0.44, "benefit_delivery_quality": 0.62, "automatic_stabilizer_strength": 0.58},
        {"scenario": "broad_progressive_capacity", "tax_revenue": 500, "output": 1500, "administrative_capacity": 0.80, "compliance_strength": 0.82, "progressivity": 0.76, "benefit_delivery_quality": 0.82, "automatic_stabilizer_strength": 0.78},
        {"scenario": "fragmented_informal_capacity", "tax_revenue": 280, "output": 1500, "administrative_capacity": 0.44, "compliance_strength": 0.38, "progressivity": 0.34, "benefit_delivery_quality": 0.42, "automatic_stabilizer_strength": 0.36},
        {"scenario": "resilience_oriented_fiscal_state", "tax_revenue": 460, "output": 1500, "administrative_capacity": 0.76, "compliance_strength": 0.78, "progressivity": 0.68, "benefit_delivery_quality": 0.78, "automatic_stabilizer_strength": 0.82},
    ])


def build_digital_administration() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "paper_fragmented_access", "digital_access": 0.24, "identity_coverage": 0.48, "application_simplicity": 0.34, "appeal_access": 0.38, "automation_error_risk": 0.28, "data_protection": 0.40, "human_support": 0.58},
        {"scenario": "automated_high_error_system", "digital_access": 0.62, "identity_coverage": 0.72, "application_simplicity": 0.56, "appeal_access": 0.34, "automation_error_risk": 0.74, "data_protection": 0.42, "human_support": 0.28},
        {"scenario": "digital_inclusion_with_human_support", "digital_access": 0.78, "identity_coverage": 0.84, "application_simplicity": 0.78, "appeal_access": 0.76, "automation_error_risk": 0.20, "data_protection": 0.76, "human_support": 0.80},
        {"scenario": "mobile_payment_reach_low_appeal", "digital_access": 0.70, "identity_coverage": 0.76, "application_simplicity": 0.68, "appeal_access": 0.38, "automation_error_risk": 0.42, "data_protection": 0.46, "human_support": 0.44},
        {"scenario": "rights_based_digital_administration", "digital_access": 0.82, "identity_coverage": 0.88, "application_simplicity": 0.84, "appeal_access": 0.82, "automation_error_risk": 0.14, "data_protection": 0.84, "human_support": 0.78},
    ])


def build_adaptive_protection() -> pd.DataFrame:
    return pd.DataFrame([
        {"shock": "heat_wave_income_loss", "baseline_exposure": 0.62, "scale_up_capacity": 0.48, "payment_speed": 0.52, "registry_quality": 0.58, "local_delivery_capacity": 0.54, "benefit_adequacy": 0.46, "post_shock_vulnerability": 0.56},
        {"shock": "flood_displacement", "baseline_exposure": 0.74, "scale_up_capacity": 0.42, "payment_speed": 0.44, "registry_quality": 0.50, "local_delivery_capacity": 0.38, "benefit_adequacy": 0.40, "post_shock_vulnerability": 0.68},
        {"shock": "food_price_spike", "baseline_exposure": 0.70, "scale_up_capacity": 0.62, "payment_speed": 0.68, "registry_quality": 0.64, "local_delivery_capacity": 0.60, "benefit_adequacy": 0.58, "post_shock_vulnerability": 0.48},
        {"shock": "pandemic_labor_shutdown", "baseline_exposure": 0.82, "scale_up_capacity": 0.58, "payment_speed": 0.56, "registry_quality": 0.62, "local_delivery_capacity": 0.52, "benefit_adequacy": 0.54, "post_shock_vulnerability": 0.58},
        {"shock": "adaptive_resilience_preparedness", "baseline_exposure": 0.60, "scale_up_capacity": 0.82, "payment_speed": 0.84, "registry_quality": 0.80, "local_delivery_capacity": 0.78, "benefit_adequacy": 0.76, "post_shock_vulnerability": 0.30},
    ])


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "welfare_state_social_protection.sqlite"
    names = [
        "household_tax_transfer",
        "social_spending_scenarios",
        "program_coverage",
        "welfare_regime_scenarios",
        "life_course_risk",
        "care_family_policy",
        "fiscal_capacity",
        "digital_administration",
        "adaptive_protection",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_household_tax_transfer(),
        build_social_spending_scenarios(),
        build_program_coverage(),
        build_welfare_regime_scenarios(),
        build_life_course_risk(),
        build_care_family_policy(),
        build_fiscal_capacity(),
        build_digital_administration(),
        build_adaptive_protection(),
    ]

    filenames = [
        "household_tax_transfer.csv",
        "social_spending_scenarios.csv",
        "program_coverage.csv",
        "welfare_regime_scenarios.csv",
        "life_course_risk.csv",
        "care_family_policy.csv",
        "fiscal_capacity.csv",
        "digital_administration.csv",
        "adaptive_protection.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created welfare state and social protection base data.")


if __name__ == "__main__":
    main()
