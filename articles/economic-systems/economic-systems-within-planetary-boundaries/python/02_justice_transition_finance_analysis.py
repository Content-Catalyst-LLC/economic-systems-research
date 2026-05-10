"""
Justice, transition capacity, finance direction, and boundary-aware accounting.
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
    justice = pd.read_csv(PROCESSED_DIR / "ecological_space_justice.csv")
    transition = pd.read_csv(PROCESSED_DIR / "transition_capacity.csv")
    finance = pd.read_csv(PROCESSED_DIR / "finance_direction.csv")
    accounting = pd.read_csv(PROCESSED_DIR / "boundary_accounting.csv")

    justice["ecological_space_stress"] = (
        0.28 * justice["resource_claim"]
        + 0.22 * justice["historic_pressure"]
        + 0.20 * justice["harm_exposure"]
        + 0.12 * (1 - justice["adaptive_capacity"])
        + 0.10 * (1 - justice["voice"])
        + 0.08 * justice["development_need"]
    )
    justice["justice_adjusted_sustainability"] = (
        0.32 * justice["development_need"]
        + 0.26 * (1 - justice["harm_exposure"])
        + 0.20 * justice["adaptive_capacity"]
        + 0.12 * justice["voice"]
        + 0.10 * (1 - justice["historic_pressure"])
    )
    justice.to_csv(TABLE_DIR / "ecological_space_justice_results_python.csv", index=False)

    transition["transition_capacity_score"] = (
        0.20 * transition["state_capacity"]
        + 0.18 * transition["public_investment"]
        + 0.18 * transition["social_legitimacy"]
        + 0.16 * transition["technological_capability"]
        + 0.14 * transition["coordination"]
        + 0.14 * transition["adaptive_governance"]
    )
    transition.to_csv(TABLE_DIR / "transition_capacity_results_python.csv", index=False)

    finance["finance_direction_score"] = (
        0.18 * (1 - finance["fossil_exposure"])
        + 0.20 * finance["restoration_investment"]
        + 0.20 * finance["resilience_investment"]
        + 0.16 * finance["circular_materials"]
        + 0.16 * finance["public_goods_alignment"]
        + 0.10 * (1 - finance["short_term_return_pressure"])
    )
    finance.to_csv(TABLE_DIR / "finance_direction_results_python.csv", index=False)

    accounting["boundary_aware_progress"] = (
        0.30 * accounting["wellbeing"]
        + 0.22 * accounting["inclusion"]
        + 0.20 * accounting["natural_capital"]
        + 0.12 * (1 - accounting["material_throughput"])
        + 0.12 * (1 - accounting["ecological_pressure"])
        + 0.04 * ((accounting["gdp_growth"] - accounting["gdp_growth"].min()) / (accounting["gdp_growth"].max() - accounting["gdp_growth"].min()))
    )
    accounting.to_csv(TABLE_DIR / "boundary_accounting_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(justice["group"], justice["ecological_space_stress"])
    ax.set_title("Ecological Space Stress")
    ax.set_ylabel("Composite stress score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "ecological_space_stress_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(transition["scenario"], transition["transition_capacity_score"])
    ax.set_title("Transition Capacity")
    ax.set_ylabel("Composite transition capacity score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "transition_capacity_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(finance["portfolio"], finance["finance_direction_score"])
    ax.set_title("Finance Direction Toward Safe Operating Space")
    ax.set_ylabel("Composite finance direction score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "finance_direction_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(accounting["scenario"], accounting["boundary_aware_progress"])
    ax.set_title("Boundary-Aware Progress")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "boundary_aware_progress_python.png", dpi=300)
    plt.close(fig)

    print(justice[["group", "ecological_space_stress", "justice_adjusted_sustainability"]])
    print(transition[["scenario", "transition_capacity_score"]])
    print(finance[["portfolio", "finance_direction_score"]])
    print(accounting[["scenario", "boundary_aware_progress"]])


if __name__ == "__main__":
    main()
