"""
Resilience, fragility, adaptive capacity, and shock-impact analysis.
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
    resilience = pd.read_csv(PROCESSED_DIR / "resilience_scenarios.csv")
    fragility = pd.read_csv(PROCESSED_DIR / "fragility_scenarios.csv")
    adaptive = pd.read_csv(PROCESSED_DIR / "adaptive_capacity.csv")
    shocks = pd.read_csv(PROCESSED_DIR / "shock_scenarios.csv")

    resilience["resilience_score"] = (
        0.18 * resilience["buffers"]
        + 0.18 * resilience["redundancy"]
        + 0.18 * resilience["coordination"]
        + 0.14 * resilience["trust"]
        + 0.16 * resilience["learning"]
        + 0.16 * resilience["recovery_capacity"]
    )
    resilience.to_csv(TABLE_DIR / "resilience_results_python.csv", index=False)

    fragility["fragility_score"] = (
        0.20 * fragility["leverage"]
        + 0.18 * fragility["concentration"]
        + 0.20 * fragility["exposure"]
        + 0.18 * fragility["underinvestment"]
        + 0.14 * fragility["inequality"]
        + 0.10 * fragility["political_fragmentation"]
    )
    fragility.to_csv(TABLE_DIR / "fragility_results_python.csv", index=False)

    adaptive["adaptive_capacity_score"] = (
        0.18 * adaptive["information"]
        + 0.18 * adaptive["fiscal_space"]
        + 0.16 * adaptive["skills"]
        + 0.16 * adaptive["flexibility"]
        + 0.16 * adaptive["legitimacy"]
        + 0.16 * adaptive["implementation_capacity"]
    )
    adaptive.to_csv(TABLE_DIR / "adaptive_capacity_results_python.csv", index=False)

    shocks["vulnerability"] = (
        0.26 * shocks["household_vulnerability"]
        + 0.22 * shocks["firm_vulnerability"]
        + 0.18 * (1 - shocks["public_capacity"])
        + 0.18 * (1 - shocks["infrastructure_integrity"])
        + 0.16 * (1 - shocks["recovery_speed"])
    )
    shocks["shock_impact"] = shocks["shock_magnitude"] * shocks["vulnerability"]
    shocks["recovery_capacity_score"] = (
        0.30 * shocks["public_capacity"]
        + 0.28 * shocks["infrastructure_integrity"]
        + 0.24 * shocks["recovery_speed"]
        + 0.18 * (1 - shocks["vulnerability"])
    )
    shocks.to_csv(TABLE_DIR / "shock_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(resilience["scenario"], resilience["resilience_score"])
    ax.set_title("Economic Resilience")
    ax.set_ylabel("Composite resilience score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "resilience_score_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(fragility["scenario"], fragility["fragility_score"])
    ax.set_title("Economic Fragility")
    ax.set_ylabel("Composite fragility score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "fragility_score_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(adaptive["scenario"], adaptive["adaptive_capacity_score"])
    ax.set_title("Adaptive Capacity")
    ax.set_ylabel("Composite adaptive-capacity score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "adaptive_capacity_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(shocks["shock"], shocks["shock_impact"])
    ax.set_title("Shock Impact")
    ax.set_ylabel("Shock magnitude × vulnerability")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "shock_impact_python.png", dpi=300)
    plt.close(fig)

    print(resilience[["scenario", "resilience_score"]])
    print(fragility[["scenario", "fragility_score"]])
    print(adaptive[["scenario", "adaptive_capacity_score"]])
    print(shocks[["shock", "vulnerability", "shock_impact", "recovery_capacity_score"]])


if __name__ == "__main__":
    main()
