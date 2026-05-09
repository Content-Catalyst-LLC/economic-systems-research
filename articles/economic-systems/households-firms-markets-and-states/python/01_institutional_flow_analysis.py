"""
Analyze institutional income flows among households, firms, and states.
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
    flows = pd.read_csv(PROCESSED_DIR / "institutional_flow_scenarios.csv")

    flows["household_saving"] = (
        flows["household_wages"]
        + flows["household_transfers"]
        + flows["asset_income"]
        - flows["taxes_paid"]
        - flows["debt_service"]
        - flows["household_consumption"]
    )

    flows["firm_profit"] = (
        flows["firm_revenue"]
        - flows["labor_cost"]
        - flows["capital_cost"]
        - flows["input_cost"]
    )

    flows["public_borrowing"] = (
        flows["public_spending"]
        + flows["public_transfers"]
        + flows["public_debt_interest"]
        - flows["tax_revenue"]
    )

    flows["household_stability"] = (flows["household_saving"] >= 0).astype(int)
    flows["productive_capacity"] = (flows["firm_profit"] > 0).astype(int)
    flows["institutional_capacity"] = (flows["public_borrowing"] <= 350).astype(int)

    flows["reproduction_score"] = (
        flows["household_stability"]
        + flows["productive_capacity"]
        + flows["institutional_capacity"]
    )

    flows["wage_share_of_firm_revenue"] = flows["labor_cost"] / flows["firm_revenue"]
    flows["tax_share_of_revenue"] = flows["tax_revenue"] / flows["firm_revenue"]
    flows["transfer_support_ratio"] = flows["household_transfers"] / flows["household_wages"]

    flows.to_csv(TABLE_DIR / "institutional_flow_results_python.csv", index=False)

    plot_data = flows[["scenario", "household_saving", "firm_profit", "public_borrowing"]].set_index("scenario")
    plot_data.plot(kind="bar", figsize=(10, 5))
    plt.title("Institutional Flow Balances by Scenario")
    plt.ylabel("Flow units")
    plt.xlabel("Scenario")
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()
    plt.savefig(FIGURE_DIR / "institutional_flow_balances_python.png", dpi=300)
    plt.close()

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(flows["scenario"], flows["reproduction_score"])
    ax.set_title("System Reproduction Score")
    ax.set_ylabel("Score out of 3")
    ax.set_xlabel("Scenario")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "reproduction_score_python.png", dpi=300)
    plt.close()

    print(flows[["scenario", "household_saving", "firm_profit", "public_borrowing", "reproduction_score"]])


if __name__ == "__main__":
    main()
