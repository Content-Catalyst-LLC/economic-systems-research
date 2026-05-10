"""
Infrastructure readiness, skills systems, capture risk, regional clusters, and green industrial policy.
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
    infra = pd.read_csv(PROCESSED_DIR / "infrastructure_energy_scenarios.csv")
    skills = pd.read_csv(PROCESSED_DIR / "skills_labor_scenarios.csv")
    capture = pd.read_csv(PROCESSED_DIR / "capture_risk_scenarios.csv")
    clusters = pd.read_csv(PROCESSED_DIR / "regional_cluster_scenarios.csv")
    green = pd.read_csv(PROCESSED_DIR / "green_industrial_policy_scenarios.csv")

    infra["industrial_readiness_score"] = (
        0.20 * infra["transport_reliability"]
        + 0.18 * infra["port_access"]
        + 0.22 * infra["energy_reliability"]
        + 0.13 * infra["water_reliability"]
        + 0.14 * infra["digital_connectivity"]
        + 0.13 * infra["industrial_land_readiness"]
    )
    infra.to_csv(TABLE_DIR / "infrastructure_energy_results_python.csv", index=False)

    skills["upgrading_capacity_score"] = (
        0.22 * skills["technical_training_depth"]
        + 0.18 * skills["apprenticeship_capacity"]
        + 0.22 * skills["engineering_depth"]
        + 0.14 * skills["labor_security"]
        + 0.12 * skills["wage_progression"]
        + 0.12 * skills["learning_retention"]
    )
    skills.to_csv(TABLE_DIR / "skills_labor_results_python.csv", index=False)

    capture["capture_risk_score"] = (
        0.20 * capture["market_concentration"]
        + 0.20 * capture["lobbying_intensity"]
        + 0.20 * (1 - capture["evaluation_strength"])
        + 0.16 * capture["open_ended_support"]
        + 0.16 * capture["performance_shortfall"]
        + 0.08 * (1 - capture["public_disclosure"])
    )
    capture.to_csv(TABLE_DIR / "capture_risk_results_python.csv", index=False)

    clusters["cluster_depth_score"] = (
        0.20 * clusters["supplier_density"]
        + 0.18 * clusters["skills_depth"]
        + 0.20 * clusters["infrastructure_quality"]
        + 0.18 * clusters["research_linkage"]
        + 0.12 * clusters["regional_inclusion"]
        + 0.12 * clusters["export_connectivity"]
    )
    clusters.to_csv(TABLE_DIR / "regional_cluster_results_python.csv", index=False)

    green["green_industrial_score"] = (
        0.18 * green["productivity_gain"] / green["productivity_gain"].max()
        + 0.22 * green["emissions_reduction"] / green["emissions_reduction"].max()
        + 0.18 * green["domestic_linkage"]
        + 0.16 * green["employment_quality"]
        + 0.18 * green["resilience_value"]
        + 0.08 * (1 - green["material_risk"])
    )
    green.to_csv(TABLE_DIR / "green_industrial_policy_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(infra["region"], infra["industrial_readiness_score"])
    ax.set_title("Infrastructure and Energy Readiness")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "infrastructure_readiness_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(skills["scenario"], skills["upgrading_capacity_score"])
    ax.set_title("Skills and Labor Upgrading Capacity")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "skills_labor_upgrading_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(capture["program"], capture["capture_risk_score"])
    ax.set_title("Industrial Policy Capture Risk")
    ax.set_ylabel("Composite risk score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "capture_risk_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(clusters["cluster"], clusters["cluster_depth_score"])
    ax.set_title("Regional Cluster Depth")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "regional_cluster_depth_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(green["sector"], green["green_industrial_score"])
    ax.set_title("Green Industrial Policy Score")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "green_industrial_policy_python.png", dpi=300)
    plt.close(fig)

    print(infra[["region", "industrial_readiness_score"]])
    print(skills[["scenario", "upgrading_capacity_score"]])
    print(capture[["program", "capture_risk_score"]])
    print(clusters[["cluster", "cluster_depth_score"]])
    print(green[["sector", "green_industrial_score"]])


if __name__ == "__main__":
    main()
