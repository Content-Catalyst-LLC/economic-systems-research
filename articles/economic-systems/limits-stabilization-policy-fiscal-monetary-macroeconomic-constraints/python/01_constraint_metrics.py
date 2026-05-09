"""
Calculate stabilization-policy constraint metrics.

This script summarizes policy constraints by phase and creates figures for:
- inflation/output-gap constraints
- interest-growth and debt constraints
- lower-bound monetary constraints
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


def load_panel() -> pd.DataFrame:
    panel = pd.read_csv(PROCESSED_DIR / "stabilization_constraints_quarterly_panel.csv", parse_dates=["date"])
    panel = panel.sort_values("date").reset_index(drop=True)
    return panel


def create_phase_summary(panel: pd.DataFrame) -> pd.DataFrame:
    summary = (
        panel.groupby("constraint_phase")
        .agg(
            observations=("date", "count"),
            avg_real_gdp_growth_annualized=("real_gdp_growth_annualized", "mean"),
            avg_unemployment_rate=("unemployment_rate", "mean"),
            avg_output_gap_pct=("output_gap_pct", "mean"),
            avg_cpi_inflation_yoy_pct=("cpi_inflation_yoy_pct", "mean"),
            avg_federal_funds_rate=("federal_funds_rate", "mean"),
            avg_treasury_10y=("treasury_10y", "mean"),
            avg_debt_to_gdp=("debt_to_gdp", "mean"),
            avg_interest_growth_gap=("interest_growth_gap", "mean"),
            avg_debt_stabilizing_primary_balance_pct_gdp=("debt_stabilizing_primary_balance_pct_gdp", "mean"),
            lower_bound_share=("lower_bound_constraint_flag", "mean"),
            inflation_constraint_share=("inflation_constraint_flag", "mean"),
            fiscal_space_constraint_share=("fiscal_space_constraint_flag", "mean"),
            avg_crowding_out_proxy=("crowding_out_proxy", "mean"),
        )
        .reset_index()
    )

    summary.to_csv(TABLE_DIR / "constraint_phase_summary_python.csv", index=False)
    return summary


def export_constraint_metrics(panel: pd.DataFrame) -> pd.DataFrame:
    metrics = panel[
        [
            "date",
            "constraint_phase",
            "output_gap_pct",
            "cpi_inflation_yoy_pct",
            "federal_funds_rate",
            "treasury_10y",
            "debt_to_gdp",
            "interest_growth_gap",
            "debt_stabilizing_primary_balance_pct_gdp",
            "lower_bound_constraint_flag",
            "inflation_constraint_flag",
            "fiscal_space_constraint_flag",
            "crowding_out_proxy",
        ]
    ].copy()

    metrics.to_csv(TABLE_DIR / "fiscal_space_constraint_metrics.csv", index=False)
    return metrics


def plot_with_recession_shading(panel: pd.DataFrame, y: str, title: str, y_label: str, filename: str) -> None:
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(panel["date"], panel[y], linewidth=1.5)

    in_recession = False
    start_date = None
    for _, row in panel.iterrows():
        if row["recession_indicator"] == 1 and not in_recession:
            in_recession = True
            start_date = row["date"]
        if row["recession_indicator"] == 0 and in_recession:
            ax.axvspan(start_date, row["date"], alpha=0.15)
            in_recession = False

    if in_recession and start_date is not None:
        ax.axvspan(start_date, panel["date"].max(), alpha=0.15)

    ax.set_title(title)
    ax.set_ylabel(y_label)
    ax.set_xlabel("")
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / filename, dpi=300)
    plt.close(fig)


def main() -> None:
    panel = load_panel()
    summary = create_phase_summary(panel)
    metrics = export_constraint_metrics(panel)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(panel["output_gap_pct"], panel["cpi_inflation_yoy_pct"], alpha=0.65)
    ax.axhline(4.0, linewidth=1)
    ax.axvline(0.0, linewidth=1)
    ax.set_title("Inflation and Output-Gap Constraints")
    ax.set_xlabel("Output gap (%)")
    ax.set_ylabel("CPI inflation, year over year (%)")
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "inflation_output_gap_constraints.png", dpi=300)
    plt.close(fig)

    plot_with_recession_shading(
        panel,
        y="interest_growth_gap",
        title="Interest-Growth Gap Across the Cycle",
        y_label="Interest-growth gap proxy",
        filename="debt_ratio_and_interest_growth_gap.png",
    )

    plot_with_recession_shading(
        panel,
        y="federal_funds_rate",
        title="Policy Rate and Lower-Bound Context",
        y_label="Federal funds rate (%)",
        filename="policy_rate_lower_bound_context.png",
    )

    print(summary)
    print(metrics.tail())


if __name__ == "__main__":
    main()
