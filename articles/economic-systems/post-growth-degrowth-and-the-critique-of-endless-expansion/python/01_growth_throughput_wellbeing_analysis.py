"""
Growth dependence, throughput, wellbeing, and work-time analysis.
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
    growth = pd.read_csv(PROCESSED_DIR / "growth_dependence.csv")
    throughput = pd.read_csv(PROCESSED_DIR / "throughput_scenarios.csv")
    wellbeing = pd.read_csv(PROCESSED_DIR / "wellbeing_dashboard.csv")
    work = pd.read_csv(PROCESSED_DIR / "work_time_care.csv")

    growth["growth_dependence_score"] = growth[
        [
            "employment_dependency",
            "debt_service_dependency",
            "fiscal_dependency",
            "asset_dependency",
            "pension_dependency",
            "housing_market_dependency",
            "political_legitimacy_dependency",
        ]
    ].mean(axis=1)
    growth.to_csv(TABLE_DIR / "growth_dependence_results_python.csv", index=False)

    throughput["throughput_index"] = throughput["population"] * throughput["affluence"] * throughput["intensity"]
    throughput["wellbeing_per_throughput"] = throughput["wellbeing_index"] / throughput["throughput_index"]
    throughput["just_throughput_score"] = (
        0.36 * throughput["wellbeing_index"]
        + 0.28 * throughput["distribution_quality"]
        + 0.20 * (1 - throughput["throughput_index"] / throughput["throughput_index"].max())
        + 0.16 * (1 - throughput["intensity"] / throughput["intensity"].max())
    )
    throughput.to_csv(TABLE_DIR / "throughput_results_python.csv", index=False)

    wellbeing_columns = [
        "health",
        "time_balance",
        "security",
        "equality",
        "public_goods",
        "ecological_quality",
        "care_support",
        "social_trust",
    ]
    wellbeing["wellbeing_score"] = wellbeing[wellbeing_columns].mean(axis=1)
    wellbeing.to_csv(TABLE_DIR / "wellbeing_results_python.csv", index=False)

    work["total_work_hours"] = work["paid_work_hours"] + work["unpaid_care_hours"]
    work["time_care_score"] = (
        0.20 * (1 - work["paid_work_hours"] / work["paid_work_hours"].max())
        + 0.18 * (work["leisure_hours"] / work["leisure_hours"].max())
        + 0.20 * work["labor_security"]
        + 0.22 * work["care_support"]
        + 0.20 * work["time_sovereignty"]
    )
    work.to_csv(TABLE_DIR / "work_time_care_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(growth["scenario"], growth["growth_dependence_score"])
    ax.set_title("Growth Dependence")
    ax.set_ylabel("Composite growth-dependence score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "growth_dependence_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(throughput["scenario"], throughput["throughput_index"])
    ax.set_title("Throughput Index")
    ax.set_ylabel("Population × affluence × intensity")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "throughput_index_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(wellbeing["scenario"], wellbeing["wellbeing_score"])
    ax.set_title("Wellbeing Beyond Output")
    ax.set_ylabel("Composite wellbeing score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "wellbeing_score_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(work["scenario"], work["time_care_score"])
    ax.set_title("Time, Care, and Work")
    ax.set_ylabel("Composite time-care score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "time_care_python.png", dpi=300)
    plt.close(fig)

    print(growth[["scenario", "growth_dependence_score"]])
    print(throughput[["scenario", "throughput_index", "wellbeing_per_throughput", "just_throughput_score"]])
    print(wellbeing[["scenario", "wellbeing_score"]])
    print(work[["scenario", "total_work_hours", "time_care_score"]])


if __name__ == "__main__":
    main()
