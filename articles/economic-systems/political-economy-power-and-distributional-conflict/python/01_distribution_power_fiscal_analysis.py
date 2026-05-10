"""
Income shares, fiscal incidence, and power asymmetry.
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
    income = pd.read_csv(PROCESSED_DIR / "income_distribution.csv")
    power = pd.read_csv(PROCESSED_DIR / "power_groups.csv")
    fiscal = pd.read_csv(PROCESSED_DIR / "fiscal_incidence.csv")

    income["total_income"] = income["wages"] + income["profits"] + income["rents"]
    income["wage_share"] = income["wages"] / income["total_income"]
    income["profit_share"] = income["profits"] / income["total_income"]
    income["rent_share"] = income["rents"] / income["total_income"]
    income["net_fiscal_position"] = income["benefits_received"] + income["public_goods_value"] - income["taxes_paid"]
    income["distributional_concentration_score"] = income["profit_share"] + income["rent_share"]
    income.to_csv(TABLE_DIR / "income_distribution_results_python.csv", index=False)

    power["power_asymmetry_score"] = (
        0.20 * power["ownership_power"]
        + 0.16 * power["organization_power"]
        + 0.16 * power["access_power"]
        + 0.14 * power["mobility_power"]
        + 0.14 * power["voice_power"]
        + 0.10 * power["media_influence"]
        + 0.10 * power["legal_position"]
    )
    power.to_csv(TABLE_DIR / "power_asymmetry_results_python.csv", index=False)

    fiscal["gross_income_after_tax"] = fiscal["market_income"] - fiscal["taxes_paid"]
    fiscal["disposable_income"] = fiscal["gross_income_after_tax"] + fiscal["cash_transfers"]
    fiscal["service_adjusted_income"] = fiscal["disposable_income"] + fiscal["services_received"]
    fiscal["net_fiscal_position"] = fiscal["cash_transfers"] + fiscal["services_received"] - fiscal["taxes_paid"]
    fiscal["post_burden_income"] = fiscal["service_adjusted_income"] - fiscal["debt_service"] - fiscal["housing_cost"]
    fiscal.to_csv(TABLE_DIR / "fiscal_incidence_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(income["scenario"], income["wage_share"])
    ax.set_title("Wage Share by Political-Economic Scenario")
    ax.set_ylabel("Wages / total income")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "wage_share_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(income["scenario"], income["distributional_concentration_score"])
    ax.set_title("Profit + Rent Share")
    ax.set_ylabel("Composite concentration share")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "profit_rent_share_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(power["group"], power["power_asymmetry_score"])
    ax.set_title("Power Asymmetry by Group")
    ax.set_ylabel("Composite power score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "power_asymmetry_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(fiscal["group"], fiscal["net_fiscal_position"])
    ax.set_title("Net Fiscal Position")
    ax.set_ylabel("Transfers + services - taxes")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "net_fiscal_position_python.png", dpi=300)
    plt.close(fig)

    print(income[["scenario", "wage_share", "profit_share", "rent_share", "net_fiscal_position"]])
    print(power[["group", "power_asymmetry_score"]])
    print(fiscal[["group", "disposable_income", "service_adjusted_income", "post_burden_income", "net_fiscal_position"]])


if __name__ == "__main__":
    main()
