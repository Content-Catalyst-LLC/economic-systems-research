"""
Housing, globalization, crisis response, and sustainable capitalism.
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
    housing = pd.read_csv(PROCESSED_DIR / "housing_household_vulnerability.csv")
    globalization = pd.read_csv(PROCESSED_DIR / "globalization_hybrids.csv")
    crisis = pd.read_csv(PROCESSED_DIR / "crisis_sustainability.csv")

    housing["housing_vulnerability_score"] = (
        0.20 * housing["rent_burden"]
        + 0.18 * housing["mortgage_debt"]
        + 0.18 * housing["asset_price_volatility"]
        + 0.14 * (1 - housing["tenant_protection"])
        + 0.12 * (1 - housing["public_housing_capacity"])
        + 0.10 * (1 - housing["household_resilience"])
        + 0.08 * housing["wealth_concentration_pressure"]
    )
    housing.to_csv(TABLE_DIR / "housing_vulnerability_results_python.csv", index=False)

    globalization["dependent_hybridization_score"] = (
        0.18 * globalization["value_chain_dependence"]
        + 0.18 * (1 - globalization["domestic_supplier_depth"])
        + 0.18 * globalization["foreign_currency_exposure"]
        + 0.16 * (1 - globalization["technology_sovereignty"])
        + 0.12 * (1 - globalization["labor_standards"])
        + 0.08 * (1 - globalization["industrial_policy_capacity"])
        + 0.10 * globalization["external_vulnerability"]
    )
    globalization["developmental_upgrading_score"] = (
        0.20 * globalization["domestic_supplier_depth"]
        + 0.18 * globalization["technology_sovereignty"]
        + 0.18 * globalization["labor_standards"]
        + 0.20 * globalization["industrial_policy_capacity"]
        + 0.12 * (1 - globalization["foreign_currency_exposure"])
        + 0.12 * (1 - globalization["external_vulnerability"])
    )
    globalization.to_csv(TABLE_DIR / "globalization_hybrid_results_python.csv", index=False)

    crisis["crisis_response_score"] = (
        0.18 * crisis["automatic_stabilizers"]
        + 0.16 * crisis["public_investment_capacity"]
        + 0.18 * crisis["household_buffer"]
        + 0.14 * crisis["financial_regulation"]
        + 0.14 * crisis["industrial_adaptation"]
        + 0.10 * crisis["ecological_constraint"]
        + 0.10 * crisis["democratic_legitimacy"]
    )
    crisis["sustainable_capitalism_score"] = (
        0.18 * crisis["public_investment_capacity"]
        + 0.16 * crisis["household_buffer"]
        + 0.14 * crisis["financial_regulation"]
        + 0.18 * crisis["industrial_adaptation"]
        + 0.18 * crisis["ecological_constraint"]
        + 0.16 * crisis["democratic_legitimacy"]
    )
    crisis.to_csv(TABLE_DIR / "crisis_sustainability_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(housing["housing_regime"], housing["housing_vulnerability_score"])
    ax.set_title("Housing and Household Vulnerability")
    ax.set_ylabel("Composite vulnerability")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "housing_vulnerability_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(globalization["scenario"], globalization["dependent_hybridization_score"])
    ax.set_title("Dependent Hybridization in Global Capitalism")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "dependent_hybridization_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(crisis["scenario"], crisis["crisis_response_score"])
    ax.set_title("Crisis Response Capacity")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "crisis_response_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(crisis["scenario"], crisis["sustainable_capitalism_score"])
    ax.set_title("Sustainable Capitalism Score")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "sustainable_capitalism_python.png", dpi=300)
    plt.close(fig)

    print(housing[["housing_regime", "housing_vulnerability_score"]])
    print(globalization[["scenario", "dependent_hybridization_score", "developmental_upgrading_score"]])
    print(crisis[["scenario", "crisis_response_score", "sustainable_capitalism_score"]])


if __name__ == "__main__":
    main()
