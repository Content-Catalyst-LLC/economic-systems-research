"""
Market access, risk distribution, and reproduction dynamics.
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


def simulate_reproduction(row: pd.Series, periods: int = 20) -> pd.DataFrame:
    household_capacity = 100.0
    productive_capacity = 100.0
    institutional_capacity = 100.0
    records = []

    for period in range(periods):
        records.append({
            "scenario": row["scenario"],
            "period": period,
            "household_capacity": household_capacity,
            "productive_capacity": productive_capacity,
            "institutional_capacity": institutional_capacity,
            "system_capacity": (household_capacity + productive_capacity + institutional_capacity) / 3,
        })

        household_capacity = household_capacity + 0.05 * row["household_saving"] - 0.03 * row["debt_service"]
        productive_capacity = productive_capacity + 0.04 * row["firm_profit"] + 0.01 * row["public_spending"] - 0.02 * row["input_cost"]
        institutional_capacity = institutional_capacity + 0.02 * row["tax_revenue"] - 0.015 * row["public_borrowing"] + 0.01 * row["public_spending"]

    return pd.DataFrame(records)


def main() -> None:
    flows = pd.read_csv(TABLE_DIR / "institutional_flow_results_python.csv")
    access = pd.read_csv(PROCESSED_DIR / "market_access_scenarios.csv")
    risk = pd.read_csv(PROCESSED_DIR / "risk_distribution_scenarios.csv")

    access["effective_access"] = (
        0.34 * access["income_command"]
        + 0.30 * access["institutional_access"]
        + 0.22 * (1 - access["price_burden"])
        + 0.14 * access["need_index"]
    )
    access["access_gap"] = access["need_index"] - access["effective_access"]
    access["deprivation_flag"] = (access["access_gap"] > 0.25).astype(int)
    access["weighted_access_gap"] = access["access_gap"] * access["population_weight"]

    access_summary = pd.DataFrame([{
        "weighted_access_gap": access["weighted_access_gap"].sum(),
        "population_share_deprived": (access["deprivation_flag"] * access["population_weight"]).sum(),
        "weighted_effective_access": (access["effective_access"] * access["population_weight"]).sum() / access["population_weight"].sum(),
        "weighted_need_index": (access["need_index"] * access["population_weight"]).sum() / access["population_weight"].sum(),
    }])

    risk["household_state_risk_balance"] = risk["state_risk"] - risk["household_risk"]
    risk["market_firm_risk_balance"] = risk["market_risk"] - risk["firm_risk"]
    risk["risk_concentration_index"] = (
        risk[["household_risk", "firm_risk", "market_risk", "state_risk"]].max(axis=1)
        - risk[["household_risk", "firm_risk", "market_risk", "state_risk"]].min(axis=1)
    )

    reproduction = pd.concat([simulate_reproduction(row) for _, row in flows.iterrows()], ignore_index=True)

    access.to_csv(TABLE_DIR / "market_access_metrics_python.csv", index=False)
    access_summary.to_csv(TABLE_DIR / "market_access_summary_python.csv", index=False)
    risk.to_csv(TABLE_DIR / "risk_reproduction_metrics_python.csv", index=False)
    reproduction.to_csv(TABLE_DIR / "reproduction_capacity_paths_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(access["group"], access["effective_access"])
    ax.set_title("Effective Market and Institutional Access")
    ax.set_ylabel("Effective access score")
    ax.set_xlabel("Household group")
    ax.tick_params(axis="x", rotation=35)
    plt.tight_layout()
    plt.savefig(FIGURE_DIR / "market_access_python.png", dpi=300)
    plt.close()

    risk_plot = risk.set_index("scenario")[["household_risk", "firm_risk", "market_risk", "state_risk"]]
    risk_plot.plot(kind="bar", stacked=True, figsize=(10, 5))
    plt.title("Risk Distribution Across Institutional Actors")
    plt.ylabel("Risk share")
    plt.xlabel("Scenario")
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()
    plt.savefig(FIGURE_DIR / "risk_distribution_python.png", dpi=300)
    plt.close()

    fig, ax = plt.subplots(figsize=(10, 5))
    for scenario, group in reproduction.groupby("scenario"):
        ax.plot(group["period"], group["system_capacity"], label=scenario)
    ax.set_title("System Reproduction Capacity Paths")
    ax.set_xlabel("Period")
    ax.set_ylabel("System capacity index")
    ax.legend(fontsize=7)
    plt.tight_layout()
    plt.savefig(FIGURE_DIR / "reproduction_capacity_paths_python.png", dpi=300)
    plt.close()

    print(access_summary)
    print(risk[["scenario", "risk_concentration_index"]])


if __name__ == "__main__":
    main()
