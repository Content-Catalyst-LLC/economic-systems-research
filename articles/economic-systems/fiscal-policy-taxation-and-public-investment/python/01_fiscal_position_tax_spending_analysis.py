"""
Fiscal position, tax distribution, spending composition, and debt dynamics.
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
    fiscal = pd.read_csv(PROCESSED_DIR / "fiscal_position_scenarios.csv")
    taxes = pd.read_csv(PROCESSED_DIR / "tax_distribution_scenarios.csv")
    spending = pd.read_csv(PROCESSED_DIR / "spending_composition_scenarios.csv")

    fiscal["budget_balance"] = fiscal["tax_revenue"] - fiscal["public_spending"]
    fiscal["primary_balance"] = fiscal["tax_revenue"] - fiscal["primary_spending"]
    fiscal["tax_ratio"] = fiscal["tax_revenue"] / fiscal["output"]
    fiscal["spending_ratio"] = fiscal["public_spending"] / fiscal["output"]
    fiscal["debt_to_output"] = fiscal["debt_stock"] / fiscal["output"]
    fiscal["interest_cost"] = fiscal["interest_rate"] * fiscal["debt_stock"]
    fiscal["next_period_debt"] = fiscal["debt_stock"] + (fiscal["public_spending"] - fiscal["tax_revenue"]) + fiscal["interest_cost"]
    fiscal["next_period_debt_to_output"] = fiscal["next_period_debt"] / fiscal["output"]
    fiscal.to_csv(TABLE_DIR / "fiscal_position_results_python.csv", index=False)

    taxes["effective_tax_rate"] = taxes["tax_paid"] / taxes["income"]
    taxes["consumption_tax_rate"] = taxes["consumption_tax_paid"] / taxes["income"]
    taxes["total_tax_with_consumption_and_wealth"] = taxes["tax_paid"] + taxes["consumption_tax_paid"] + taxes["wealth_tax_paid"]
    taxes["broad_effective_tax_rate"] = taxes["total_tax_with_consumption_and_wealth"] / taxes["income"]
    taxes["net_transfer_position"] = taxes["transfer_received"] - taxes["total_tax_with_consumption_and_wealth"]
    taxes.to_csv(TABLE_DIR / "tax_distribution_results_python.csv", index=False)

    spending["public_investment_share"] = spending["public_investment_component"] / spending["spending_amount"]
    spending["current_service_share"] = spending["current_service_component"] / spending["spending_amount"]
    spending["weighted_resilience_contribution"] = spending["spending_amount"] * spending["resilience_score"]
    spending.to_csv(TABLE_DIR / "spending_composition_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(fiscal["scenario"], fiscal["next_period_debt_to_output"])
    ax.set_title("Next-Period Public Debt to Output")
    ax.set_ylabel("Debt / output")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "debt_dynamics_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(taxes["income_group"], taxes["effective_tax_rate"], marker="o", label="Direct ETR")
    ax.plot(taxes["income_group"], taxes["broad_effective_tax_rate"], marker="o", label="Broad ETR")
    ax.set_title("Effective Tax Rates by Income Group")
    ax.set_ylabel("Tax paid / income")
    ax.tick_params(axis="x", rotation=35)
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "tax_progressivity_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    spending.set_index("spending_category")[["public_investment_component", "current_service_component"]].plot(kind="bar", stacked=True, ax=ax)
    ax.set_title("Public Spending Composition")
    ax.set_ylabel("Spending amount")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "spending_composition_python.png", dpi=300)
    plt.close(fig)

    print(fiscal[["scenario", "budget_balance", "tax_ratio", "next_period_debt_to_output"]])
    print(taxes[["income_group", "effective_tax_rate", "broad_effective_tax_rate", "net_transfer_position"]])
    print(spending[["spending_category", "public_investment_share", "resilience_score"]])


if __name__ == "__main__":
    main()
