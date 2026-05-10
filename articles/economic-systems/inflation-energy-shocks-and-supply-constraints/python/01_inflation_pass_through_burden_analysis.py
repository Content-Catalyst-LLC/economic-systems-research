"""
Inflation rates, energy pass-through, real wages, household energy burden, and import-price shocks.
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
    prices = pd.read_csv(PROCESSED_DIR / "price_index_scenarios.csv")
    pass_through = pd.read_csv(PROCESSED_DIR / "sector_energy_pass_through_scenarios.csv")
    households = pd.read_csv(PROCESSED_DIR / "household_energy_burden_scenarios.csv")
    imports = pd.read_csv(PROCESSED_DIR / "import_price_transmission_scenarios.csv")

    prices["inflation_rate"] = prices.groupby("scenario")["price_level"].pct_change().fillna(0)
    prices["cumulative_inflation"] = prices["price_level"] / prices.groupby("scenario")["price_level"].transform("first") - 1
    prices.to_csv(TABLE_DIR / "inflation_results_python.csv", index=False)

    pass_through["estimated_price_change"] = (
        pass_through["alpha_energy"] * pass_through["energy_cost_change"]
        + pass_through["beta_wage"] * pass_through["wage_cost_change"]
        + pass_through["gamma_materials"] * pass_through["materials_cost_change"]
    )
    pass_through["energy_share_of_pass_through"] = (
        pass_through["alpha_energy"] * pass_through["energy_cost_change"]
    ) / pass_through["estimated_price_change"]
    pass_through.to_csv(TABLE_DIR / "energy_pass_through_results_python.csv", index=False)

    households["household_energy_burden"] = households["energy_spending"] / households["income"]
    households["transport_fuel_burden"] = households["transport_fuel_spending"] / households["income"]
    households["combined_energy_transport_burden"] = (
        households["energy_spending"] + households["transport_fuel_spending"]
    ) / households["income"]
    households["real_wage"] = households.apply(
        lambda row: row["nominal_wage"] / row["price_level_relative"] if row["nominal_wage"] > 0 else 0,
        axis=1,
    )
    households["energy_poverty_flag"] = (households["combined_energy_transport_burden"] > 0.15).astype(int)
    households.to_csv(TABLE_DIR / "household_energy_burden_results_python.csv", index=False)

    imports["import_price_change"] = imports["world_price_change"] + imports["exchange_rate_effect"]
    imports["weighted_import_inflation_pressure"] = (
        imports["import_price_change"] * imports["import_dependence"] * (0.5 + imports["energy_share_of_imports"])
    )
    imports.to_csv(TABLE_DIR / "import_price_transmission_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    for scenario, group in prices.groupby("scenario"):
        ax.plot(group["period"], group["price_level"], label=scenario)
    ax.set_title("Price Level Paths Under Inflation Scenarios")
    ax.set_xlabel("Period")
    ax.set_ylabel("Price index")
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "inflation_paths_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(pass_through["sector"], pass_through["estimated_price_change"])
    ax.set_title("Estimated Sector Price Change From Energy and Input Pass-Through")
    ax.set_ylabel("Estimated price change")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "energy_pass_through_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(households["household_group"], households["combined_energy_transport_burden"])
    ax.axhline(0.15, linestyle="--", label="stress threshold")
    ax.set_title("Household Energy and Transport Burden")
    ax.set_ylabel("Share of income")
    ax.tick_params(axis="x", rotation=35)
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "household_energy_burden_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(imports["scenario"], imports["weighted_import_inflation_pressure"])
    ax.set_title("Weighted Import Inflation Pressure")
    ax.set_ylabel("Weighted pressure")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "import_price_transmission_python.png", dpi=300)
    plt.close(fig)

    print(prices.head())
    print(pass_through[["sector", "estimated_price_change", "energy_share_of_pass_through"]])
    print(households[["household_group", "combined_energy_transport_burden", "energy_poverty_flag"]])
    print(imports[["scenario", "import_price_change", "weighted_import_inflation_pressure"]])


if __name__ == "__main__":
    main()
