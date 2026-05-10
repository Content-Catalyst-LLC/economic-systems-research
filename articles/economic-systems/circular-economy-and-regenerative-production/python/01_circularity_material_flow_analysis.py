"""
Circularity, material flows, product life, design quality, and value retention.
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
    material = pd.read_csv(PROCESSED_DIR / "material_flow_scenarios.csv")
    design = pd.read_csv(PROCESSED_DIR / "product_life_design.csv")
    pathways = pd.read_csv(PROCESSED_DIR / "value_retention_pathways.csv")

    material["circularity_ratio"] = material["recovered_material"] / material["total_material_input"]
    material["virgin_material_input"] = material["total_material_input"] - material["recovered_material"]
    material["waste_reduction_ratio"] = 1 - (material["residual_waste"] / material["total_throughput"])
    material["circular_performance_score"] = (
        0.28 * material["circularity_ratio"]
        + 0.24 * material["waste_reduction_ratio"]
        + 0.18 * (1 - material["virgin_extraction_pressure"])
        + 0.14 * (1 - material["leakage_risk"])
        + 0.16 * (1 - (material["total_throughput"] / material["total_throughput"].max()))
    )
    material.to_csv(TABLE_DIR / "material_flow_results_python.csv", index=False)

    design["product_life_extension"] = design["actual_product_life"] / design["baseline_product_life"]
    design["design_for_circularity_score"] = (
        0.18 * design["durability"]
        + 0.18 * design["repairability"]
        + 0.16 * design["modularity"]
        + 0.16 * design["disassembly_score"]
        + 0.14 * design["material_separability"]
        + 0.10 * (1 - design["proprietary_lock_in"])
        + 0.08 * (design["product_life_extension"] / design["product_life_extension"].max())
    )
    design.to_csv(TABLE_DIR / "product_life_design_results_python.csv", index=False)

    pathways["value_retention_score"] = (
        0.22 * pathways["material_retention"]
        + 0.18 * pathways["energy_retention"]
        + 0.18 * pathways["labor_value_retention"]
        + 0.20 * pathways["functional_retention"]
        + 0.10 * (1 - pathways["processing_intensity"])
        + 0.12 * (1 - pathways["quality_loss"])
    )
    pathways.to_csv(TABLE_DIR / "value_retention_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(material["scenario"], material["circularity_ratio"])
    ax.set_title("Circularity Ratio")
    ax.set_ylabel("Recovered material / total material input")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "circularity_ratio_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(material["scenario"], material["waste_reduction_ratio"])
    ax.set_title("Waste Reduction Ratio")
    ax.set_ylabel("1 - residual waste / throughput")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "waste_reduction_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(design["product"], design["design_for_circularity_score"])
    ax.set_title("Design for Circularity")
    ax.set_ylabel("Composite design score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "design_for_circularity_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(pathways["pathway"], pathways["value_retention_score"])
    ax.set_title("Value Retention by Circular Pathway")
    ax.set_ylabel("Composite value-retention score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "value_retention_python.png", dpi=300)
    plt.close(fig)

    print(material[["scenario", "circularity_ratio", "waste_reduction_ratio", "circular_performance_score"]])
    print(design[["product", "product_life_extension", "design_for_circularity_score"]])
    print(pathways[["pathway", "value_retention_score"]])


if __name__ == "__main__":
    main()
