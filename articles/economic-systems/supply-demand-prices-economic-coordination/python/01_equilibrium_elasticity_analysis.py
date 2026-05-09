"""
Solve linear supply-demand equilibrium and calculate elasticities.
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


def solve_equilibrium(a: float, b: float, c: float, d: float, markup_rate: float = 0.0) -> tuple[float, float]:
    competitive_price = (a - c) / (b + d)
    price = competitive_price * (1 + markup_rate)
    quantity = a - b * price
    return price, quantity


def qd(p, a, b):
    return a - b * p


def qs(p, c, d):
    return c + d * p


def main() -> None:
    scenarios = pd.read_csv(PROCESSED_DIR / "market_parameter_scenarios.csv")

    records = []
    for _, row in scenarios.iterrows():
        price, quantity = solve_equilibrium(row["a"], row["b"], row["c"], row["d"], row["markup_rate"])
        demand_elasticity = -row["b"] * (price / quantity)
        supply_elasticity = row["d"] * (price / quantity)
        marginal_social_cost_price = price + row["external_cost"]

        records.append({
            **row.to_dict(),
            "equilibrium_price": price,
            "equilibrium_quantity": quantity,
            "demand_elasticity": demand_elasticity,
            "supply_elasticity": supply_elasticity,
            "marginal_social_cost_price": marginal_social_cost_price,
            "social_cost_gap": marginal_social_cost_price - price,
        })

    results = pd.DataFrame(records)

    baseline = results.loc[results["scenario"] == "baseline"].iloc[0]
    results["price_change_from_baseline"] = results["equilibrium_price"] - baseline["equilibrium_price"]
    results["quantity_change_from_baseline"] = results["equilibrium_quantity"] - baseline["equilibrium_quantity"]

    results.to_csv(TABLE_DIR / "equilibrium_results_python.csv", index=False)
    results[[
        "market",
        "scenario",
        "equilibrium_price",
        "equilibrium_quantity",
        "demand_elasticity",
        "supply_elasticity",
        "price_change_from_baseline",
        "quantity_change_from_baseline",
    ]].to_csv(TABLE_DIR / "elasticity_results_python.csv", index=False)

    # Baseline and shock diagrams
    p = np.linspace(0, 90, 400)

    baseline_row = results[results["scenario"] == "baseline"].iloc[0]
    shock_row = results[results["scenario"] == "negative_supply_shock"].iloc[0]
    demand_row = results[results["scenario"] == "demand_expansion"].iloc[0]

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(p, qd(p, baseline_row["a"], baseline_row["b"]), label="Demand")
    ax.plot(p, qs(p, baseline_row["c"], baseline_row["d"]), label="Supply")
    ax.scatter(baseline_row["equilibrium_price"], baseline_row["equilibrium_quantity"], label="Equilibrium")
    ax.set_title("Baseline Supply and Demand Equilibrium")
    ax.set_xlabel("Price")
    ax.set_ylabel("Quantity")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "supply_demand_baseline_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(p, qd(p, baseline_row["a"], baseline_row["b"]), label="Demand")
    ax.plot(p, qs(p, baseline_row["c"], baseline_row["d"]), label="Supply")
    ax.plot(p, qs(p, shock_row["c"], shock_row["d"]), linestyle="--", label="Supply shock")
    ax.scatter([baseline_row["equilibrium_price"], shock_row["equilibrium_price"]],
               [baseline_row["equilibrium_quantity"], shock_row["equilibrium_quantity"]])
    ax.set_title("Negative Supply Shock")
    ax.set_xlabel("Price")
    ax.set_ylabel("Quantity")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "supply_shock_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(p, qd(p, baseline_row["a"], baseline_row["b"]), label="Demand")
    ax.plot(p, qd(p, demand_row["a"], demand_row["b"]), linestyle="--", label="Demand expansion")
    ax.plot(p, qs(p, baseline_row["c"], baseline_row["d"]), label="Supply")
    ax.scatter([baseline_row["equilibrium_price"], demand_row["equilibrium_price"]],
               [baseline_row["equilibrium_quantity"], demand_row["equilibrium_quantity"]])
    ax.set_title("Demand Expansion")
    ax.set_xlabel("Price")
    ax.set_ylabel("Quantity")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "demand_shift_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(results["scenario"], results["demand_elasticity"], label="Demand elasticity")
    ax.plot(results["scenario"], results["supply_elasticity"], marker="o", label="Supply elasticity")
    ax.set_title("Point Elasticities at Equilibrium")
    ax.set_ylabel("Elasticity")
    ax.tick_params(axis="x", rotation=35)
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "elasticity_profiles_python.png", dpi=300)
    plt.close(fig)

    print(results[["scenario", "equilibrium_price", "equilibrium_quantity", "demand_elasticity", "supply_elasticity"]])


if __name__ == "__main__":
    main()
