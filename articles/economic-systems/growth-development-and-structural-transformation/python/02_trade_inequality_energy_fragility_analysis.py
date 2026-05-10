"""
Trade diversification, inequality, energy intensity, ecological pressure, and developmental fragility.
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
    trade = pd.read_csv(PROCESSED_DIR / "trade_export_diversification_scenarios.csv")
    inequality = pd.read_csv(PROCESSED_DIR / "inequality_inclusion_scenarios.csv")
    energy = pd.read_csv(PROCESSED_DIR / "energy_ecology_scenarios.csv")
    debt = pd.read_csv(PROCESSED_DIR / "debt_fragility_scenarios.csv")

    trade["developmental_trade_score"] = (
        0.30 * (1 - trade["export_concentration"])
        + 0.22 * trade["manufacturing_export_share"]
        + 0.24 * trade["technology_depth"]
        + 0.14 * (1 - trade["terms_of_trade_volatility"])
        + 0.10 * trade["foreign_exchange_resilience"]
    )
    trade.to_csv(TABLE_DIR / "trade_diversification_results_python.csv", index=False)

    inequality["inclusion_score"] = (
        0.28 * (1 - inequality["gini_index"])
        + 0.22 * (1 - inequality["informal_labor_share"])
        + 0.20 * inequality["education_access"]
        + 0.15 * inequality["health_access"]
        + 0.15 * inequality["regional_inclusion"]
    )
    inequality.to_csv(TABLE_DIR / "inequality_inclusion_results_python.csv", index=False)

    energy["energy_intensity"] = energy["energy_use"] / energy["output"]
    energy["emissions_intensity"] = energy["emissions"] / energy["output"]
    energy["sustainable_growth_score"] = (
        0.30 * (1 - energy["energy_intensity"] / energy["energy_intensity"].max())
        + 0.30 * (1 - energy["emissions_intensity"] / energy["emissions_intensity"].max())
        + 0.25 * energy["renewable_share"]
        + 0.15 * (1 - energy["resource_stress"])
    )
    energy.to_csv(TABLE_DIR / "energy_ecology_results_python.csv", index=False)

    debt["middle_income_fragility_score"] = (
        0.22 * debt["external_debt_ratio"]
        + 0.20 * debt["fx_debt_share"]
        + 0.16 * debt["short_term_debt_share"]
        + 0.18 * debt["export_concentration"]
        + 0.14 * (1 - debt["reserve_buffer"])
        + 0.10 * (1 - debt["productivity_momentum"])
    )
    debt.to_csv(TABLE_DIR / "debt_fragility_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(trade["scenario"], trade["export_concentration"])
    ax.set_title("Export Concentration")
    ax.set_ylabel("Concentration score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "export_concentration_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(inequality["scenario"], inequality["inclusion_score"])
    ax.set_title("Developmental Inclusion Score")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "inequality_inclusion_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(energy["scenario"], energy["energy_intensity"])
    ax.set_title("Energy Intensity by Growth Path")
    ax.set_ylabel("Energy use / output")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "energy_intensity_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(debt["scenario"], debt["middle_income_fragility_score"])
    ax.set_title("Developmental Fragility Score")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "development_fragility_python.png", dpi=300)
    plt.close(fig)

    print(trade[["scenario", "developmental_trade_score"]])
    print(inequality[["scenario", "inclusion_score"]])
    print(energy[["scenario", "energy_intensity", "sustainable_growth_score"]])
    print(debt[["scenario", "middle_income_fragility_score"]])


if __name__ == "__main__":
    main()
