"""
Conditionality, austerity, commodity debt vulnerability, capital-flow sudden stops, restructuring, and sustainable finance.
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
    conditionality = pd.read_csv(PROCESSED_DIR / "conditionality_scenarios.csv")
    austerity = pd.read_csv(PROCESSED_DIR / "austerity_adjustment_scenarios.csv")
    commodity = pd.read_csv(PROCESSED_DIR / "commodity_debt_scenarios.csv")
    capital = pd.read_csv(PROCESSED_DIR / "capital_flow_scenarios.csv")
    restructuring = pd.read_csv(PROCESSED_DIR / "restructuring_scenarios.csv")
    sustainable = pd.read_csv(PROCESSED_DIR / "sustainable_finance_scenarios.csv")

    conditionality["policy_space_pressure"] = (
        0.22 * conditionality["fiscal_compression"]
        + 0.18 * (1 - conditionality["social_spending_protection"])
        + 0.18 * (1 - conditionality["public_investment_protection"])
        + 0.16 * conditionality["privatization_pressure"]
        + 0.14 * (1 - conditionality["policy_space"])
        + 0.12 * (1 - conditionality["developmental_alignment"])
    )
    conditionality.to_csv(TABLE_DIR / "conditionality_results_python.csv", index=False)

    austerity["public_capacity_erosion_score"] = (
        0.18 * austerity["austerity_intensity"]
        + 0.16 * austerity["health_spending_cut"]
        + 0.16 * austerity["education_spending_cut"]
        + 0.18 * austerity["infrastructure_cut"]
        + 0.12 * austerity["wage_compression"]
        + 0.10 * austerity["growth_damage"]
        + 0.10 * austerity["poverty_pressure"]
    )
    austerity.to_csv(TABLE_DIR / "austerity_adjustment_results_python.csv", index=False)

    commodity["commodity_debt_service_ratio"] = commodity["external_debt_service"] / commodity["export_earnings"]
    commodity["commodity_debt_vulnerability_score"] = (
        0.22 * commodity["commodity_export_share"]
        + 0.22 * commodity["commodity_debt_service_ratio"] / commodity["commodity_debt_service_ratio"].max()
        + 0.18 * (1 - commodity["commodity_price_index"] / commodity["commodity_price_index"].max())
        + 0.18 * (1 - commodity["stabilization_fund"])
        + 0.20 * (1 - commodity["diversification_effort"])
    )
    commodity.to_csv(TABLE_DIR / "commodity_debt_results_python.csv", index=False)

    capital["sudden_stop_risk_score"] = (
        0.18 * capital["portfolio_share"]
        + 0.14 * (1 - capital["fdi_share"])
        + 0.20 * capital["short_term_debt_share"]
        + 0.18 * capital["capital_flow_reversal"]
        + 0.14 * capital["reserve_loss"]
        + 0.16 * capital["currency_depreciation"]
    )
    capital.to_csv(TABLE_DIR / "capital_flow_results_python.csv", index=False)

    restructuring["post_restructuring_debt"] = restructuring["initial_debt"] * (1 - restructuring["restructuring_haircut"])
    restructuring["resolution_quality_score"] = (
        0.22 * restructuring["restructuring_haircut"]
        + 0.18 * restructuring["maturity_extension"]
        + 0.18 * restructuring["interest_relief"]
        + 0.18 * restructuring["social_spending_floor"]
        + 0.16 * restructuring["growth_recovery"]
        + 0.08 * restructuring["creditor_acceptance"]
    )
    restructuring.to_csv(TABLE_DIR / "restructuring_results_python.csv", index=False)

    sustainable["sustainable_finance_score"] = (
        0.22 * sustainable["productive_investment"]
        + 0.18 * sustainable["domestic_capability"]
        + 0.18 * sustainable["export_resilience"]
        + 0.14 * sustainable["social_protection"]
        + 0.14 * sustainable["ecological_resilience"]
        + 0.14 * sustainable["debt_manageability"]
    )
    sustainable.to_csv(TABLE_DIR / "sustainable_finance_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(conditionality["program"], conditionality["policy_space_pressure"])
    ax.set_title("Policy-Space Pressure from Conditionality")
    ax.set_ylabel("Composite pressure")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "conditionality_policy_space_pressure_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(austerity["scenario"], austerity["public_capacity_erosion_score"])
    ax.set_title("Public Capacity Erosion Under Adjustment")
    ax.set_ylabel("Composite erosion")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "austerity_public_capacity_erosion_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(commodity["scenario"], commodity["commodity_debt_vulnerability_score"])
    ax.set_title("Commodity-Linked Debt Vulnerability")
    ax.set_ylabel("Composite vulnerability")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "commodity_debt_vulnerability_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(capital["scenario"], capital["sudden_stop_risk_score"])
    ax.set_title("Capital-Flow Sudden Stop Risk")
    ax.set_ylabel("Composite risk")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "sudden_stop_risk_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(restructuring["scenario"], restructuring["resolution_quality_score"])
    ax.set_title("Debt Restructuring Resolution Quality")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "restructuring_resolution_quality_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(sustainable["scenario"], sustainable["sustainable_finance_score"])
    ax.set_title("Sustainable Development Finance")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "sustainable_finance_score_python.png", dpi=300)
    plt.close(fig)

    print(conditionality[["program", "policy_space_pressure"]])
    print(austerity[["scenario", "public_capacity_erosion_score"]])
    print(commodity[["scenario", "commodity_debt_vulnerability_score"]])
    print(capital[["scenario", "sudden_stop_risk_score"]])
    print(restructuring[["scenario", "post_restructuring_debt", "resolution_quality_score"]])
    print(sustainable[["scenario", "sustainable_finance_score"]])


if __name__ == "__main__":
    main()
