"""
Strategic sectors, support conditionality, and development finance.
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
    sectors = pd.read_csv(PROCESSED_DIR / "strategic_sector_scenarios.csv")
    support = pd.read_csv(PROCESSED_DIR / "support_conditionality_scenarios.csv")
    finance = pd.read_csv(PROCESSED_DIR / "development_finance_scenarios.csv")

    sectors["sector_output_share"] = sectors["sector_output"] / sectors["total_output"]
    sectors["sector_productivity"] = sectors["sector_output"] / sectors["sector_labor"]
    sectors["export_ratio"] = sectors["sector_exports"] / sectors["sector_output"]
    sectors["strategic_priority_score"] = (
        0.22 * sectors["sector_output_share"] / sectors["sector_output_share"].max()
        + 0.22 * sectors["export_ratio"]
        + 0.22 * sectors["technology_depth"]
        + 0.18 * sectors["learning_potential"]
        + 0.16 * sectors["domestic_linkage_potential"]
    )
    sectors.to_csv(TABLE_DIR / "strategic_sector_results_python.csv", index=False)

    merged = support.merge(sectors[["sector", "sector_output"]], on="sector", how="left")
    merged["support_intensity"] = merged["public_support"] / merged["sector_output"]
    merged["performance_score"] = (
        0.22 * merged["productivity_gain"] / merged["productivity_gain"].max()
        + 0.18 * merged["export_growth"] / merged["export_growth"].max()
        + 0.18 * merged["employment_gain"] / merged["employment_gain"].max()
        + 0.18 * merged["local_supplier_share"]
        + 0.16 * merged["emissions_reduction"] / merged["emissions_reduction"].max()
        + 0.08 * (1 - merged["support_duration_years"] / merged["support_duration_years"].max())
    )
    merged["conditionality_gap"] = merged["performance_score"] - merged["support_intensity"] / merged["support_intensity"].max()
    merged["withdrawal_flag"] = (merged["conditionality_gap"] < -0.15).astype(int)
    merged.to_csv(TABLE_DIR / "support_conditionality_results_python.csv", index=False)

    finance["development_finance_alignment_score"] = (
        0.26 * finance["patient_credit_share"]
        + 0.24 * finance["industrial_credit_share"]
        + 0.20 * (1 - finance["speculative_credit_share"])
        + 0.12 * (1 - finance["fx_debt_exposure"])
        + 0.10 * finance["development_bank_capacity"]
        + 0.08 * finance["credit_monitoring_quality"]
    )
    finance.to_csv(TABLE_DIR / "development_finance_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(sectors["sector"], sectors["strategic_priority_score"])
    ax.set_title("Strategic Sector Priority Scores")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "sectoral_priority_scores_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(sectors["sector_productivity"], sectors["export_ratio"])
    for _, row in sectors.iterrows():
        ax.annotate(row["sector"], (row["sector_productivity"], row["export_ratio"]), fontsize=7)
    ax.set_title("Productivity and Export Performance by Strategic Sector")
    ax.set_xlabel("Sector productivity")
    ax.set_ylabel("Export ratio")
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "productivity_export_performance_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(merged["sector"], merged["performance_score"])
    ax.set_title("Support Conditionality Performance Score")
    ax.set_ylabel("Composite performance")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "support_conditionality_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(finance["scenario"], finance["development_finance_alignment_score"])
    ax.set_title("Development Finance Alignment")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "development_finance_alignment_python.png", dpi=300)
    plt.close(fig)

    print(sectors[["sector", "sector_output_share", "sector_productivity", "export_ratio", "strategic_priority_score"]])
    print(merged[["sector", "support_intensity", "performance_score", "conditionality_gap", "withdrawal_flag"]])
    print(finance[["scenario", "development_finance_alignment_score"]])


if __name__ == "__main__":
    main()
