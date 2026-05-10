"""
Real rates, debt-service stress, policy reaction functions, and financial conditions.
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
    policy = pd.read_csv(PROCESSED_DIR / "policy_rate_scenarios.csv")
    debt = pd.read_csv(PROCESSED_DIR / "debt_service_scenarios.csv")
    conditions = pd.read_csv(PROCESSED_DIR / "financial_conditions_scenarios.csv")

    policy["real_rate"] = policy["nominal_rate"] - policy["expected_inflation"]
    policy["policy_rate_rule"] = (
        policy["neutral_rate"]
        + policy["a_inflation"] * policy["inflation_gap"]
        + policy["b_output"] * policy["output_gap"]
    )
    policy["stance_gap"] = policy["nominal_rate"] - policy["policy_rate_rule"]
    policy.to_csv(TABLE_DIR / "policy_rate_results_python.csv", index=False)

    debt["debt_service_ratio"] = debt["debt_service"] / debt["income"]
    debt["additional_debt_service"] = debt["debt_stock"] * debt["repricing_share"] * debt["rate_shock"] / 12
    debt["post_shock_debt_service"] = debt["debt_service"] + debt["additional_debt_service"]
    debt["post_shock_dsr"] = debt["post_shock_debt_service"] / debt["income"]
    debt["monetary_exposure_score"] = (
        0.45 * debt["post_shock_dsr"].clip(upper=0.55) / 0.55
        + 0.35 * debt["repricing_share"]
        + 0.20 * debt["rate_shock"] / debt["rate_shock"].max()
    )
    debt.to_csv(TABLE_DIR / "debt_service_results_python.csv", index=False)

    conditions["financial_conditions_index"] = (
        conditions["policy_rate"]
        + conditions["credit_spread"]
        + conditions["exchange_rate_pressure"]
        + conditions["lending_tightness"] * 0.08
        + conditions["market_liquidity_stress"] * 0.08
        - conditions["equity_price_change"] * 0.18
    )
    conditions["credit_restriction_score"] = (
        0.28 * conditions["credit_spread"] / conditions["credit_spread"].max()
        + 0.28 * conditions["lending_tightness"]
        + 0.24 * conditions["market_liquidity_stress"]
        + 0.20 * conditions["equity_price_change"].clip(upper=0).abs() / conditions["equity_price_change"].clip(upper=0).abs().max()
    )
    conditions.to_csv(TABLE_DIR / "financial_conditions_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(policy["scenario"], policy["real_rate"])
    ax.axhline(0, linestyle="--")
    ax.set_title("Real Interest Rates by Monetary Scenario")
    ax.set_ylabel("Nominal rate minus expected inflation")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "real_rates_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(debt["borrower_group"], debt["post_shock_dsr"])
    ax.set_title("Post-Shock Debt-Service Ratios")
    ax.set_ylabel("Debt service / income")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "debt_service_stress_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(conditions["scenario"], conditions["financial_conditions_index"])
    ax.set_title("Composite Financial Conditions Index")
    ax.set_ylabel("Composite restraint score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "financial_conditions_index_python.png", dpi=300)
    plt.close(fig)

    print(policy[["scenario", "real_rate", "policy_rate_rule", "stance_gap"]])
    print(debt[["borrower_group", "post_shock_dsr", "monetary_exposure_score"]])
    print(conditions[["scenario", "financial_conditions_index", "credit_restriction_score"]])


if __name__ == "__main__":
    main()
