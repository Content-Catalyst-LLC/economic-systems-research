"""
Capital accumulation, capital intensity, investment rates, and NPV analysis.
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


def simulate_capital(row: pd.Series, periods: int = 15) -> pd.DataFrame:
    capital = float(row["initial_capital"])
    rows = []

    for period in range(periods + 1):
        rows.append({
            "scenario": row["scenario"],
            "period": period,
            "capital_stock": capital,
            "annual_investment": row["annual_investment"],
            "depreciation_rate": row["depreciation_rate"],
            "labor": row["labor"],
            "output": row["output"],
            "capital_intensity": capital / row["labor"],
            "investment_rate": row["annual_investment"] / row["output"],
        })

        capital = capital + row["annual_investment"] - row["depreciation_rate"] * capital

    return pd.DataFrame(rows)


def npv(cashflows: np.ndarray, rate: float) -> float:
    periods = np.arange(len(cashflows))
    return float(np.sum(cashflows / ((1 + rate) ** periods)))


def main() -> None:
    capital_scenarios = pd.read_csv(PROCESSED_DIR / "capital_stock_scenarios.csv")
    projects = pd.read_csv(PROCESSED_DIR / "investment_project_scenarios.csv")

    paths = pd.concat(
        [simulate_capital(row, periods=15) for _, row in capital_scenarios.iterrows()],
        ignore_index=True,
    )
    paths.to_csv(TABLE_DIR / "capital_accumulation_results_python.csv", index=False)

    intensity_summary = (
        paths.groupby("scenario")
        .agg(
            final_capital_stock=("capital_stock", "last"),
            final_capital_intensity=("capital_intensity", "last"),
            average_investment_rate=("investment_rate", "mean"),
        )
        .reset_index()
    )
    intensity_summary.to_csv(TABLE_DIR / "capital_intensity_results_python.csv", index=False)

    project_records = []
    cashflow_cols = [f"cashflow_year_{i}" for i in range(0, 6)]
    discount_rates = np.linspace(0.01, 0.12, 12)

    sensitivity_records = []
    for _, project in projects.iterrows():
        cashflows = project[cashflow_cols].to_numpy(dtype=float)
        private = npv(cashflows, project["private_discount_rate"])
        public = npv(cashflows, project["public_discount_rate"])

        project_records.append({
            "project": project["project"],
            "npv_private": private,
            "npv_public": public,
            "public_private_npv_gap": public - private,
        })

        for rate in discount_rates:
            sensitivity_records.append({
                "project": project["project"],
                "discount_rate": rate,
                "npv": npv(cashflows, rate),
            })

    project_results = pd.DataFrame(project_records)
    sensitivity = pd.DataFrame(sensitivity_records)

    project_results.to_csv(TABLE_DIR / "npv_project_results_python.csv", index=False)
    sensitivity.to_csv(TABLE_DIR / "npv_discount_sensitivity_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    for scenario, group in paths.groupby("scenario"):
        ax.plot(group["period"], group["capital_stock"], label=scenario)
    ax.set_title("Capital Stock Paths Under Investment and Depreciation Scenarios")
    ax.set_xlabel("Period")
    ax.set_ylabel("Capital stock")
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "capital_stock_paths_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    for project, group in sensitivity.groupby("project"):
        ax.plot(group["discount_rate"], group["npv"], label=project)
    ax.axhline(0, linestyle="--")
    ax.set_title("NPV Sensitivity to Discount Rate")
    ax.set_xlabel("Discount rate")
    ax.set_ylabel("Net present value")
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "npv_discount_rate_sensitivity_python.png", dpi=300)
    plt.close(fig)

    print(intensity_summary)
    print(project_results)


if __name__ == "__main__":
    main()
