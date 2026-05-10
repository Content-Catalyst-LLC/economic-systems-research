"""
Regime comparison, distribution, financialization, labor systems, and corporate governance.
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
    regimes = pd.read_csv(PROCESSED_DIR / "regime_scenarios.csv")
    finance = pd.read_csv(PROCESSED_DIR / "financialization_scenarios.csv")
    labor = pd.read_csv(PROCESSED_DIR / "labor_skill_systems.csv")
    governance = pd.read_csv(PROCESSED_DIR / "corporate_governance.csv")

    regimes["profit"] = regimes["revenue"] - regimes["cost"]
    regimes["wage_share"] = regimes["wages"] / regimes["output"]
    regimes["profit_share"] = regimes["profit"] / regimes["output"]
    regimes["institutional_advantage_score"] = (
        0.20 * regimes["finance_patience"]
        + 0.20 * regimes["labor_coordination"]
        + 0.18 * regimes["welfare_buffer"]
        + 0.18 * regimes["state_coordination"]
        + 0.12 * regimes["innovation_radical"]
        + 0.12 * regimes["innovation_incremental"]
    )
    regimes.to_csv(TABLE_DIR / "regime_distribution_results_python.csv", index=False)

    finance["financialization_score"] = (
        0.20 * finance["asset_price_intensity"]
        + 0.18 * finance["household_debt"]
        + 0.18 * finance["corporate_leverage"]
        + 0.18 * finance["shareholder_payout_pressure"]
        + 0.14 * finance["buyback_intensity"]
        + 0.12 * finance["speculative_pressure"]
    )
    finance["productive_finance_score"] = (
        0.44 * finance["productive_investment"]
        + 0.20 * (1 - finance["speculative_pressure"])
        + 0.18 * (1 - finance["shareholder_payout_pressure"])
        + 0.18 * (1 - finance["asset_price_intensity"])
    )
    finance.to_csv(TABLE_DIR / "financialization_results_python.csv", index=False)

    labor["labor_coordination_score"] = (
        0.18 * labor["employment_protection"]
        + 0.20 * labor["collective_bargaining"]
        + 0.16 * labor["union_density"]
        + 0.14 * labor["vocational_training"]
        + 0.14 * labor["firm_specific_skills"]
        + 0.10 * labor["wage_compression"]
        + 0.08 * labor["general_skills"]
    )
    labor.to_csv(TABLE_DIR / "labor_skill_results_python.csv", index=False)

    governance["stakeholder_governance_score"] = (
        0.18 * (1 - governance["short_term_pressure"])
        + 0.18 * governance["stakeholder_voice"]
        + 0.16 * governance["worker_representation"]
        + 0.16 * governance["patient_capital"]
        + 0.14 * governance["reinvestment_orientation"]
        + 0.10 * governance["supplier_coordination"]
        + 0.08 * governance["community_accountability"]
    )
    governance.to_csv(TABLE_DIR / "corporate_governance_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(regimes["regime"], regimes["wage_share"])
    ax.set_title("Wage Share by Capitalist Regime")
    ax.set_ylabel("Wages / output")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "wage_share_by_regime_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(regimes["regime"], regimes["institutional_advantage_score"])
    ax.set_title("Comparative Institutional Advantage")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "institutional_advantage_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(finance["scenario"], finance["financialization_score"])
    ax.set_title("Financialization Score")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "financialization_score_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(labor["system"], labor["labor_coordination_score"])
    ax.set_title("Labor Coordination and Skill Formation")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "labor_coordination_python.png", dpi=300)
    plt.close(fig)

    print(regimes[["regime", "profit", "wage_share", "profit_share", "institutional_advantage_score"]])
    print(finance[["scenario", "financialization_score", "productive_finance_score"]])
    print(labor[["system", "labor_coordination_score"]])
    print(governance[["governance", "stakeholder_governance_score"]])


if __name__ == "__main__":
    main()
