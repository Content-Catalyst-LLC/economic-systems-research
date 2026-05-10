"""
Finance, currency vulnerability, regional inequality, labor exposure, ecological burden, and strategic resilience.
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
    finance = pd.read_csv(PROCESSED_DIR / "finance_currency_scenarios.csv")
    regions = pd.read_csv(PROCESSED_DIR / "regional_inequality_scenarios.csv")
    labor = pd.read_csv(PROCESSED_DIR / "labor_exposure_scenarios.csv")
    ecology = pd.read_csv(PROCESSED_DIR / "ecological_trade_scenarios.csv")
    resilience = pd.read_csv(PROCESSED_DIR / "strategic_resilience_scenarios.csv")

    finance["external_vulnerability_score"] = (
        0.22 * finance["foreign_currency_debt"]
        + 0.20 * finance["capital_flow_volatility"]
        + 0.18 * (1 - finance["reserve_buffer"])
        + 0.16 * finance["current_account_pressure"]
        + 0.14 * finance["external_financing_need"]
        + 0.10 * (1 - finance["policy_space"])
    )
    finance.to_csv(TABLE_DIR / "finance_currency_results_python.csv", index=False)

    regions["globalization_advantage_score"] = (
        0.20 * regions["export_linkage"]
        + 0.20 * regions["productivity"]
        + 0.18 * regions["infrastructure_depth"]
        + 0.16 * regions["capital_access"]
        + 0.14 * regions["market_access"]
        + 0.12 * regions["institutional_capacity"]
    )
    regions.to_csv(TABLE_DIR / "regional_inequality_results_python.csv", index=False)

    labor["labor_exposure_risk"] = (
        0.24 * labor["import_competition"]
        + 0.22 * labor["offshoring_risk"]
        + 0.18 * (1 - labor["wage_bargaining_strength"])
        + 0.14 * (1 - labor["skills_transferability"])
        + 0.12 * (1 - labor["employment_security"])
        + 0.10 * (1 - labor["adjustment_support"])
    )
    labor.to_csv(TABLE_DIR / "labor_exposure_results_python.csv", index=False)

    ecology["ecological_burden_score"] = (
        0.22 * ecology["embodied_emissions_imports"]
        + 0.20 * ecology["domestic_emissions_intensity"]
        + 0.20 * ecology["resource_extraction_burden"]
        + 0.14 * ecology["waste_displacement"]
        + 0.12 * (1 - ecology["supply_chain_traceability"])
        + 0.12 * (1 - ecology["ecological_regulation_alignment"])
    )
    ecology.to_csv(TABLE_DIR / "ecological_trade_results_python.csv", index=False)

    resilience["sustainable_trade_resilience_score"] = (
        0.20 * resilience["supplier_diversification"]
        + 0.22 * resilience["domestic_capability"]
        + 0.16 * resilience["strategic_stock_buffer"]
        + 0.16 * resilience["regional_redundancy"]
        + 0.12 * resilience["import_substitution_capacity"]
        + 0.14 * resilience["cooperative_trade_access"]
    )
    resilience.to_csv(TABLE_DIR / "strategic_resilience_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(finance["scenario"], finance["external_vulnerability_score"])
    ax.set_title("External Financial Vulnerability")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "external_vulnerability_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(regions["region"], regions["globalization_advantage_score"])
    ax.set_title("Regional Advantage Under Globalization")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "regional_inequality_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(labor["sector"], labor["labor_exposure_risk"])
    ax.set_title("Labor Exposure to Globalization Stress")
    ax.set_ylabel("Composite risk")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "labor_exposure_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(ecology["scenario"], ecology["ecological_burden_score"])
    ax.set_title("Ecological Burden in Trade Structure")
    ax.set_ylabel("Composite burden score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "ecological_trade_burden_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(resilience["scenario"], resilience["sustainable_trade_resilience_score"])
    ax.set_title("Sustainable Trade Resilience")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "sustainable_trade_resilience_python.png", dpi=300)
    plt.close(fig)

    print(finance[["scenario", "external_vulnerability_score"]])
    print(regions[["region", "globalization_advantage_score"]])
    print(labor[["sector", "labor_exposure_risk"]])
    print(ecology[["scenario", "ecological_burden_score"]])
    print(resilience[["scenario", "sustainable_trade_resilience_score"]])


if __name__ == "__main__":
    main()
