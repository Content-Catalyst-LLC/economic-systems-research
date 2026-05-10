"""
Income distribution, redistribution, wealth concentration, and public-service-adjusted living standards.
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


def weighted_gini(values, weights):
    df = pd.DataFrame({"value": values, "weight": weights}).sort_values("value")
    df["cum_weight"] = df["weight"].cumsum()
    df["cum_value_weight"] = (df["value"] * df["weight"]).cumsum()
    total_weight = df["weight"].sum()
    total_value_weight = (df["value"] * df["weight"]).sum()
    if total_value_weight == 0:
        return 0
    cum_pop = df["cum_weight"] / total_weight
    cum_income = df["cum_value_weight"] / total_value_weight
    cum_pop_prev = pd.concat([pd.Series([0.0]), cum_pop.iloc[:-1]], ignore_index=True)
    cum_income_prev = pd.concat([pd.Series([0.0]), cum_income.iloc[:-1]], ignore_index=True)
    area = ((cum_income + cum_income_prev) * (cum_pop - cum_pop_prev) / 2).sum()
    return 1 - 2 * area


def main() -> None:
    income = pd.read_csv(PROCESSED_DIR / "income_distribution.csv")
    wealth = pd.read_csv(PROCESSED_DIR / "wealth_distribution.csv")

    income["disposable_income"] = income["market_income"] - income["taxes"] + income["transfers"]
    income["service_adjusted_income"] = income["disposable_income"] + income["public_service_value"]
    income["housing_adjusted_income"] = income["service_adjusted_income"] - income["housing_cost"] - income["debt_service"]
    income["market_income_share"] = income["market_income"] / income["market_income"].sum()
    income["disposable_income_share"] = income["disposable_income"] / income["disposable_income"].sum()
    income["service_adjusted_share"] = income["service_adjusted_income"] / income["service_adjusted_income"].sum()
    income["tax_rate"] = income["taxes"] / income["market_income"]
    income["transfer_rate"] = income["transfers"] / income["market_income"]
    income["housing_cost_burden"] = income["housing_cost"] / income["disposable_income"]
    income["redistributive_gain"] = income["disposable_income"] - income["market_income"]
    income["market_gini"] = weighted_gini(income["market_income"], income["population_share"])
    income["disposable_gini"] = weighted_gini(income["disposable_income"], income["population_share"])
    income["service_adjusted_gini"] = weighted_gini(income["service_adjusted_income"], income["population_share"])
    income.to_csv(TABLE_DIR / "income_redistribution_results_python.csv", index=False)

    wealth["net_wealth"] = wealth["wealth"] - wealth["debt"]
    wealth["wealth_share"] = wealth["wealth"] / wealth["wealth"].sum()
    wealth["net_wealth_share"] = wealth["net_wealth"] / wealth["net_wealth"].sum()
    wealth["next_period_wealth"] = wealth["wealth"] * (1 + wealth["asset_return"]) + wealth["inheritance_receipts"]
    wealth["next_period_wealth_share"] = wealth["next_period_wealth"] / wealth["next_period_wealth"].sum()
    wealth.to_csv(TABLE_DIR / "wealth_concentration_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(income["group"], income["market_income"], marker="o", label="Market income")
    ax.plot(income["group"], income["disposable_income"], marker="o", label="Disposable income")
    ax.plot(income["group"], income["service_adjusted_income"], marker="o", label="Service-adjusted income")
    ax.set_title("Market, Disposable, and Service-Adjusted Income")
    ax.set_ylabel("Income units")
    ax.tick_params(axis="x", rotation=35)
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "income_redistribution_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(income["group"], income["housing_cost_burden"])
    ax.set_title("Housing Cost Burden by Income Group")
    ax.set_ylabel("Housing cost / disposable income")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "housing_cost_burden_by_decile_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(wealth["group"], wealth["wealth_share"])
    ax.set_title("Wealth Share by Group")
    ax.set_ylabel("Share of total wealth")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "wealth_concentration_python.png", dpi=300)
    plt.close(fig)

    summary = pd.DataFrame([
        {"metric": "market_gini", "value": income["market_gini"].iloc[0]},
        {"metric": "disposable_gini", "value": income["disposable_gini"].iloc[0]},
        {"metric": "service_adjusted_gini", "value": income["service_adjusted_gini"].iloc[0]},
        {"metric": "redistributive_effect_market_to_disposable", "value": income["market_gini"].iloc[0] - income["disposable_gini"].iloc[0]},
        {"metric": "redistributive_effect_market_to_service_adjusted", "value": income["market_gini"].iloc[0] - income["service_adjusted_gini"].iloc[0]},
    ])
    summary.to_csv(TABLE_DIR / "redistribution_summary_python.csv", index=False)

    print(summary)
    print(income[["group", "market_income", "disposable_income", "service_adjusted_income", "housing_adjusted_income"]])
    print(wealth[["group", "wealth_share", "net_wealth_share", "next_period_wealth_share"]])


if __name__ == "__main__":
    main()
