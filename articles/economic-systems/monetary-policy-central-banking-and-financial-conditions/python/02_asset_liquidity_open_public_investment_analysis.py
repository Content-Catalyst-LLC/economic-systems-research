"""
Asset repricing, bank liquidity, open economy pressure, public debt service, and investment affordability.
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


def present_value(cash_flow: float, discount_rate: float, duration_years: int) -> float:
    return sum(cash_flow / ((1 + discount_rate) ** t) for t in range(1, duration_years + 1))


def main() -> None:
    assets = pd.read_csv(PROCESSED_DIR / "asset_valuation_scenarios.csv")
    liquidity = pd.read_csv(PROCESSED_DIR / "bank_liquidity_scenarios.csv")
    open_economy = pd.read_csv(PROCESSED_DIR / "open_economy_scenarios.csv")
    public_debt = pd.read_csv(PROCESSED_DIR / "public_debt_interaction_scenarios.csv")
    investment = pd.read_csv(PROCESSED_DIR / "sustainable_investment_scenarios.csv")

    assets["pv_before_rate_shock"] = assets.apply(lambda r: present_value(r["cash_flow"], r["discount_rate"], int(r["duration_years"])), axis=1)
    assets["pv_after_rate_shock"] = assets.apply(lambda r: present_value(r["cash_flow"], r["discount_rate"] + r["rate_shock"], int(r["duration_years"])), axis=1)
    assets["valuation_change_pct"] = (assets["pv_after_rate_shock"] - assets["pv_before_rate_shock"]) / assets["pv_before_rate_shock"]
    assets.to_csv(TABLE_DIR / "asset_valuation_results_python.csv", index=False)

    liquidity["liquidity_coverage_ratio"] = liquidity["liquid_assets"] / liquidity["short_term_outflows"]
    liquidity["stressed_outflows"] = liquidity["short_term_outflows"] * (1 + liquidity["deposit_outflow_shock"])
    liquidity["stressed_lcr"] = liquidity["liquid_assets"] / liquidity["stressed_outflows"]
    liquidity["liquidity_resilience_score"] = (
        0.42 * liquidity["stressed_lcr"].clip(upper=2.0) / 2.0
        + 0.28 * liquidity["collateral_quality"]
        + 0.30 * liquidity["central_bank_access"]
    )
    liquidity.to_csv(TABLE_DIR / "bank_liquidity_results_python.csv", index=False)

    open_economy["rate_differential"] = open_economy["domestic_rate"] - open_economy["world_rate"]
    open_economy["exchange_rate_pressure_score"] = (
        0.30 * open_economy["rate_differential"].clip(upper=0).abs() / open_economy["rate_differential"].clip(upper=0).abs().max()
        + 0.25 * open_economy["risk_premium"] / open_economy["risk_premium"].max()
        + 0.20 * open_economy["capital_flow_pressure"].clip(lower=0) / open_economy["capital_flow_pressure"].clip(lower=0).max()
        + 0.15 * open_economy["fx_debt_exposure"]
        + 0.10 * open_economy["import_price_exposure"]
    )
    open_economy.to_csv(TABLE_DIR / "open_economy_results_python.csv", index=False)

    public_debt["current_debt_service"] = public_debt["public_debt"] * public_debt["average_interest_rate"]
    public_debt["shock_adjusted_interest_rate"] = public_debt["average_interest_rate"] + public_debt["share_rolling_over"] * public_debt["rate_shock"]
    public_debt["shock_adjusted_debt_service"] = public_debt["public_debt"] * public_debt["shock_adjusted_interest_rate"]
    public_debt["debt_service_to_output"] = public_debt["shock_adjusted_debt_service"] / public_debt["output"]
    public_debt["investment_need_to_output"] = public_debt["public_investment_need"] / public_debt["output"]
    public_debt.to_csv(TABLE_DIR / "public_debt_interaction_results_python.csv", index=False)

    investment["post_shock_financing_cost"] = investment["financing_cost"] + investment["rate_shock"]
    investment["investment_affordability_gap"] = investment["expected_social_return"] - investment["post_shock_financing_cost"]
    investment["strategic_affordability_score"] = (
        0.45 * investment["investment_affordability_gap"].clip(lower=-0.05).add(0.05) / 0.10
        + 0.35 * investment["strategic_priority"]
        + 0.20 * investment["expected_social_return"] / investment["expected_social_return"].max()
    )
    investment.to_csv(TABLE_DIR / "sustainable_investment_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(assets["asset_class"], assets["valuation_change_pct"])
    ax.axhline(0, linestyle="--")
    ax.set_title("Asset Valuation Change After Rate Shock")
    ax.set_ylabel("Percent change")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "asset_repricing_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(liquidity["institution"], liquidity["stressed_lcr"])
    ax.axhline(1, linestyle="--", label="LCR = 1")
    ax.set_title("Stressed Liquidity Coverage Ratio")
    ax.set_ylabel("Liquid assets / stressed outflows")
    ax.tick_params(axis="x", rotation=35)
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "bank_liquidity_stress_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(open_economy["scenario"], open_economy["exchange_rate_pressure_score"])
    ax.set_title("Open-Economy Exchange-Rate Pressure Score")
    ax.set_ylabel("Pressure score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "open_economy_pressure_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(public_debt["scenario"], public_debt["debt_service_to_output"])
    ax.set_title("Shock-Adjusted Public Debt Service to Output")
    ax.set_ylabel("Debt service / output")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "public_debt_service_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(investment["investment_area"], investment["investment_affordability_gap"])
    ax.axhline(0, linestyle="--")
    ax.set_title("Sustainable Investment Affordability Gap")
    ax.set_ylabel("Expected social return minus financing cost")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "sustainable_investment_affordability_python.png", dpi=300)
    plt.close(fig)

    print(assets[["asset_class", "valuation_change_pct"]])
    print(liquidity[["institution", "stressed_lcr", "liquidity_resilience_score"]])
    print(open_economy[["scenario", "exchange_rate_pressure_score"]])
    print(public_debt[["scenario", "debt_service_to_output"]])
    print(investment[["investment_area", "investment_affordability_gap", "strategic_affordability_score"]])


if __name__ == "__main__":
    main()
