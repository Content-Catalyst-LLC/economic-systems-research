"""
Effective access and intertemporal reproduction constraints.
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


def simulate_capacity(row: pd.Series) -> pd.DataFrame:
    produced = [row["initial_produced_capacity"]]
    ecological = [row["initial_ecological_capacity"]]

    for _ in range(1, int(row["periods"])):
        next_produced = produced[-1] + row["investment"] + row["maintenance"] - row["depreciation_rate"] * produced[-1]
        next_ecological = ecological[-1] + row["ecological_restoration"] + row["regenerative_capacity"] - row["resource_use"]
        produced.append(next_produced)
        ecological.append(next_ecological)

    return pd.DataFrame({
        "scenario": row["scenario"],
        "period": list(range(int(row["periods"]))),
        "produced_capacity": produced,
        "ecological_capacity": ecological,
    })


def main() -> None:
    households = pd.read_csv(PROCESSED_DIR / "access_households.csv")
    reproduction_params = pd.read_csv(PROCESSED_DIR / "reproduction_constraints.csv")

    households["effective_access"] = (
        0.35 * households["income_command"]
        + 0.35 * households["institutional_access"]
        + 0.20 * (1 - households["price_index"])
        + 0.10 * households["need_index"]
    )

    households["access_gap"] = households["need_index"] - households["effective_access"]
    households["deprivation_flag"] = (households["access_gap"] > 0.25).astype(int)
    households["weighted_access_gap"] = households["access_gap"] * households["population_weight"]
    households["weighted_deprivation"] = households["deprivation_flag"] * households["population_weight"]

    access_summary = pd.DataFrame([{
        "population_weighted_access_gap": households["weighted_access_gap"].sum(),
        "population_share_deprived": households["weighted_deprivation"].sum(),
        "avg_effective_access": (households["effective_access"] * households["population_weight"]).sum() / households["population_weight"].sum(),
        "avg_need_index": (households["need_index"] * households["population_weight"]).sum() / households["population_weight"].sum(),
    }])

    households.to_csv(TABLE_DIR / "effective_access_metrics_python.csv", index=False)
    access_summary.to_csv(TABLE_DIR / "effective_access_summary_python.csv", index=False)

    reproduction = pd.concat(
        [simulate_capacity(row) for _, row in reproduction_params.iterrows()],
        ignore_index=True,
    )

    reproduction.to_csv(TABLE_DIR / "intertemporal_reproduction_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(households["household_group"], households["effective_access"])
    ax.set_title("Effective Access by Household Group")
    ax.set_ylabel("Effective access score")
    ax.set_xlabel("Household group")
    ax.tick_params(axis="x", rotation=35)
    plt.tight_layout()
    plt.savefig(FIGURE_DIR / "effective_access_python.png", dpi=300)
    plt.close()

    fig, ax = plt.subplots(figsize=(9, 5))
    for scenario, group in reproduction.groupby("scenario"):
        ax.plot(group["period"], group["produced_capacity"], label=f"{scenario}: produced")
        ax.plot(group["period"], group["ecological_capacity"], linestyle="--", label=f"{scenario}: ecological")
    ax.set_title("Intertemporal Capacity Paths")
    ax.set_xlabel("Period")
    ax.set_ylabel("Capacity index")
    ax.legend(fontsize=7)
    plt.tight_layout()
    plt.savefig(FIGURE_DIR / "intertemporal_capacity_paths_python.png", dpi=300)
    plt.close()

    regen = reproduction_params.copy()
    regen["use_exceeds_regeneration"] = regen["resource_use"] > (regen["regenerative_capacity"] + regen["ecological_restoration"])
    regen.to_csv(TABLE_DIR / "ecological_regeneration_constraint_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(regen["scenario"], regen["resource_use"], label="Resource use")
    ax.plot(regen["scenario"], regen["regenerative_capacity"] + regen["ecological_restoration"], marker="o", label="Regeneration + restoration")
    ax.set_title("Ecological Use and Regenerative Capacity")
    ax.set_ylabel("Capacity units")
    ax.tick_params(axis="x", rotation=35)
    ax.legend()
    plt.tight_layout()
    plt.savefig(FIGURE_DIR / "ecological_regeneration_constraint_python.png", dpi=300)
    plt.close()

    print(access_summary)
    print(regen[["scenario", "resource_use", "regenerative_capacity", "ecological_restoration", "use_exceeds_regeneration"]])


if __name__ == "__main__":
    main()
