"""
Estimate a simple Okun-style relationship between GDP growth and unemployment changes.

This is not a definitive structural model. It is an article companion example that
shows how output growth and labor-market stress can be examined reproducibly.
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
    panel = pd.read_csv(PROCESSED_DIR / "economic_resilience_quarterly_panel.csv", parse_dates=["date"])

    model_df = panel[
        [
            "date",
            "real_gdp_growth_annualized",
            "delta_unemployment_rate",
            "recession_indicator",
            "output_gap_pct",
        ]
    ].dropna()

    x = sm.add_constant(model_df["real_gdp_growth_annualized"])
    y = model_df["delta_unemployment_rate"]

    model = sm.OLS(y, x).fit(cov_type="HC1")

    results = pd.DataFrame({
        "term": model.params.index,
        "estimate": model.params.values,
        "std_error_hc1": model.bse.values,
        "t_value": model.tvalues.values,
        "p_value": model.pvalues.values,
    })

    results.to_csv(TABLE_DIR / "okun_python_results.csv", index=False)

    with open(TABLE_DIR / "okun_python_model_summary.txt", "w", encoding="utf-8") as handle:
        handle.write(model.summary().as_text())

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(model_df["real_gdp_growth_annualized"], model_df["delta_unemployment_rate"], alpha=0.65)

    fitted = model.predict(x)
    order = model_df["real_gdp_growth_annualized"].argsort()
    ax.plot(
        model_df["real_gdp_growth_annualized"].iloc[order],
        fitted.iloc[order],
        linewidth=1.5,
    )

    ax.axhline(0, linewidth=1)
    ax.axvline(0, linewidth=1)
    ax.set_title("Okun-Style Relationship: GDP Growth and Unemployment Change")
    ax.set_xlabel("Real GDP growth, annualized (%)")
    ax.set_ylabel("Quarterly change in unemployment rate")
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "okun_relationship_python.png", dpi=300)
    plt.close(fig)

    print(results)


if __name__ == "__main__":
    main()
