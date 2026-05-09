"""
Input-output and distribution analysis for production, distribution, and exchange.

Solves:
    x = A x + f
    x = (I - A)^(-1) f
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
    scenarios = pd.read_csv(PROCESSED_DIR / "final_demand_exchange_scenarios.csv")
    sectors = pd.read_csv(PROCESSED_DIR / "production_sectors.csv")

    sector_codes = list(A.index)
    I = np.eye(len(sector_codes))
    leontief_inverse = np.linalg.inv(I - A.values)

    records = []

    for _, row in scenarios.iterrows():
        scenario = row["scenario"]
        f = row[sector_codes].to_numpy(dtype=float).reshape(-1, 1)
        x = leontief_inverse @ f

        for sector_code, final_demand, total_output in zip(sector_codes, f.flatten(), x.flatten()):
            records.append({
                "scenario": scenario,
                "sector_code": sector_code,
                "final_demand": final_demand,
                "total_output": total_output,
                "indirect_output_requirement": total_output - final_demand,
                "output_multiplier": total_output / final_demand if final_demand else np.nan,
            })

    results = pd.DataFrame(records).merge(sectors, on="sector_code", how="left")

    results["labor_income"] = results["total_output"] * results["labor_share"]
    results["non_labor_income"] = results["total_output"] * results["non_labor_share"]
    results["public_or_mixed_income"] = results["total_output"] * results["public_or_mixed_share"]
    results["ecological_throughput"] = results["total_output"] * results["ecological_intensity"]
    results["employment_requirement"] = results["total_output"] * results["employment_intensity"]
    results["exchange_dependency"] = results["total_output"] * results["trade_exposure"]

    baseline = results[results["scenario"] == "baseline"][["sector_code", "total_output"]].rename(
        columns={"total_output": "baseline_output"}
    )
    results = results.merge(baseline, on="sector_code", how="left")
    results["output_change_from_baseline"] = results["total_output"] - results["baseline_output"]

    results.to_csv(PROCESSED_DIR / "production_distribution_exchange_results.csv", index=False)
    results.to_csv(TABLE_DIR / "input_output_distribution_python.csv", index=False)

    summary = (
        results.groupby("scenario")
        .agg(
            total_output=("total_output", "sum"),
            total_final_demand=("final_demand", "sum"),
            total_labor_income=("labor_income", "sum"),
            total_non_labor_income=("non_labor_income", "sum"),
            total_public_or_mixed_income=("public_or_mixed_income", "sum"),
            total_ecological_throughput=("ecological_throughput", "sum"),
            total_employment_requirement=("employment_requirement", "sum"),
            total_exchange_dependency=("exchange_dependency", "sum"),
        )
        .reset_index()
    )

    summary["system_labor_share"] = summary["total_labor_income"] / summary["total_output"]
    summary["system_non_labor_share"] = summary["total_non_labor_income"] / summary["total_output"]
    summary.to_csv(TABLE_DIR / "labor_share_distribution_python.csv", index=False)

    baseline_plot = results[results["scenario"] == "baseline"]

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(baseline_plot["sector_code"], baseline_plot["total_output"])
    ax.set_title("Baseline Total Output by Sector")
    ax.set_ylabel("Total output")
    ax.set_xlabel("Sector")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "sector_output_distribution_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(baseline_plot["sector_code"], baseline_plot["labor_income"], label="Labor income")
    ax.bar(
        baseline_plot["sector_code"],
        baseline_plot["non_labor_income"],
        bottom=baseline_plot["labor_income"],
        label="Non-labor income",
    )
    ax.set_title("Labor and Non-Labor Income by Sector")
    ax.set_ylabel("Income claims")
    ax.set_xlabel("Sector")
    ax.tick_params(axis="x", rotation=35)
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "labor_nonlabor_income_python.png", dpi=300)
    plt.close(fig)

    print(summary)


if __name__ == "__main__":
    main()
