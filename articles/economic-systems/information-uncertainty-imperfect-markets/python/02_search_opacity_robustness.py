"""
Information search, consumer opacity, and robustness under deep uncertainty.
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
    search = pd.read_csv(PROCESSED_DIR / "information_search_scenarios.csv")
    uncertainty = pd.read_csv(PROCESSED_DIR / "uncertainty_scenarios.csv")
    consumers = pd.read_csv(PROCESSED_DIR / "consumer_complexity_scenarios.csv")

    search["total_information_cost"] = search["cost_information"] + search["time_cost"] + search["processing_cost"]
    search["net_information_value"] = search["benefit_information"] - search["total_information_cost"]
    best_info = search.loc[search["net_information_value"].idxmax()].copy()
    search.to_csv(TABLE_DIR / "information_search_results_python.csv", index=False)
    pd.DataFrame([best_info]).to_csv(TABLE_DIR / "best_information_search_level_python.csv", index=False)

    scenario_cols = ["good_case", "moderate_case", "bad_case", "transition_case", "systemic_crisis_case"]
    uncertainty["expected_equal_weight_payoff"] = uncertainty[scenario_cols].mean(axis=1)
    uncertainty["worst_case"] = uncertainty[scenario_cols].min(axis=1)
    uncertainty["payoff_range"] = uncertainty[scenario_cols].max(axis=1) - uncertainty[scenario_cols].min(axis=1)
    uncertainty["robustness_rank"] = uncertainty["worst_case"].rank(ascending=False, method="dense")
    uncertainty.to_csv(TABLE_DIR / "robustness_results_python.csv", index=False)

    consumers["effective_intelligibility"] = (
        0.35 * consumers["disclosure_quality"]
        + 0.25 * consumers["trust_index"]
        + 0.20 * (1 - consumers["complexity_index"])
        + 0.12 * (1 - consumers["hidden_fee_index"])
        + 0.08 * (1 - consumers["switching_cost_index"])
    )
    consumers["opacity_risk"] = 1 - consumers["effective_intelligibility"]
    consumers.to_csv(TABLE_DIR / "consumer_opacity_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(search["information_level"], search["benefit_information"], label="Benefit of information")
    ax.plot(search["information_level"], search["total_information_cost"], label="Total information cost")
    ax.plot(search["information_level"], search["net_information_value"], label="Net information value")
    ax.axvline(best_info["information_level"], linestyle="--", label="best search level")
    ax.set_title("Information Search: Benefit, Cost, and Net Value")
    ax.set_xlabel("Information level")
    ax.set_ylabel("Value")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "information_search_net_value_python.png", dpi=300)
    plt.close(fig)

    long_uncertainty = uncertainty.melt(
        id_vars="action",
        value_vars=scenario_cols,
        var_name="scenario",
        value_name="payoff",
    )
    pivot = long_uncertainty.pivot(index="action", columns="scenario", values="payoff")
    fig, ax = plt.subplots(figsize=(10, 5))
    pivot.plot(kind="bar", ax=ax)
    ax.set_title("Scenario Payoffs Under Deep Uncertainty")
    ax.set_ylabel("Payoff")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "robustness_scenario_payoffs_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(consumers["market"], consumers["opacity_risk"])
    ax.set_title("Consumer Market Opacity Risk")
    ax.set_ylabel("Opacity risk")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "consumer_opacity_python.png", dpi=300)
    plt.close(fig)

    print(search[["information_level", "net_information_value"]].head())
    print(uncertainty[["action", "expected_equal_weight_payoff", "worst_case", "robustness_rank"]])
    print(consumers[["market", "effective_intelligibility", "opacity_risk"]])


if __name__ == "__main__":
    main()
