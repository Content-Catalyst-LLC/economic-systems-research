"""
Network contagion, household leverage, macroprudential buffers, and sustainability shocks.
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
    institutions = pd.read_csv(PROCESSED_DIR / "institution_balance_sheets.csv")
    exposures = pd.read_csv(PROCESSED_DIR / "network_exposure_matrix.csv")
    households = pd.read_csv(PROCESSED_DIR / "household_leverage_scenarios.csv")
    buffers = pd.read_csv(PROCESSED_DIR / "macroprudential_buffer_scenarios.csv")
    sustainability = pd.read_csv(PROCESSED_DIR / "sustainability_shock_scenarios.csv")

    institutions["equity"] = institutions["assets"] - institutions["debt"]
    equity_map = dict(zip(institutions["institution"], institutions["equity"]))

    exposure_results = (
        exposures.groupby("to_institution")
        .agg(total_incoming_exposure=("exposure", "sum"))
        .reset_index()
        .rename(columns={"to_institution": "institution"})
    )
    exposure_results["receiver_equity"] = exposure_results["institution"].map(equity_map)
    exposure_results["incoming_exposure_to_equity"] = exposure_results["total_incoming_exposure"] / exposure_results["receiver_equity"]
    exposure_results["contagion_vulnerability_flag"] = (exposure_results["incoming_exposure_to_equity"] > 0.80).astype(int)
    exposure_results.to_csv(TABLE_DIR / "network_contagion_results_python.csv", index=False)

    households["loan_to_value"] = households.apply(
        lambda row: row["mortgage_debt"] / row["housing_value"] if row["housing_value"] > 0 else 0,
        axis=1,
    )
    households["debt_service_ratio"] = households["debt_service"] / households["income"]
    households["housing_value_after_15pct_shock"] = households["housing_value"] * 0.85
    households["ltv_after_housing_shock"] = households.apply(
        lambda row: row["mortgage_debt"] / row["housing_value_after_15pct_shock"] if row["housing_value_after_15pct_shock"] > 0 else 0,
        axis=1,
    )
    households["negative_equity_flag"] = (households["ltv_after_housing_shock"] > 1).astype(int)
    households["household_stress_score"] = (
        0.45 * households["ltv_after_housing_shock"].clip(upper=1.5) / 1.5
        + 0.35 * households["debt_service_ratio"].clip(upper=0.7) / 0.7
        + 0.20 * (1 - (households["liquid_savings"] / households["income"]).clip(upper=0.5) / 0.5)
    )
    households.to_csv(TABLE_DIR / "household_leverage_results_python.csv", index=False)

    buffers["macroprudential_resilience_score"] = (
        0.24 * (buffers["capital_buffer"] / buffers["capital_buffer"].max())
        + 0.24 * (buffers["liquidity_buffer"] / buffers["liquidity_buffer"].max())
        + 0.20 * (buffers["countercyclical_buffer"] / buffers["countercyclical_buffer"].max())
        + 0.16 * (1 - buffers["loan_to_value_limit"])
        + 0.16 * buffers["stress_test_strength"]
    )
    buffers.to_csv(TABLE_DIR / "macroprudential_buffer_results_python.csv", index=False)

    sustainability["expected_loss"] = sustainability["portfolio_exposure"] * sustainability["loss_given_shock"]
    sustainability["systemic_sustainability_risk_score"] = (
        0.36 * sustainability["expected_loss"]
        + 0.28 * sustainability["liquidity_impact"]
        + 0.22 * sustainability["public_backstop_need"]
        + 0.14 * sustainability["portfolio_exposure"]
    )
    sustainability.to_csv(TABLE_DIR / "sustainability_shock_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(exposure_results["institution"], exposure_results["incoming_exposure_to_equity"])
    ax.axhline(0.80, linestyle="--", label="vulnerability threshold")
    ax.set_title("Network Exposure Relative to Receiver Equity")
    ax.set_ylabel("Incoming exposure / equity")
    ax.tick_params(axis="x", rotation=35)
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "network_contagion_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(households["household_group"], households["household_stress_score"])
    ax.set_title("Household Leverage Stress Score")
    ax.set_ylabel("Stress score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "household_leverage_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(buffers["scenario"], buffers["macroprudential_resilience_score"])
    ax.set_title("Macroprudential Resilience Score")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "macroprudential_buffers_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(sustainability["shock"], sustainability["systemic_sustainability_risk_score"])
    ax.set_title("Sustainability-Linked Systemic Risk Score")
    ax.set_ylabel("Risk score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "sustainability_shock_python.png", dpi=300)
    plt.close(fig)

    print(exposure_results)
    print(households[["household_group", "ltv_after_housing_shock", "household_stress_score"]])
    print(buffers[["scenario", "macroprudential_resilience_score"]])
    print(sustainability[["shock", "systemic_sustainability_risk_score"]])


if __name__ == "__main__":
    main()
