"""
Poverty rates, poverty gaps, multidimensional deprivation, capability, and economic inclusion.
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
    household = pd.read_csv(PROCESSED_DIR / "household_poverty_scenarios.csv")
    deprivation = pd.read_csv(PROCESSED_DIR / "multidimensional_deprivation.csv")
    capability = pd.read_csv(PROCESSED_DIR / "capability_scenarios.csv")
    inclusion = pd.read_csv(PROCESSED_DIR / "inclusion_scenarios.csv")

    household["poverty_status"] = household["income"] < household["poverty_line"]
    household["poverty_gap"] = (household["poverty_line"] - household["income"]).clip(lower=0)
    household["normalized_poverty_gap"] = household["poverty_gap"] / household["poverty_line"]
    household["post_cost_income"] = household["income"] - household["housing_cost"] - household["debt_service"] - household["health_cost"]
    household["vulnerability_score"] = (
        0.24 * (1 - household["savings"] / household["savings"].max())
        + 0.22 * (household["debt_service"] / household["income"])
        + 0.22 * (household["housing_cost"] / household["income"])
        + 0.14 * (household["health_cost"] / household["income"])
        + 0.18 * household["shock_exposure"]
    )
    household.to_csv(TABLE_DIR / "household_poverty_results_python.csv", index=False)

    poverty_summary = pd.DataFrame([
        {"metric": "poverty_rate", "value": household["poverty_status"].mean()},
        {"metric": "average_poverty_gap_population", "value": household["poverty_gap"].sum() / len(household)},
        {"metric": "average_normalized_gap_among_poor", "value": household.loc[household["poverty_status"], "normalized_poverty_gap"].mean()},
        {"metric": "average_vulnerability_score", "value": household["vulnerability_score"].mean()},
    ])
    poverty_summary.to_csv(TABLE_DIR / "poverty_summary_python.csv", index=False)

    deprivation_columns = [
        "health_deprivation",
        "education_deprivation",
        "housing_deprivation",
        "sanitation_deprivation",
        "food_deprivation",
        "transport_deprivation",
        "digital_deprivation",
        "safety_deprivation",
        "institutional_exclusion",
    ]
    deprivation["multidimensional_deprivation_score"] = deprivation[deprivation_columns].mean(axis=1)
    deprivation.to_csv(TABLE_DIR / "multidimensional_deprivation_results_python.csv", index=False)

    capability["capability_score"] = (
        0.18 * capability["income_score"]
        + 0.17 * capability["health_score"]
        + 0.17 * capability["education_score"]
        + 0.14 * capability["mobility_score"]
        + 0.12 * capability["safety_score"]
        + 0.10 * capability["time_score"]
        + 0.12 * capability["institutional_access"]
    )
    capability["conversion_condition_score"] = capability[
        ["health_score", "education_score", "mobility_score", "safety_score", "time_score", "institutional_access"]
    ].mean(axis=1)
    capability["real_freedom_proxy"] = capability["income_score"] * capability["conversion_condition_score"]
    capability.to_csv(TABLE_DIR / "capability_results_python.csv", index=False)

    inclusion["inclusion_score"] = (
        0.16 * inclusion["work_access"]
        + 0.14 * inclusion["finance_access"]
        + 0.18 * inclusion["service_access"]
        + 0.16 * inclusion["infrastructure_access"]
        + 0.12 * inclusion["digital_access"]
        + 0.10 * inclusion["legal_recognition"]
        + 0.14 * inclusion["participation_security"]
    )
    inclusion.to_csv(TABLE_DIR / "inclusion_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(household["household"], household["normalized_poverty_gap"])
    ax.set_title("Normalized Poverty Gap by Household")
    ax.set_ylabel("Gap / poverty line")
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "poverty_gap_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(deprivation["community"], deprivation["multidimensional_deprivation_score"])
    ax.set_title("Multidimensional Deprivation")
    ax.set_ylabel("Average deprivation score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "multidimensional_deprivation_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(capability["scenario"], capability["capability_score"])
    ax.set_title("Capability Score")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "capability_score_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(inclusion["scenario"], inclusion["inclusion_score"])
    ax.set_title("Economic Inclusion Score")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "inclusion_score_python.png", dpi=300)
    plt.close(fig)

    print(poverty_summary)
    print(deprivation[["community", "multidimensional_deprivation_score"]])
    print(capability[["scenario", "capability_score", "conversion_condition_score", "real_freedom_proxy"]])
    print(inclusion[["scenario", "inclusion_score"]])


if __name__ == "__main__":
    main()
