"""
Exchange, trade exposure, and ecological throughput scenario analysis.
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
    results = pd.read_csv(PROCESSED_DIR / "production_distribution_exchange_results.csv")

    scenario_summary = (
        results.groupby("scenario")
        .agg(
            total_output=("total_output", "sum"),
            total_labor_income=("labor_income", "sum"),
            total_non_labor_income=("non_labor_income", "sum"),
            total_ecological_throughput=("ecological_throughput", "sum"),
            total_exchange_dependency=("exchange_dependency", "sum"),
            total_public_goods_dependence=("public_goods_dependence", "mean"),
        )
        .reset_index()
    )

    scenario_summary["labor_share"] = scenario_summary["total_labor_income"] / scenario_summary["total_output"]
    scenario_summary["non_labor_share"] = scenario_summary["total_non_labor_income"] / scenario_summary["total_output"]
    scenario_summary["exchange_dependency_ratio"] = scenario_summary["total_exchange_dependency"] / scenario_summary["total_output"]
    scenario_summary["throughput_per_output"] = scenario_summary["total_ecological_throughput"] / scenario_summary["total_output"]

    scenario_summary.to_csv(TABLE_DIR / "exchange_scenario_results_python.csv", index=False)
    scenario_summary.to_csv(TABLE_DIR / "ecological_throughput_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(scenario_summary["scenario"], scenario_summary["exchange_dependency_ratio"])
    ax.set_title("Exchange Dependency by Scenario")
    ax.set_ylabel("Exchange dependency ratio")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "exchange_scenarios_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(scenario_summary["scenario"], scenario_summary["throughput_per_output"])
    ax.set_title("Ecological Throughput per Unit of Output")
    ax.set_ylabel("Throughput per output")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "ecological_throughput_python.png", dpi=300)
    plt.close(fig)

    print(scenario_summary)


if __name__ == "__main__":
    main()
