"""
Simulate shared resource stock paths under multiple governance regimes.
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


def regeneration(stock: float, rate: float, carrying_capacity: float) -> float:
    return rate * stock * (1 - stock / carrying_capacity)


def simulate_stock(resource: pd.Series, governance: pd.Series, users: pd.DataFrame, periods: int = 40) -> pd.DataFrame:
    stock = float(resource["initial_stock"])
    rows = []

    baseline_harvest = users["baseline_extraction"].sum()
    governed_harvest = users["governed_extraction"].sum()

    for period in range(periods + 1):
        regen = regeneration(stock, resource["regeneration_rate"], resource["carrying_capacity"])

        harvest = (
            baseline_harvest * governance["extraction_multiplier"]
            if governance["scenario"] in ["open_access_weak_governance", "captured_governance"]
            else governed_harvest * governance["extraction_multiplier"]
        )

        rows.append({
            "resource": resource["resource"],
            "governance_scenario": governance["scenario"],
            "period": period,
            "stock": stock,
            "regeneration": regen,
            "harvest": harvest,
            "harvest_regeneration_balance": regen - harvest,
            "critical_stock_threshold": resource["critical_stock_threshold"],
            "depletion_risk_flag": int(stock < resource["critical_stock_threshold"]),
        })

        stock = max(0, stock + regen - harvest)

    return pd.DataFrame(rows)


def main() -> None:
    resources = pd.read_csv(PROCESSED_DIR / "resource_scenarios.csv")
    users = pd.read_csv(PROCESSED_DIR / "user_extraction_profiles.csv")
    governance = pd.read_csv(PROCESSED_DIR / "governance_scenarios.csv")

    fishery = resources[resources["resource"] == "fishery"].iloc[0]

    paths = pd.concat(
        [simulate_stock(fishery, gov, users, periods=40) for _, gov in governance.iterrows()],
        ignore_index=True,
    )
    paths.to_csv(TABLE_DIR / "commons_stock_paths_python.csv", index=False)

    summary = (
        paths.groupby("governance_scenario")
        .agg(
            final_stock=("stock", "last"),
            minimum_stock=("stock", "min"),
            average_harvest=("harvest", "mean"),
            average_regeneration=("regeneration", "mean"),
            periods_in_depletion_risk=("depletion_risk_flag", "sum"),
        )
        .reset_index()
    )
    summary.to_csv(TABLE_DIR / "commons_stock_summary_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    for scenario, group in paths.groupby("governance_scenario"):
        ax.plot(group["period"], group["stock"], label=scenario)
    ax.axhline(fishery["critical_stock_threshold"], linestyle="--", label="critical threshold")
    ax.set_title("Shared Resource Stock Paths Under Governance Regimes")
    ax.set_xlabel("Period")
    ax.set_ylabel("Resource stock")
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "commons_stock_paths_python.png", dpi=300)
    plt.close(fig)

    final = paths[paths["period"] == paths["period"].max()].copy()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(final["governance_scenario"], final["stock"])
    ax.set_title("Final Stock by Governance Scenario")
    ax.set_ylabel("Final stock")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "final_stock_by_governance_python.png", dpi=300)
    plt.close(fig)

    balance_plot = paths[paths["governance_scenario"].isin(["open_access_weak_governance", "community_governance", "polycentric_governance"])]
    fig, ax = plt.subplots(figsize=(10, 5))
    for scenario, group in balance_plot.groupby("governance_scenario"):
        ax.plot(group["period"], group["harvest_regeneration_balance"], label=scenario)
    ax.axhline(0, linestyle="--")
    ax.set_title("Regeneration Minus Harvest")
    ax.set_xlabel("Period")
    ax.set_ylabel("Regeneration - harvest")
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "harvest_regeneration_balance_python.png", dpi=300)
    plt.close(fig)

    print(summary)


if __name__ == "__main__":
    main()
