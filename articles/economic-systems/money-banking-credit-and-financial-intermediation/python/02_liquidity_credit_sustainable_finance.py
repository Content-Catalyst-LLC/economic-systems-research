"""
Liquidity stress, credit allocation, monetary hierarchy, and sustainable finance.
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
    liquidity = pd.read_csv(PROCESSED_DIR / "liquidity_stress_scenarios.csv")
    credit = pd.read_csv(PROCESSED_DIR / "credit_allocation_scenarios.csv")
    hierarchy = pd.read_csv(PROCESSED_DIR / "monetary_hierarchy_scenarios.csv")
    sustainable = pd.read_csv(PROCESSED_DIR / "sustainable_finance_scenarios.csv")

    liquidity["liquidity_coverage_ratio"] = liquidity["hqla"] / liquidity["net_cash_outflows"]
    liquidity["stress_liquidity_score"] = (
        0.50 * liquidity["liquidity_coverage_ratio"].clip(upper=2.0) / 2.0
        + 0.25 * (1 - liquidity["deposit_outflow_rate"])
        + 0.25 * liquidity["market_funding_rollover_rate"]
    )
    liquidity["liquidity_stress_flag"] = (liquidity["liquidity_coverage_ratio"] < 1.0).astype(int)
    liquidity.to_csv(TABLE_DIR / "liquidity_stress_results_python.csv", index=False)

    credit["developmental_credit_score"] = (
        0.34 * credit["productive_score"]
        + 0.28 * credit["resilience_score"]
        + 0.22 * credit["inclusion_score"]
        + 0.16 * (1 - credit["speculation_score"])
    )
    credit["weighted_developmental_contribution"] = credit["flow_share"] * credit["developmental_credit_score"]
    credit.to_csv(TABLE_DIR / "credit_allocation_results_python.csv", index=False)

    hierarchy["monetary_safety_index"] = (
        0.35 * hierarchy["safety_score"]
        + 0.30 * hierarchy["liquidity_score"]
        + 0.20 * hierarchy["public_backstop_score"]
        + 0.15 * hierarchy["collateral_acceptance_score"]
    )
    hierarchy.to_csv(TABLE_DIR / "monetary_hierarchy_results_python.csv", index=False)

    sustainable["sustainable_finance_score"] = (
        0.16 * sustainable["financial_return_score"]
        + 0.27 * sustainable["resilience_score"]
        + 0.27 * sustainable["ecological_alignment_score"]
        + 0.20 * sustainable["inclusion_score"]
        + 0.10 * (1 - sustainable["systemic_risk_score"])
    )
    sustainable.to_csv(TABLE_DIR / "sustainable_finance_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(liquidity["institution"], liquidity["liquidity_coverage_ratio"])
    ax.axhline(1.0, linestyle="--", label="coverage threshold")
    ax.set_title("Liquidity Coverage Under Stress")
    ax.set_ylabel("HQLA / net cash outflows")
    ax.tick_params(axis="x", rotation=35)
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "liquidity_stress_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(credit["credit_channel"], credit["flow_share"])
    ax.plot(credit["credit_channel"], credit["developmental_credit_score"], marker="o", label="Developmental score")
    ax.set_title("Credit Allocation: Flow Share and Developmental Score")
    ax.set_ylabel("Share / score")
    ax.tick_params(axis="x", rotation=35)
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "credit_allocation_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(hierarchy["claim"], hierarchy["monetary_safety_index"])
    ax.set_title("Monetary Hierarchy Safety Index")
    ax.set_ylabel("Safety index")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "monetary_hierarchy_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(sustainable["finance_use"], sustainable["sustainable_finance_score"])
    ax.set_title("Sustainable Finance Score")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "sustainable_finance_python.png", dpi=300)
    plt.close(fig)

    print(liquidity[["institution", "liquidity_coverage_ratio", "liquidity_stress_flag"]])
    print(credit[["credit_channel", "developmental_credit_score"]])
    print(sustainable[["finance_use", "sustainable_finance_score"]])


if __name__ == "__main__":
    main()
