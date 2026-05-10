"""
Aggregate demand, output gaps, business-cycle phases, multipliers, and Okun-style unemployment response.
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
    demand = pd.read_csv(PROCESSED_DIR / "aggregate_demand_scenarios.csv")
    cycle = pd.read_csv(PROCESSED_DIR / "business_cycle_phase_scenarios.csv")
    fiscal = pd.read_csv(PROCESSED_DIR / "fiscal_stabilization_scenarios.csv")
    inflation = pd.read_csv(PROCESSED_DIR / "inflation_unemployment_policy_scenarios.csv")

    demand["output"] = demand["consumption"] + demand["investment"] + demand["government_spending"] + demand["net_exports"]
    demand["output_gap"] = (demand["output"] - demand["potential_output"]) / demand["potential_output"]
    demand["consumption_share"] = demand["consumption"] / demand["output"]
    demand["investment_share"] = demand["investment"] / demand["output"]
    demand["government_share"] = demand["government_spending"] / demand["output"]
    demand["net_exports_share"] = demand["net_exports"] / demand["output"]
    demand.to_csv(TABLE_DIR / "aggregate_demand_results_python.csv", index=False)

    cycle["output_growth"] = cycle["output_index"].pct_change().fillna(0)
    cycle["employment_growth"] = cycle["employment_index"].pct_change().fillna(0)
    cycle["cycle_fragility_score"] = (
        0.35 * (1 - cycle["expectations_index"])
        + 0.30 * cycle["credit_growth"].clip(upper=0).abs()
        + 0.20 * cycle["inventory_pressure"].clip(lower=0)
        + 0.15 * cycle["output_growth"].clip(upper=0).abs()
    )
    cycle.to_csv(TABLE_DIR / "business_cycle_phase_results_python.csv", index=False)

    fiscal["delta_y"] = fiscal["fiscal_multiplier"] * fiscal["delta_g"]
    fiscal["stabilized_gap"] = fiscal["initial_output_gap"] + (fiscal["delta_y"] / 1000) + (0.04 * fiscal["automatic_stabilizer_strength"])
    fiscal["stabilization_score"] = (
        0.40 * fiscal["automatic_stabilizer_strength"]
        + 0.35 * fiscal["public_capacity_score"]
        + 0.25 * fiscal["stabilized_gap"].clip(lower=-0.10, upper=0.05).add(0.10) / 0.15
    )
    fiscal.to_csv(TABLE_DIR / "fiscal_stabilization_results_python.csv", index=False)

    inflation["policy_tradeoff_score"] = (
        0.35 * inflation["inflation_pressure"]
        + 0.25 * inflation["unemployment_gap"].clip(lower=0) / inflation["unemployment_gap"].clip(lower=0).max()
        + 0.25 * inflation["supply_shock_intensity"]
        + 0.15 * inflation["policy_rate_response"].abs()
    )
    inflation.to_csv(TABLE_DIR / "inflation_unemployment_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    demand.set_index("scenario")[["consumption", "investment", "government_spending", "net_exports"]].plot(kind="bar", stacked=True, ax=ax)
    ax.set_title("Aggregate Demand Components by Scenario")
    ax.set_ylabel("Value")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "aggregate_demand_components_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(demand["scenario"], demand["output_gap"])
    ax.axhline(0, linestyle="--")
    ax.set_title("Output Gap by Scenario")
    ax.set_ylabel("(Y - Y*) / Y*")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "output_gap_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(cycle["year"], cycle["output_index"], label="Output index")
    ax.plot(cycle["year"], cycle["employment_index"], label="Employment index")
    ax.plot(cycle["year"], cycle["expectations_index"] * 100, label="Expectations index x100")
    ax.set_title("Business-Cycle Phase Dynamics")
    ax.set_xlabel("Year")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "business_cycle_phase_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(fiscal["scenario"], fiscal["stabilization_score"])
    ax.set_title("Fiscal Stabilization Score")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "fiscal_stabilization_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(inflation["scenario"], inflation["policy_tradeoff_score"])
    ax.set_title("Inflation-Unemployment Policy Tradeoff Score")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "inflation_unemployment_policy_python.png", dpi=300)
    plt.close(fig)

    print(demand[["scenario", "output", "output_gap"]])
    print(cycle[["year", "cycle_phase", "cycle_fragility_score"]])
    print(fiscal[["scenario", "delta_y", "stabilization_score"]])


if __name__ == "__main__":
    main()
