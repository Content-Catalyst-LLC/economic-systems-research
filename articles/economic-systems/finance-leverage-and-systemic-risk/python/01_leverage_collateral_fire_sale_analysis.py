"""
Leverage amplification, collateral haircuts, funding gaps, and fire-sale spirals.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
FIGURE_DIR = BASE_DIR / "outputs" / "figures"
TABLE_DIR = BASE_DIR / "outputs" / "tables"

for directory in [FIGURE_DIR, TABLE_DIR]:
    directory.mkdir(parents=True, exist_ok=True)


def simulate_fire_sale(initial_price: float, initial_leverage: float, initial_sales: float, periods: int = 12) -> pd.DataFrame:
    price = initial_price
    leverage = initial_leverage
    sales = initial_sales
    rows = []

    for period in range(periods + 1):
        rows.append({
            "period": period,
            "price_index": price,
            "leverage": leverage,
            "forced_sales": sales,
        })
        price = max(35, price - 0.06 * sales - 0.35 * max(leverage - 10, 0))
        leverage = min(35, leverage * (100 / max(price, 1)) * 0.98)
        sales = max(0, 0.22 * max(leverage - 8, 0) + 0.18 * (100 - price))

    return pd.DataFrame(rows)


def main() -> None:
    institutions = pd.read_csv(PROCESSED_DIR / "institution_balance_sheets.csv")
    shocks = pd.read_csv(PROCESSED_DIR / "asset_shock_scenarios.csv")
    collateral = pd.read_csv(PROCESSED_DIR / "collateral_haircut_scenarios.csv")
    funding = pd.read_csv(PROCESSED_DIR / "funding_gap_scenarios.csv")

    institutions["equity"] = institutions["assets"] - institutions["debt"]
    institutions["leverage"] = institutions["assets"] / institutions["equity"]
    institutions["debt_to_equity"] = institutions["debt"] / institutions["equity"]
    institutions["capital_ratio"] = institutions["equity"] / institutions["assets"]

    records = []
    for _, inst in institutions.iterrows():
        for _, shock in shocks.iterrows():
            assets_after = inst["assets"] * (1 - shock["asset_shock"])
            equity_after = assets_after - inst["debt"]
            equity_loss_pct = (equity_after - inst["equity"]) / inst["equity"]
            records.append({
                "institution": inst["institution"],
                "shock_name": shock["shock_name"],
                "asset_shock": shock["asset_shock"],
                "initial_leverage": inst["leverage"],
                "equity_before": inst["equity"],
                "equity_after_shock": equity_after,
                "equity_loss_pct": equity_loss_pct,
                "insolvent_flag": int(equity_after < 0),
            })

    leverage_results = pd.DataFrame(records)
    leverage_results.to_csv(TABLE_DIR / "leverage_amplification_results_python.csv", index=False)

    collateral["borrowing_capacity_before"] = (1 - collateral["haircut_before"]) * collateral["collateral_value"]
    collateral["borrowing_capacity_after"] = (1 - collateral["haircut_after"]) * collateral["collateral_value"]
    collateral["haircut_funding_gap"] = collateral["outstanding_borrowing"] - collateral["borrowing_capacity_after"]
    collateral["margin_call_flag"] = (collateral["haircut_funding_gap"] > 0).astype(int)
    collateral.to_csv(TABLE_DIR / "collateral_haircut_results_python.csv", index=False)

    funding["raw_funding_gap"] = funding["short_term_liabilities"] - funding["liquid_assets"]
    funding["rollover_adjusted_gap"] = funding["short_term_liabilities"] * (1 - funding["rollover_rate"]) - funding["liquid_assets"]
    funding["backstop_adjusted_gap"] = funding["rollover_adjusted_gap"] * (1 - funding["emergency_liquidity_access"])
    funding["funding_stress_flag"] = (funding["backstop_adjusted_gap"] > 0).astype(int)
    funding.to_csv(TABLE_DIR / "funding_gap_results_python.csv", index=False)

    fire_sale = simulate_fire_sale(initial_price=100, initial_leverage=13, initial_sales=12, periods=12)
    fire_sale.to_csv(TABLE_DIR / "fire_sale_spiral_results_python.csv", index=False)

    pivot = leverage_results.pivot_table(
        index="asset_shock",
        columns="institution",
        values="equity_loss_pct",
        aggfunc="mean",
    )

    fig, ax = plt.subplots(figsize=(10, 5))
    pivot.plot(ax=ax)
    ax.set_title("Equity Loss Amplification Under Asset Shocks")
    ax.set_xlabel("Asset shock")
    ax.set_ylabel("Equity change (%)")
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "leverage_amplification_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(collateral["scenario"], collateral["haircut_funding_gap"])
    ax.axhline(0, linestyle="--")
    ax.set_title("Funding Gap From Collateral Haircut Shock")
    ax.set_ylabel("Funding gap")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "collateral_haircut_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(fire_sale["period"], fire_sale["price_index"], label="Price index")
    ax.plot(fire_sale["period"], fire_sale["leverage"], label="Leverage")
    ax.plot(fire_sale["period"], fire_sale["forced_sales"], label="Forced sales")
    ax.set_title("Stylized Fire-Sale Spiral")
    ax.set_xlabel("Period")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "fire_sale_spiral_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(funding["institution"], funding["backstop_adjusted_gap"])
    ax.axhline(0, linestyle="--")
    ax.set_title("Backstop-Adjusted Funding Gap")
    ax.set_ylabel("Funding gap")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "funding_gap_python.png", dpi=300)
    plt.close(fig)

    print(leverage_results.head())
    print(collateral[["scenario", "haircut_funding_gap", "margin_call_flag"]])
    print(funding[["institution", "backstop_adjusted_gap", "funding_stress_flag"]])


if __name__ == "__main__":
    main()
