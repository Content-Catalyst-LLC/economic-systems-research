"""
Social spending, disposable income, program coverage, replacement rates, and welfare regimes.
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
    household = pd.read_csv(PROCESSED_DIR / "household_tax_transfer.csv")
    spending = pd.read_csv(PROCESSED_DIR / "social_spending_scenarios.csv")
    coverage = pd.read_csv(PROCESSED_DIR / "program_coverage.csv")
    regimes = pd.read_csv(PROCESSED_DIR / "welfare_regime_scenarios.csv")

    household["disposable_income"] = household["market_income"] - household["taxes"] + household["transfers"]
    household["service_adjusted_income"] = household["disposable_income"] + household["service_value"]
    household["post_cost_security_income"] = (
        household["service_adjusted_income"] - household["housing_cost"] - household["care_cost"]
    )
    household["redistributive_gain"] = household["disposable_income"] - household["market_income"]
    household.to_csv(TABLE_DIR / "household_tax_transfer_results_python.csv", index=False)

    spending["social_spending_ratio"] = spending["social_spending"] / spending["output"]
    spending["core_protection_spending"] = (
        spending["healthcare_spending"] + spending["pensions"] + spending["unemployment"]
        + spending["family_policy"] + spending["housing_support"] + spending["disability_support"]
    )
    spending["protection_strength_score"] = (
        0.24 * spending["social_spending_ratio"] / spending["social_spending_ratio"].max()
        + 0.18 * spending["healthcare_spending"] / spending["healthcare_spending"].max()
        + 0.18 * spending["pensions"] / spending["pensions"].max()
        + 0.14 * spending["unemployment"] / spending["unemployment"].max()
        + 0.14 * spending["family_policy"] / spending["family_policy"].max()
        + 0.12 * spending["administration_quality"]
    )
    spending.to_csv(TABLE_DIR / "social_spending_results_python.csv", index=False)

    coverage["coverage_rate"] = coverage["covered_population"] / coverage["target_population"]
    coverage["replacement_rate"] = coverage["benefit"] / coverage["previous_earnings"]
    coverage["effective_protection_score"] = (
        0.28 * coverage["coverage_rate"]
        + 0.24 * coverage["replacement_rate"]
        + 0.18 * coverage["take_up_rate"]
        + 0.16 * (1 - coverage["administrative_burden"])
        + 0.14 * (1 - coverage["stigma_cost"])
    )
    coverage.to_csv(TABLE_DIR / "program_coverage_results_python.csv", index=False)

    regimes["regime_strength_score"] = (
        0.18 * regimes["universalism"]
        + 0.12 * regimes["targeting_precision"]
        + 0.18 * regimes["benefit_adequacy"]
        + 0.18 * regimes["service_quality"]
        + 0.14 * regimes["labor_market_security"]
        + 0.10 * regimes["dignity_score"]
        + 0.10 * regimes["political_durability"]
    )
    regimes.to_csv(TABLE_DIR / "welfare_regime_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(spending["scenario"], spending["social_spending_ratio"])
    ax.set_title("Social Spending Ratio")
    ax.set_ylabel("Social spending / output")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "social_spending_ratio_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(coverage["program"], coverage["effective_protection_score"])
    ax.set_title("Effective Protection by Program")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "effective_protection_score_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(regimes["regime"], regimes["regime_strength_score"])
    ax.set_title("Welfare Regime Strength")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "welfare_regime_strength_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(household["household"], household["market_income"], marker="o", label="Market income")
    ax.plot(household["household"], household["disposable_income"], marker="o", label="Disposable income")
    ax.plot(household["household"], household["service_adjusted_income"], marker="o", label="Service-adjusted income")
    ax.set_title("Market, Disposable, and Service-Adjusted Income")
    ax.set_ylabel("Income units")
    ax.tick_params(axis="x", rotation=35)
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "tax_transfer_income_python.png", dpi=300)
    plt.close(fig)

    print(household[["household", "market_income", "disposable_income", "service_adjusted_income", "post_cost_security_income"]])
    print(spending[["scenario", "social_spending_ratio", "protection_strength_score"]])
    print(coverage[["program", "coverage_rate", "replacement_rate", "effective_protection_score"]])
    print(regimes[["regime", "regime_strength_score"]])


if __name__ == "__main__":
    main()
