"""
Debt and monetary constraint analysis.

This script estimates simple relationships among policy rates, inflation, output gaps,
debt ratios, and recession indicators. It also exports debt-stabilizing balance metrics.
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
    panel = pd.read_csv(PROCESSED_DIR / "stabilization_constraints_quarterly_panel.csv", parse_dates=["date"])

    debt_metrics = panel[
        [
            "date",
            "debt_to_gdp",
            "treasury_10y",
            "real_gdp_growth_annualized",
            "cpi_inflation_yoy_pct",
            "nominal_growth_proxy",
            "interest_growth_gap",
            "debt_stabilizing_primary_balance_pct_gdp",
            "fiscal_space_constraint_flag",
        ]
    ].dropna(subset=["debt_to_gdp"])

    debt_metrics.to_csv(TABLE_DIR / "debt_stabilizing_balance_python.csv", index=False)

    model_df = panel[
        [
            "federal_funds_rate",
            "cpi_inflation_yoy_pct",
            "output_gap_pct",
            "delta_unemployment_rate",
            "recession_indicator",
            "lower_bound_constraint_flag",
            "inflation_constraint_flag",
        ]
    ].dropna()

    x = sm.add_constant(
        model_df[
            [
                "cpi_inflation_yoy_pct",
                "output_gap_pct",
                "delta_unemployment_rate",
                "recession_indicator",
                "lower_bound_constraint_flag",
                "inflation_constraint_flag",
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

    results.to_csv(TABLE_DIR / "monetary_constraint_python_results.csv", index=False)

    with open(TABLE_DIR / "monetary_constraint_python_model_summary.txt", "w", encoding="utf-8") as handle:
        handle.write(model.summary().as_text())

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(panel["treasury_10y"], panel["crowding_out_proxy"], alpha=0.65)
    ax.set_title("Crowding-Out Proxy and Long-Term Rates")
    ax.set_xlabel("10-year Treasury rate (%)")
    ax.set_ylabel("Crowding-out proxy")
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "crowding_out_proxy_python.png", dpi=300)
    plt.close(fig)

    print(results)
    print(debt_metrics.tail())


if __name__ == "__main__":
    main()
