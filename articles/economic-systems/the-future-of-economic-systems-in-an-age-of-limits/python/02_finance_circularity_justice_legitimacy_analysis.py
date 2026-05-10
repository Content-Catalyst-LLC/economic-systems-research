"""
Finance direction, circularity, technology governance, global asymmetry, and democratic legitimacy analysis.
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
    finance = pd.read_csv(PROCESSED_DIR / "finance_direction.csv")
    circular = pd.read_csv(PROCESSED_DIR / "circular_repair_systems.csv")
    technology = pd.read_csv(PROCESSED_DIR / "technology_governance.csv")
    asymmetry = pd.read_csv(PROCESSED_DIR / "global_asymmetry.csv")
    legitimacy = pd.read_csv(PROCESSED_DIR / "democratic_legitimacy.csv")

    finance["finance_direction_score"] = (
        0.18 * (1 - finance["fossil_exposure"])
        + 0.20 * finance["resilience_investment"]
        + 0.18 * finance["restoration"]
        + 0.18 * finance["public_goods_alignment"]
        + 0.12 * (1 - finance["short_termism"])
        + 0.14 * finance["adaptation_finance"]
    )
    finance.to_csv(TABLE_DIR / "finance_direction_results_python.csv", index=False)

    circular["circular_repair_score"] = (
        0.18 * circular["repairability"]
        + 0.16 * circular["reuse"]
        + 0.16 * circular["remanufacturing"]
        + 0.16 * circular["material_recovery"]
        + 0.16 * circular["maintenance_culture"]
        + 0.18 * circular["regeneration"]
    )
    circular.to_csv(TABLE_DIR / "circular_repair_results_python.csv", index=False)

    technology["technology_governance_score"] = (
        0.16 * technology["productivity"]
        + 0.18 * technology["distribution"]
        + 0.20 * technology["public_purpose"]
        + 0.16 * technology["energy_demand_control"]
        + 0.14 * technology["labor_transition_support"]
        + 0.16 * technology["capability_expansion"]
    )
    technology.to_csv(TABLE_DIR / "technology_governance_results_python.csv", index=False)

    asymmetry["excess_reduction_obligation"] = (
        0.30 * asymmetry["material_footprint"]
        + 0.28 * asymmetry["historic_responsibility"]
        + 0.16 * asymmetry["adaptive_capacity"]
        + 0.18 * asymmetry["finance_obligation"]
        + 0.08 * (1 - asymmetry["basic_needs_gap"])
    )
    asymmetry["development_priority_score"] = (
        0.34 * asymmetry["development_need"]
        + 0.28 * asymmetry["basic_needs_gap"]
        + 0.14 * (1 - asymmetry["adaptive_capacity"])
        + 0.12 * (1 - asymmetry["historic_responsibility"])
        + 0.12 * (1 - asymmetry["material_footprint"])
    )
    asymmetry.to_csv(TABLE_DIR / "global_asymmetry_results_python.csv", index=False)

    legitimacy["democratic_legitimacy_score"] = (
        0.18 * legitimacy["fairness"]
        + 0.18 * legitimacy["affordability"]
        + 0.16 * legitimacy["voice"]
        + 0.16 * legitimacy["trust"]
        + 0.18 * legitimacy["visible_benefit"]
        + 0.14 * legitimacy["policy_stability"]
    )
    legitimacy.to_csv(TABLE_DIR / "democratic_legitimacy_results_python.csv", index=False)

    datasets = [
        (finance, "portfolio", "finance_direction_score", "Finance Direction", "finance_direction_python.png"),
        (circular, "system", "circular_repair_score", "Circularity, Repair, and Regeneration", "circular_repair_python.png"),
        (technology, "scenario", "technology_governance_score", "Technology Governance", "technology_governance_python.png"),
        (asymmetry, "country_group", "development_priority_score", "Development Priority", "development_priority_python.png"),
        (legitimacy, "scenario", "democratic_legitimacy_score", "Democratic Transition Legitimacy", "democratic_legitimacy_python.png"),
    ]

    for df, label, value, title, filename in datasets:
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(df[label], df[value])
        ax.set_title(title)
        ax.set_ylabel(value.replace("_", " "))
        ax.tick_params(axis="x", rotation=35)
        fig.tight_layout()
        fig.savefig(FIGURE_DIR / filename, dpi=300)
        plt.close(fig)

    print(finance[["portfolio", "finance_direction_score"]])
    print(circular[["system", "circular_repair_score"]])
    print(technology[["scenario", "technology_governance_score"]])
    print(asymmetry[["country_group", "excess_reduction_obligation", "development_priority_score"]])
    print(legitimacy[["scenario", "democratic_legitimacy_score"]])


if __name__ == "__main__":
    main()
