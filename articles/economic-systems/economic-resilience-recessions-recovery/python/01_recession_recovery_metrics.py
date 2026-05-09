"""
Calculate recession episode and recovery metrics.

This script identifies recession episodes from the quarterly recession indicator and
measures how long it takes real GDP and payroll employment to regain their
pre-recession levels.
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
    panel = pd.read_csv(PROCESSED_DIR / "economic_resilience_quarterly_panel.csv", parse_dates=["date"])
    panel = panel.sort_values("date").reset_index(drop=True)
    return panel


def identify_recession_episodes(panel: pd.DataFrame) -> pd.DataFrame:
    recession = panel["recession_indicator"].fillna(0).astype(int)
    starts = panel.index[(recession.eq(1)) & (recession.shift(1, fill_value=0).eq(0))].tolist()
    ends = panel.index[(recession.eq(1)) & (recession.shift(-1, fill_value=0).eq(0))].tolist()

    records = []
    for episode_number, (start_idx, end_idx) in enumerate(zip(starts, ends), start=1):
        peak_idx = max(start_idx - 1, 0)
        trough_idx = end_idx

        pre_peak_gdp = panel.loc[peak_idx, "real_gdp"]
        pre_peak_payroll = panel.loc[peak_idx, "payroll_employment"]

        after = panel.loc[trough_idx:].copy()

        gdp_recovery_candidates = after.index[after["real_gdp"] >= pre_peak_gdp].tolist()
        payroll_recovery_candidates = after.index[after["payroll_employment"] >= pre_peak_payroll].tolist()

        gdp_recovery_idx = gdp_recovery_candidates[0] if gdp_recovery_candidates else None
        payroll_recovery_idx = payroll_recovery_candidates[0] if payroll_recovery_candidates else None

        records.append({
            "episode": episode_number,
            "pre_recession_peak_quarter": panel.loc[peak_idx, "date"],
            "recession_start_quarter": panel.loc[start_idx, "date"],
            "recession_end_quarter": panel.loc[end_idx, "date"],
            "recession_length_quarters": end_idx - start_idx + 1,
            "pre_peak_real_gdp": pre_peak_gdp,
            "trough_real_gdp": panel.loc[trough_idx, "real_gdp"],
            "real_gdp_peak_to_trough_pct": ((panel.loc[trough_idx, "real_gdp"] / pre_peak_gdp) - 1) * 100,
            "gdp_recovery_quarter": panel.loc[gdp_recovery_idx, "date"] if gdp_recovery_idx is not None else pd.NaT,
            "quarters_to_gdp_recovery": gdp_recovery_idx - peak_idx if gdp_recovery_idx is not None else None,
            "pre_peak_payroll_employment": pre_peak_payroll,
            "trough_payroll_employment": panel.loc[trough_idx, "payroll_employment"],
            "payroll_peak_to_trough_pct": ((panel.loc[trough_idx, "payroll_employment"] / pre_peak_payroll) - 1) * 100,
            "payroll_recovery_quarter": panel.loc[payroll_recovery_idx, "date"] if payroll_recovery_idx is not None else pd.NaT,
            "quarters_to_payroll_recovery": payroll_recovery_idx - peak_idx if payroll_recovery_idx is not None else None,
            "peak_unemployment_rate_during_episode": panel.loc[start_idx:end_idx, "unemployment_rate"].max(),
            "avg_output_gap_during_episode": panel.loc[start_idx:end_idx, "output_gap_pct"].mean(),
        })

    episodes = pd.DataFrame(records)
    episodes.to_csv(TABLE_DIR / "recession_episode_metrics.csv", index=False)
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


def build_gdp_recovery_index(panel: pd.DataFrame, episodes: pd.DataFrame) -> None:
    if episodes.empty:
        return

    records = []
    for _, episode in episodes.iterrows():
        peak_quarter = pd.to_datetime(episode["pre_recession_peak_quarter"])
        peak_gdp = episode["pre_peak_real_gdp"]

        window = panel[(panel["date"] >= peak_quarter)].head(20).copy()
        window["quarters_since_peak"] = range(len(window))
        window["real_gdp_index_peak_100"] = (window["real_gdp"] / peak_gdp) * 100
        window["episode"] = int(episode["episode"])
        records.append(window[["episode", "quarters_since_peak", "real_gdp_index_peak_100"]])

    indexed = pd.concat(records, ignore_index=True)
    indexed.to_csv(TABLE_DIR / "gdp_recovery_index.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    for episode, group in indexed.groupby("episode"):
        ax.plot(group["quarters_since_peak"], group["real_gdp_index_peak_100"], linewidth=1, label=f"Episode {episode}")

    ax.axhline(100, linestyle="--", linewidth=1)
    ax.set_title("Real GDP Recovery Indexed to Pre-Recession Peak")
    ax.set_xlabel("Quarters since pre-recession peak")
    ax.set_ylabel("Real GDP index, peak = 100")
    ax.legend(loc="best", fontsize=7)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "gdp_recovery_index.png", dpi=300)
    plt.close(fig)


def main() -> None:
    panel = load_panel()
    episodes = identify_recession_episodes(panel)

    plot_with_recession_shading(
        panel=panel,
        y="unemployment_rate",
        title="Unemployment Rate with Recession Periods",
        y_label="Unemployment rate (%)",
        filename="unemployment_with_recessions.png",
    )

    plot_with_recession_shading(
        panel=panel,
        y="output_gap_pct",
        title="Output Gap with Recession Periods",
        y_label="Output gap (%)",
        filename="output_gap_with_recessions.png",
    )

    build_gdp_recovery_index(panel, episodes)
    print(f"Saved recession metrics to {TABLE_DIR / 'recession_episode_metrics.csv'}")


if __name__ == "__main__":
    main()
