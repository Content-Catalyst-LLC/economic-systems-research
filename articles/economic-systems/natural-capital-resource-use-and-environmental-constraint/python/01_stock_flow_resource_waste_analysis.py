"""
Stock-flow accounting, resource-use ratios, waste constraints, and sector resource pressure.
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
    stock = pd.read_csv(PROCESSED_DIR / "stock_flow_scenarios.csv")
    resources = pd.read_csv(PROCESSED_DIR / "resource_use_constraints.csv")
    sectors = pd.read_csv(PROCESSED_DIR / "sector_resource_pressure.csv")
    ecosystem = pd.read_csv(PROCESSED_DIR / "ecosystem_functions.csv")

    stock["natural_capital_next"] = stock["natural_capital_t"] + stock["regeneration"] - stock["degradation"]
    stock["regeneration_gap"] = stock["degradation"] - stock["regeneration"]
    stock["threshold_distance"] = stock["natural_capital_next"] - stock["threshold"]
    stock["stock_risk_score"] = (
        0.24 * (stock["regeneration_gap"].clip(lower=0) / stock["regeneration_gap"].clip(lower=0).max())
        + 0.22 * (1 - (stock["threshold_distance"].clip(lower=0) / stock["threshold_distance"].clip(lower=0).max()))
        + 0.20 * stock["life_support_importance"]
        + 0.20 * stock["irreversibility"]
        + 0.14 * (stock["degradation"] / stock["degradation"].max())
    )
    stock.to_csv(TABLE_DIR / "stock_flow_results_python.csv", index=False)

    resources["resource_use_ratio"] = resources.apply(
        lambda row: row["resource_use"] / row["regenerative_capacity"] if row["regenerative_capacity"] > 0 else float("inf"),
        axis=1,
    )
    resources["waste_constraint_ratio"] = resources["emissions"] / resources["absorptive_capacity"]
    finite_ratio = resources["resource_use_ratio"].replace(float("inf"), resources.loc[resources["resource_use_ratio"] != float("inf"), "resource_use_ratio"].max() * 1.5)
    resources["resource_constraint_score"] = (
        0.26 * (finite_ratio / finite_ratio.max())
        + 0.24 * (resources["waste_constraint_ratio"] / resources["waste_constraint_ratio"].max())
        + 0.18 * resources["social_necessity"]
        + 0.18 * (1 - resources["substitutability"])
        + 0.14 * (resources["resource_use"] / resources["resource_use"].max())
    )
    resources.to_csv(TABLE_DIR / "resource_use_constraint_results_python.csv", index=False)

    sectors["sector_pressure_score"] = (
        0.18 * sectors["material_intensity"]
        + 0.18 * sectors["energy_intensity"]
        + 0.16 * sectors["water_intensity"]
        + 0.14 * sectors["land_intensity"]
        + 0.14 * sectors["waste_intensity"]
        + 0.12 * sectors["import_dependence"]
        + 0.08 * sectors["social_necessity"]
    )
    sectors.to_csv(TABLE_DIR / "sector_resource_pressure_results_python.csv", index=False)

    ecosystem["ecosystem_function_score"] = (
        0.18 * ecosystem["water_filtration"]
        + 0.18 * ecosystem["flood_buffering"]
        + 0.18 * ecosystem["carbon_storage"]
        + 0.16 * ecosystem["habitat_support"]
        + 0.14 * ecosystem["soil_protection"]
        + 0.10 * ecosystem["pollination_support"]
        + 0.06 * (1 - ecosystem["market_visibility"])
    )
    ecosystem.to_csv(TABLE_DIR / "ecosystem_function_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(stock["system"], stock["natural_capital_next"])
    ax.set_title("Natural Capital Next Period")
    ax.set_ylabel("Stock index")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "natural_capital_next_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(resources["resource"], resources["waste_constraint_ratio"])
    ax.set_title("Waste Constraint Ratio")
    ax.set_ylabel("Emissions / absorptive capacity")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "waste_constraint_ratio_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(sectors["sector"], sectors["sector_pressure_score"])
    ax.set_title("Sector Resource Pressure")
    ax.set_ylabel("Composite pressure score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "sector_resource_pressure_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(ecosystem["ecosystem"], ecosystem["ecosystem_function_score"])
    ax.set_title("Ecosystem Function Score")
    ax.set_ylabel("Composite function score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "ecosystem_function_python.png", dpi=300)
    plt.close(fig)

    print(stock[["system", "natural_capital_next", "regeneration_gap", "threshold_distance", "stock_risk_score"]])
    print(resources[["resource", "resource_use_ratio", "waste_constraint_ratio", "resource_constraint_score"]])
    print(sectors[["sector", "sector_pressure_score"]])
    print(ecosystem[["ecosystem", "ecosystem_function_score"]])


if __name__ == "__main__":
    main()
