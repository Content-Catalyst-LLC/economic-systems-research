"""
Budget, essentials burden, fragility, and inflation scenario analysis.
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


SPENDING_CATEGORIES = ["rent", "food", "transport", "utilities", "health", "other"]


def apply_inflation(row: pd.Series, scenario: pd.Series) -> dict:
    adjusted = {}
    for category in SPENDING_CATEGORIES:
        multiplier = scenario[f"{category}_multiplier"]
        adjusted[category] = row[category] * multiplier
    return adjusted


def main() -> None:
    households = pd.read_csv(PROCESSED_DIR / "household_profiles.csv")
    inflation = pd.read_csv(PROCESSED_DIR / "inflation_scenarios.csv")

    records = []

    for _, household in households.iterrows():
        for _, scenario in inflation.iterrows():
            adjusted = apply_inflation(household, scenario)

            total_consumption = sum(adjusted.values())
            essentials = adjusted["rent"] + adjusted["food"] + adjusted["transport"] + adjusted["utilities"] + adjusted["health"]
            total_command = household["income"] + household["transfers"] + household["liquid_assets"]

            saving = (
                household["income"]
                + household["transfers"]
                + household["liquid_assets"]
                - household["debt_service"]
                - household["other_fixed_burdens"]
                - total_consumption
            )

            essentials_ratio = essentials / (household["income"] + household["transfers"])
            fragility_ratio = (
                essentials + household["debt_service"] + household["other_fixed_burdens"]
            ) / total_command

            effective_access = (
                household["income"] + household["transfers"] + household["liquid_assets"] - household["debt_service"]
            ) / essentials if essentials > 0 else float("nan")

            records.append({
                "household_group": household["household_group"],
                "scenario": scenario["scenario"],
                "population_weight": household["population_weight"],
                "total_consumption": total_consumption,
                "essentials_spending": essentials,
                "saving": saving,
                "essentials_ratio": essentials_ratio,
                "fragility_ratio": fragility_ratio,
                "effective_access": effective_access,
                "negative_saving_flag": int(saving < 0),
                "high_fragility_flag": int(fragility_ratio > 0.75),
            })

    results = pd.DataFrame(records)

    results.to_csv(TABLE_DIR / "household_budget_results_python.csv", index=False)
    results.to_csv(TABLE_DIR / "essentials_fragility_results_python.csv", index=False)

    summary = (
        results.groupby("scenario")
        .apply(lambda g: pd.Series({
            "weighted_essentials_ratio": (g["essentials_ratio"] * g["population_weight"]).sum() / g["population_weight"].sum(),
            "weighted_fragility_ratio": (g["fragility_ratio"] * g["population_weight"]).sum() / g["population_weight"].sum(),
            "population_share_negative_saving": (g["negative_saving_flag"] * g["population_weight"]).sum() / g["population_weight"].sum(),
            "population_share_high_fragility": (g["high_fragility_flag"] * g["population_weight"]).sum() / g["population_weight"].sum(),
        }))
        .reset_index()
    )
    summary.to_csv(TABLE_DIR / "budget_fragility_summary_python.csv", index=False)

    baseline = results[results["scenario"] == "baseline"]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(baseline["household_group"], baseline["essentials_ratio"])
    ax.set_title("Baseline Essentials Burden by Household Group")
    ax.set_ylabel("Essentials spending / income + transfers")
    ax.set_xlabel("Household group")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "essentials_burden_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(baseline["household_group"], baseline["fragility_ratio"])
    ax.set_title("Baseline Household Fragility Ratio")
    ax.set_ylabel("Essentials + debt + fixed burdens / total command")
    ax.set_xlabel("Household group")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "fragility_ratio_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(summary["scenario"], summary["weighted_fragility_ratio"])
    ax.set_title("Weighted Fragility Ratio by Scenario")
    ax.set_ylabel("Weighted fragility ratio")
    ax.set_xlabel("Scenario")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "inflation_scenario_fragility_python.png", dpi=300)
    plt.close(fig)

    print(summary)


if __name__ == "__main__":
    main()
