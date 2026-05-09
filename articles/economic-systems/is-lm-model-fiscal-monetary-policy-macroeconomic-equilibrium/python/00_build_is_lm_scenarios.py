"""
Build IS-LM model scenarios and solve equilibrium output/interest rates.

Model:
    IS: Y = alpha - beta * r + fiscal_shift
    LM: r = gamma * Y - money_shift

Equilibrium:
    Y* = (alpha + beta * money_shift + fiscal_shift) / (1 + beta * gamma)
    r* = gamma * Y* - money_shift
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
TABLE_DIR = BASE_DIR / "outputs" / "tables"

for directory in [PROCESSED_DIR, TABLE_DIR]:
    directory.mkdir(parents=True, exist_ok=True)


def solve_is_lm(alpha: float, beta: float, gamma: float, fiscal_shift: float, money_shift: float) -> tuple[float, float]:
    output = (alpha + beta * money_shift + fiscal_shift) / (1 + beta * gamma)
    interest_rate = gamma * output - money_shift
    return output, interest_rate


def scenario_table() -> pd.DataFrame:
    scenarios = [
        {
            "scenario": "baseline",
            "alpha": 1000.0,
            "beta": 25.0,
            "gamma": 0.02,
            "fiscal_shift": 0.0,
            "money_shift": 0.0,
            "lm_slope_type": "baseline",
            "description": "Baseline short-run IS-LM equilibrium.",
        },
        {
            "scenario": "expansionary_fiscal_policy",
            "alpha": 1000.0,
            "beta": 25.0,
            "gamma": 0.02,
            "fiscal_shift": 100.0,
            "money_shift": 0.0,
            "lm_slope_type": "baseline",
            "description": "Government spending or tax policy raises aggregate demand.",
        },
        {
            "scenario": "expansionary_monetary_policy",
            "alpha": 1000.0,
            "beta": 25.0,
            "gamma": 0.02,
            "fiscal_shift": 0.0,
            "money_shift": 4.0,
            "lm_slope_type": "baseline",
            "description": "Monetary expansion shifts LM right/down by lowering rates for a given output level.",
        },
        {
            "scenario": "coordinated_expansion",
            "alpha": 1000.0,
            "beta": 25.0,
            "gamma": 0.02,
            "fiscal_shift": 100.0,
            "money_shift": 4.0,
            "lm_slope_type": "baseline",
            "description": "Fiscal expansion and monetary accommodation occur together.",
        },
        {
            "scenario": "steep_lm_fiscal_policy",
            "alpha": 1000.0,
            "beta": 25.0,
            "gamma": 0.05,
            "fiscal_shift": 100.0,
            "money_shift": 0.0,
            "lm_slope_type": "steep",
            "description": "Fiscal policy with a steep LM curve creates stronger interest-rate pressure.",
        },
        {
            "scenario": "flat_lm_fiscal_policy",
            "alpha": 1000.0,
            "beta": 25.0,
            "gamma": 0.005,
            "fiscal_shift": 100.0,
            "money_shift": 0.0,
            "lm_slope_type": "flat",
            "description": "Fiscal policy with a flat LM curve creates less crowding-out pressure.",
        },
        {
            "scenario": "liquidity_trap_case",
            "alpha": 1000.0,
            "beta": 25.0,
            "gamma": 0.001,
            "fiscal_shift": 100.0,
            "money_shift": 4.0,
            "lm_slope_type": "very_flat",
            "description": "Very flat LM approximation used to demonstrate liquidity-trap-style intuition.",
        },
        {
            "scenario": "low_interest_sensitive_investment",
            "alpha": 1000.0,
            "beta": 8.0,
            "gamma": 0.02,
            "fiscal_shift": 100.0,
            "money_shift": 4.0,
            "lm_slope_type": "baseline",
            "description": "Investment is less responsive to interest-rate movements.",
        },
        {
            "scenario": "high_interest_sensitive_investment",
            "alpha": 1000.0,
            "beta": 50.0,
            "gamma": 0.02,
            "fiscal_shift": 100.0,
            "money_shift": 4.0,
            "lm_slope_type": "baseline",
            "description": "Investment is more responsive to interest-rate movements.",
        },
    ]

    df = pd.DataFrame(scenarios)

    solutions = df.apply(
        lambda row: solve_is_lm(
            row["alpha"],
            row["beta"],
            row["gamma"],
            row["fiscal_shift"],
            row["money_shift"],
        ),
        axis=1,
    )

    df["equilibrium_output"] = [value[0] for value in solutions]
    df["equilibrium_interest_rate"] = [value[1] for value in solutions]

    baseline = df.loc[df["scenario"] == "baseline"].iloc[0]
    df["delta_output_from_baseline"] = df["equilibrium_output"] - baseline["equilibrium_output"]
    df["delta_interest_from_baseline"] = df["equilibrium_interest_rate"] - baseline["equilibrium_interest_rate"]

    df["fiscal_multiplier_model"] = 1 / (1 + df["beta"] * df["gamma"])
    df["monetary_multiplier_model"] = df["beta"] / (1 + df["beta"] * df["gamma"])
    df["crowding_out_indicator"] = df["delta_interest_from_baseline"].clip(lower=0)

    return df


def save_sqlite(results: pd.DataFrame) -> None:
    db_path = PROCESSED_DIR / "is_lm_model.sqlite"
    with sqlite3.connect(db_path) as conn:
        results.to_sql("is_lm_scenario_results", conn, if_exists="replace", index=False)

        conn.execute("""
        CREATE VIEW IF NOT EXISTS policy_multiplier_summary AS
        SELECT
            scenario,
            lm_slope_type,
            fiscal_multiplier_model,
            monetary_multiplier_model,
            equilibrium_output,
            equilibrium_interest_rate,
            delta_output_from_baseline,
            delta_interest_from_baseline
        FROM is_lm_scenario_results
        ORDER BY scenario;
        """)


def main() -> None:
    results = scenario_table()

    baseline_params = results.loc[results["scenario"] == "baseline", [
        "alpha",
        "beta",
        "gamma",
        "fiscal_shift",
        "money_shift",
    ]]

    baseline_params.to_csv(PROCESSED_DIR / "is_lm_baseline_parameters.csv", index=False)
    results.to_csv(PROCESSED_DIR / "is_lm_policy_scenarios.csv", index=False)
    results.to_csv(PROCESSED_DIR / "is_lm_scenario_results.csv", index=False)
    save_sqlite(results)

    print(results[[
        "scenario",
        "equilibrium_output",
        "equilibrium_interest_rate",
        "delta_output_from_baseline",
        "delta_interest_from_baseline",
    ]])


if __name__ == "__main__":
    main()
