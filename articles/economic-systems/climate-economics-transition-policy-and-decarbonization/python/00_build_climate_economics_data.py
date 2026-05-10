"""
Build stylized datasets for climate economics, transition policy, and decarbonization.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_sector_emissions() -> pd.DataFrame:
    return pd.DataFrame([
        {"sector": "electricity_power", "output": 520, "energy_intensity": 0.70, "carbon_intensity": 0.42, "old_emissions_intensity": 0.42, "new_emissions_intensity": 0.25, "years": 5, "abatement_readiness": 0.78},
        {"sector": "transport_mobility", "output": 440, "energy_intensity": 0.82, "carbon_intensity": 0.48, "old_emissions_intensity": 0.50, "new_emissions_intensity": 0.38, "years": 5, "abatement_readiness": 0.54},
        {"sector": "buildings_heat", "output": 360, "energy_intensity": 0.64, "carbon_intensity": 0.36, "old_emissions_intensity": 0.38, "new_emissions_intensity": 0.28, "years": 5, "abatement_readiness": 0.58},
        {"sector": "heavy_industry", "output": 410, "energy_intensity": 0.90, "carbon_intensity": 0.55, "old_emissions_intensity": 0.62, "new_emissions_intensity": 0.52, "years": 5, "abatement_readiness": 0.34},
        {"sector": "agriculture_land_use", "output": 300, "energy_intensity": 0.46, "carbon_intensity": 0.40, "old_emissions_intensity": 0.32, "new_emissions_intensity": 0.29, "years": 5, "abatement_readiness": 0.42},
        {"sector": "public_services_infrastructure", "output": 260, "energy_intensity": 0.38, "carbon_intensity": 0.30, "old_emissions_intensity": 0.24, "new_emissions_intensity": 0.18, "years": 5, "abatement_readiness": 0.62},
    ])


def build_policy_packages() -> pd.DataFrame:
    return pd.DataFrame([
        {"package": "price_only_low_support", "carbon_price_strength": 0.74, "regulatory_strength": 0.28, "public_investment": 0.24, "industrial_policy": 0.22, "social_protection": 0.18, "implementation_capacity": 0.38},
        {"package": "standards_and_public_investment", "carbon_price_strength": 0.42, "regulatory_strength": 0.74, "public_investment": 0.76, "industrial_policy": 0.56, "social_protection": 0.58, "implementation_capacity": 0.66},
        {"package": "green_industrial_strategy", "carbon_price_strength": 0.48, "regulatory_strength": 0.66, "public_investment": 0.78, "industrial_policy": 0.84, "social_protection": 0.62, "implementation_capacity": 0.70},
        {"package": "just_transition_investment_compact", "carbon_price_strength": 0.44, "regulatory_strength": 0.70, "public_investment": 0.82, "industrial_policy": 0.76, "social_protection": 0.84, "implementation_capacity": 0.76},
        {"package": "weak_voluntary_transition", "carbon_price_strength": 0.18, "regulatory_strength": 0.24, "public_investment": 0.22, "industrial_policy": 0.20, "social_protection": 0.24, "implementation_capacity": 0.30},
    ])


def build_transition_investment() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "credible_public_de_risking", "public_investment": 0.78, "private_capital": 0.70, "policy_credibility": 0.76, "cost_of_capital_support": 0.72, "permitting_capacity": 0.66, "grid_readiness": 0.68},
        {"scenario": "high_capital_cost_uncertainty", "public_investment": 0.46, "private_capital": 0.42, "policy_credibility": 0.38, "cost_of_capital_support": 0.30, "permitting_capacity": 0.44, "grid_readiness": 0.38},
        {"scenario": "public_infrastructure_push", "public_investment": 0.84, "private_capital": 0.58, "policy_credibility": 0.70, "cost_of_capital_support": 0.64, "permitting_capacity": 0.62, "grid_readiness": 0.72},
        {"scenario": "private_led_green_finance", "public_investment": 0.48, "private_capital": 0.76, "policy_credibility": 0.58, "cost_of_capital_support": 0.54, "permitting_capacity": 0.50, "grid_readiness": 0.48},
        {"scenario": "fragmented_transition_finance", "public_investment": 0.36, "private_capital": 0.44, "policy_credibility": 0.34, "cost_of_capital_support": 0.32, "permitting_capacity": 0.36, "grid_readiness": 0.34},
    ])


def build_carbon_lock_in() -> pd.DataFrame:
    return pd.DataFrame([
        {"system": "gas_distribution_networks", "capital_stock_life": 0.74, "infrastructure_dependence": 0.82, "incumbent_power": 0.68, "consumer_switching_barrier": 0.66, "replacement_readiness": 0.42, "stranded_asset_risk": 0.70},
        {"system": "suburban_auto_dependence", "capital_stock_life": 0.68, "infrastructure_dependence": 0.88, "incumbent_power": 0.52, "consumer_switching_barrier": 0.84, "replacement_readiness": 0.36, "stranded_asset_risk": 0.52},
        {"system": "coal_power_assets", "capital_stock_life": 0.58, "infrastructure_dependence": 0.62, "incumbent_power": 0.70, "consumer_switching_barrier": 0.34, "replacement_readiness": 0.72, "stranded_asset_risk": 0.86},
        {"system": "industrial_process_heat", "capital_stock_life": 0.80, "infrastructure_dependence": 0.76, "incumbent_power": 0.64, "consumer_switching_barrier": 0.52, "replacement_readiness": 0.30, "stranded_asset_risk": 0.62},
        {"system": "grid_transmission_bottlenecks", "capital_stock_life": 0.64, "infrastructure_dependence": 0.82, "incumbent_power": 0.44, "consumer_switching_barrier": 0.40, "replacement_readiness": 0.46, "stranded_asset_risk": 0.36},
    ])


def build_damage_adaptation() -> pd.DataFrame:
    return pd.DataFrame([
        {"region": "heat_exposed_city", "temperature_stress": 0.82, "flood_exposure": 0.38, "wildfire_smoke": 0.48, "economic_exposure": 0.66, "vulnerability": 0.70, "adaptation_capacity": 0.42, "public_health_capacity": 0.50},
        {"region": "coastal_settlement", "temperature_stress": 0.50, "flood_exposure": 0.86, "wildfire_smoke": 0.22, "economic_exposure": 0.74, "vulnerability": 0.68, "adaptation_capacity": 0.46, "public_health_capacity": 0.54},
        {"region": "agricultural_dryland", "temperature_stress": 0.76, "flood_exposure": 0.26, "wildfire_smoke": 0.52, "economic_exposure": 0.62, "vulnerability": 0.74, "adaptation_capacity": 0.34, "public_health_capacity": 0.40},
        {"region": "wealthy_resilient_region", "temperature_stress": 0.44, "flood_exposure": 0.32, "wildfire_smoke": 0.30, "economic_exposure": 0.50, "vulnerability": 0.26, "adaptation_capacity": 0.82, "public_health_capacity": 0.78},
        {"region": "low_income_delta_region", "temperature_stress": 0.68, "flood_exposure": 0.90, "wildfire_smoke": 0.18, "economic_exposure": 0.78, "vulnerability": 0.86, "adaptation_capacity": 0.22, "public_health_capacity": 0.30},
    ])


def build_just_transition() -> pd.DataFrame:
    return pd.DataFrame([
        {"community": "coal_region_declining_tax_base", "worker_exposure": 0.86, "retraining": 0.38, "regional_investment": 0.34, "income_support": 0.40, "public_services": 0.42, "new_industry_pipeline": 0.32, "labor_standards": 0.44},
        {"community": "refinery_port_transition", "worker_exposure": 0.72, "retraining": 0.52, "regional_investment": 0.50, "income_support": 0.48, "public_services": 0.54, "new_industry_pipeline": 0.58, "labor_standards": 0.56},
        {"community": "clean_manufacturing_cluster", "worker_exposure": 0.34, "retraining": 0.70, "regional_investment": 0.78, "income_support": 0.60, "public_services": 0.66, "new_industry_pipeline": 0.82, "labor_standards": 0.72},
        {"community": "rural_energy_land_use_region", "worker_exposure": 0.50, "retraining": 0.48, "regional_investment": 0.56, "income_support": 0.44, "public_services": 0.50, "new_industry_pipeline": 0.58, "labor_standards": 0.52},
        {"community": "just_transition_compact_region", "worker_exposure": 0.62, "retraining": 0.78, "regional_investment": 0.82, "income_support": 0.76, "public_services": 0.80, "new_industry_pipeline": 0.78, "labor_standards": 0.84},
    ])


def build_hard_to_abate() -> pd.DataFrame:
    return pd.DataFrame([
        {"sector": "steel", "process_emissions": 0.72, "temperature_requirement": 0.78, "technology_readiness": 0.44, "procurement_leverage": 0.72, "demand_reduction_potential": 0.40, "carbon_capture_relevance": 0.42},
        {"sector": "cement", "process_emissions": 0.86, "temperature_requirement": 0.72, "technology_readiness": 0.36, "procurement_leverage": 0.68, "demand_reduction_potential": 0.52, "carbon_capture_relevance": 0.70},
        {"sector": "chemicals", "process_emissions": 0.66, "temperature_requirement": 0.64, "technology_readiness": 0.42, "procurement_leverage": 0.46, "demand_reduction_potential": 0.38, "carbon_capture_relevance": 0.50},
        {"sector": "shipping", "process_emissions": 0.48, "temperature_requirement": 0.42, "technology_readiness": 0.40, "procurement_leverage": 0.34, "demand_reduction_potential": 0.30, "carbon_capture_relevance": 0.12},
        {"sector": "aviation", "process_emissions": 0.54, "temperature_requirement": 0.36, "technology_readiness": 0.26, "procurement_leverage": 0.22, "demand_reduction_potential": 0.46, "carbon_capture_relevance": 0.18},
    ])


def build_global_equity() -> pd.DataFrame:
    return pd.DataFrame([
        {"country_group": "high_income_historical_emitters", "historic_responsibility": 0.88, "current_emissions": 0.58, "fiscal_capacity": 0.86, "climate_vulnerability": 0.32, "development_need": 0.24, "technology_capacity": 0.84},
        {"country_group": "emerging_industrial_economies", "historic_responsibility": 0.42, "current_emissions": 0.76, "fiscal_capacity": 0.54, "climate_vulnerability": 0.58, "development_need": 0.64, "technology_capacity": 0.58},
        {"country_group": "low_income_vulnerable_countries", "historic_responsibility": 0.08, "current_emissions": 0.12, "fiscal_capacity": 0.18, "climate_vulnerability": 0.86, "development_need": 0.88, "technology_capacity": 0.22},
        {"country_group": "small_island_states", "historic_responsibility": 0.04, "current_emissions": 0.04, "fiscal_capacity": 0.24, "climate_vulnerability": 0.92, "development_need": 0.70, "technology_capacity": 0.28},
        {"country_group": "resource_exporting_transition_states", "historic_responsibility": 0.36, "current_emissions": 0.46, "fiscal_capacity": 0.42, "climate_vulnerability": 0.56, "development_need": 0.58, "technology_capacity": 0.38},
    ])


def build_implementation_credibility() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "target_rich_capacity_poor", "target_clarity": 0.82, "administrative_capacity": 0.34, "fiscal_commitment": 0.38, "policy_durability": 0.32, "public_trust": 0.36, "coordination_capacity": 0.30},
        {"scenario": "credible_transition_state", "target_clarity": 0.78, "administrative_capacity": 0.76, "fiscal_commitment": 0.74, "policy_durability": 0.72, "public_trust": 0.68, "coordination_capacity": 0.74},
        {"scenario": "volatile_policy_reversal", "target_clarity": 0.60, "administrative_capacity": 0.48, "fiscal_commitment": 0.42, "policy_durability": 0.22, "public_trust": 0.30, "coordination_capacity": 0.40},
        {"scenario": "local_capacity_strong_national_weak", "target_clarity": 0.52, "administrative_capacity": 0.58, "fiscal_commitment": 0.46, "policy_durability": 0.44, "public_trust": 0.54, "coordination_capacity": 0.38},
        {"scenario": "mission_oriented_public_capacity", "target_clarity": 0.84, "administrative_capacity": 0.82, "fiscal_commitment": 0.80, "policy_durability": 0.78, "public_trust": 0.72, "coordination_capacity": 0.84},
    ])


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "climate_economics_transition_policy_decarbonization.sqlite"
    names = [
        "sector_emissions",
        "policy_packages",
        "transition_investment",
        "carbon_lock_in",
        "damage_adaptation",
        "just_transition",
        "hard_to_abate",
        "global_equity",
        "implementation_credibility",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_sector_emissions(),
        build_policy_packages(),
        build_transition_investment(),
        build_carbon_lock_in(),
        build_damage_adaptation(),
        build_just_transition(),
        build_hard_to_abate(),
        build_global_equity(),
        build_implementation_credibility(),
    ]

    filenames = [
        "sector_emissions.csv",
        "policy_packages.csv",
        "transition_investment.csv",
        "carbon_lock_in.csv",
        "damage_adaptation.csv",
        "just_transition.csv",
        "hard_to_abate.csv",
        "global_equity.csv",
        "implementation_credibility.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created climate economics, transition policy, and decarbonization base data.")


if __name__ == "__main__":
    main()
