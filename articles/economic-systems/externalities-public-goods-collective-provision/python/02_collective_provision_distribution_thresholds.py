"""
Collective provision, contribution, burden distribution, and threshold analysis.
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
    contributions = pd.read_csv(PROCESSED_DIR / "contribution_scenarios.csv")
    finance = pd.read_csv(PROCESSED_DIR / "collective_finance_scenarios.csv")
    burden = pd.read_csv(PROCESSED_DIR / "burden_distribution_groups.csv")
    schedules = pd.read_csv(TABLE_DIR / "externality_schedules_python.csv")

    contributions["free_rider_flag"] = ((contributions["contribution"] <= 1) & (contributions["benefit_share"] > 0)).astype(int)
    contribution_summary = (
        contributions.groupby("scenario")
        .agg(
            total_contribution=("contribution", "sum"),
            benefit_coverage=("benefit_share", "sum"),
            free_rider_groups=("free_rider_flag", "sum"),
        )
        .reset_index()
    )
    contribution_summary.to_csv(TABLE_DIR / "free_rider_contribution_python.csv", index=False)
    contributions.to_csv(TABLE_DIR / "free_rider_contribution_detail_python.csv", index=False)

    finance["collective_provision_capacity"] = finance["tax_revenue"] + finance["borrowing_capacity"] + finance["pooled_funds"]
    finance["total_collective_need"] = finance["maintenance_need"] + finance["preparedness_need"]
    finance["capacity_gap"] = finance["collective_provision_capacity"] - finance["total_collective_need"]
    finance["capacity_ratio"] = finance["collective_provision_capacity"] / finance["total_collective_need"]
    finance.to_csv(TABLE_DIR / "collective_finance_results_python.csv", index=False)

    burden["raw_burden_score"] = (
        0.52 * burden["exposure_index"]
        + 0.28 * (1 - burden["income_index"])
        + 0.20 * (1 - burden["political_voice_index"])
    )
    burden["weighted_burden"] = burden["raw_burden_score"] * burden["population_weight"]
    burden["burden_share"] = burden["weighted_burden"] / burden["weighted_burden"].sum()
    burden.to_csv(TABLE_DIR / "burden_distribution_python.csv", index=False)

    threshold_summary = (
        schedules.groupby("scenario")
        .apply(lambda g: pd.Series({
            "max_damage": g["damage"].max(),
            "critical_threshold": g["critical_threshold"].iloc[0],
            "threshold_crossed": int((g["damage"] > g["critical_threshold"].iloc[0]).any()),
            "first_threshold_output": g.loc[g["damage"] > g["critical_threshold"].iloc[0], "output"].min()
            if (g["damage"] > g["critical_threshold"].iloc[0]).any() else None,
        }))
        .reset_index()
    )
    threshold_summary.to_csv(TABLE_DIR / "threshold_damage_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(9, 5))
    for scenario, group in contributions.groupby("scenario"):
        ax.plot(group["contributor_group"], group["contribution"], marker="o", label=scenario)
    ax.set_title("Public Good Contribution by Scenario")
    ax.set_ylabel("Contribution")
    ax.tick_params(axis="x", rotation=35)
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "free_rider_contributions_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(burden["group"], burden["burden_share"])
    ax.set_title("Distribution of Externality Burden")
    ax.set_ylabel("Burden share")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "burden_distribution_python.png", dpi=300)
    plt.close(fig)

    threshold_plot = schedules[schedules["scenario"].isin(["baseline_pollution_externality", "ecological_threshold_risk"])]
    fig, ax = plt.subplots(figsize=(9, 5))
    for scenario, group in threshold_plot.groupby("scenario"):
        ax.plot(group["output"], group["damage"], label=scenario)
        ax.axhline(group["critical_threshold"].iloc[0], linestyle="--")
    ax.set_title("Accumulated Damage and Critical Thresholds")
    ax.set_xlabel("Output / time proxy")
    ax.set_ylabel("Accumulated damage")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "threshold_damage_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(finance["scenario"], finance["capacity_ratio"])
    ax.set_title("Collective Provision Capacity Relative to Need")
    ax.set_ylabel("Capacity / need")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "collective_finance_capacity_python.png", dpi=300)
    plt.close(fig)

    print(contribution_summary)
    print(finance[["scenario", "capacity_ratio", "capacity_gap"]])
    print(threshold_summary)


if __name__ == "__main__":
    main()
