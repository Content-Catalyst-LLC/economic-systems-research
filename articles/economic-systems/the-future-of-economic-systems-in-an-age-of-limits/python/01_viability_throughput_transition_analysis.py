"""
Future viability, throughput pressure, transition capacity, and well-being measurement analysis.
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
    viability = pd.read_csv(PROCESSED_DIR / "future_viability.csv")
    throughput = pd.read_csv(PROCESSED_DIR / "throughput_pressure.csv")
    transition = pd.read_csv(PROCESSED_DIR / "transition_capacity.csv")
    wellbeing = pd.read_csv(PROCESSED_DIR / "wellbeing_measurement.csv")

    viability["future_viability_score"] = (
        0.22 * (1 - viability["ecological_pressure"])
        + 0.20 * viability["institutional_capacity"]
        + 0.18 * viability["social_inclusion"]
        + 0.16 * viability["resilience"]
        + 0.12 * viability["public_trust"]
        + 0.12 * viability["adaptive_learning"]
    )
    viability.to_csv(TABLE_DIR / "future_viability_results_python.csv", index=False)

    throughput["throughput_pressure"] = throughput["population"] * throughput["affluence"] * throughput["material_intensity"]
    throughput["wellbeing_per_throughput"] = throughput["wellbeing"] / throughput["throughput_pressure"]
    throughput["viable_throughput_score"] = (
        0.34 * throughput["wellbeing"]
        + 0.26 * throughput["inclusion"]
        + 0.22 * (1 - throughput["throughput_pressure"] / throughput["throughput_pressure"].max())
        + 0.18 * (1 - throughput["material_intensity"] / throughput["material_intensity"].max())
    )
    throughput.to_csv(TABLE_DIR / "throughput_pressure_results_python.csv", index=False)

    transition["transition_capacity_score"] = (
        0.18 * transition["public_investment"]
        + 0.18 * transition["policy_credibility"]
        + 0.16 * transition["technology"]
        + 0.16 * transition["social_trust"]
        + 0.16 * transition["implementation_capacity"]
        + 0.16 * transition["coordination"]
    )
    transition.to_csv(TABLE_DIR / "transition_capacity_results_python.csv", index=False)

    wellbeing["wellbeing_score"] = wellbeing[
        ["health", "security", "inclusion", "ecological_quality", "public_goods", "care", "time_balance"]
    ].mean(axis=1)
    wellbeing.to_csv(TABLE_DIR / "wellbeing_measurement_results_python.csv", index=False)

    datasets = [
        (viability, "scenario", "future_viability_score", "Future Viability", "future_viability_python.png"),
        (throughput, "scenario", "throughput_pressure", "Throughput Pressure", "throughput_pressure_python.png"),
        (transition, "scenario", "transition_capacity_score", "Transition Capacity", "transition_capacity_python.png"),
        (wellbeing, "scenario", "wellbeing_score", "Well-Being Beyond Output", "wellbeing_beyond_output_python.png"),
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

    print(viability[["scenario", "future_viability_score"]])
    print(throughput[["scenario", "throughput_pressure", "wellbeing_per_throughput", "viable_throughput_score"]])
    print(transition[["scenario", "transition_capacity_score"]])
    print(wellbeing[["scenario", "wellbeing_score"]])


if __name__ == "__main__":
    main()
