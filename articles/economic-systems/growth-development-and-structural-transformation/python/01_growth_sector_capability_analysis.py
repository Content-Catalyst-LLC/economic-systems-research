"""
Growth paths, labor productivity, sectoral transformation, and development capability.
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
    growth = pd.read_csv(PROCESSED_DIR / "growth_path_scenarios.csv")
    sectors = pd.read_csv(PROCESSED_DIR / "sector_transformation_scenarios.csv")
    capability = pd.read_csv(PROCESSED_DIR / "development_capability_scenarios.csv")
    urban = pd.read_csv(PROCESSED_DIR / "urban_infrastructure_scenarios.csv")

    growth["growth_rate"] = growth.groupby("scenario")["output"].pct_change().fillna(0)
    growth["cumulative_growth"] = growth["output"] / growth.groupby("scenario")["output"].transform("first") - 1
    growth["labor_productivity"] = growth["output"] / growth["labor"]
    growth.to_csv(TABLE_DIR / "growth_results_python.csv", index=False)

    totals = sectors.groupby("scenario")[["sector_output", "sector_labor"]].sum().rename(
        columns={"sector_output": "total_output", "sector_labor": "total_labor"}
    )
    sectors = sectors.merge(totals, on="scenario")
    sectors["output_share"] = sectors["sector_output"] / sectors["total_output"]
    sectors["labor_share"] = sectors["sector_labor"] / sectors["total_labor"]
    sectors["sector_productivity"] = sectors["sector_output"] / sectors["sector_labor"]
    sectors["productivity_gap_to_economy"] = sectors["sector_productivity"] - (sectors["total_output"] / sectors["total_labor"])
    sectors.to_csv(TABLE_DIR / "sector_transformation_results_python.csv", index=False)

    capability["capability_index"] = (
        0.22 * capability["income_index"]
        + 0.20 * capability["health_index"]
        + 0.20 * capability["education_index"]
        + 0.22 * capability["infrastructure_index"]
        + 0.16 * capability["security_index"]
    )
    capability.to_csv(TABLE_DIR / "development_capability_results_python.csv", index=False)

    urban["urban_development_capacity_score"] = (
        0.25 * urban["infrastructure_depth"]
        + 0.22 * urban["housing_access"]
        + 0.22 * urban["transit_access"]
        + 0.22 * urban["spatial_inclusion"]
        + 0.09 * urban["urbanization_rate"]
    )
    urban.to_csv(TABLE_DIR / "urban_infrastructure_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    for scenario, group in growth.groupby("scenario"):
        ax.plot(group["period"], group["output"], label=scenario)
    ax.set_title("Growth Paths by Development Scenario")
    ax.set_xlabel("Period")
    ax.set_ylabel("Output index")
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "growth_paths_python.png", dpi=300)
    plt.close(fig)

    output_pivot = sectors.pivot(index="scenario", columns="sector", values="output_share")
    fig, ax = plt.subplots(figsize=(10, 5))
    output_pivot.plot(kind="bar", stacked=True, ax=ax)
    ax.set_title("Sectoral Output Shares")
    ax.set_ylabel("Share of output")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "sectoral_output_shares_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    productivity_pivot = sectors.pivot(index="scenario", columns="sector", values="sector_productivity")
    productivity_pivot.plot(kind="bar", ax=ax)
    ax.set_title("Sectoral Labor Productivity")
    ax.set_ylabel("Output per worker")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "sectoral_labor_productivity_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(capability["scenario"], capability["capability_index"])
    ax.set_title("Development Capability Index")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "development_capability_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(urban["scenario"], urban["urban_development_capacity_score"])
    ax.set_title("Urban Infrastructure and Spatial Inclusion Capacity")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "urban_infrastructure_python.png", dpi=300)
    plt.close(fig)

    print(growth.head())
    print(sectors[["scenario", "sector", "output_share", "labor_share", "sector_productivity"]])
    print(capability[["scenario", "capability_index"]])
    print(urban[["scenario", "urban_development_capacity_score"]])


if __name__ == "__main__":
    main()
