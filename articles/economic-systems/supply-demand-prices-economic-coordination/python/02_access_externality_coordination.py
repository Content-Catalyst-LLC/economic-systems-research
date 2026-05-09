"""
Effective demand, market access, external costs, and coordination gaps.
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
    access = pd.read_csv(PROCESSED_DIR / "market_access_groups.csv")
    external = pd.read_csv(PROCESSED_DIR / "external_cost_scenarios.csv")

    access["effective_demand"] = (
        0.30 * access["need_index"]
        + 0.30 * access["income_command"]
        + 0.18 * access["credit_access"]
        + 0.17 * access["institutional_access"]
        + 0.05 * (1 - access["price_burden"])
    )
    access["unmet_need_gap"] = access["need_index"] - access["effective_demand"]
    access["market_exclusion_flag"] = (access["unmet_need_gap"] > 0.25).astype(int)
    access["weighted_unmet_need"] = access["unmet_need_gap"] * access["population_weight"]
    access["weighted_effective_demand"] = access["effective_demand"] * access["population_weight"]

    access_summary = pd.DataFrame([{
        "population_weighted_effective_demand": access["weighted_effective_demand"].sum() / access["population_weight"].sum(),
        "population_weighted_unmet_need": access["weighted_unmet_need"].sum(),
        "population_share_market_excluded": (access["market_exclusion_flag"] * access["population_weight"]).sum(),
    }])

    external["marginal_social_cost"] = external["private_price"] + external["marginal_external_cost"]
    external["net_social_value_adjustment"] = external["public_good_benefit"] - external["marginal_external_cost"]
    external["social_cost_gap"] = external["marginal_social_cost"] - external["private_price"]

    access.to_csv(TABLE_DIR / "market_access_metrics_python.csv", index=False)
    access_summary.to_csv(TABLE_DIR / "market_access_summary_python.csv", index=False)
    external.to_csv(TABLE_DIR / "social_cost_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(access["group"], access["need_index"], label="Need")
    ax.plot(access["group"], access["effective_demand"], marker="o", label="Effective demand")
    ax.set_title("Need and Effective Market Demand")
    ax.set_ylabel("Index")
    ax.tick_params(axis="x", rotation=35)
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "effective_demand_access_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(external["sector"], external["private_price"], label="Private price")
    ax.plot(external["sector"], external["marginal_social_cost"], marker="o", label="Marginal social cost")
    ax.set_title("Private Price and Marginal Social Cost")
    ax.set_ylabel("Price / cost index")
    ax.tick_params(axis="x", rotation=35)
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "social_cost_gap_python.png", dpi=300)
    plt.close(fig)

    print(access_summary)
    print(external[["sector", "private_price", "marginal_social_cost", "social_cost_gap"]])


if __name__ == "__main__":
    main()
