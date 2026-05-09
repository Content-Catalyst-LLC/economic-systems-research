"""
Time poverty, public goods, and household resilience simulations.
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


def simulate_asset_depletion(row: pd.Series, monthly_shock: float, months: int = 24) -> pd.DataFrame:
    assets = row["liquid_assets"]
    records = []

    for month in range(months + 1):
        records.append({
            "household_group": row["household_group"],
            "month": month,
            "liquid_assets_remaining": max(assets, 0),
        })
        assets -= monthly_shock

    return pd.DataFrame(records)


def main() -> None:
    households = pd.read_csv(PROCESSED_DIR / "household_profiles.csv")
    public_goods = pd.read_csv(PROCESSED_DIR / "public_goods_scenarios.csv")

    households["rest_discretionary_hours"] = (
        24
        - households["paid_labor_hours"]
        - households["care_hours"]
        - households["commute_hours"]
        - households["household_admin_hours"]
    )
    households["time_poverty_flag"] = (households["rest_discretionary_hours"] < 8).astype(int)
    households["time_burden_hours"] = (
        households["paid_labor_hours"]
        + households["care_hours"]
        + households["commute_hours"]
        + households["household_admin_hours"]
    )

    households.to_csv(TABLE_DIR / "time_poverty_results_python.csv", index=False)

    public_records = []

    for _, household in households.iterrows():
        for _, scenario in public_goods.iterrows():
            transport_adjusted = household["transport"] * (1 - scenario["transport_private_cost_reduction"])
            health_adjusted = household["health"] * (1 - scenario["health_private_cost_reduction"])
            care_proxy_cost = household["care_hours"] * 120
            care_adjusted = care_proxy_cost * (1 - scenario["childcare_private_cost_reduction"])

            private_burden_reduction = (
                household["transport"]
                + household["health"]
                + care_proxy_cost
                - transport_adjusted
                - health_adjusted
                - care_adjusted
            )

            adjusted_rest = household["rest_discretionary_hours"] + scenario["time_savings_hours"]

            public_records.append({
                "household_group": household["household_group"],
                "scenario": scenario["scenario"],
                "population_weight": household["population_weight"],
                "private_burden_reduction": private_burden_reduction,
                "adjusted_rest_discretionary_hours": adjusted_rest,
                "institutional_support_index": scenario["institutional_support_index"],
                "public_goods_welfare_score": (
                    0.35 * scenario["institutional_support_index"]
                    + 0.35 * min(adjusted_rest / 10, 1)
                    + 0.30 * min(private_burden_reduction / 700, 1)
                ),
            })

    public_results = pd.DataFrame(public_records)
    public_results.to_csv(TABLE_DIR / "public_goods_welfare_results_python.csv", index=False)

    public_summary = (
        public_results.groupby("scenario")
        .apply(lambda g: pd.Series({
            "weighted_private_burden_reduction": (g["private_burden_reduction"] * g["population_weight"]).sum() / g["population_weight"].sum(),
            "weighted_rest_hours": (g["adjusted_rest_discretionary_hours"] * g["population_weight"]).sum() / g["population_weight"].sum(),
            "weighted_public_goods_welfare_score": (g["public_goods_welfare_score"] * g["population_weight"]).sum() / g["population_weight"].sum(),
        }))
        .reset_index()
    )
    public_summary.to_csv(TABLE_DIR / "public_goods_welfare_summary_python.csv", index=False)

    asset_paths = pd.concat(
        [simulate_asset_depletion(row, monthly_shock=450, months=24) for _, row in households.iterrows()],
        ignore_index=True,
    )
    asset_paths.to_csv(TABLE_DIR / "asset_depletion_paths_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(households["household_group"], households["rest_discretionary_hours"])
    ax.set_title("Rest and Discretionary Time by Household Group")
    ax.set_ylabel("Hours per day")
    ax.set_xlabel("Household group")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "time_poverty_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(public_summary["scenario"], public_summary["weighted_public_goods_welfare_score"])
    ax.set_title("Public Goods and Household Welfare Score")
    ax.set_ylabel("Weighted welfare score")
    ax.set_xlabel("Scenario")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "public_goods_welfare_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    for group, data in asset_paths.groupby("household_group"):
        ax.plot(data["month"], data["liquid_assets_remaining"], label=group)
    ax.set_title("Liquid Asset Depletion Under Monthly Shock")
    ax.set_xlabel("Month")
    ax.set_ylabel("Liquid assets remaining")
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "asset_depletion_paths_python.png", dpi=300)
    plt.close(fig)

    print(public_summary)


if __name__ == "__main__":
    main()
