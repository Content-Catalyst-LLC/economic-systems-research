"""
Trend-cycle decomposition and macroeconomic stability metrics.

This script uses the Hodrick-Prescott filter from statsmodels to create a simple
trend-cycle decomposition of log real GDP and calculates volatility metrics.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.tsa.filters.hp_filter import hpfilter
import statsmodels.api as sm


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
FIGURE_DIR = BASE_DIR / "outputs" / "figures"
TABLE_DIR = BASE_DIR / "outputs" / "tables"

for directory in [FIGURE_DIR, TABLE_DIR]:
    directory.mkdir(parents=True, exist_ok=True)


def main() -> None:
    panel = pd.read_csv(PROCESSED_DIR / "business_cycles_quarterly_panel.csv", parse_dates=["date"])
    panel = panel.sort_values("date").dropna(subset=["real_gdp"]).copy()

    panel["log_real_gdp"] = np.log(panel["real_gdp"])
    cycle, trend = hpfilter(panel["log_real_gdp"], lamb=1600)
    panel["hp_cycle_log_real_gdp"] = cycle
    panel["hp_trend_log_real_gdp"] = trend
    panel["hp_cycle_pct"] = panel["hp_cycle_log_real_gdp"] * 100

    trend_cycle = panel[[
        "date",
        "real_gdp",
        "log_real_gdp",
        "hp_trend_log_real_gdp",
        "hp_cycle_log_real_gdp",
        "hp_cycle_pct",
        "recession_indicator",
        "business_cycle_phase",
        "output_gap_pct",
    ]]

    trend_cycle.to_csv(TABLE_DIR / "trend_cycle_decomposition.csv", index=False)

    volatility = (
        panel.groupby("business_cycle_phase")
        .agg(
            observations=("date", "count"),
            gdp_growth_volatility=("real_gdp_growth_annualized", "std"),
            output_gap_volatility=("output_gap_pct", "std"),
            unemployment_change_volatility=("delta_unemployment_rate", "std"),
            hp_cycle_volatility=("hp_cycle_pct", "std"),
        )
        .reset_index()
    )
    volatility.to_csv(TABLE_DIR / "cycle_volatility_metrics.csv", index=False)

    # Simple persistence model: output gap today vs lagged output gap and recession phase.
    regression_df = panel[[
        "output_gap_pct",
        "recession_indicator",
        "federal_funds_rate",
    ]].copy()
    regression_df["output_gap_lag"] = regression_df["output_gap_pct"].shift(1)
    regression_df = regression_df.dropna()

    x = sm.add_constant(regression_df[["output_gap_lag", "recession_indicator", "federal_funds_rate"]])
    y = regression_df["output_gap_pct"]
    model = sm.OLS(y, x).fit(cov_type="HC1")

    model_results = pd.DataFrame({
        "term": model.params.index,
        "estimate": model.params.values,
        "std_error_hc1": model.bse.values,
        "t_value": model.tvalues.values,
        "p_value": model.pvalues.values,
    })
    model_results.to_csv(TABLE_DIR / "output_gap_persistence_python_results.csv", index=False)

    with open(TABLE_DIR / "output_gap_persistence_python_summary.txt", "w", encoding="utf-8") as handle:
        handle.write(model.summary().as_text())

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(panel["date"], panel["log_real_gdp"], label="Log real GDP", linewidth=1.3)
    ax.plot(panel["date"], panel["hp_trend_log_real_gdp"], label="HP trend", linewidth=1.3)
    ax.set_title("Trend-Cycle Decomposition of Real GDP")
    ax.set_xlabel("")
    ax.set_ylabel("Log real GDP")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "trend_cycle_decomposition_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(panel["date"], panel["hp_cycle_pct"], linewidth=1.3)
    ax.axhline(0, linewidth=1)
    ax.set_title("Estimated Cyclical Component of Real GDP")
    ax.set_xlabel("")
    ax.set_ylabel("Cycle component (%)")
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "estimated_gdp_cycle_component.png", dpi=300)
    plt.close(fig)

    print(volatility)
    print(model_results)


if __name__ == "__main__":
    main()
