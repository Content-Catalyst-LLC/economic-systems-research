"""
Calculate comparative statics and policy multipliers for IS-LM scenarios.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
TABLE_DIR = BASE_DIR / "outputs" / "tables"

TABLE_DIR.mkdir(parents=True, exist_ok=True)


def main() -> None:
    df = pd.read_csv(PROCESSED_DIR / "is_lm_scenario_results.csv")

    comparative = df[[
        "scenario",
        "lm_slope_type",
        "alpha",
        "beta",
        "gamma",
        "fiscal_shift",
        "money_shift",
        "equilibrium_output",
        "equilibrium_interest_rate",
        "delta_output_from_baseline",
        "delta_interest_from_baseline",
        "fiscal_multiplier_model",
        "monetary_multiplier_model",
        "crowding_out_indicator",
    ]].copy()

    comparative.to_csv(TABLE_DIR / "is_lm_comparative_statics_python.csv", index=False)

    multipliers = (
        comparative.groupby("lm_slope_type")
        .agg(
            scenarios=("scenario", "count"),
            avg_fiscal_multiplier=("fiscal_multiplier_model", "mean"),
            avg_monetary_multiplier=("monetary_multiplier_model", "mean"),
            avg_output_gain=("delta_output_from_baseline", "mean"),
            avg_interest_change=("delta_interest_from_baseline", "mean"),
            avg_crowding_out_indicator=("crowding_out_indicator", "mean"),
        )
        .reset_index()
    )

    multipliers.to_csv(TABLE_DIR / "is_lm_policy_multipliers_python.csv", index=False)

    print(comparative)
    print(multipliers)


if __name__ == "__main__":
    main()
