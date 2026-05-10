"""
Supply bottlenecks, market-power price amplification, and resilience policy scoring.
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
    bottlenecks = pd.read_csv(PROCESSED_DIR / "supply_bottleneck_scenarios.csv")
    market_power = pd.read_csv(PROCESSED_DIR / "market_power_price_amplification_scenarios.csv")
    resilience = pd.read_csv(PROCESSED_DIR / "resilience_policy_scenarios.csv")

    bottlenecks["effective_output_capacity"] = bottlenecks[
        ["capital_capacity", "labor_capacity", "energy_capacity", "logistics_capacity", "supply_availability"]
    ].min(axis=1)
    bottlenecks["bottleneck_gap"] = 1 - bottlenecks["effective_output_capacity"]
    bottlenecks["inflationary_bottleneck_pressure"] = (
        0.30 * (1 - bottlenecks["energy_capacity"])
        + 0.25 * (1 - bottlenecks["logistics_capacity"])
        + 0.25 * (1 - bottlenecks["supply_availability"])
        + 0.10 * (1 - bottlenecks["labor_capacity"])
        + 0.10 * (1 - bottlenecks["capital_capacity"])
    )
    bottlenecks.to_csv(TABLE_DIR / "supply_bottleneck_results_python.csv", index=False)

    market_power["baseline_pass_through"] = market_power["cost_shock"]
    market_power["amplified_price_change"] = (
        market_power["cost_shock"]
        + 0.45 * market_power["market_concentration_index"] * market_power["margin_expansion"]
        + 0.25 * market_power["demand_necessity_score"] * market_power["margin_expansion"]
    )
    market_power["price_amplification_score"] = market_power["amplified_price_change"] - market_power["baseline_pass_through"]
    market_power.to_csv(TABLE_DIR / "market_power_results_python.csv", index=False)

    resilience["long_run_resilience_score"] = (
        0.24 * resilience["energy_resilience"]
        + 0.22 * resilience["supply_diversification"]
        + 0.18 * resilience["household_protection"]
        + 0.18 * resilience["infrastructure_capacity"]
        + 0.18 * resilience["public_buffer_capacity"]
    )
    resilience["balanced_policy_score"] = (
        0.70 * resilience["long_run_resilience_score"]
        + 0.30 * resilience["near_term_disinflation"]
    )
    resilience.to_csv(TABLE_DIR / "resilience_policy_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(bottlenecks["scenario"], bottlenecks["inflationary_bottleneck_pressure"])
    ax.set_title("Inflationary Bottleneck Pressure")
    ax.set_ylabel("Composite pressure score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "supply_bottleneck_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(market_power["sector"], market_power["price_amplification_score"])
    ax.set_title("Price Amplification From Market Power")
    ax.set_ylabel("Amplification score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "market_power_amplification_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(resilience["policy"], resilience["balanced_policy_score"])
    ax.set_title("Balanced Inflation Resilience Policy Score")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "resilience_policy_python.png", dpi=300)
    plt.close(fig)

    print(bottlenecks[["scenario", "effective_output_capacity", "inflationary_bottleneck_pressure"]])
    print(market_power[["sector", "amplified_price_change", "price_amplification_score"]])
    print(resilience[["policy", "long_run_resilience_score", "balanced_policy_score"]])


if __name__ == "__main__":
    main()
