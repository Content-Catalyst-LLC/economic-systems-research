"""
Calculate business-cycle episode metrics.

This script identifies recession and expansion episodes from the quarterly NBER-based
recession indicator and calculates duration, amplitude, and phase summaries.
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
    panel = pd.read_csv(PROCESSED_DIR / "business_cycles_quarterly_panel.csv", parse_dates=["date"])
    panel = panel.sort_values("date").reset_index(drop=True)
    return panel


def identify_phase_episodes(panel: pd.DataFrame) -> pd.DataFrame:
    phase = panel["business_cycle_phase"].fillna("unknown")
    episode_id = (phase != phase.shift()).cumsum()
    episode_df = panel.copy()
    episode_df["episode_id"] = episode_id

    records = []
    for episode, group in episode_df.groupby("episode_id"):
        group = group.sort_values("date")
        phase_name = group["business_cycle_phase"].iloc[0]

        start_gdp = group["real_gdp"].dropna().iloc[0] if group["real_gdp"].notna().any() else None
        end_gdp = group["real_gdp"].dropna().iloc[-1] if group["real_gdp"].notna().any() else None
        start_unemployment = group["unemployment_rate"].dropna().iloc[0] if group["unemployment_rate"].notna().any() else None
        end_unemployment = group["unemployment_rate"].dropna().iloc[-1] if group["unemployment_rate"].notna().any() else None

        records.append({
            "episode_id": int(episode),
            "business_cycle_phase": phase_name,
            "start_quarter": group["date"].min(),
            "end_quarter": group["date"].max(),
            "duration_quarters": len(group),
            "start_real_gdp": start_gdp,
            "end_real_gdp": end_gdp,
            "real_gdp_change_pct": ((end_gdp / start_gdp) - 1) * 100 if start_gdp and end_gdp else None,
            "start_unemployment_rate": start_unemployment,
            "end_unemployment_rate": end_unemployment,
            "unemployment_rate_change": end_unemployment - start_unemployment if start_unemployment is not None and end_unemployment is not None else None,
            "avg_real_gdp_growth_annualized": group["real_gdp_growth_annualized"].mean(),
            "avg_output_gap_pct": group["output_gap_pct"].mean(),
            "avg_federal_funds_rate": group["federal_funds_rate"].mean(),
            "avg_payroll_growth_yoy_pct": group["payroll_growth_yoy_pct"].mean(),
            "avg_industrial_production_yoy_pct": group["industrial_production_yoy_pct"].mean(),
        })

    episodes = pd.DataFrame(records)
    episodes.to_csv(TABLE_DIR / "business_cycle_episode_metrics.csv", index=False)
    return episodes


def create_phase_summary(panel: pd.DataFrame) -> pd.DataFrame:
    summary = (
        panel.groupby("business_cycle_phase")
        .agg(
            observations=("date", "count"),
            avg_real_gdp_growth_annualized=("real_gdp_growth_annualized", "mean"),
            avg_unemployment_rate=("unemployment_rate", "mean"),
            avg_delta_unemployment_rate=("delta_unemployment_rate", "mean"),
            avg_output_gap_pct=("output_gap_pct", "mean"),
            avg_payroll_growth_yoy_pct=("payroll_growth_yoy_pct", "mean"),
            avg_industrial_production_yoy_pct=("industrial_production_yoy_pct", "mean"),
            avg_retail_sales_yoy_pct=("retail_sales_yoy_pct", "mean"),
            avg_real_income_yoy_pct=("real_income_yoy_pct", "mean"),
            avg_federal_funds_rate=("federal_funds_rate", "mean"),
        )
        .reset_index()
    )

    summary.to_csv(TABLE_DIR / "phase_summary_python.csv", index=False)
    return summary


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
    episodes = identify_phase_episodes(panel)
    summary = create_phase_summary(panel)

    plot_with_recession_shading(
        panel=panel,
        y="real_gdp",
        title="Real GDP Across Business-Cycle Phases",
        y_label="Real GDP",
        filename="real_gdp_with_recessions.png",
    )

    plot_with_recession_shading(
        panel=panel,
        y="unemployment_rate",
        title="Unemployment Across Business-Cycle Phases",
        y_label="Unemployment rate (%)",
        filename="unemployment_with_cycle_phases.png",
    )

    plot_with_recession_shading(
        panel=panel,
        y="output_gap_pct",
        title="Output Gap Across Business-Cycle Phases",
        y_label="Output gap (%)",
        filename="output_gap_cycle.png",
    )

    print(episodes.tail())
    print(summary)


if __name__ == "__main__":
    main()
