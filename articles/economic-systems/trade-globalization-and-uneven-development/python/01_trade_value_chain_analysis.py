"""
Trade openness, export concentration, domestic value capture, global value-chain position, and terms-of-trade pressure.
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
    trade = pd.read_csv(PROCESSED_DIR / "trade_position_scenarios.csv")
    basket = pd.read_csv(PROCESSED_DIR / "export_basket_scenarios.csv")
    value_chain = pd.read_csv(PROCESSED_DIR / "value_chain_scenarios.csv")
    terms = pd.read_csv(PROCESSED_DIR / "terms_of_trade_scenarios.csv")

    trade["trade_openness"] = (trade["exports"] + trade["imports"]) / trade["output"]
    trade["trade_balance"] = trade["exports"] - trade["imports"]
    trade["import_dependence_score"] = (
        0.40 * trade["strategic_import_dependence"]
        + 0.30 * trade["intermediate_import_share"]
        + 0.30 * trade["energy_import_share"]
    )
    trade.to_csv(TABLE_DIR / "trade_position_results_python.csv", index=False)

    totals = basket.groupby("scenario")["export_value"].sum().rename("total_exports")
    basket = basket.merge(totals, on="scenario")
    basket["export_share"] = basket["export_value"] / basket["total_exports"]
    concentration = basket.groupby("scenario")["export_share"].apply(lambda s: (s ** 2).sum()).reset_index(name="export_concentration_index")
    concentration["diversification_score"] = 1 - concentration["export_concentration_index"]
    concentration.to_csv(TABLE_DIR / "export_concentration_results_python.csv", index=False)
    basket.to_csv(TABLE_DIR / "export_basket_results_python.csv", index=False)

    value_chain["domestic_value_capture"] = value_chain["domestic_value_added"] / value_chain["gross_exports"]
    value_chain["command_position_score"] = (
        0.24 * value_chain["domestic_value_capture"]
        + 0.20 * value_chain["lead_firm_control"]
        + 0.20 * value_chain["technology_control"]
        + 0.16 * value_chain["branding_control"]
        + 0.12 * (1 - value_chain["assembly_dependence"])
        + 0.08 * value_chain["upgrading_potential"]
    )
    value_chain.to_csv(TABLE_DIR / "value_chain_results_python.csv", index=False)

    terms["terms_of_trade"] = terms["export_price_index"] / terms["import_price_index"]
    terms["terms_of_trade_vulnerability"] = (
        0.34 * (1 - terms["terms_of_trade"] / terms["terms_of_trade"].max())
        + 0.24 * terms["commodity_share"]
        + 0.22 * terms["imported_food_energy_share"]
        + 0.20 * (1 - terms["stabilization_fund_strength"])
    )
    terms.to_csv(TABLE_DIR / "terms_of_trade_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(trade["scenario"], trade["trade_openness"])
    ax.set_title("Trade Openness by Scenario")
    ax.set_ylabel("(Exports + imports) / output")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "trade_openness_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(concentration["scenario"], concentration["export_concentration_index"])
    ax.set_title("Export Concentration")
    ax.set_ylabel("Sum of squared export shares")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "export_concentration_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(value_chain["scenario"], value_chain["domestic_value_capture"])
    ax.set_title("Domestic Value Capture in Gross Exports")
    ax.set_ylabel("Domestic value added / gross exports")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "domestic_value_capture_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(value_chain["scenario"], value_chain["command_position_score"])
    ax.set_title("Global Value-Chain Command Position")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "value_chain_position_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(terms["scenario"], terms["terms_of_trade_vulnerability"])
    ax.set_title("Terms-of-Trade Vulnerability")
    ax.set_ylabel("Composite vulnerability")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "terms_of_trade_vulnerability_python.png", dpi=300)
    plt.close(fig)

    print(trade[["scenario", "trade_openness", "trade_balance", "import_dependence_score"]])
    print(concentration)
    print(value_chain[["scenario", "domestic_value_capture", "command_position_score"]])
    print(terms[["scenario", "terms_of_trade", "terms_of_trade_vulnerability"]])


if __name__ == "__main__":
    main()
