"""
Taylor-rule-style policy gap analysis.

This script estimates a simple relationship between the federal funds rate,
inflation, output gaps, unemployment changes, and recession periods.

It also exports a policy-rate gap figure based on the illustrative Taylor-rule benchmark
created in the data pipeline.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
FIGURE_DIR = BASE_DIR / "outputs" / "figures"
TABLE_DIR = BASE_DIR / "outputs" / "tables"

for directory in [FIGURE_DIR, TABLE_DIR]:
    directory.mkdir(parents=True, exist_ok=True)


def main() -> None:
    panel = pd.read_csv(PROCESSED_DIR / "stabilization_policy_quarterly_panel.csv", parse_dates=["date"])

    model_df = panel[
        [
            "date",
            "federal_funds_rate",
            "cpi_inflation_yoy_pct",
            "output_gap_pct",
            "delta_unemployment_rate",
            "recession_indicator",
            "policy_rate_gap",
            "taylor_rule_rate",
        ]
    ].dropna()

    x = sm.add_constant(
        model_df[
            [
                "cpi_inflation_yoy_pct",
                "output_gap_pct",
                "delta_unemployment_rate",
                "recession_indicator",
            ]
        ]
    )
    y = model_df["federal_funds_rate"]

    model = sm.OLS(y, x).fit(cov_type="HC1")

    results = pd.DataFrame({
        "term": model.params.index,
        "estimate": model.params.values,
        "std_error_hc1": model.bse.values,
        "t_value": model.tvalues.values,
        "p_value": model.pvalues.values,
    })

    results.to_csv(TABLE_DIR / "taylor_gap_python_results.csv", index=False)

    with open(TABLE_DIR / "taylor_gap_python_model_summary.txt", "w", encoding="utf-8") as handle:
        handle.write(model.summary().as_text())

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(model_df["date"], model_df["federal_funds_rate"], label="Federal funds rate", linewidth=1.4)
    ax.plot(model_df["date"], model_df["taylor_rule_rate"], label="Illustrative Taylor-rule benchmark", linewidth=1.1)
    ax.set_title("Federal Funds Rate and Illustrative Taylor-Rule Benchmark")
    ax.set_xlabel("")
    ax.set_ylabel("Rate (%)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "taylor_rule_benchmark_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(model_df["output_gap_pct"], model_df["policy_rate_gap"], alpha=0.65)
    ax.axhline(0, linewidth=1)
    ax.axvline(0, linewidth=1)
    ax.set_title("Policy Rate Gap and Output Gap")
    ax.set_xlabel("Output gap (%)")
    ax.set_ylabel("Federal funds rate minus benchmark")
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "taylor_gap_scatter_python.png", dpi=300)
    plt.close(fig)

    print(results)


if __name__ == "__main__":
    main()
