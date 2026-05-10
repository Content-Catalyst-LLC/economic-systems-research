"""
Household resilience, firm supply chains, finance, labor adaptation, ecological risk, and recovery learning.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
FIGURE_DIR = BASE_DIR / "outputs" / "figures"
TABLE_DIR = BASE_DIR / "outputs" / "tables"

for directory in [FIGURE_DIR, TABLE_DIR]:
    directory.mkdir(parents=True, exist_ok=True)


def main() -> None:
    households = pd.read_csv(PROCESSED_DIR / "household_resilience.csv")
    firms = pd.read_csv(PROCESSED_DIR / "firm_supply_chain.csv")
    finance = pd.read_csv(PROCESSED_DIR / "financial_fragility.csv")
    labor = pd.read_csv(PROCESSED_DIR / "labor_adaptation.csv")
    ecology = pd.read_csv(PROCESSED_DIR / "ecological_energy_risk.csv")
    recovery = pd.read_csv(PROCESSED_DIR / "recovery_learning.csv")

    households["distributional_resilience_score"] = (
        0.22 * households["income_security"]
        + 0.18 * households["savings"]
        + 0.18 * households["care_access"]
        + 0.18 * households["housing_stability"]
        + 0.14 * households["social_protection"]
        + 0.10 * households["mobility"]
    )
    households.to_csv(TABLE_DIR / "household_resilience_results_python.csv", index=False)

    firms["supply_chain_resilience_score"] = (
        0.22 * (1 - firms["supplier_concentration"])
        + 0.20 * firms["inventory_buffer"]
        + 0.16 * firms["credit_access"]
        + 0.16 * firms["demand_diversification"]
        + 0.12 * firms["digital_continuity"]
        + 0.14 * firms["adaptation_capability"]
    )
    firms.to_csv(TABLE_DIR / "firm_supply_chain_results_python.csv", index=False)

    finance["financial_fragility_score"] = (
        0.20 * finance["leverage"]
        + 0.20 * finance["refinancing_risk"]
        + 0.16 * finance["asset_price_dependence"]
        + 0.16 * (1 - finance["liquidity_buffer"])
        + 0.12 * (1 - finance["regulatory_capacity"])
        + 0.16 * finance["contagion_channels"]
    )
    finance.to_csv(TABLE_DIR / "financial_fragility_results_python.csv", index=False)

    labor["labor_adaptive_capacity_score"] = (
        0.18 * labor["skill_transferability"]
        + 0.18 * labor["training_capacity"]
        + 0.18 * labor["income_support"]
        + 0.14 * labor["mobility_support"]
        + 0.18 * labor["place_based_investment"]
        + 0.14 * labor["employer_diversity"]
    )
    labor.to_csv(TABLE_DIR / "labor_adaptation_results_python.csv", index=False)

    ecology["ecological_energy_vulnerability_score"] = (
        0.20 * ecology["energy_volatility"]
        + 0.18 * ecology["water_stress"]
        + 0.22 * ecology["climate_hazard"]
        + 0.14 * ecology["material_dependency"]
        + 0.14 * (1 - ecology["adaptation_investment"])
        + 0.12 * (1 - ecology["ecosystem_integrity"])
    )
    ecology.to_csv(TABLE_DIR / "ecological_energy_risk_results_python.csv", index=False)

    recovery["recovery_learning_score"] = (
        0.16 * recovery["response_speed"]
        + 0.18 * recovery["public_capacity"]
        + 0.16 * recovery["household_stability"]
        + 0.16 * recovery["infrastructure_integrity"]
        + 0.18 * recovery["institutional_learning"]
        + 0.16 * recovery["transformational_adaptation"]
    )
    recovery.to_csv(TABLE_DIR / "recovery_learning_results_python.csv", index=False)

    datasets = [
        (households, "household_group", "distributional_resilience_score", "Household Resilience", "household_resilience_python.png"),
        (firms, "firm_type", "supply_chain_resilience_score", "Firm and Supply Chain Resilience", "supply_chain_resilience_python.png"),
        (finance, "system", "financial_fragility_score", "Financial Fragility", "financial_fragility_python.png"),
        (labor, "region", "labor_adaptive_capacity_score", "Labor Adaptive Capacity", "labor_adaptive_capacity_python.png"),
        (ecology, "system", "ecological_energy_vulnerability_score", "Ecological and Energy Vulnerability", "ecological_energy_vulnerability_python.png"),
        (recovery, "scenario", "recovery_learning_score", "Recovery and Learning", "recovery_learning_python.png"),
    ]

    for df, label, value, title, filename in datasets:
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(df[label], df[value])
        ax.set_title(title)
        ax.set_ylabel(value.replace("_", " "))
        ax.tick_params(axis="x", rotation=35)
        fig.tight_layout()
        fig.savefig(FIGURE_DIR / filename, dpi=300)
        plt.close(fig)

    print(households[["household_group", "distributional_resilience_score"]])
    print(firms[["firm_type", "supply_chain_resilience_score"]])
    print(finance[["system", "financial_fragility_score"]])
    print(labor[["region", "labor_adaptive_capacity_score"]])
    print(ecology[["system", "ecological_energy_vulnerability_score"]])
    print(recovery[["scenario", "recovery_learning_score"]])


if __name__ == "__main__":
    main()
