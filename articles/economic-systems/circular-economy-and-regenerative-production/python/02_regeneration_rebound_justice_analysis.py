"""
Regenerative balance, circular infrastructure, labor models, rebound, and circular justice.
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
    regeneration = pd.read_csv(PROCESSED_DIR / "regenerative_production.csv")
    infrastructure = pd.read_csv(PROCESSED_DIR / "infrastructure_policy.csv")
    labor = pd.read_csv(PROCESSED_DIR / "labor_business_models.csv")
    rebound = pd.read_csv(PROCESSED_DIR / "rebound_scale_scenarios.csv")
    justice = pd.read_csv(PROCESSED_DIR / "circular_justice.csv")

    regeneration["regenerative_balance"] = regeneration["ecological_restoration"] - regeneration["ecological_degradation"]
    regeneration["regenerative_production_score"] = (
        0.20 * ((regeneration["regenerative_balance"] - regeneration["regenerative_balance"].min()) / (regeneration["regenerative_balance"].max() - regeneration["regenerative_balance"].min()))
        + 0.16 * regeneration["soil_health"]
        + 0.16 * regeneration["water_retention"]
        + 0.16 * regeneration["biodiversity"]
        + 0.16 * regeneration["local_capability"]
        + 0.16 * regeneration["stewardship_labor"]
    )
    regeneration.to_csv(TABLE_DIR / "regenerative_production_results_python.csv", index=False)

    infrastructure["circular_infrastructure_score"] = (
        0.12 * infrastructure["collection_systems"]
        + 0.12 * infrastructure["sorting_capacity"]
        + 0.16 * infrastructure["repair_hubs"]
        + 0.14 * infrastructure["reverse_logistics"]
        + 0.16 * infrastructure["product_standards"]
        + 0.12 * infrastructure["public_procurement"]
        + 0.10 * infrastructure["digital_product_passports"]
        + 0.08 * infrastructure["right_to_repair"]
    )
    infrastructure.to_csv(TABLE_DIR / "infrastructure_policy_results_python.csv", index=False)

    labor["circular_labor_model_score"] = (
        0.16 * labor["repair_jobs"]
        + 0.16 * labor["remanufacturing_jobs"]
        + 0.16 * labor["maintenance_capacity"]
        + 0.16 * labor["worker_skill_depth"]
        + 0.14 * labor["producer_responsibility"]
        + 0.12 * labor["durability_incentive"]
        + 0.10 * labor["local_value_capture"]
    )
    labor.to_csv(TABLE_DIR / "labor_business_model_results_python.csv", index=False)

    rebound["net_efficiency_gain"] = rebound["efficiency_gain"] - rebound["induced_additional_use"]
    rebound["scale_adjusted_circularity_score"] = (
        0.24 * rebound["circularity_ratio"]
        + 0.22 * rebound["scale_discipline"]
        + 0.20 * (1 - ((rebound["absolute_throughput_change"] - rebound["absolute_throughput_change"].min()) / (rebound["absolute_throughput_change"].max() - rebound["absolute_throughput_change"].min())))
        + 0.18 * ((rebound["net_efficiency_gain"] - rebound["net_efficiency_gain"].min()) / (rebound["net_efficiency_gain"].max() - rebound["net_efficiency_gain"].min()))
        + 0.16 * ((rebound["wellbeing_gain"] - rebound["wellbeing_gain"].min()) / (rebound["wellbeing_gain"].max() - rebound["wellbeing_gain"].min()))
    )
    rebound.to_csv(TABLE_DIR / "rebound_scale_results_python.csv", index=False)

    justice["circular_justice_score"] = (
        0.18 * justice["pollution_reduction"]
        + 0.18 * justice["job_quality"]
        + 0.16 * justice["local_value_capture"]
        + 0.16 * justice["decision_voice"]
        + 0.16 * (1 - justice["hazard_exposure"])
        + 0.16 * justice["access_to_repair"]
    )
    justice.to_csv(TABLE_DIR / "circular_justice_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(regeneration["scenario"], regeneration["regenerative_balance"])
    ax.set_title("Regenerative Balance")
    ax.set_ylabel("Ecological restoration - ecological degradation")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "regenerative_balance_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(infrastructure["policy_system"], infrastructure["circular_infrastructure_score"])
    ax.set_title("Circular Infrastructure and Policy Capacity")
    ax.set_ylabel("Composite infrastructure score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "circular_infrastructure_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(labor["model"], labor["circular_labor_model_score"])
    ax.set_title("Circular Labor and Business Model Score")
    ax.set_ylabel("Composite labor-model score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "circular_labor_model_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(rebound["scenario"], rebound["scale_adjusted_circularity_score"])
    ax.set_title("Scale-Adjusted Circularity")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "scale_adjusted_circularity_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(justice["group"], justice["circular_justice_score"])
    ax.set_title("Circular Justice")
    ax.set_ylabel("Composite justice score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "circular_justice_python.png", dpi=300)
    plt.close(fig)

    print(regeneration[["scenario", "regenerative_balance", "regenerative_production_score"]])
    print(infrastructure[["policy_system", "circular_infrastructure_score"]])
    print(labor[["model", "circular_labor_model_score"]])
    print(rebound[["scenario", "net_efficiency_gain", "scale_adjusted_circularity_score"]])
    print(justice[["group", "circular_justice_score"]])


if __name__ == "__main__":
    main()
