"""
Inflation conflict, debt and rent pressure, globalization, crisis burden-sharing, and legitimacy.
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
    inflation = pd.read_csv(PROCESSED_DIR / "inflation_labor_conflict.csv")
    debt = pd.read_csv(PROCESSED_DIR / "debt_rent_conflict.csv")
    welfare = pd.read_csv(PROCESSED_DIR / "welfare_globalization_crisis.csv")
    legitimacy = pd.read_csv(PROCESSED_DIR / "legitimacy_conflict.csv")

    inflation["real_wage_change"] = inflation["nominal_wage_growth"] - inflation["price_inflation"]
    inflation["real_margin_pressure"] = inflation["profit_margin_change"] - inflation["price_inflation"]
    inflation["inflation_conflict_score"] = (
        0.24 * inflation["price_inflation"] / inflation["price_inflation"].max()
        + 0.18 * inflation["interest_rate_shock"] / inflation["interest_rate_shock"].max()
        + 0.22 * inflation["unemployment_pressure"]
        + 0.18 * (1 - inflation["bargaining_strength"])
        + 0.18 * inflation["profit_margin_change"].clip(lower=0) / inflation["profit_margin_change"].clip(lower=0).max()
    )
    inflation.to_csv(TABLE_DIR / "inflation_labor_conflict_results_python.csv", index=False)

    debt["debt_to_income"] = debt["debt_stock"] / debt["income"]
    debt["interest_burden"] = debt["debt_stock"] * debt["interest_rate"] / debt["income"]
    debt["debt_rent_pressure_score"] = (
        0.22 * debt["debt_to_income"] / debt["debt_to_income"].max()
        + 0.18 * debt["interest_burden"] / debt["interest_burden"].max()
        + 0.18 * debt["rent_burden"]
        + 0.16 * debt["asset_owner_gain"]
        + 0.14 * (1 - debt["debtor_relief_access"])
        + 0.12 * debt["legal_enforcement_strength"]
    )
    debt.to_csv(TABLE_DIR / "debt_rent_conflict_results_python.csv", index=False)

    welfare["social_compromise_score"] = (
        0.22 * welfare["welfare_buffer"]
        + 0.18 * welfare["tax_progressivity"]
        + 0.18 * welfare["labor_voice"]
        + 0.14 * (1 - welfare["capital_mobility"])
        + 0.10 * (1 - welfare["austerity_pressure"])
        + 0.18 * welfare["public_trust"]
    )
    welfare["globalization_constraint_score"] = (
        0.32 * welfare["capital_mobility"]
        + 0.24 * welfare["trade_exposure"]
        + 0.22 * welfare["austerity_pressure"]
        + 0.12 * (1 - welfare["labor_voice"])
        + 0.10 * (1 - welfare["tax_progressivity"])
    )
    welfare.to_csv(TABLE_DIR / "welfare_globalization_crisis_results_python.csv", index=False)

    legitimacy["conflict_intensity_score"] = (
        0.22 * legitimacy["inequality_pressure"]
        + 0.18 * legitimacy["inflation_pressure"]
        + 0.18 * legitimacy["unemployment_pressure"]
        + 0.20 * legitimacy["representation_gap"]
        + 0.22 * legitimacy["shock_exposure"]
    )
    legitimacy["legitimacy_score"] = (
        0.26 * legitimacy["fairness"]
        + 0.24 * legitimacy["security"]
        + 0.24 * legitimacy["voice"]
        + 0.26 * legitimacy["institutional_trust"]
    )
    legitimacy.to_csv(TABLE_DIR / "legitimacy_conflict_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(inflation["scenario"], inflation["inflation_conflict_score"])
    ax.set_title("Inflation and Distributional Conflict")
    ax.set_ylabel("Composite conflict score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "inflation_conflict_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(debt["scenario"], debt["debt_rent_pressure_score"])
    ax.set_title("Debt and Rent Pressure")
    ax.set_ylabel("Composite pressure score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "debt_rent_pressure_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(welfare["scenario"], welfare["social_compromise_score"])
    ax.set_title("Social Compromise and Welfare Buffering")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "social_compromise_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(legitimacy["scenario"], legitimacy["legitimacy_score"])
    ax.set_title("Legitimacy")
    ax.set_ylabel("Composite legitimacy score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "legitimacy_python.png", dpi=300)
    plt.close(fig)

    print(inflation[["scenario", "real_wage_change", "inflation_conflict_score"]])
    print(debt[["scenario", "debt_to_income", "interest_burden", "debt_rent_pressure_score"]])
    print(welfare[["scenario", "social_compromise_score", "globalization_constraint_score"]])
    print(legitimacy[["scenario", "conflict_intensity_score", "legitimacy_score"]])


if __name__ == "__main__":
    main()
