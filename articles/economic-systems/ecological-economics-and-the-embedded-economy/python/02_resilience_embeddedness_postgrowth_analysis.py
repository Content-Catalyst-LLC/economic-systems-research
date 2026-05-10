"""
Embeddedness, commons governance, resilience, and post-growth scenarios.
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
    embedded = pd.read_csv(PROCESSED_DIR / "embeddedness_scenarios.csv")
    resilience = pd.read_csv(PROCESSED_DIR / "resilience_commons.csv")
    postgrowth = pd.read_csv(PROCESSED_DIR / "postgrowth_scenarios.csv")

    embedded["embeddedness_score"] = (
        0.18 * embedded["ecology_integrity"]
        + 0.18 * embedded["care_capacity"]
        + 0.16 * embedded["public_institutions"]
        + 0.14 * embedded["infrastructure_maintenance"]
        + 0.14 * embedded["cultural_reciprocity"]
        + 0.10 * (1 - embedded["market_dependence"])
        + 0.10 * embedded["community_resilience"]
    )
    embedded.to_csv(TABLE_DIR / "embeddedness_results_python.csv", index=False)

    resilience["resilience_score"] = (
        0.16 * resilience["diversity"]
        + 0.14 * resilience["redundancy"]
        + 0.16 * resilience["regeneration"]
        + 0.16 * resilience["governance"]
        + 0.12 * resilience["maintenance"]
        + 0.12 * resilience["learning"]
        + 0.08 * resilience["monitoring"]
        + 0.06 * resilience["participation"]
    )
    resilience["commons_governance_score"] = (
        0.18 * resilience["governance"]
        + 0.16 * resilience["monitoring"]
        + 0.16 * resilience["participation"]
        + 0.16 * resilience["learning"]
        + 0.18 * resilience["regeneration"]
        + 0.16 * resilience["maintenance"]
    )
    resilience.to_csv(TABLE_DIR / "resilience_commons_results_python.csv", index=False)

    postgrowth["net_throughput_pressure"] = (
        postgrowth["throughput_growth"] - postgrowth["efficiency_gain"] + postgrowth["rebound_effect"]
    )
    postgrowth["postgrowth_viability_score"] = (
        0.24 * postgrowth["wellbeing_change"].add(0.05) / postgrowth["wellbeing_change"].add(0.05).max()
        + 0.22 * (1 - postgrowth["inequality_pressure"])
        + 0.22 * postgrowth["public_services"]
        + 0.18 * (1 - postgrowth["net_throughput_pressure"].rank(pct=True))
        + 0.14 * (postgrowth["efficiency_gain"] / postgrowth["efficiency_gain"].max())
    )
    postgrowth.to_csv(TABLE_DIR / "postgrowth_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(embedded["scenario"], embedded["embeddedness_score"])
    ax.set_title("Embedded Economy Score")
    ax.set_ylabel("Composite embeddedness score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "embeddedness_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(resilience["system"], resilience["resilience_score"])
    ax.set_title("Socio-Ecological Resilience")
    ax.set_ylabel("Composite resilience score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "resilience_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(resilience["system"], resilience["commons_governance_score"])
    ax.set_title("Commons Governance")
    ax.set_ylabel("Composite governance score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "commons_governance_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(postgrowth["scenario"], postgrowth["postgrowth_viability_score"])
    ax.set_title("Post-Growth Viability")
    ax.set_ylabel("Composite viability score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "postgrowth_viability_python.png", dpi=300)
    plt.close(fig)

    print(embedded[["scenario", "embeddedness_score"]])
    print(resilience[["system", "resilience_score", "commons_governance_score"]])
    print(postgrowth[["scenario", "net_throughput_pressure", "postgrowth_viability_score"]])


if __name__ == "__main__":
    main()
