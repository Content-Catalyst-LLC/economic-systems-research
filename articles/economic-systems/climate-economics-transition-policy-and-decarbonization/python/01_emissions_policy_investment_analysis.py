"""
Emissions identities, decarbonization rates, policy packages, investment, and carbon lock-in.
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
    sectors = pd.read_csv(PROCESSED_DIR / "sector_emissions.csv")
    policies = pd.read_csv(PROCESSED_DIR / "policy_packages.csv")
    investment = pd.read_csv(PROCESSED_DIR / "transition_investment.csv")
    lock_in = pd.read_csv(PROCESSED_DIR / "carbon_lock_in.csv")

    sectors["emissions"] = sectors["output"] * sectors["energy_intensity"] * sectors["carbon_intensity"]
    sectors["decarbonization_rate"] = (sectors["old_emissions_intensity"] - sectors["new_emissions_intensity"]) / sectors["years"]
    sectors["transition_priority_score"] = (
        0.34 * (sectors["emissions"] / sectors["emissions"].max())
        + 0.24 * (1 - sectors["abatement_readiness"])
        + 0.22 * (1 - sectors["decarbonization_rate"] / sectors["decarbonization_rate"].max())
        + 0.20 * sectors["energy_intensity"]
    )
    sectors.to_csv(TABLE_DIR / "sector_emissions_results_python.csv", index=False)

    policies["policy_mix_score"] = (
        0.18 * policies["carbon_price_strength"]
        + 0.20 * policies["regulatory_strength"]
        + 0.22 * policies["public_investment"]
        + 0.18 * policies["industrial_policy"]
        + 0.12 * policies["social_protection"]
        + 0.10 * policies["implementation_capacity"]
    )
    policies["legitimacy_risk"] = (
        0.30 * policies["carbon_price_strength"]
        + 0.25 * (1 - policies["social_protection"])
        + 0.20 * (1 - policies["public_investment"])
        + 0.15 * (1 - policies["implementation_capacity"])
        + 0.10 * (1 - policies["regulatory_strength"])
    )
    policies.to_csv(TABLE_DIR / "policy_package_results_python.csv", index=False)

    investment["transition_investment_score"] = (
        0.22 * investment["public_investment"]
        + 0.20 * investment["private_capital"]
        + 0.22 * investment["policy_credibility"]
        + 0.16 * investment["cost_of_capital_support"]
        + 0.10 * investment["permitting_capacity"]
        + 0.10 * investment["grid_readiness"]
    )
    investment.to_csv(TABLE_DIR / "transition_investment_results_python.csv", index=False)

    lock_in["lock_in_score"] = (
        0.18 * lock_in["capital_stock_life"]
        + 0.20 * lock_in["infrastructure_dependence"]
        + 0.18 * lock_in["incumbent_power"]
        + 0.16 * lock_in["consumer_switching_barrier"]
        + 0.14 * (1 - lock_in["replacement_readiness"])
        + 0.14 * lock_in["stranded_asset_risk"]
    )
    lock_in.to_csv(TABLE_DIR / "carbon_lock_in_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(sectors["sector"], sectors["emissions"])
    ax.set_title("Sector Emissions")
    ax.set_ylabel("Output × energy intensity × carbon intensity")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "sector_emissions_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(sectors["sector"], sectors["decarbonization_rate"])
    ax.set_title("Annual Decarbonization Rate")
    ax.set_ylabel("Change in emissions intensity per year")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "decarbonization_rate_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(policies["package"], policies["policy_mix_score"])
    ax.set_title("Transition Policy Mix Score")
    ax.set_ylabel("Composite policy score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "policy_mix_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(lock_in["system"], lock_in["lock_in_score"])
    ax.set_title("Carbon Lock-In")
    ax.set_ylabel("Composite lock-in score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "carbon_lock_in_python.png", dpi=300)
    plt.close(fig)

    print(sectors[["sector", "emissions", "decarbonization_rate", "transition_priority_score"]])
    print(policies[["package", "policy_mix_score", "legitimacy_risk"]])
    print(investment[["scenario", "transition_investment_score"]])
    print(lock_in[["system", "lock_in_score"]])


if __name__ == "__main__":
    main()
