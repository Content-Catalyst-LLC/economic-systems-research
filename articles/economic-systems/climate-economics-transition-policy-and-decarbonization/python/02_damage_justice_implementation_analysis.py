"""
Climate damage, adaptation, just transition, hard-to-abate sectors, global equity, and implementation credibility.
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
    damage = pd.read_csv(PROCESSED_DIR / "damage_adaptation.csv")
    justice = pd.read_csv(PROCESSED_DIR / "just_transition.csv")
    hard = pd.read_csv(PROCESSED_DIR / "hard_to_abate.csv")
    equity = pd.read_csv(PROCESSED_DIR / "global_equity.csv")
    implementation = pd.read_csv(PROCESSED_DIR / "implementation_credibility.csv")

    damage["damage_risk_score"] = (
        0.18 * damage["temperature_stress"]
        + 0.18 * damage["flood_exposure"]
        + 0.12 * damage["wildfire_smoke"]
        + 0.18 * damage["economic_exposure"]
        + 0.18 * damage["vulnerability"]
        + 0.10 * (1 - damage["adaptation_capacity"])
        + 0.06 * (1 - damage["public_health_capacity"])
    )
    damage.to_csv(TABLE_DIR / "damage_adaptation_results_python.csv", index=False)

    justice["just_transition_score"] = (
        0.16 * (1 - justice["worker_exposure"])
        + 0.16 * justice["retraining"]
        + 0.18 * justice["regional_investment"]
        + 0.14 * justice["income_support"]
        + 0.14 * justice["public_services"]
        + 0.12 * justice["new_industry_pipeline"]
        + 0.10 * justice["labor_standards"]
    )
    justice.to_csv(TABLE_DIR / "just_transition_results_python.csv", index=False)

    hard["hard_to_abate_score"] = (
        0.22 * hard["process_emissions"]
        + 0.18 * hard["temperature_requirement"]
        + 0.20 * (1 - hard["technology_readiness"])
        + 0.14 * (1 - hard["procurement_leverage"])
        + 0.12 * (1 - hard["demand_reduction_potential"])
        + 0.14 * hard["carbon_capture_relevance"]
    )
    hard.to_csv(TABLE_DIR / "hard_to_abate_results_python.csv", index=False)

    equity["finance_obligation_score"] = (
        0.28 * equity["historic_responsibility"]
        + 0.18 * equity["current_emissions"]
        + 0.24 * equity["fiscal_capacity"]
        + 0.12 * equity["technology_capacity"]
        + 0.10 * equity["climate_vulnerability"]
        + 0.08 * equity["development_need"]
    )
    equity["support_need_score"] = (
        0.28 * equity["climate_vulnerability"]
        + 0.24 * equity["development_need"]
        + 0.18 * (1 - equity["fiscal_capacity"])
        + 0.14 * (1 - equity["technology_capacity"])
        + 0.10 * (1 - equity["historic_responsibility"])
        + 0.06 * equity["current_emissions"]
    )
    equity.to_csv(TABLE_DIR / "global_equity_results_python.csv", index=False)

    implementation["implementation_credibility_score"] = (
        0.16 * implementation["target_clarity"]
        + 0.20 * implementation["administrative_capacity"]
        + 0.18 * implementation["fiscal_commitment"]
        + 0.18 * implementation["policy_durability"]
        + 0.12 * implementation["public_trust"]
        + 0.16 * implementation["coordination_capacity"]
    )
    implementation.to_csv(TABLE_DIR / "implementation_credibility_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(damage["region"], damage["damage_risk_score"])
    ax.set_title("Climate Damage Risk")
    ax.set_ylabel("Composite risk score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "damage_risk_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(justice["community"], justice["just_transition_score"])
    ax.set_title("Just Transition Score")
    ax.set_ylabel("Composite just-transition score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "just_transition_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(hard["sector"], hard["hard_to_abate_score"])
    ax.set_title("Hard-to-Abate Sector Score")
    ax.set_ylabel("Composite difficulty score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "hard_to_abate_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(equity["country_group"], equity["support_need_score"])
    ax.set_title("Global Climate Support Need")
    ax.set_ylabel("Composite support-need score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "global_support_need_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(implementation["scenario"], implementation["implementation_credibility_score"])
    ax.set_title("Implementation Credibility")
    ax.set_ylabel("Composite credibility score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "implementation_credibility_python.png", dpi=300)
    plt.close(fig)

    print(damage[["region", "damage_risk_score"]])
    print(justice[["community", "just_transition_score"]])
    print(hard[["sector", "hard_to_abate_score"]])
    print(equity[["country_group", "finance_obligation_score", "support_need_score"]])
    print(implementation[["scenario", "implementation_credibility_score"]])


if __name__ == "__main__":
    main()
