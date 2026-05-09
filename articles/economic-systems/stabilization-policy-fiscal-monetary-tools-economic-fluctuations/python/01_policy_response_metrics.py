"""
Calculate recession policy-response metrics.

This script identifies recession episodes from the quarterly recession indicator and
summarizes monetary and fiscal indicators around downturns.
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
    panel = pd.read_csv(PROCESSED_DIR / "stabilization_policy_quarterly_panel.csv", parse_dates=["date"])
    panel = panel.sort_values("date").reset_index(drop=True)
    return panel


def create_phase_summary(panel: pd.DataFrame) -> pd.DataFrame:
    summary = (
        panel.groupby("policy_phase")
        .agg(
            observations=("date", "count"),
            avg_real_gdp_growth_annualized=("real_gdp_growth_annualized", "mean"),
            avg_unemployment_rate=("unemployment_rate", "mean"),
            avg_output_gap_pct=("output_gap_pct", "mean"),
            avg_cpi_inflation_yoy_pct=("cpi_inflation_yoy_pct", "mean"),
            avg_federal_funds_rate=("federal_funds_rate", "mean"),
            avg_delta_federal_funds_rate=("delta_federal_funds_rate", "mean"),
            avg_gov_spending_growth_yoy_pct=("gov_spending_growth_yoy_pct", "mean"),
            avg_policy_rate_gap=("policy_rate_gap", "mean"),
        )
        .reset_index()
    )

    summary.to_csv(TABLE_DIR / "stabilization_phase_summary_python.csv", index=False)
    return summary


def identify_policy_response_episodes(panel: pd.DataFrame) -> pd.DataFrame:
    recession = panel["recession_indicator"].fillna(0).astype(int)
    starts = panel.index[(recession.eq(1)) & (recession.shift(1, fill_value=0).eq(0))].tolist()
    ends = panel.index[(recession.eq(1)) & (recession.shift(-1, fill_value=0).eq(0))].tolist()

    records = []
    for episode_number, (start_idx, end_idx) in enumerate(zip(starts, ends), start=1):
        pre_window = panel.loc[max(0, start_idx - 4):max(0, start_idx - 1)].copy()
        recession_window = panel.loc[start_idx:end_idx].copy()
        post_window = panel.loc[end_idx + 1:min(len(panel) - 1, end_idx + 4)].copy()

        records.append({
            "episode": episode_number,
            "recession_start_quarter": panel.loc[start_idx, "date"],
            "recession_end_quarter": panel.loc[end_idx, "date"],
            "duration_quarters": end_idx - start_idx + 1,
            "pre_recession_avg_federal_funds_rate": pre_window["federal_funds_rate"].mean(),
            "recession_avg_federal_funds_rate": recession_window["federal_funds_rate"].mean(),
            "post_recession_avg_federal_funds_rate": post_window["federal_funds_rate"].mean(),
            "federal_funds_rate_change_pre_to_recession": recession_window["federal_funds_rate"].mean() - pre_window["federal_funds_rate"].mean(),
            "pre_recession_avg_output_gap": pre_window["output_gap_pct"].mean(),
            "recession_avg_output_gap": recession_window["output_gap_pct"].mean(),
            "post_recession_avg_output_gap": post_window["output_gap_pct"].mean(),
            "recession_peak_unemployment_rate": recession_window["unemployment_rate"].max(),
            "pre_recession_avg_gov_spending_growth": pre_window["gov_spending_growth_yoy_pct"].mean(),
            "recession_avg_gov_spending_growth": recession_window["gov_spending_growth_yoy_pct"].mean(),
            "post_recession_avg_gov_spending_growth": post_window["gov_spending_growth_yoy_pct"].mean(),
        })

    episodes = pd.DataFrame(records)
    episodes.to_csv(TABLE_DIR / "policy_response_episode_metrics.csv", index=False)
    return episodes


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
    episodes = identify_policy_response_episodes(panel)

    plot_with_recession_shading(
        panel,
        y="federal_funds_rate",
        title="Federal Funds Rate Across Stabilization Episodes",
        y_label="Federal funds rate (%)",
        filename="unemployment_and_policy_rate.png",
    )

    plot_with_recession_shading(
        panel,
        y="output_gap_pct",
        title="Output Gap Across Stabilization Episodes",
        y_label="Output gap (%)",
        filename="output_gap_and_fed_funds.png",
    )

    plot_with_recession_shading(
        panel,
        y="gov_spending_growth_yoy_pct",
        title="Real Government Consumption and Investment Growth",
        y_label="Year-over-year growth (%)",
        filename="government_spending_growth.png",
    )

    print(summary)
    print(episodes.tail())


if __name__ == "__main__":
    main()
