"""
Maintenance backlog, ownership claims, finance direction, and sustainable investment.
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


def build_backlog_paths(group: pd.DataFrame) -> pd.DataFrame:
    group = group.sort_values("period")
    backlog = float(group["initial_backlog"].iloc[0])
    rows = []

    for _, row in group.iterrows():
        rows.append({
            "scenario": row["scenario"],
            "period": int(row["period"]) - 1,
            "maintenance_backlog": backlog,
            "new_maintenance_need": row["new_maintenance_need"],
            "actual_maintenance": row["actual_maintenance"],
        })
        backlog = backlog + row["new_maintenance_need"] - row["actual_maintenance"]

    rows.append({
        "scenario": group["scenario"].iloc[0],
        "period": int(group["period"].max()),
        "maintenance_backlog": backlog,
        "new_maintenance_need": 0,
        "actual_maintenance": 0,
    })

    return pd.DataFrame(rows)


def main() -> None:
    maintenance = pd.read_csv(PROCESSED_DIR / "maintenance_scenarios.csv")
    ownership = pd.read_csv(PROCESSED_DIR / "ownership_distribution_scenarios.csv")
    finance = pd.read_csv(PROCESSED_DIR / "finance_direction_scenarios.csv")
    sustainable = pd.read_csv(PROCESSED_DIR / "sustainable_investment_scenarios.csv")

    backlog_paths = pd.concat(
        [build_backlog_paths(group) for _, group in maintenance.groupby("scenario")],
        ignore_index=True,
    )
    backlog_paths.to_csv(TABLE_DIR / "maintenance_backlog_results_python.csv", index=False)

    ownership["capital_income_share"] = ownership["profit_share"] + ownership["rent_share"]
    ownership["public_capacity_share"] = ownership["tax_public_share"] + ownership["public_reinvestment_share"]
    ownership["labor_to_capital_claim_ratio"] = ownership["wage_share"] / ownership["capital_income_share"]
    ownership.to_csv(TABLE_DIR / "ownership_claims_results_python.csv", index=False)

    finance["developmental_allocation_score"] = (
        0.35 * finance["productive_capacity_score"]
        + 0.35 * finance["resilience_score"]
        + 0.15 * (1 - finance["speculation_score"])
        + 0.15 * (1 - finance["extraction_score"])
    )
    finance["weighted_development_contribution"] = finance["flow_share"] * finance["developmental_allocation_score"]
    finance.to_csv(TABLE_DIR / "finance_direction_results_python.csv", index=False)

    sustainable["sustainable_investment_score"] = (
        0.18 * sustainable["financial_return_score"]
        + 0.26 * sustainable["resilience_score"]
        + 0.24 * sustainable["ecological_alignment_score"]
        + 0.22 * sustainable["public_value_score"]
        + 0.10 * sustainable["maintenance_score"]
    )
    sustainable.to_csv(TABLE_DIR / "sustainable_investment_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    for scenario, group in backlog_paths.groupby("scenario"):
        ax.plot(group["period"], group["maintenance_backlog"], label=scenario)
    ax.set_title("Maintenance Backlog Paths")
    ax.set_xlabel("Period")
    ax.set_ylabel("Maintenance backlog")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "maintenance_backlog_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(ownership["scenario"], ownership["labor_to_capital_claim_ratio"])
    ax.set_title("Labor-to-Capital Claim Ratio")
    ax.set_ylabel("Wage share / capital income share")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "ownership_claims_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(finance["finance_channel"], finance["flow_share"])
    ax.plot(finance["finance_channel"], finance["developmental_allocation_score"], marker="o", label="Developmental score")
    ax.set_title("Finance Direction: Flow Share and Developmental Score")
    ax.set_ylabel("Share / score")
    ax.tick_params(axis="x", rotation=35)
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "finance_direction_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(sustainable["project"], sustainable["sustainable_investment_score"])
    ax.set_title("Sustainable Investment Score")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "sustainable_investment_score_python.png", dpi=300)
    plt.close(fig)

    print(backlog_paths.tail())
    print(ownership[["scenario", "labor_to_capital_claim_ratio"]])
    print(sustainable[["project", "sustainable_investment_score"]])


if __name__ == "__main__":
    main()
