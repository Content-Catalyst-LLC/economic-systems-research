"""
Sufficiency, finance dependence, decoupling, degrowth transition, and global justice.
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
    sufficiency = pd.read_csv(PROCESSED_DIR / "sufficiency.csv")
    finance = pd.read_csv(PROCESSED_DIR / "finance_growth_dependence.csv")
    decoupling = pd.read_csv(PROCESSED_DIR / "decoupling_rebound.csv")
    transition = pd.read_csv(PROCESSED_DIR / "degrowth_transition.csv")
    justice = pd.read_csv(PROCESSED_DIR / "global_justice.csv")

    sufficiency["sufficiency_ratio"] = sufficiency["needs_met"] / sufficiency["throughput_required"]
    sufficiency["social_sufficiency_score"] = (
        0.28 * sufficiency["needs_met"]
        + 0.22 * (1 - sufficiency["throughput_required"])
        + 0.16 * sufficiency["time_security"]
        + 0.14 * sufficiency["public_access"]
        + 0.10 * sufficiency["care_capacity"]
        + 0.10 * sufficiency["dignity"]
    )
    sufficiency.to_csv(TABLE_DIR / "sufficiency_results_python.csv", index=False)

    finance["finance_growth_dependence_score"] = (
        0.18 * finance["private_debt"]
        + 0.18 * finance["public_debt_pressure"]
        + 0.20 * finance["asset_valuation_pressure"]
        + 0.16 * finance["pension_return_dependency"]
        + 0.16 * finance["housing_speculation"]
        + 0.12 * (1 - finance["real_investment_alignment"])
    )
    finance.to_csv(TABLE_DIR / "finance_growth_dependence_results_python.csv", index=False)

    decoupling["net_efficiency_gain"] = decoupling["intensity_reduction"] - decoupling["additional_demand"]
    decoupling["absolute_decoupling_success"] = (decoupling["absolute_throughput_change"] < 0).astype(int)
    decoupling["transition_performance_score"] = (
        0.32 * ((decoupling["net_efficiency_gain"] - decoupling["net_efficiency_gain"].min()) / (decoupling["net_efficiency_gain"].max() - decoupling["net_efficiency_gain"].min()))
        + 0.28 * (1 - ((decoupling["absolute_throughput_change"] - decoupling["absolute_throughput_change"].min()) / (decoupling["absolute_throughput_change"].max() - decoupling["absolute_throughput_change"].min())))
        + 0.22 * ((decoupling["wellbeing_gain"] - decoupling["wellbeing_gain"].min()) / (decoupling["wellbeing_gain"].max() - decoupling["wellbeing_gain"].min()))
        + 0.18 * decoupling["absolute_decoupling_success"]
    )
    decoupling.to_csv(TABLE_DIR / "decoupling_rebound_results_python.csv", index=False)

    transition["degrowth_transition_score"] = (
        0.18 * transition["throughput_reduction"]
        + 0.20 * transition["redistribution"]
        + 0.20 * transition["public_services"]
        + 0.16 * transition["democratic_legitimacy"]
        + 0.14 * transition["macro_stabilization"]
        + 0.12 * transition["employment_security"]
    )
    transition.to_csv(TABLE_DIR / "degrowth_transition_results_python.csv", index=False)

    justice["excess_reduction_responsibility"] = (
        0.32 * justice["material_footprint"]
        + 0.28 * justice["historic_responsibility"]
        + 0.18 * justice["adaptive_capacity"]
        + 0.14 * justice["transition_finance_obligation"]
        + 0.08 * (1 - justice["basic_needs_gap"])
    )
    justice["development_priority_score"] = (
        0.34 * justice["development_need"]
        + 0.28 * justice["basic_needs_gap"]
        + 0.16 * (1 - justice["adaptive_capacity"])
        + 0.12 * (1 - justice["historic_responsibility"])
        + 0.10 * (1 - justice["material_footprint"])
    )
    justice.to_csv(TABLE_DIR / "global_justice_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(sufficiency["system"], sufficiency["sufficiency_ratio"])
    ax.set_title("Sufficiency Ratio")
    ax.set_ylabel("Needs met / throughput required")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "sufficiency_ratio_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(finance["system"], finance["finance_growth_dependence_score"])
    ax.set_title("Finance Growth Dependence")
    ax.set_ylabel("Composite finance-dependence score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "finance_growth_dependence_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(decoupling["scenario"], decoupling["absolute_throughput_change"])
    ax.axhline(0.0, linestyle="--")
    ax.set_title("Absolute Throughput Change")
    ax.set_ylabel("Change in total throughput")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "absolute_throughput_change_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(transition["scenario"], transition["degrowth_transition_score"])
    ax.set_title("Degrowth Transition Credibility")
    ax.set_ylabel("Composite transition score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "degrowth_transition_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(justice["country_group"], justice["development_priority_score"])
    ax.set_title("Development Priority")
    ax.set_ylabel("Composite development priority score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "global_development_priority_python.png", dpi=300)
    plt.close(fig)

    print(sufficiency[["system", "sufficiency_ratio", "social_sufficiency_score"]])
    print(finance[["system", "finance_growth_dependence_score"]])
    print(decoupling[["scenario", "net_efficiency_gain", "absolute_throughput_change", "transition_performance_score"]])
    print(transition[["scenario", "degrowth_transition_score"]])
    print(justice[["country_group", "excess_reduction_responsibility", "development_priority_score"]])


if __name__ == "__main__":
    main()
