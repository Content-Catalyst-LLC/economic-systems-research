"""
Build stylized datasets for inflation, energy shocks, and supply constraints.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_price_index_scenarios() -> pd.DataFrame:
    rows = []
    paths = {
        "stable_price_environment": [100, 102, 104, 106, 108, 110],
        "demand_led_inflation": [100, 103, 107, 112, 118, 124],
        "energy_shock_inflation": [100, 104, 113, 121, 126, 129],
        "supply_bottleneck_inflation": [100, 103, 110, 118, 123, 126],
        "policy_stabilized_disinflation": [100, 104, 111, 116, 118, 119],
        "resilience_reduced_pass_through": [100, 103, 108, 112, 114, 116],
    }
    for scenario, values in paths.items():
        for period, price_level in enumerate(values):
            rows.append({"scenario": scenario, "period": period, "price_level": price_level})
    return pd.DataFrame(rows)


def build_sector_energy_pass_through_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"sector": "freight_transport", "energy_cost_change": 0.28, "wage_cost_change": 0.05, "materials_cost_change": 0.04, "alpha_energy": 0.62, "beta_wage": 0.22, "gamma_materials": 0.16},
        {"sector": "food_processing", "energy_cost_change": 0.24, "wage_cost_change": 0.04, "materials_cost_change": 0.12, "alpha_energy": 0.38, "beta_wage": 0.24, "gamma_materials": 0.38},
        {"sector": "fertilizer_and_agriculture", "energy_cost_change": 0.35, "wage_cost_change": 0.03, "materials_cost_change": 0.16, "alpha_energy": 0.58, "beta_wage": 0.12, "gamma_materials": 0.30},
        {"sector": "manufacturing_inputs", "energy_cost_change": 0.22, "wage_cost_change": 0.06, "materials_cost_change": 0.14, "alpha_energy": 0.36, "beta_wage": 0.26, "gamma_materials": 0.38},
        {"sector": "public_utilities", "energy_cost_change": 0.30, "wage_cost_change": 0.04, "materials_cost_change": 0.08, "alpha_energy": 0.72, "beta_wage": 0.12, "gamma_materials": 0.16},
        {"sector": "construction_materials", "energy_cost_change": 0.21, "wage_cost_change": 0.05, "materials_cost_change": 0.18, "alpha_energy": 0.30, "beta_wage": 0.18, "gamma_materials": 0.52},
        {"sector": "digital_infrastructure", "energy_cost_change": 0.18, "wage_cost_change": 0.07, "materials_cost_change": 0.06, "alpha_energy": 0.48, "beta_wage": 0.32, "gamma_materials": 0.20},
    ])


def build_household_energy_burden_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"household_group": "lowest_income_renter", "income": 2200, "energy_spending": 310, "transport_fuel_spending": 220, "nominal_wage": 18, "price_level_relative": 1.12},
        {"household_group": "working_class_commuter", "income": 3600, "energy_spending": 360, "transport_fuel_spending": 420, "nominal_wage": 24, "price_level_relative": 1.11},
        {"household_group": "median_household", "income": 5600, "energy_spending": 420, "transport_fuel_spending": 390, "nominal_wage": 32, "price_level_relative": 1.10},
        {"household_group": "suburban_high_transport_dependence", "income": 6900, "energy_spending": 500, "transport_fuel_spending": 620, "nominal_wage": 39, "price_level_relative": 1.10},
        {"household_group": "retired_fixed_income", "income": 3100, "energy_spending": 390, "transport_fuel_spending": 160, "nominal_wage": 0, "price_level_relative": 1.13},
        {"household_group": "high_income_buffered", "income": 12800, "energy_spending": 620, "transport_fuel_spending": 520, "nominal_wage": 72, "price_level_relative": 1.09},
    ])


def build_import_price_transmission_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "moderate_energy_import_shock", "world_price_change": 0.18, "exchange_rate_effect": 0.04, "import_dependence": 0.45, "energy_share_of_imports": 0.32},
        {"scenario": "currency_depreciation_energy_spike", "world_price_change": 0.24, "exchange_rate_effect": 0.12, "import_dependence": 0.52, "energy_share_of_imports": 0.38},
        {"scenario": "food_and_fertilizer_import_shock", "world_price_change": 0.20, "exchange_rate_effect": 0.06, "import_dependence": 0.36, "energy_share_of_imports": 0.20},
        {"scenario": "reserve_currency_tightening", "world_price_change": 0.14, "exchange_rate_effect": 0.16, "import_dependence": 0.48, "energy_share_of_imports": 0.30},
        {"scenario": "diversified_supply_low_pass_through", "world_price_change": 0.16, "exchange_rate_effect": 0.03, "import_dependence": 0.24, "energy_share_of_imports": 0.18},
    ])


def build_supply_bottleneck_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "normal_capacity", "capital_capacity": 0.94, "labor_capacity": 0.93, "energy_capacity": 0.95, "logistics_capacity": 0.92, "supply_availability": 0.94},
        {"scenario": "energy_bottleneck", "capital_capacity": 0.92, "labor_capacity": 0.91, "energy_capacity": 0.68, "logistics_capacity": 0.88, "supply_availability": 0.86},
        {"scenario": "port_and_logistics_congestion", "capital_capacity": 0.90, "labor_capacity": 0.88, "energy_capacity": 0.90, "logistics_capacity": 0.62, "supply_availability": 0.74},
        {"scenario": "labor_and_care_constraint", "capital_capacity": 0.91, "labor_capacity": 0.66, "energy_capacity": 0.87, "logistics_capacity": 0.82, "supply_availability": 0.80},
        {"scenario": "climate_food_supply_shock", "capital_capacity": 0.88, "labor_capacity": 0.86, "energy_capacity": 0.82, "logistics_capacity": 0.78, "supply_availability": 0.58},
        {"scenario": "resilient_redundancy", "capital_capacity": 0.92, "labor_capacity": 0.90, "energy_capacity": 0.88, "logistics_capacity": 0.87, "supply_availability": 0.89},
    ])


def build_market_power_price_amplification_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"sector": "competitive_food_retail", "cost_shock": 0.10, "market_concentration_index": 0.22, "margin_expansion": 0.01, "demand_necessity_score": 0.85},
        {"sector": "concentrated_energy_distribution", "cost_shock": 0.18, "market_concentration_index": 0.72, "margin_expansion": 0.05, "demand_necessity_score": 0.96},
        {"sector": "shipping_and_freight", "cost_shock": 0.16, "market_concentration_index": 0.64, "margin_expansion": 0.06, "demand_necessity_score": 0.82},
        {"sector": "building_materials", "cost_shock": 0.14, "market_concentration_index": 0.58, "margin_expansion": 0.04, "demand_necessity_score": 0.70},
        {"sector": "pharmaceutical_inputs", "cost_shock": 0.11, "market_concentration_index": 0.68, "margin_expansion": 0.05, "demand_necessity_score": 0.92},
        {"sector": "competitive_consumer_goods", "cost_shock": 0.08, "market_concentration_index": 0.20, "margin_expansion": 0.01, "demand_necessity_score": 0.42},
    ])


def build_resilience_policy_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"policy": "monetary_tightening_only", "energy_resilience": 0.18, "supply_diversification": 0.16, "household_protection": 0.22, "infrastructure_capacity": 0.20, "public_buffer_capacity": 0.24, "near_term_disinflation": 0.62},
        {"policy": "targeted_household_energy_support", "energy_resilience": 0.22, "supply_diversification": 0.18, "household_protection": 0.82, "infrastructure_capacity": 0.24, "public_buffer_capacity": 0.48, "near_term_disinflation": 0.34},
        {"policy": "strategic_reserves_and_storage", "energy_resilience": 0.66, "supply_diversification": 0.48, "household_protection": 0.44, "infrastructure_capacity": 0.58, "public_buffer_capacity": 0.76, "near_term_disinflation": 0.42},
        {"policy": "grid_and_public_transit_investment", "energy_resilience": 0.82, "supply_diversification": 0.62, "household_protection": 0.64, "infrastructure_capacity": 0.86, "public_buffer_capacity": 0.70, "near_term_disinflation": 0.28},
        {"policy": "resilient_supply_chain_strategy", "energy_resilience": 0.66, "supply_diversification": 0.86, "household_protection": 0.52, "infrastructure_capacity": 0.78, "public_buffer_capacity": 0.72, "near_term_disinflation": 0.36},
        {"policy": "integrated_resilience_package", "energy_resilience": 0.88, "supply_diversification": 0.84, "household_protection": 0.78, "infrastructure_capacity": 0.88, "public_buffer_capacity": 0.86, "near_term_disinflation": 0.50},
    ])


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "inflation_energy_shocks_supply_constraints.sqlite"
    names = [
        "price_index_scenarios",
        "sector_energy_pass_through_scenarios",
        "household_energy_burden_scenarios",
        "import_price_transmission_scenarios",
        "supply_bottleneck_scenarios",
        "market_power_price_amplification_scenarios",
        "resilience_policy_scenarios",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_price_index_scenarios(),
        build_sector_energy_pass_through_scenarios(),
        build_household_energy_burden_scenarios(),
        build_import_price_transmission_scenarios(),
        build_supply_bottleneck_scenarios(),
        build_market_power_price_amplification_scenarios(),
        build_resilience_policy_scenarios(),
    ]

    filenames = [
        "price_index_scenarios.csv",
        "sector_energy_pass_through_scenarios.csv",
        "household_energy_burden_scenarios.csv",
        "import_price_transmission_scenarios.csv",
        "supply_bottleneck_scenarios.csv",
        "market_power_price_amplification_scenarios.csv",
        "resilience_policy_scenarios.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created inflation, energy shocks, and supply constraints base data.")


if __name__ == "__main__":
    main()
