"""
Governance regimes, justice burdens, resilience, strategic dependence, and substitution scenarios.
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
    governance = pd.read_csv(PROCESSED_DIR / "governance_regimes.csv")
    burdens = pd.read_csv(PROCESSED_DIR / "justice_burdens.csv")
    resilience = pd.read_csv(PROCESSED_DIR / "resilience_dependency.csv")
    substitution = pd.read_csv(PROCESSED_DIR / "substitution_efficiency.csv")

    governance["resource_governance_score"] = (
        0.14 * governance["secure_tenure"]
        + 0.16 * governance["monitoring"]
        + 0.16 * governance["participation"]
        + 0.14 * governance["enforcement"]
        + 0.16 * governance["adaptive_rules"]
        + 0.12 * governance["equity"]
        + 0.12 * governance["regeneration_alignment"]
    )
    governance.to_csv(TABLE_DIR / "governance_regime_results_python.csv", index=False)

    burdens["justice_burden_score"] = (
        0.24 * burdens["exposure"]
        + 0.18 * (1 - burdens["income_buffer"])
        + 0.18 * (1 - burdens["public_infrastructure"])
        + 0.16 * (1 - burdens["adaptive_capacity"])
        + 0.14 * (1 - burdens["political_voice"])
        + 0.10 * (1 - burdens["benefit_capture"])
    )
    burdens.to_csv(TABLE_DIR / "justice_burden_results_python.csv", index=False)

    resilience["ecological_resilience_score"] = (
        0.18 * resilience["diversity"]
        + 0.18 * resilience["regeneration"]
        + 0.16 * resilience["redundancy"]
        + 0.16 * resilience["governance"]
        + 0.12 * resilience["strategic_reserve"]
        + 0.10 * (1 - resilience["import_dependence"])
        + 0.10 * (1 - resilience["shock_exposure"])
    )
    resilience["strategic_dependency_score"] = (
        0.30 * resilience["import_dependence"]
        + 0.24 * resilience["shock_exposure"]
        + 0.16 * (1 - resilience["diversity"])
        + 0.16 * (1 - resilience["redundancy"])
        + 0.14 * (1 - resilience["strategic_reserve"])
    )
    resilience.to_csv(TABLE_DIR / "resilience_dependency_results_python.csv", index=False)

    substitution["technology_optimism_risk_score"] = (
        0.22 * substitution["rebound_effect"] / substitution["rebound_effect"].max()
        + 0.22 * substitution["ecological_irreplaceability"]
        + 0.18 * (1 - substitution["absolute_reduction"])
        + 0.14 * substitution["substitution_feasibility"]
        + 0.12 * (1 - substitution["innovation_quality"])
        + 0.12 * substitution["efficiency_gain"]
    )
    substitution["real_pressure_reduction_score"] = (
        0.30 * substitution["absolute_reduction"]
        + 0.22 * substitution["efficiency_gain"]
        + 0.18 * (1 - substitution["rebound_effect"])
        + 0.18 * substitution["innovation_quality"]
        + 0.12 * substitution["substitution_feasibility"]
    )
    substitution.to_csv(TABLE_DIR / "substitution_efficiency_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(governance["regime"], governance["resource_governance_score"])
    ax.set_title("Resource Governance Score")
    ax.set_ylabel("Composite governance score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "resource_governance_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(burdens["group"], burdens["justice_burden_score"])
    ax.set_title("Ecological Justice Burden")
    ax.set_ylabel("Composite burden score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "justice_burden_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(resilience["system"], resilience["strategic_dependency_score"])
    ax.set_title("Strategic Resource Dependence")
    ax.set_ylabel("Composite dependency score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "strategic_dependency_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(substitution["scenario"], substitution["real_pressure_reduction_score"])
    ax.set_title("Real Environmental Pressure Reduction")
    ax.set_ylabel("Composite reduction score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "pressure_reduction_python.png", dpi=300)
    plt.close(fig)

    print(governance[["regime", "resource_governance_score"]])
    print(burdens[["group", "justice_burden_score"]])
    print(resilience[["system", "ecological_resilience_score", "strategic_dependency_score"]])
    print(substitution[["scenario", "technology_optimism_risk_score", "real_pressure_reduction_score"]])


if __name__ == "__main__":
    main()
