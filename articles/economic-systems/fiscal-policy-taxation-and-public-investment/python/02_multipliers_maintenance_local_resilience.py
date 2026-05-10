"""
Fiscal multipliers, infrastructure maintenance gaps, local fiscal capacity, and resilience investment.
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
    multipliers = pd.read_csv(PROCESSED_DIR / "fiscal_multiplier_scenarios.csv")
    maintenance = pd.read_csv(PROCESSED_DIR / "infrastructure_maintenance_scenarios.csv")
    local = pd.read_csv(PROCESSED_DIR / "local_fiscal_capacity_scenarios.csv")
    resilience = pd.read_csv(PROCESSED_DIR / "public_investment_resilience_scenarios.csv")

    multipliers["delta_y"] = multipliers["fiscal_multiplier"] * multipliers["delta_g"]
    multipliers["stabilization_development_score"] = (
        0.35 * multipliers["fiscal_multiplier"] / multipliers["fiscal_multiplier"].max()
        + 0.25 * multipliers["slack_index"]
        + 0.20 * multipliers["speed_score"]
        + 0.20 * multipliers["long_run_capacity_score"]
    )
    multipliers.to_csv(TABLE_DIR / "fiscal_multiplier_results_python.csv", index=False)

    maintenance["maintenance_gap"] = maintenance["maintenance_needed"] - maintenance["maintenance_actual"]
    maintenance["maintenance_gap_ratio"] = maintenance["maintenance_gap"] / maintenance["maintenance_needed"]
    maintenance["deferred_liability_score"] = (
        0.40 * maintenance["maintenance_gap_ratio"]
        + 0.35 * maintenance["failure_risk_index"]
        + 0.25 * maintenance["replacement_cost_if_deferred"] / maintenance["replacement_cost_if_deferred"].max()
    )
    maintenance.to_csv(TABLE_DIR / "infrastructure_maintenance_results_python.csv", index=False)

    local["tax_base_index"] = local["tax_base_per_capita"] / local["tax_base_per_capita"].max()
    local["transfer_index"] = local["intergovernmental_transfer_per_capita"] / local["intergovernmental_transfer_per_capita"].max()
    local["fiscal_capacity_score"] = (
        0.55 * local["tax_base_index"]
        + 0.25 * local["transfer_index"]
        - 0.12 * local["service_need_index"]
        - 0.08 * local["infrastructure_age_index"]
    )
    local["territorial_stress_score"] = (
        0.45 * local["service_need_index"]
        + 0.35 * local["infrastructure_age_index"]
        + 0.20 * (1 - local["tax_base_index"])
    )
    local.to_csv(TABLE_DIR / "local_fiscal_capacity_results_python.csv", index=False)

    resilience["avoided_loss_return"] = resilience["avoided_future_losses"] / resilience["public_investment"]
    resilience["resilience_investment_score"] = (
        0.32 * resilience["avoided_loss_return"] / resilience["avoided_loss_return"].max()
        + 0.22 * resilience["productivity_gain"] / resilience["productivity_gain"].max()
        + 0.23 * resilience["equity_score"]
        + 0.23 * resilience["climate_resilience_score"]
    )
    resilience.to_csv(TABLE_DIR / "public_investment_resilience_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(multipliers["instrument"], multipliers["delta_y"])
    ax.set_title("Estimated Output Effects by Fiscal Instrument")
    ax.set_ylabel("ΔY")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "fiscal_multipliers_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(maintenance["asset_class"], maintenance["maintenance_gap"])
    ax.set_title("Infrastructure Maintenance Gap")
    ax.set_ylabel("Needed minus actual maintenance")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "maintenance_gap_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(local["locality"], local["territorial_stress_score"])
    ax.set_title("Local Fiscal and Infrastructure Stress")
    ax.set_ylabel("Stress score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "local_fiscal_capacity_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(resilience["investment_area"], resilience["resilience_investment_score"])
    ax.set_title("Public Investment Resilience Score")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "public_investment_resilience_python.png", dpi=300)
    plt.close(fig)

    print(multipliers[["instrument", "delta_y", "stabilization_development_score"]])
    print(maintenance[["asset_class", "maintenance_gap", "deferred_liability_score"]])
    print(local[["locality", "fiscal_capacity_score", "territorial_stress_score"]])
    print(resilience[["investment_area", "avoided_loss_return", "resilience_investment_score"]])


if __name__ == "__main__":
    main()
