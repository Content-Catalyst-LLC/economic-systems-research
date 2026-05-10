"""
Private and social optimum analysis for externalities and public goods.
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


def build_schedule(row: pd.Series, q_max: int = 120) -> pd.DataFrame:
    q = np.arange(1, q_max + 1)

    mpc = row["mpc_intercept"] + row["mpc_slope"] * q
    mec = row["mec_intercept"] + row["mec_slope"] * q
    msc = mpc + mec

    mpb = row["mpb_intercept"] + row["mpb_slope"] * q
    meb = row["meb_intercept"] + row["meb_slope"] * q
    msb = mpb + meb

    damage = np.cumsum(np.maximum(mec, 0)) / 10

    return pd.DataFrame({
        "scenario": row["scenario"],
        "output": q,
        "MPC": mpc,
        "MEC": mec,
        "MSC": msc,
        "MPB": mpb,
        "MEB": meb,
        "MSB": msb,
        "damage": damage,
        "critical_threshold": row["critical_threshold"],
        "threshold_crossed": (damage > row["critical_threshold"]).astype(int),
    })


def nearest_crossing_output(schedule: pd.DataFrame, left: str, right: str) -> int:
    idx = (schedule[left] - schedule[right]).abs().idxmin()
    return int(schedule.loc[idx, "output"])


def main() -> None:
    scenarios = pd.read_csv(PROCESSED_DIR / "externality_scenarios.csv")
    public_goods = pd.read_csv(PROCESSED_DIR / "public_good_scenarios.csv")

    schedules = pd.concat([build_schedule(row) for _, row in scenarios.iterrows()], ignore_index=True)
    schedules.to_csv(TABLE_DIR / "externality_schedules_python.csv", index=False)

    summary_records = []
    for scenario, group in schedules.groupby("scenario"):
        private_output = nearest_crossing_output(group, "MPB", "MPC")
        social_output = nearest_crossing_output(group, "MSB", "MSC")
        threshold_rows = group[group["threshold_crossed"] == 1]
        threshold_output = int(threshold_rows["output"].iloc[0]) if not threshold_rows.empty else None

        summary_records.append({
            "scenario": scenario,
            "private_output": private_output,
            "social_output": social_output,
            "private_minus_social_output": private_output - social_output,
            "threshold_crossing_output": threshold_output,
        })

    optimum = pd.DataFrame(summary_records)
    optimum.to_csv(TABLE_DIR / "private_social_optimum_python.csv", index=False)

    public_goods["social_benefit"] = public_goods["private_benefit"] + public_goods["external_benefit"]
    public_goods["underprovision_gap"] = public_goods["social_need"] - public_goods["voluntary_provision"]
    public_goods["private_incentive_gap"] = public_goods["social_benefit"] - public_goods["private_benefit"]
    public_goods["social_return_ratio"] = public_goods["social_benefit"] / public_goods["private_cost"]
    public_goods.to_csv(TABLE_DIR / "public_good_underprovision_python.csv", index=False)

    baseline = schedules[schedules["scenario"] == "baseline_pollution_externality"]

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(baseline["output"], baseline["MPC"], label="MPC")
    ax.plot(baseline["output"], baseline["MSC"], label="MSC")
    ax.plot(baseline["output"], baseline["MPB"], label="MPB")
    ax.set_title("Private Cost, Social Cost, and Marginal Benefit")
    ax.set_xlabel("Output")
    ax.set_ylabel("Marginal value / cost")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "private_vs_social_cost_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(public_goods["public_good"], public_goods["social_need"], label="Social need")
    ax.plot(public_goods["public_good"], public_goods["voluntary_provision"], marker="o", label="Voluntary provision")
    ax.set_title("Public Good Underprovision")
    ax.set_ylabel("Provision index")
    ax.tick_params(axis="x", rotation=35)
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "public_good_underprovision_python.png", dpi=300)
    plt.close(fig)

    print(optimum)
    print(public_goods[["public_good", "social_need", "voluntary_provision", "underprovision_gap"]])


if __name__ == "__main__":
    main()
