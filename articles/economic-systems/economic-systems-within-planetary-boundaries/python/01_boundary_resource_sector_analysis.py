"""
Boundary pressure, resource-use identities, sector pressure, and coupled-system analysis.
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
    boundaries = pd.read_csv(PROCESSED_DIR / "boundary_pressure.csv")
    resources = pd.read_csv(PROCESSED_DIR / "resource_use_identity.csv")
    sectors = pd.read_csv(PROCESSED_DIR / "sector_pressure.csv")
    coupled = pd.read_csv(PROCESSED_DIR / "coupled_systems.csv")

    boundaries["boundary_pressure_ratio"] = boundaries["economic_pressure"] / boundaries["earth_system_capacity"]
    boundaries["overshoot_gap"] = (boundaries["boundary_pressure_ratio"] - 1).clip(lower=0)
    boundaries["boundary_priority_score"] = (
        0.34 * (boundaries["boundary_pressure_ratio"] / boundaries["boundary_pressure_ratio"].max())
        + 0.20 * boundaries["irreversibility"]
        + 0.18 * boundaries["system_connectivity"]
        + 0.16 * (1 - boundaries["policy_response"])
        + 0.12 * (boundaries["overshoot_gap"] / boundaries["overshoot_gap"].max())
    )
    boundaries.to_csv(TABLE_DIR / "boundary_pressure_results_python.csv", index=False)

    resources["resource_use"] = resources["population"] * resources["affluence"] * resources["resource_intensity"]
    resources["resource_wellbeing_efficiency"] = resources["wellbeing_index"] / resources["resource_use"]
    resources["just_resource_performance"] = (
        0.34 * resources["wellbeing_index"]
        + 0.28 * resources["distribution_quality"]
        + 0.20 * (1 - resources["resource_use"] / resources["resource_use"].max())
        + 0.18 * (1 - resources["resource_intensity"] / resources["resource_intensity"].max())
    )
    resources.to_csv(TABLE_DIR / "resource_use_identity_results_python.csv", index=False)

    sectors["sector_pressure_score"] = (
        0.20 * sectors["climate"]
        + 0.18 * sectors["biosphere"]
        + 0.16 * sectors["land"]
        + 0.14 * sectors["freshwater"]
        + 0.14 * sectors["nutrients"]
        + 0.10 * sectors["novel_entities"]
        + 0.08 * sectors["social_necessity"]
    )
    sectors["transition_priority_score"] = sectors["sector_pressure_score"] * (1 - sectors["transition_readiness"])
    sectors.to_csv(TABLE_DIR / "sector_pressure_results_python.csv", index=False)

    coupled["coupled_pressure_score"] = (
        0.25 * coupled["energy_pressure"]
        + 0.25 * coupled["food_pressure"]
        + 0.20 * coupled["land_pressure"]
        + 0.18 * coupled["water_pressure"]
        + 0.07 * (1 - coupled["governance_integration"])
        + 0.05 * (1 - coupled["adaptation_capacity"])
    )
    coupled.to_csv(TABLE_DIR / "coupled_systems_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(boundaries["boundary"], boundaries["boundary_pressure_ratio"])
    ax.axhline(1.0, linestyle="--")
    ax.set_title("Boundary Pressure Ratio")
    ax.set_ylabel("Economic pressure / Earth-system capacity")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "boundary_pressure_ratio_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(resources["scenario"], resources["resource_use"])
    ax.set_title("Resource Use Identity")
    ax.set_ylabel("Population × affluence × resource intensity")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "resource_use_identity_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(sectors["sector"], sectors["sector_pressure_score"])
    ax.set_title("Sector Boundary Pressure")
    ax.set_ylabel("Composite pressure score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "sector_boundary_pressure_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(coupled["system"], coupled["coupled_pressure_score"])
    ax.set_title("Coupled System Pressure")
    ax.set_ylabel("Composite coupled pressure score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "coupled_system_pressure_python.png", dpi=300)
    plt.close(fig)

    print(boundaries[["boundary", "boundary_pressure_ratio", "overshoot_gap", "boundary_priority_score"]])
    print(resources[["scenario", "resource_use", "resource_wellbeing_efficiency", "just_resource_performance"]])
    print(sectors[["sector", "sector_pressure_score", "transition_priority_score"]])
    print(coupled[["system", "coupled_pressure_score"]])


if __name__ == "__main__":
    main()
