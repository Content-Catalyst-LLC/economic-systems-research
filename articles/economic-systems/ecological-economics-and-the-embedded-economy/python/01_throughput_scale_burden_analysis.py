"""
Throughput, scale, waste, sector footprints, and ecological burden.
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
    throughput = pd.read_csv(PROCESSED_DIR / "throughput_scenarios.csv")
    sectors = pd.read_csv(PROCESSED_DIR / "sector_footprints.csv")
    burdens = pd.read_csv(PROCESSED_DIR / "ecological_burdens.csv")
    strong = pd.read_csv(PROCESSED_DIR / "strong_sustainability.csv")

    throughput["throughput"] = throughput["energy_input"] + throughput["material_input"]
    throughput["waste_residual"] = throughput["throughput"] - throughput["recovered_throughput"]
    throughput["recovery_rate"] = throughput["recovered_throughput"] / throughput["throughput"]
    throughput["scale_ratio"] = throughput["economic_scale"] / throughput["ecological_capacity"]
    throughput["overshoot_risk"] = throughput["scale_ratio"].clip(lower=0)
    throughput.to_csv(TABLE_DIR / "throughput_scale_results_python.csv", index=False)

    sectors["material_footprint"] = sectors["domestic_extraction"] + sectors["imports"] - sectors["exports"]
    sectors["ecological_pressure_score"] = (
        0.20 * sectors["material_footprint"] / sectors["material_footprint"].max()
        + 0.18 * sectors["energy_intensity"]
        + 0.18 * sectors["water_pressure"]
        + 0.18 * sectors["land_pressure"]
        + 0.16 * sectors["waste_intensity"]
        + 0.10 * sectors["social_necessity"]
    )
    sectors.to_csv(TABLE_DIR / "sector_footprint_results_python.csv", index=False)

    burdens["ecological_burden_score"] = (
        0.24 * burdens["exposure"]
        + 0.18 * (1 - burdens["income_buffer"])
        + 0.18 * (1 - burdens["infrastructure"])
        + 0.18 * (1 - burdens["adaptive_capacity"])
        + 0.10 * (1 - burdens["political_voice"])
        + 0.12 * (1 - burdens["historical_responsibility"])
    )
    burdens.to_csv(TABLE_DIR / "ecological_burden_results_python.csv", index=False)

    strong["critical_natural_capital_score"] = (
        0.24 * (1 - strong["substitutability"])
        + 0.22 * strong["threshold_risk"]
        + 0.20 * strong["irreversibility"]
        + 0.14 * (1 - strong["regeneration_rate"])
        + 0.20 * strong["life_support_importance"]
    )
    strong.to_csv(TABLE_DIR / "strong_sustainability_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(throughput["scenario"], throughput["scale_ratio"])
    ax.set_title("Ecological Scale Ratio")
    ax.set_ylabel("Economic scale / ecological capacity")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "scale_ratio_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(throughput["scenario"], throughput["waste_residual"])
    ax.set_title("Waste Residual")
    ax.set_ylabel("Throughput - recovered throughput")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "waste_residual_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(sectors["sector"], sectors["ecological_pressure_score"])
    ax.set_title("Sector Ecological Pressure")
    ax.set_ylabel("Composite pressure score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "sector_ecological_pressure_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(burdens["group"], burdens["ecological_burden_score"])
    ax.set_title("Ecological Burden by Group")
    ax.set_ylabel("Composite burden score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "ecological_burden_python.png", dpi=300)
    plt.close(fig)

    print(throughput[["scenario", "throughput", "waste_residual", "recovery_rate", "scale_ratio", "wellbeing_index"]])
    print(sectors[["sector", "material_footprint", "ecological_pressure_score"]])
    print(burdens[["group", "ecological_burden_score"]])
    print(strong[["system", "critical_natural_capital_score"]])


if __name__ == "__main__":
    main()
