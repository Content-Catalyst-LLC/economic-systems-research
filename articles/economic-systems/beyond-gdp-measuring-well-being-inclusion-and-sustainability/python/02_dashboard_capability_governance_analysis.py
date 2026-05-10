"""
Capability conversion, care visibility, subjective well-being, and indicator governance.
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
    capability = pd.read_csv(PROCESSED_DIR / "capability_conversion.csv")
    care = pd.read_csv(PROCESSED_DIR / "care_time_use.csv")
    subjective = pd.read_csv(PROCESSED_DIR / "subjective_wellbeing.csv")
    governance = pd.read_csv(PROCESSED_DIR / "indicator_governance.csv")

    capability["capability_score"] = (
        0.18 * capability["resources"]
        + 0.20 * capability["public_goods"]
        + 0.16 * capability["health_conversion"]
        + 0.16 * capability["education_conversion"]
        + 0.12 * capability["transport_access"]
        + 0.12 * capability["care_support"]
        + 0.06 * (1 - capability["discrimination_barrier"])
    )
    capability.to_csv(TABLE_DIR / "capability_conversion_results_python.csv", index=False)

    care["total_work_hours"] = care["paid_work_hours"] + care["unpaid_care_hours"]
    care["care_visibility_score"] = (
        0.24 * (care["unpaid_care_hours"] / care["unpaid_care_hours"].max())
        + 0.18 * care["formal_recognition"]
        + 0.20 * care["support_services"]
        + 0.18 * (1 - care["time_stress"])
        + 0.20 * (care["leisure_hours"] / care["leisure_hours"].max())
    )
    care.to_csv(TABLE_DIR / "care_time_use_results_python.csv", index=False)

    subjective["subjective_wellbeing_score"] = (
        0.28 * subjective["life_satisfaction"]
        + 0.20 * (1 - subjective["stress"])
        + 0.20 * subjective["meaning"]
        + 0.18 * subjective["social_trust"]
        + 0.14 * (1 - subjective["loneliness"])
    )
    subjective["income_wellbeing_gap"] = subjective["income_index"] - subjective["subjective_wellbeing_score"]
    subjective.to_csv(TABLE_DIR / "subjective_wellbeing_results_python.csv", index=False)

    governance["governance_usefulness_score"] = (
        0.14 * governance["clarity"]
        + 0.20 * governance["multidimensionality"]
        + 0.16 * governance["public_legibility"]
        + 0.16 * (1 - governance["gaming_risk"])
        + 0.20 * governance["policy_linkage"]
        + 0.14 * governance["local_relevance"]
    )
    governance.to_csv(TABLE_DIR / "indicator_governance_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(capability["household_type"], capability["capability_score"])
    ax.set_title("Capability Conversion")
    ax.set_ylabel("Composite capability score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "capability_conversion_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(care["group"], care["care_visibility_score"])
    ax.set_title("Care Visibility")
    ax.set_ylabel("Composite care visibility score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "care_visibility_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(subjective["community"], subjective["subjective_wellbeing_score"])
    ax.set_title("Subjective Well-Being")
    ax.set_ylabel("Composite subjective well-being score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "subjective_wellbeing_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(governance["system"], governance["governance_usefulness_score"])
    ax.set_title("Indicator Governance Usefulness")
    ax.set_ylabel("Composite governance score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "indicator_governance_python.png", dpi=300)
    plt.close(fig)

    print(capability[["household_type", "capability_score"]])
    print(care[["group", "total_work_hours", "care_visibility_score"]])
    print(subjective[["community", "subjective_wellbeing_score", "income_wellbeing_gap"]])
    print(governance[["system", "governance_usefulness_score"]])


if __name__ == "__main__":
    main()
