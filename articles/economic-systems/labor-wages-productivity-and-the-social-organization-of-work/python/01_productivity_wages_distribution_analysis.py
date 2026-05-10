"""
Labor productivity, wage share, unit labor cost, and wage-productivity divergence.
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
    sectors = pd.read_csv(PROCESSED_DIR / "sector_labor_scenarios.csv")
    series = pd.read_csv(PROCESSED_DIR / "wage_productivity_time_series.csv")

    sectors["labor_productivity"] = sectors["output"] / sectors["hours_worked"]
    sectors["wage_share"] = sectors["total_wages"] / sectors["output"]
    sectors["average_wage"] = sectors["total_wages"] / sectors["hours_worked"]
    sectors["unit_labor_cost"] = sectors["average_wage"] / sectors["labor_productivity"]
    sectors["care_adjusted_social_value_index"] = (
        sectors["labor_productivity"] * 0.45
        + sectors["employment_quality_index"] * 4.0
        + sectors["care_intensity"] * 2.5
    )
    sectors.to_csv(TABLE_DIR / "productivity_wage_share_results_python.csv", index=False)

    series["productivity_wage_divergence"] = series["productivity_index"] - series["wage_index"]
    series["strong_bargaining_gap"] = series["productivity_index"] - series["compensation_with_strong_bargaining"]
    series["wage_productivity_ratio"] = series["wage_index"] / series["productivity_index"]
    series.to_csv(TABLE_DIR / "wage_productivity_divergence_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(sectors["sector"], sectors["labor_productivity"], label="Labor productivity")
    ax.plot(sectors["sector"], sectors["wage_share"] * 10, marker="o", label="Wage share x10")
    ax.set_title("Labor Productivity and Wage Share by Sector")
    ax.set_ylabel("Index / ratio")
    ax.tick_params(axis="x", rotation=35)
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "productivity_wage_share_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(series["year"], series["productivity_index"], label="Productivity index")
    ax.plot(series["year"], series["wage_index"], label="Wage index")
    ax.plot(series["year"], series["compensation_with_strong_bargaining"], label="Strong-bargaining compensation")
    ax.set_title("Wage-Productivity Divergence")
    ax.set_xlabel("Year")
    ax.set_ylabel("Index")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "wage_productivity_divergence_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(sectors["sector"], sectors["unit_labor_cost"])
    ax.set_title("Unit Labor Cost by Sector")
    ax.set_ylabel("Unit labor cost")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "unit_labor_cost_python.png", dpi=300)
    plt.close(fig)

    print(sectors[["sector", "labor_productivity", "wage_share", "unit_labor_cost"]])
    print(series[["year", "productivity_wage_divergence"]].tail())


if __name__ == "__main__":
    main()
