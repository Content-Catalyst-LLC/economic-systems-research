"""
Analyze allocation scenarios and public-priority trade-offs.
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


TOTAL_RESOURCES = 1000.0


def main() -> None:
    scenarios = pd.read_csv(PROCESSED_DIR / "allocation_scenarios.csv")
    priorities = pd.read_csv(PROCESSED_DIR / "allocation_priorities.csv")

    results = scenarios.merge(priorities, on="priority", how="left")
    results["allocation_units"] = results["share"] * TOTAL_RESOURCES

    baseline = results[results["scenario"] == "baseline"][["priority", "allocation_units"]].rename(
        columns={"allocation_units": "baseline_allocation_units"}
    )

    results = results.merge(baseline, on="priority", how="left")
    results["change_from_baseline"] = results["allocation_units"] - results["baseline_allocation_units"]
    results["essentiality_weighted_allocation"] = results["allocation_units"] * results["essentiality"]
    results["resilience_weighted_allocation"] = results["allocation_units"] * results["resilience_value"]

    scenario_summary = (
        results.groupby("scenario")
        .agg(
            total_allocation=("allocation_units", "sum"),
            essentiality_weighted_total=("essentiality_weighted_allocation", "sum"),
            resilience_weighted_total=("resilience_weighted_allocation", "sum"),
            restoration_allocation=("allocation_units", lambda x: x[results.loc[x.index, "priority"].eq("Ecological Restoration")].sum()),
            care_allocation=("allocation_units", lambda x: x[results.loc[x.index, "priority"].eq("Care")].sum()),
            infrastructure_allocation=("allocation_units", lambda x: x[results.loc[x.index, "priority"].eq("Infrastructure")].sum()),
        )
        .reset_index()
    )

    results.to_csv(TABLE_DIR / "allocation_results_python.csv", index=False)
    scenario_summary.to_csv(TABLE_DIR / "allocation_scenario_summary_python.csv", index=False)

    pivot = results.pivot(index="priority", columns="scenario", values="allocation_units")
    pivot.plot(kind="bar", figsize=(10, 5))
    plt.title("Allocation of Scarce Resources Across Social Priorities")
    plt.ylabel("Resource units")
    plt.xlabel("Priority")
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()
    plt.savefig(FIGURE_DIR / "allocation_scenarios_python.png", dpi=300)
    plt.close()

    print(scenario_summary)


if __name__ == "__main__":
    main()
