"""
Build stylized datasets for trade, globalization, and uneven development.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_trade_position_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "high_value_exporter", "exports": 520, "imports": 430, "output": 1600, "strategic_import_dependence": 0.28, "intermediate_import_share": 0.34, "energy_import_share": 0.18},
        {"scenario": "commodity_exporter", "exports": 420, "imports": 390, "output": 1250, "strategic_import_dependence": 0.46, "intermediate_import_share": 0.30, "energy_import_share": 0.22},
        {"scenario": "import_dependent_growth_model", "exports": 330, "imports": 510, "output": 1450, "strategic_import_dependence": 0.62, "intermediate_import_share": 0.48, "energy_import_share": 0.40},
        {"scenario": "assembly_export_platform", "exports": 610, "imports": 560, "output": 1500, "strategic_import_dependence": 0.58, "intermediate_import_share": 0.72, "energy_import_share": 0.24},
        {"scenario": "balanced_strategic_integration", "exports": 470, "imports": 455, "output": 1550, "strategic_import_dependence": 0.34, "intermediate_import_share": 0.38, "energy_import_share": 0.20},
        {"scenario": "fragmentation_stress_path", "exports": 360, "imports": 500, "output": 1420, "strategic_import_dependence": 0.68, "intermediate_import_share": 0.54, "energy_import_share": 0.46},
    ])


def build_export_basket_scenarios() -> pd.DataFrame:
    rows = []
    baskets = {
        "commodity_exporter": {"energy": 190, "minerals": 110, "agriculture": 70, "manufacturing": 35, "knowledge_services": 15},
        "assembly_export_platform": {"energy": 20, "minerals": 20, "agriculture": 30, "manufacturing": 440, "knowledge_services": 100},
        "diversified_upgrader": {"energy": 45, "minerals": 35, "agriculture": 55, "manufacturing": 250, "knowledge_services": 190},
        "high_value_exporter": {"energy": 25, "minerals": 20, "agriculture": 30, "manufacturing": 220, "knowledge_services": 225},
        "low_value_trade_dependence": {"energy": 55, "minerals": 70, "agriculture": 80, "manufacturing": 115, "knowledge_services": 25},
    }
    for scenario, basket in baskets.items():
        for export_category, export_value in basket.items():
            rows.append({"scenario": scenario, "export_category": export_category, "export_value": export_value})
    return pd.DataFrame(rows)


def build_value_chain_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "design_ip_command_position", "gross_exports": 520, "domestic_value_added": 390, "lead_firm_control": 0.88, "technology_control": 0.86, "branding_control": 0.82, "assembly_dependence": 0.18, "upgrading_potential": 0.78},
        {"scenario": "contract_manufacturing_position", "gross_exports": 610, "domestic_value_added": 190, "lead_firm_control": 0.26, "technology_control": 0.32, "branding_control": 0.18, "assembly_dependence": 0.82, "upgrading_potential": 0.46},
        {"scenario": "resource_extraction_position", "gross_exports": 420, "domestic_value_added": 250, "lead_firm_control": 0.34, "technology_control": 0.28, "branding_control": 0.12, "assembly_dependence": 0.10, "upgrading_potential": 0.30},
        {"scenario": "supplier_upgrading_path", "gross_exports": 470, "domestic_value_added": 285, "lead_firm_control": 0.52, "technology_control": 0.58, "branding_control": 0.36, "assembly_dependence": 0.44, "upgrading_potential": 0.68},
        {"scenario": "digital_platform_dependency", "gross_exports": 360, "domestic_value_added": 150, "lead_firm_control": 0.22, "technology_control": 0.18, "branding_control": 0.24, "assembly_dependence": 0.20, "upgrading_potential": 0.34},
    ])


def build_terms_of_trade_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "commodity_price_boom", "export_price_index": 125, "import_price_index": 105, "commodity_share": 0.72, "imported_food_energy_share": 0.30, "stabilization_fund_strength": 0.62},
        {"scenario": "commodity_price_collapse", "export_price_index": 82, "import_price_index": 108, "commodity_share": 0.74, "imported_food_energy_share": 0.34, "stabilization_fund_strength": 0.34},
        {"scenario": "energy_import_shock", "export_price_index": 102, "import_price_index": 130, "commodity_share": 0.24, "imported_food_energy_share": 0.58, "stabilization_fund_strength": 0.48},
        {"scenario": "diversified_export_stability", "export_price_index": 112, "import_price_index": 108, "commodity_share": 0.26, "imported_food_energy_share": 0.24, "stabilization_fund_strength": 0.72},
        {"scenario": "manufacturing_margin_squeeze", "export_price_index": 104, "import_price_index": 118, "commodity_share": 0.18, "imported_food_energy_share": 0.36, "stabilization_fund_strength": 0.44},
    ])


def build_finance_currency_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "reserve_currency_flexibility", "foreign_currency_debt": 0.12, "capital_flow_volatility": 0.22, "reserve_buffer": 0.82, "current_account_pressure": 0.20, "external_financing_need": 0.24, "policy_space": 0.78},
        {"scenario": "foreign_currency_debt_dependence", "foreign_currency_debt": 0.62, "capital_flow_volatility": 0.58, "reserve_buffer": 0.34, "current_account_pressure": 0.60, "external_financing_need": 0.66, "policy_space": 0.28},
        {"scenario": "volatile_portfolio_inflow_model", "foreign_currency_debt": 0.38, "capital_flow_volatility": 0.72, "reserve_buffer": 0.42, "current_account_pressure": 0.48, "external_financing_need": 0.52, "policy_space": 0.36},
        {"scenario": "managed_openness_with_buffers", "foreign_currency_debt": 0.24, "capital_flow_volatility": 0.32, "reserve_buffer": 0.70, "current_account_pressure": 0.30, "external_financing_need": 0.32, "policy_space": 0.68},
        {"scenario": "energy_import_currency_stress", "foreign_currency_debt": 0.44, "capital_flow_volatility": 0.50, "reserve_buffer": 0.38, "current_account_pressure": 0.66, "external_financing_need": 0.58, "policy_space": 0.30},
    ])


def build_regional_inequality_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"region": "global_city_finance_tech", "export_linkage": 0.82, "productivity": 0.88, "infrastructure_depth": 0.86, "capital_access": 0.90, "market_access": 0.86, "institutional_capacity": 0.82},
        {"region": "port_logistics_corridor", "export_linkage": 0.76, "productivity": 0.66, "infrastructure_depth": 0.78, "capital_access": 0.62, "market_access": 0.84, "institutional_capacity": 0.64},
        {"region": "deindustrialized_interior", "export_linkage": 0.28, "productivity": 0.40, "infrastructure_depth": 0.48, "capital_access": 0.34, "market_access": 0.36, "institutional_capacity": 0.42},
        {"region": "resource_extraction_zone", "export_linkage": 0.70, "productivity": 0.52, "infrastructure_depth": 0.44, "capital_access": 0.50, "market_access": 0.42, "institutional_capacity": 0.34},
        {"region": "secondary_city_upgrading_cluster", "export_linkage": 0.54, "productivity": 0.60, "infrastructure_depth": 0.64, "capital_access": 0.56, "market_access": 0.58, "institutional_capacity": 0.60},
    ])


def build_labor_exposure_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"sector": "advanced_services", "import_competition": 0.18, "offshoring_risk": 0.24, "wage_bargaining_strength": 0.70, "skills_transferability": 0.76, "employment_security": 0.68, "adjustment_support": 0.64},
        {"sector": "traditional_manufacturing", "import_competition": 0.74, "offshoring_risk": 0.66, "wage_bargaining_strength": 0.42, "skills_transferability": 0.46, "employment_security": 0.38, "adjustment_support": 0.32},
        {"sector": "commodity_extraction", "import_competition": 0.28, "offshoring_risk": 0.20, "wage_bargaining_strength": 0.54, "skills_transferability": 0.34, "employment_security": 0.42, "adjustment_support": 0.30},
        {"sector": "logistics_and_ports", "import_competition": 0.36, "offshoring_risk": 0.22, "wage_bargaining_strength": 0.50, "skills_transferability": 0.58, "employment_security": 0.52, "adjustment_support": 0.48},
        {"sector": "low_value_assembly", "import_competition": 0.62, "offshoring_risk": 0.78, "wage_bargaining_strength": 0.26, "skills_transferability": 0.32, "employment_security": 0.24, "adjustment_support": 0.26},
    ])


def build_ecological_trade_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "domestic_clean_consumption_imported_burden", "embodied_emissions_imports": 0.72, "domestic_emissions_intensity": 0.34, "resource_extraction_burden": 0.62, "waste_displacement": 0.58, "supply_chain_traceability": 0.30, "ecological_regulation_alignment": 0.28},
        {"scenario": "high_carbon_export_model", "embodied_emissions_imports": 0.30, "domestic_emissions_intensity": 0.76, "resource_extraction_burden": 0.70, "waste_displacement": 0.34, "supply_chain_traceability": 0.34, "ecological_regulation_alignment": 0.32},
        {"scenario": "traceable_low_carbon_trade", "embodied_emissions_imports": 0.32, "domestic_emissions_intensity": 0.28, "resource_extraction_burden": 0.30, "waste_displacement": 0.22, "supply_chain_traceability": 0.78, "ecological_regulation_alignment": 0.74},
        {"scenario": "extractive_supply_chain_dependency", "embodied_emissions_imports": 0.50, "domestic_emissions_intensity": 0.52, "resource_extraction_burden": 0.82, "waste_displacement": 0.42, "supply_chain_traceability": 0.26, "ecological_regulation_alignment": 0.22},
        {"scenario": "circular_regional_trade_path", "embodied_emissions_imports": 0.28, "domestic_emissions_intensity": 0.30, "resource_extraction_burden": 0.28, "waste_displacement": 0.18, "supply_chain_traceability": 0.72, "ecological_regulation_alignment": 0.80},
    ])


def build_strategic_resilience_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "pure_efficiency_fragility", "supplier_diversification": 0.24, "domestic_capability": 0.30, "strategic_stock_buffer": 0.20, "regional_redundancy": 0.18, "import_substitution_capacity": 0.26, "cooperative_trade_access": 0.60},
        {"scenario": "strategic_autonomy_with_cooperation", "supplier_diversification": 0.70, "domestic_capability": 0.68, "strategic_stock_buffer": 0.62, "regional_redundancy": 0.66, "import_substitution_capacity": 0.58, "cooperative_trade_access": 0.72},
        {"scenario": "isolationist_resilience_failure", "supplier_diversification": 0.32, "domestic_capability": 0.42, "strategic_stock_buffer": 0.48, "regional_redundancy": 0.28, "import_substitution_capacity": 0.46, "cooperative_trade_access": 0.18},
        {"scenario": "green_resilient_integration", "supplier_diversification": 0.76, "domestic_capability": 0.72, "strategic_stock_buffer": 0.58, "regional_redundancy": 0.70, "import_substitution_capacity": 0.62, "cooperative_trade_access": 0.78},
        {"scenario": "single_supplier_dependency", "supplier_diversification": 0.12, "domestic_capability": 0.24, "strategic_stock_buffer": 0.22, "regional_redundancy": 0.16, "import_substitution_capacity": 0.18, "cooperative_trade_access": 0.44},
    ])


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "trade_globalization_uneven_development.sqlite"
    names = [
        "trade_position_scenarios",
        "export_basket_scenarios",
        "value_chain_scenarios",
        "terms_of_trade_scenarios",
        "finance_currency_scenarios",
        "regional_inequality_scenarios",
        "labor_exposure_scenarios",
        "ecological_trade_scenarios",
        "strategic_resilience_scenarios",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_trade_position_scenarios(),
        build_export_basket_scenarios(),
        build_value_chain_scenarios(),
        build_terms_of_trade_scenarios(),
        build_finance_currency_scenarios(),
        build_regional_inequality_scenarios(),
        build_labor_exposure_scenarios(),
        build_ecological_trade_scenarios(),
        build_strategic_resilience_scenarios(),
    ]

    filenames = [
        "trade_position_scenarios.csv",
        "export_basket_scenarios.csv",
        "value_chain_scenarios.csv",
        "terms_of_trade_scenarios.csv",
        "finance_currency_scenarios.csv",
        "regional_inequality_scenarios.csv",
        "labor_exposure_scenarios.csv",
        "ecological_trade_scenarios.csv",
        "strategic_resilience_scenarios.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created trade, globalization, and uneven development base data.")


if __name__ == "__main__":
    main()
