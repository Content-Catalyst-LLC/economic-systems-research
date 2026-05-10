"""
Build stylized datasets for economic resilience, fragility, and adaptive capacity.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_resilience_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "optimized_low_slack_economy", "buffers": 0.30, "redundancy": 0.24, "coordination": 0.48, "trust": 0.42, "learning": 0.38, "recovery_capacity": 0.40},
        {"scenario": "public_capacity_resilience_state", "buffers": 0.78, "redundancy": 0.72, "coordination": 0.82, "trust": 0.74, "learning": 0.76, "recovery_capacity": 0.80},
        {"scenario": "private_resilience_public_fragility", "buffers": 0.58, "redundancy": 0.46, "coordination": 0.36, "trust": 0.34, "learning": 0.40, "recovery_capacity": 0.42},
        {"scenario": "local_mutual_aid_resilience", "buffers": 0.52, "redundancy": 0.66, "coordination": 0.68, "trust": 0.80, "learning": 0.72, "recovery_capacity": 0.64},
        {"scenario": "austerity_undermaintained_system", "buffers": 0.24, "redundancy": 0.26, "coordination": 0.32, "trust": 0.28, "learning": 0.30, "recovery_capacity": 0.24},
    ])


def build_fragility_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "leveraged_asset_bubble", "leverage": 0.88, "concentration": 0.64, "exposure": 0.76, "underinvestment": 0.48, "inequality": 0.70, "political_fragmentation": 0.62},
        {"scenario": "concentrated_supply_chain", "leverage": 0.50, "concentration": 0.90, "exposure": 0.82, "underinvestment": 0.56, "inequality": 0.54, "political_fragmentation": 0.48},
        {"scenario": "undermaintained_public_systems", "leverage": 0.54, "concentration": 0.52, "exposure": 0.72, "underinvestment": 0.86, "inequality": 0.68, "political_fragmentation": 0.66},
        {"scenario": "balanced_resilient_system", "leverage": 0.30, "concentration": 0.34, "exposure": 0.42, "underinvestment": 0.28, "inequality": 0.32, "political_fragmentation": 0.30},
        {"scenario": "ecological_energy_fragility", "leverage": 0.48, "concentration": 0.58, "exposure": 0.88, "underinvestment": 0.70, "inequality": 0.62, "political_fragmentation": 0.54},
    ])


def build_adaptive_capacity() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "high_information_low_legitimacy", "information": 0.78, "fiscal_space": 0.48, "skills": 0.64, "flexibility": 0.58, "legitimacy": 0.34, "implementation_capacity": 0.46},
        {"scenario": "strong_public_learning_system", "information": 0.82, "fiscal_space": 0.76, "skills": 0.78, "flexibility": 0.72, "legitimacy": 0.74, "implementation_capacity": 0.80},
        {"scenario": "low_capacity_fragmented_system", "information": 0.38, "fiscal_space": 0.30, "skills": 0.44, "flexibility": 0.36, "legitimacy": 0.28, "implementation_capacity": 0.26},
        {"scenario": "community_adaptive_capacity", "information": 0.62, "fiscal_space": 0.46, "skills": 0.66, "flexibility": 0.74, "legitimacy": 0.80, "implementation_capacity": 0.60},
        {"scenario": "technology_without_coordination", "information": 0.84, "fiscal_space": 0.54, "skills": 0.76, "flexibility": 0.58, "legitimacy": 0.42, "implementation_capacity": 0.40},
    ])


def build_shock_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"shock": "inflation_energy_spike", "shock_magnitude": 0.70, "household_vulnerability": 0.66, "firm_vulnerability": 0.58, "public_capacity": 0.50, "infrastructure_integrity": 0.62, "recovery_speed": 0.46},
        {"shock": "flood_infrastructure_failure", "shock_magnitude": 0.82, "household_vulnerability": 0.72, "firm_vulnerability": 0.62, "public_capacity": 0.42, "infrastructure_integrity": 0.34, "recovery_speed": 0.34},
        {"shock": "financial_credit_contraction", "shock_magnitude": 0.76, "household_vulnerability": 0.60, "firm_vulnerability": 0.76, "public_capacity": 0.54, "infrastructure_integrity": 0.70, "recovery_speed": 0.40},
        {"shock": "public_health_emergency", "shock_magnitude": 0.80, "household_vulnerability": 0.68, "firm_vulnerability": 0.66, "public_capacity": 0.48, "infrastructure_integrity": 0.58, "recovery_speed": 0.38},
        {"shock": "cyber_logistics_disruption", "shock_magnitude": 0.68, "household_vulnerability": 0.48, "firm_vulnerability": 0.72, "public_capacity": 0.44, "infrastructure_integrity": 0.46, "recovery_speed": 0.36},
    ])


def build_household_resilience() -> pd.DataFrame:
    return pd.DataFrame([
        {"household_group": "high_income_insured", "income_security": 0.86, "savings": 0.84, "care_access": 0.78, "housing_stability": 0.82, "social_protection": 0.62, "mobility": 0.80},
        {"household_group": "median_renter_households", "income_security": 0.52, "savings": 0.42, "care_access": 0.50, "housing_stability": 0.44, "social_protection": 0.50, "mobility": 0.54},
        {"household_group": "low_income_precarious", "income_security": 0.28, "savings": 0.16, "care_access": 0.34, "housing_stability": 0.26, "social_protection": 0.46, "mobility": 0.30},
        {"household_group": "elderly_fixed_income", "income_security": 0.50, "savings": 0.38, "care_access": 0.42, "housing_stability": 0.58, "social_protection": 0.62, "mobility": 0.26},
        {"household_group": "public_support_stabilized", "income_security": 0.66, "savings": 0.34, "care_access": 0.74, "housing_stability": 0.70, "social_protection": 0.82, "mobility": 0.56},
    ])


def build_firm_supply_chain() -> pd.DataFrame:
    return pd.DataFrame([
        {"firm_type": "single_supplier_lean_inventory", "supplier_concentration": 0.88, "inventory_buffer": 0.18, "credit_access": 0.50, "demand_diversification": 0.30, "digital_continuity": 0.42, "adaptation_capability": 0.34},
        {"firm_type": "diversified_resilient_firm", "supplier_concentration": 0.34, "inventory_buffer": 0.70, "credit_access": 0.72, "demand_diversification": 0.76, "digital_continuity": 0.74, "adaptation_capability": 0.78},
        {"firm_type": "small_business_low_buffer", "supplier_concentration": 0.58, "inventory_buffer": 0.24, "credit_access": 0.30, "demand_diversification": 0.36, "digital_continuity": 0.42, "adaptation_capability": 0.38},
        {"firm_type": "critical_supplier_monopoly", "supplier_concentration": 0.92, "inventory_buffer": 0.44, "credit_access": 0.70, "demand_diversification": 0.82, "digital_continuity": 0.62, "adaptation_capability": 0.52},
        {"firm_type": "regional_redundant_network", "supplier_concentration": 0.42, "inventory_buffer": 0.66, "credit_access": 0.58, "demand_diversification": 0.62, "digital_continuity": 0.60, "adaptation_capability": 0.70},
    ])


def build_financial_fragility() -> pd.DataFrame:
    return pd.DataFrame([
        {"system": "high_leverage_short_term_debt", "leverage": 0.88, "refinancing_risk": 0.82, "asset_price_dependence": 0.78, "liquidity_buffer": 0.22, "regulatory_capacity": 0.42, "contagion_channels": 0.76},
        {"system": "well_capitalized_banking_system", "leverage": 0.36, "refinancing_risk": 0.30, "asset_price_dependence": 0.42, "liquidity_buffer": 0.78, "regulatory_capacity": 0.82, "contagion_channels": 0.34},
        {"system": "household_debt_overhang", "leverage": 0.74, "refinancing_risk": 0.60, "asset_price_dependence": 0.70, "liquidity_buffer": 0.30, "regulatory_capacity": 0.54, "contagion_channels": 0.58},
        {"system": "shadow_finance_interconnected", "leverage": 0.82, "refinancing_risk": 0.86, "asset_price_dependence": 0.80, "liquidity_buffer": 0.24, "regulatory_capacity": 0.28, "contagion_channels": 0.88},
        {"system": "public_credit_stabilizer", "leverage": 0.44, "refinancing_risk": 0.34, "asset_price_dependence": 0.38, "liquidity_buffer": 0.70, "regulatory_capacity": 0.74, "contagion_channels": 0.36},
    ])


def build_labor_adaptation() -> pd.DataFrame:
    return pd.DataFrame([
        {"region": "single_industry_region", "skill_transferability": 0.34, "training_capacity": 0.30, "income_support": 0.36, "mobility_support": 0.28, "place_based_investment": 0.32, "employer_diversity": 0.24},
        {"region": "diverse_metropolitan_region", "skill_transferability": 0.72, "training_capacity": 0.70, "income_support": 0.58, "mobility_support": 0.66, "place_based_investment": 0.58, "employer_diversity": 0.82},
        {"region": "green_transition_cluster", "skill_transferability": 0.66, "training_capacity": 0.78, "income_support": 0.64, "mobility_support": 0.58, "place_based_investment": 0.78, "employer_diversity": 0.70},
        {"region": "precarious_service_region", "skill_transferability": 0.48, "training_capacity": 0.36, "income_support": 0.30, "mobility_support": 0.40, "place_based_investment": 0.34, "employer_diversity": 0.46},
        {"region": "public_workforce_compact", "skill_transferability": 0.70, "training_capacity": 0.76, "income_support": 0.78, "mobility_support": 0.66, "place_based_investment": 0.74, "employer_diversity": 0.64},
    ])


def build_ecological_energy_risk() -> pd.DataFrame:
    return pd.DataFrame([
        {"system": "fossil_import_dependence", "energy_volatility": 0.84, "water_stress": 0.44, "climate_hazard": 0.56, "material_dependency": 0.68, "adaptation_investment": 0.34, "ecosystem_integrity": 0.42},
        {"system": "distributed_clean_resilience", "energy_volatility": 0.34, "water_stress": 0.36, "climate_hazard": 0.50, "material_dependency": 0.42, "adaptation_investment": 0.76, "ecosystem_integrity": 0.74},
        {"system": "drought_exposed_agriculture", "energy_volatility": 0.42, "water_stress": 0.86, "climate_hazard": 0.80, "material_dependency": 0.46, "adaptation_investment": 0.30, "ecosystem_integrity": 0.34},
        {"system": "coastal_infrastructure_risk", "energy_volatility": 0.48, "water_stress": 0.62, "climate_hazard": 0.88, "material_dependency": 0.54, "adaptation_investment": 0.38, "ecosystem_integrity": 0.40},
        {"system": "restorative_regional_system", "energy_volatility": 0.38, "water_stress": 0.34, "climate_hazard": 0.42, "material_dependency": 0.36, "adaptation_investment": 0.80, "ecosystem_integrity": 0.82},
    ])


def build_recovery_learning() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "rapid_rebound_no_learning", "response_speed": 0.76, "public_capacity": 0.48, "household_stability": 0.42, "infrastructure_integrity": 0.50, "institutional_learning": 0.24, "transformational_adaptation": 0.18},
        {"scenario": "slow_recovery_deep_reform", "response_speed": 0.46, "public_capacity": 0.72, "household_stability": 0.66, "infrastructure_integrity": 0.70, "institutional_learning": 0.82, "transformational_adaptation": 0.78},
        {"scenario": "fragile_recovery_repeated_loss", "response_speed": 0.34, "public_capacity": 0.30, "household_stability": 0.28, "infrastructure_integrity": 0.32, "institutional_learning": 0.22, "transformational_adaptation": 0.16},
        {"scenario": "inclusive_resilient_reconstruction", "response_speed": 0.66, "public_capacity": 0.80, "household_stability": 0.76, "infrastructure_integrity": 0.78, "institutional_learning": 0.78, "transformational_adaptation": 0.74},
        {"scenario": "market_only_recovery", "response_speed": 0.58, "public_capacity": 0.34, "household_stability": 0.36, "infrastructure_integrity": 0.46, "institutional_learning": 0.30, "transformational_adaptation": 0.22},
    ])


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "economic_resilience_fragility_adaptive_capacity.sqlite"
    names = [
        "resilience_scenarios",
        "fragility_scenarios",
        "adaptive_capacity",
        "shock_scenarios",
        "household_resilience",
        "firm_supply_chain",
        "financial_fragility",
        "labor_adaptation",
        "ecological_energy_risk",
        "recovery_learning",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_resilience_scenarios(),
        build_fragility_scenarios(),
        build_adaptive_capacity(),
        build_shock_scenarios(),
        build_household_resilience(),
        build_firm_supply_chain(),
        build_financial_fragility(),
        build_labor_adaptation(),
        build_ecological_energy_risk(),
        build_recovery_learning(),
    ]

    filenames = [
        "resilience_scenarios.csv",
        "fragility_scenarios.csv",
        "adaptive_capacity.csv",
        "shock_scenarios.csv",
        "household_resilience.csv",
        "firm_supply_chain.csv",
        "financial_fragility.csv",
        "labor_adaptation.csv",
        "ecological_energy_risk.csv",
        "recovery_learning.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created economic resilience, fragility, and adaptive capacity base data.")


if __name__ == "__main__":
    main()
