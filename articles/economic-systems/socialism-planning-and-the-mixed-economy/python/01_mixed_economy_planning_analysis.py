"""
Mixed-economy composition, planning capacity, and decommodification.
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
    mixed = pd.read_csv(PROCESSED_DIR / "mixed_economy_scenarios.csv")
    planning = pd.read_csv(PROCESSED_DIR / "planning_capacity.csv")
    decommodification = pd.read_csv(PROCESSED_DIR / "decommodification_scenarios.csv")

    mixed["mixed_economy_total"] = (
        mixed["market_allocation"]
        + mixed["public_planning"]
        + mixed["public_provision"]
        + mixed["regulation_rights"]
    )
    mixed["public_purpose_score"] = (
        0.20 * mixed["public_planning"]
        + 0.20 * mixed["public_provision"]
        + 0.16 * mixed["regulation_rights"]
        + 0.16 * mixed["public_ownership_share"]
        + 0.14 * mixed["social_rights_strength"]
        + 0.14 * mixed["social_need_weight"]
    )
    mixed["profit_dominance_score"] = (
        0.46 * mixed["market_allocation"]
        + 0.34 * mixed["private_profit_weight"]
        + 0.20 * (1 - mixed["social_rights_strength"])
    )
    mixed.to_csv(TABLE_DIR / "mixed_economy_results_python.csv", index=False)

    planning["planning_capacity_score"] = (
        0.18 * planning["state_capacity"]
        + 0.16 * planning["data_quality"]
        + 0.16 * planning["institutional_reach"]
        + 0.16 * planning["feedback_quality"]
        + 0.16 * planning["democratic_accountability"]
        + 0.10 * planning["coordination_authority"]
        + 0.08 * planning["implementation_speed"]
    )
    planning.to_csv(TABLE_DIR / "planning_capacity_results_python.csv", index=False)

    decommodification["decommodification_score"] = (
        0.18 * decommodification["healthcare_access"]
        + 0.16 * decommodification["education_access"]
        + 0.16 * decommodification["housing_security"]
        + 0.14 * decommodification["childcare_support"]
        + 0.12 * decommodification["public_transport"]
        + 0.12 * decommodification["social_insurance"]
        + 0.12 * decommodification["guaranteed_access"]
    )
    decommodification.to_csv(TABLE_DIR / "decommodification_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(mixed["scenario"], mixed["public_purpose_score"])
    ax.set_title("Public Purpose in Mixed-Economy Scenarios")
    ax.set_ylabel("Composite public-purpose score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "mixed_economy_public_purpose_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(planning["scenario"], planning["planning_capacity_score"])
    ax.set_title("Planning Capacity")
    ax.set_ylabel("Composite planning score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "planning_capacity_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(decommodification["scenario"], decommodification["decommodification_score"])
    ax.set_title("Decommodification")
    ax.set_ylabel("Composite decommodification score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "decommodification_python.png", dpi=300)
    plt.close(fig)

    print(mixed[["scenario", "public_purpose_score", "profit_dominance_score"]])
    print(planning[["scenario", "planning_capacity_score"]])
    print(decommodification[["scenario", "decommodification_score"]])


if __name__ == "__main__":
    main()
