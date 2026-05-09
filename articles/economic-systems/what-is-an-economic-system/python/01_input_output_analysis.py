"""
Input-output analysis for a stylized economic system.

This script solves:
    x = A x + f
    x = (I - A)^(-1) f

It exports total output requirements by scenario and a figure.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
FIGURE_DIR = BASE_DIR / "outputs" / "figures"
TABLE_DIR = BASE_DIR / "outputs" / "tables"

for directory in [FIGURE_DIR, TABLE_DIR]:
    directory.mkdir(parents=True, exist_ok=True)


def main() -> None:
    A = pd.read_csv(PROCESSED_DIR / "input_output_matrix.csv", index_col=0)
    demand = pd.read_csv(PROCESSED_DIR / "final_demand_scenarios.csv")
    sectors = list(A.index)

    I = np.eye(len(sectors))
    leontief_inverse = np.linalg.inv(I - A.values)

    records = []

    for _, row in demand.iterrows():
        scenario = row["scenario"]
        f = row[sectors].to_numpy(dtype=float).reshape(-1, 1)
        x = leontief_inverse @ f

        for sector, final_demand, total_output in zip(sectors, f.flatten(), x.flatten()):
            records.append({
                "scenario": scenario,
                "sector_code": sector,
                "final_demand": final_demand,
                "total_output": total_output,
                "indirect_output_requirement": total_output - final_demand,
                "output_multiplier": total_output / final_demand if final_demand != 0 else np.nan,
            })

    results = pd.DataFrame(records)

    baseline = results[results["scenario"] == "baseline"][["sector_code", "total_output"]].rename(
        columns={"total_output": "baseline_output"}
    )

    results = results.merge(baseline, on="sector_code", how="left")
    results["output_change_from_baseline"] = results["total_output"] - results["baseline_output"]

    results.to_csv(PROCESSED_DIR / "economic_system_results.csv", index=False)
    results.to_csv(TABLE_DIR / "input_output_results_python.csv", index=False)

    baseline_plot = results[results["scenario"] == "baseline"].copy()

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(baseline_plot["sector_code"], baseline_plot["total_output"])
    ax.set_title("Total Output Requirements by Sector")
    ax.set_ylabel("Total output")
    ax.set_xlabel("Sector")
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "input_output_total_output_python.png", dpi=300)
    plt.close(fig)

    scenario_totals = (
        results.groupby("scenario", as_index=False)["total_output"]
        .sum()
        .sort_values("total_output", ascending=False)
    )

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(scenario_totals["scenario"], scenario_totals["total_output"])
    ax.set_title("Total System Output by Scenario")
    ax.set_ylabel("Total output")
    ax.set_xlabel("Scenario")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "input_output_scenario_totals_python.png", dpi=300)
    plt.close(fig)

    print(results.head())
    print(scenario_totals)


if __name__ == "__main__":
    main()
