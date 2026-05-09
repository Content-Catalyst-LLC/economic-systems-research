"""
Allocation, distribution, and reproduction metrics for a stylized economic system.
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


def simulate_reproduction(row: pd.Series) -> pd.DataFrame:
    produced = [row["initial_produced_capital"]]
    natural = [row["initial_natural_capital"]]

    for _ in range(1, int(row["periods"])):
        next_produced = produced[-1] + row["investment"] - row["depreciation_rate"] * produced[-1]
        next_natural = natural[-1] + row["regeneration"] - row["depletion"]
        produced.append(next_produced)
        natural.append(next_natural)

    return pd.DataFrame({
        "scenario": row["scenario"],
        "period": list(range(int(row["periods"]))),
        "produced_capital": produced,
        "natural_capital": natural,
    })


def simple_gini(values: pd.Series) -> float:
    sorted_values = sorted(values.dropna())
    n = len(sorted_values)
    if n == 0:
        return float("nan")
    total = sum(sorted_values)
    if total == 0:
        return 0.0
    weighted_sum = sum((i + 1) * value for i, value in enumerate(sorted_values))
    return (2 * weighted_sum) / (n * total) - (n + 1) / n


def main() -> None:
    allocation = pd.read_csv(PROCESSED_DIR / "allocation_profiles.csv")
    sectors = pd.read_csv(PROCESSED_DIR / "economic_system_sectors.csv")
    results = pd.read_csv(PROCESSED_DIR / "economic_system_results.csv")
    reproduction_params = pd.read_csv(PROCESSED_DIR / "reproduction_parameters.csv")

    allocation["total_share"] = (
        allocation["consumption_share"]
        + allocation["investment_share"]
        + allocation["public_provision_share"]
        + allocation["restoration_share"]
    )
    allocation["future_capacity_share"] = allocation["investment_share"] + allocation["restoration_share"]
    allocation["collective_provision_share"] = allocation["public_provision_share"] + allocation["restoration_share"]
    allocation.to_csv(TABLE_DIR / "allocation_reproduction_metrics_python.csv", index=False)

    baseline_output = results[results["scenario"] == "baseline"][["sector_code", "total_output"]]
    distribution = baseline_output.merge(sectors, on="sector_code", how="left")
    distribution["labor_income"] = distribution["total_output"] * distribution["wage_share"]
    distribution["capital_income"] = distribution["total_output"] * distribution["profit_share"]
    distribution["public_or_mixed_income"] = distribution["total_output"] * distribution["public_or_mixed_share"]
    distribution["ecological_pressure"] = distribution["total_output"] * distribution["ecological_intensity"]
    distribution["employment_requirement"] = distribution["total_output"] * distribution["employment_intensity"]

    summary = pd.DataFrame([{
        "system_total_output": distribution["total_output"].sum(),
        "system_labor_income": distribution["labor_income"].sum(),
        "system_capital_income": distribution["capital_income"].sum(),
        "system_public_or_mixed_income": distribution["public_or_mixed_income"].sum(),
        "system_wage_share": distribution["labor_income"].sum() / distribution["total_output"].sum(),
        "system_profit_share": distribution["capital_income"].sum() / distribution["total_output"].sum(),
        "sector_output_gini": simple_gini(distribution["total_output"]),
        "sector_labor_income_gini": simple_gini(distribution["labor_income"]),
        "system_ecological_pressure": distribution["ecological_pressure"].sum(),
        "system_employment_requirement": distribution["employment_requirement"].sum(),
    }])

    distribution.to_csv(TABLE_DIR / "distribution_metrics_by_sector_python.csv", index=False)
    summary.to_csv(TABLE_DIR / "distribution_metrics_python.csv", index=False)

    reproduction = pd.concat(
        [simulate_reproduction(row) for _, row in reproduction_params.iterrows()],
        ignore_index=True,
    )
    reproduction.to_csv(TABLE_DIR / "reproduction_simulation_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(8, 5))
    baseline = allocation[allocation["scenario"] == "baseline"].iloc[0]
    shares = [
        baseline["consumption_share"],
        baseline["investment_share"],
        baseline["public_provision_share"],
        baseline["restoration_share"],
    ]
    labels = ["Consumption", "Investment", "Public provision", "Restoration"]
    ax.bar(labels, shares)
    ax.set_title("Baseline Allocation Profile")
    ax.set_ylabel("Share of output")
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "allocation_profile_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5))
    for scenario, group in reproduction.groupby("scenario"):
        ax.plot(group["period"], group["produced_capital"], label=f"{scenario}: produced")
        ax.plot(group["period"], group["natural_capital"], linestyle="--", label=f"{scenario}: natural")
    ax.set_title("Produced and Natural Capital Reproduction Paths")
    ax.set_xlabel("Period")
    ax.set_ylabel("Capital stock")
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "reproduction_constraints_python.png", dpi=300)
    plt.close(fig)

    print(summary)


if __name__ == "__main__":
    main()
