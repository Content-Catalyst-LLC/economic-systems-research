"""
Household balance sheets, credit contraction, open economy shocks, and crisis recovery paths.
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
    households = pd.read_csv(PROCESSED_DIR / "household_balance_sheet_scenarios.csv")
    credit = pd.read_csv(PROCESSED_DIR / "credit_contraction_scenarios.csv")
    open_economy = pd.read_csv(PROCESSED_DIR / "open_economy_shock_scenarios.csv")
    recovery = pd.read_csv(PROCESSED_DIR / "crisis_recovery_path_scenarios.csv")

    households["debt_burden_ratio"] = households["debt_service"] / households["income"]
    households["savings_buffer_months"] = households["liquid_savings"] / (households["income"] / 12)
    households["post_shock_income"] = households["income"] * (1 - households["job_loss_income_shock"])
    households["post_shock_debt_burden_ratio"] = households["debt_service"] / households["post_shock_income"]
    households["real_income_pressure"] = households["price_shock"] + households["job_loss_income_shock"]
    households["household_macro_fragility_score"] = (
        0.35 * households["post_shock_debt_burden_ratio"].clip(upper=0.55) / 0.55
        + 0.30 * (1 - households["savings_buffer_months"].clip(upper=4) / 4)
        + 0.20 * households["real_income_pressure"].clip(upper=0.45) / 0.45
        + 0.15 * households["job_loss_income_shock"].clip(upper=0.40) / 0.40
    )
    households.to_csv(TABLE_DIR / "household_balance_sheet_results_python.csv", index=False)

    credit["real_debt_burden"] = credit["nominal_debt"] / credit["price_level"]
    credit["real_debt_burden_change"] = credit["real_debt_burden"] / credit["nominal_debt"] - 1
    credit["credit_cycle_stress_score"] = (
        0.35 * credit["credit_growth"].clip(upper=0).abs() / 0.12
        + 0.25 * credit["real_debt_burden_change"].clip(lower=0) / credit["real_debt_burden_change"].clip(lower=0).max()
        + 0.25 * credit["asset_price_change"].clip(upper=0).abs() / 0.20
        + 0.15 * credit["default_pressure"] / 0.32
    )
    credit.to_csv(TABLE_DIR / "credit_contraction_results_python.csv", index=False)

    open_economy["transmission_score"] = open_economy["shock_intensity"] * (
        0.28 * open_economy["export_exposure"]
        + 0.28 * open_economy["import_price_exposure"]
        + 0.24 * open_economy["capital_flow_exposure"]
        + 0.20 * open_economy["fx_debt_exposure"]
    )
    open_economy.to_csv(TABLE_DIR / "open_economy_shock_results_python.csv", index=False)

    recovery["output_shortfall"] = 100 - recovery["output_index"]
    recovery["employment_shortfall"] = 100 - recovery["employment_index"]
    recovery["resilience_score"] = (
        0.40 * recovery["output_index"] / recovery["output_index"].max()
        + 0.35 * recovery["employment_index"] / recovery["employment_index"].max()
        + 0.25 * recovery["public_capacity_index"] / recovery["public_capacity_index"].max()
    )
    recovery.to_csv(TABLE_DIR / "crisis_recovery_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(households["household_group"], households["household_macro_fragility_score"])
    ax.set_title("Household Balance-Sheet Macro Fragility")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "household_balance_sheet_stress_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(credit["scenario"], credit["credit_cycle_stress_score"])
    ax.set_title("Credit Contraction and Debt-Deflation Stress")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "credit_contraction_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(open_economy["external_shock"], open_economy["transmission_score"])
    ax.set_title("Open-Economy Shock Transmission")
    ax.set_ylabel("Transmission score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "open_economy_shock_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5))
    for path, group in recovery.groupby("recovery_path"):
        ax.plot(group["period"], group["output_index"], label=path)
    ax.axhline(100, linestyle="--")
    ax.set_title("Crisis Recovery Paths")
    ax.set_xlabel("Period")
    ax.set_ylabel("Output index")
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "crisis_recovery_paths_python.png", dpi=300)
    plt.close(fig)

    print(households[["household_group", "post_shock_debt_burden_ratio", "household_macro_fragility_score"]])
    print(credit[["scenario", "real_debt_burden", "credit_cycle_stress_score"]])
    print(open_economy[["external_shock", "transmission_score"]])


if __name__ == "__main__":
    main()
