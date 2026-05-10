"""
Sector coordination, public utilities, industrial policy, crisis coordination, and sustainable transition.
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
    sectors = pd.read_csv(PROCESSED_DIR / "sector_coordination.csv")
    utilities = pd.read_csv(PROCESSED_DIR / "public_utilities.csv")
    industrial = pd.read_csv(PROCESSED_DIR / "industrial_policy.csv")
    crisis = pd.read_csv(PROCESSED_DIR / "crisis_transition_globalization.csv")

    sectors["public_coordination_need"] = (
        0.18 * sectors["planning_fit"]
        + 0.16 * sectors["public_ownership_fit"]
        + 0.18 * sectors["regulation_need"]
        + 0.16 * sectors["social_rights_need"]
        + 0.16 * sectors["network_interdependence"]
        + 0.16 * sectors["public_good_character"]
    )
    sectors["market_coordination_usefulness"] = (
        0.70 * sectors["market_fit"]
        + 0.15 * (1 - sectors["network_interdependence"])
        + 0.15 * (1 - sectors["public_good_character"])
    )
    sectors.to_csv(TABLE_DIR / "sector_coordination_results_python.csv", index=False)

    utilities["utility_public_purpose_score"] = (
        0.18 * utilities["universal_access"]
        + 0.18 * utilities["affordability"]
        + 0.16 * utilities["maintenance_investment"]
        + 0.14 * utilities["democratic_accountability"]
        + 0.14 * utilities["service_reliability"]
        + 0.10 * (1 - utilities["profit_extraction_pressure"])
        + 0.10 * utilities["regional_equity"]
    )
    utilities.to_csv(TABLE_DIR / "public_utilities_results_python.csv", index=False)

    industrial["industrial_policy_score"] = (
        0.18 * industrial["public_investment"]
        + 0.14 * industrial["sector_targeting"]
        + 0.16 * industrial["learning_policy"]
        + 0.14 * industrial["supplier_development"]
        + 0.14 * industrial["public_procurement"]
        + 0.12 * industrial["performance_discipline"]
        + 0.12 * industrial["green_transition_alignment"]
    )
    industrial.to_csv(TABLE_DIR / "industrial_policy_results_python.csv", index=False)

    crisis["crisis_coordination_score"] = (
        0.20 * crisis["public_planning"]
        + 0.18 * crisis["infrastructure_depth"]
        + 0.18 * crisis["fiscal_capacity"]
        + 0.16 * crisis["administrative_speed"]
        + 0.14 * crisis["social_protection"]
        + 0.14 * crisis["democratic_legitimacy"]
    )
    crisis["sustainable_transition_score"] = (
        0.18 * crisis["public_planning"]
        + 0.18 * crisis["infrastructure_depth"]
        + 0.14 * crisis["fiscal_capacity"]
        + 0.16 * crisis["social_protection"]
        + 0.20 * crisis["ecological_targets"]
        + 0.14 * crisis["democratic_legitimacy"]
    )
    crisis["globalization_constraint_score"] = (
        0.60 * crisis["external_finance_constraint"]
        + 0.20 * (1 - crisis["fiscal_capacity"])
        + 0.20 * (1 - crisis["public_planning"])
    )
    crisis.to_csv(TABLE_DIR / "crisis_transition_globalization_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(sectors["sector"], sectors["public_coordination_need"])
    ax.set_title("Public Coordination Need by Sector")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "sector_public_coordination_need_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(utilities["utility"], utilities["utility_public_purpose_score"])
    ax.set_title("Public Utility Purpose Score")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "public_utilities_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(industrial["scenario"], industrial["industrial_policy_score"])
    ax.set_title("Industrial Policy Capacity")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "industrial_policy_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(crisis["scenario"], crisis["sustainable_transition_score"])
    ax.set_title("Sustainable Transition Coordination")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "sustainable_transition_python.png", dpi=300)
    plt.close(fig)

    print(sectors[["sector", "public_coordination_need", "market_coordination_usefulness"]])
    print(utilities[["utility", "utility_public_purpose_score"]])
    print(industrial[["scenario", "industrial_policy_score"]])
    print(crisis[["scenario", "crisis_coordination_score", "sustainable_transition_score", "globalization_constraint_score"]])


if __name__ == "__main__":
    main()
