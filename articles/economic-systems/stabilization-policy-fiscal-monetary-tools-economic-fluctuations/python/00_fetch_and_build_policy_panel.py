"""
Build economist-grade stabilization-policy panels from public FRED CSV endpoints.

This script:
1. Downloads selected macroeconomic, fiscal, and monetary indicators.
2. Saves raw source files.
3. Builds monthly and quarterly policy panels.
4. Computes output gaps, inflation, government-spending growth, and policy-rate indicators.
5. Creates a SQLite database for SQL analysis.

No FRED API key is required.
"""

from __future__ import annotations

import sqlite3
from functools import reduce
from pathlib import Path
from typing import Dict

import numpy as np
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
TABLE_DIR = BASE_DIR / "outputs" / "tables"

for directory in [RAW_DIR, PROCESSED_DIR, TABLE_DIR]:
    directory.mkdir(parents=True, exist_ok=True)


MONTHLY_SERIES: Dict[str, str] = {
    "USREC": "recession_indicator",
    "UNRATE": "unemployment_rate",
    "PAYEMS": "payroll_employment",
    "FEDFUNDS": "federal_funds_rate",
    "TB3MS": "treasury_bill_3m",
    "CPIAUCSL": "cpi",
}

QUARTERLY_SERIES: Dict[str, str] = {
    "GDPC1": "real_gdp",
    "GDPPOT": "potential_gdp",
    "GCEC1": "real_government_consumption_investment",
}


def read_fred_series(series_id: str, value_name: str) -> pd.DataFrame:
    """Read one FRED series through the public CSV graph endpoint."""
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
    df = pd.read_csv(url)
    df.columns = ["date", value_name]
    df["date"] = pd.to_datetime(df["date"])
    df[value_name] = pd.to_numeric(df[value_name], errors="coerce")

    raw_file = RAW_DIR / f"{series_id}_{value_name}.csv"
    df.to_csv(raw_file, index=False)
    return df


def merge_frames(frames: list[pd.DataFrame]) -> pd.DataFrame:
    """Outer merge a list of date-indexed time series."""
    return reduce(lambda left, right: pd.merge(left, right, on="date", how="outer"), frames)


def build_monthly_panel() -> pd.DataFrame:
    frames = [read_fred_series(series_id, name) for series_id, name in MONTHLY_SERIES.items()]
    monthly = merge_frames(frames).sort_values("date")
    monthly = monthly.dropna(subset=["date"])

    monthly["recession_indicator"] = monthly["recession_indicator"].fillna(0).astype(int)
    monthly["policy_phase"] = monthly["recession_indicator"].map({1: "recession", 0: "expansion"})
    monthly["cpi_inflation_yoy_pct"] = monthly["cpi"].pct_change(12) * 100
    monthly["delta_unemployment_rate"] = monthly["unemployment_rate"] - monthly["unemployment_rate"].shift(1)
    monthly["delta_federal_funds_rate"] = monthly["federal_funds_rate"] - monthly["federal_funds_rate"].shift(1)
    monthly["payroll_growth_yoy_pct"] = monthly["payroll_employment"].pct_change(12) * 100

    monthly.to_csv(PROCESSED_DIR / "stabilization_policy_monthly_panel.csv", index=False)
    return monthly


def build_quarterly_panel(monthly: pd.DataFrame) -> pd.DataFrame:
    quarterly_frames = [
        read_fred_series(series_id, name) for series_id, name in QUARTERLY_SERIES.items()
    ]
    quarterly_core = merge_frames(quarterly_frames).sort_values("date")

    monthly_indexed = monthly.set_index("date").sort_index()

    quarterly_from_monthly = pd.DataFrame({
        "unemployment_rate": monthly_indexed["unemployment_rate"].resample("QS").mean(),
        "payroll_employment": monthly_indexed["payroll_employment"].resample("QS").mean(),
        "federal_funds_rate": monthly_indexed["federal_funds_rate"].resample("QS").mean(),
        "treasury_bill_3m": monthly_indexed["treasury_bill_3m"].resample("QS").mean(),
        "cpi": monthly_indexed["cpi"].resample("QS").mean(),
        "recession_indicator": monthly_indexed["recession_indicator"].resample("QS").max(),
    }).reset_index()

    quarterly = quarterly_core.merge(quarterly_from_monthly, on="date", how="outer")
    quarterly = quarterly.sort_values("date")

    quarterly["recession_indicator"] = quarterly["recession_indicator"].fillna(0).astype(int)
    quarterly["policy_phase"] = quarterly["recession_indicator"].map({1: "recession", 0: "expansion"})
    quarterly["real_gdp_growth_annualized"] = ((quarterly["real_gdp"] / quarterly["real_gdp"].shift(1)) ** 4 - 1) * 100
    quarterly["output_gap_pct"] = ((quarterly["real_gdp"] - quarterly["potential_gdp"]) / quarterly["potential_gdp"]) * 100
    quarterly["cpi_inflation_yoy_pct"] = quarterly["cpi"].pct_change(4) * 100
    quarterly["delta_unemployment_rate"] = quarterly["unemployment_rate"] - quarterly["unemployment_rate"].shift(1)
    quarterly["delta_federal_funds_rate"] = quarterly["federal_funds_rate"] - quarterly["federal_funds_rate"].shift(1)
    quarterly["payroll_growth_yoy_pct"] = quarterly["payroll_employment"].pct_change(4) * 100
    quarterly["gov_spending_growth_yoy_pct"] = quarterly["real_government_consumption_investment"].pct_change(4) * 100

    # Illustrative Taylor-rule-style benchmark:
    # i = r* + pi + 0.5(pi - pi*) + 0.5(output_gap)
    # where r* = 2 and pi* = 2. This is a teaching benchmark, not a policy prescription.
    r_star = 2.0
    pi_target = 2.0
    quarterly["taylor_rule_rate"] = (
        r_star
        + quarterly["cpi_inflation_yoy_pct"]
        + 0.5 * (quarterly["cpi_inflation_yoy_pct"] - pi_target)
        + 0.5 * quarterly["output_gap_pct"]
    )
    quarterly["policy_rate_gap"] = quarterly["federal_funds_rate"] - quarterly["taylor_rule_rate"]

    quarterly.to_csv(PROCESSED_DIR / "stabilization_policy_quarterly_panel.csv", index=False)
    return quarterly


def save_sqlite(monthly: pd.DataFrame, quarterly: pd.DataFrame) -> None:
    db_path = PROCESSED_DIR / "stabilization_policy.sqlite"
    with sqlite3.connect(db_path) as conn:
        monthly.to_sql("monthly_policy_indicators", conn, if_exists="replace", index=False)
        quarterly.to_sql("quarterly_policy_indicators", conn, if_exists="replace", index=False)

        conn.execute("""
        CREATE VIEW IF NOT EXISTS quarterly_policy_phase_summary AS
        SELECT
            policy_phase,
            COUNT(*) AS observations,
            AVG(real_gdp_growth_annualized) AS avg_real_gdp_growth_annualized,
            AVG(unemployment_rate) AS avg_unemployment_rate,
            AVG(output_gap_pct) AS avg_output_gap_pct,
            AVG(cpi_inflation_yoy_pct) AS avg_cpi_inflation_yoy_pct,
            AVG(federal_funds_rate) AS avg_federal_funds_rate,
            AVG(gov_spending_growth_yoy_pct) AS avg_gov_spending_growth_yoy_pct,
            AVG(policy_rate_gap) AS avg_policy_rate_gap
        FROM quarterly_policy_indicators
        GROUP BY policy_phase;
        """)


def main() -> None:
    monthly = build_monthly_panel()
    quarterly = build_quarterly_panel(monthly)
    save_sqlite(monthly, quarterly)

    print("Created:")
    print(f"  {PROCESSED_DIR / 'stabilization_policy_monthly_panel.csv'}")
    print(f"  {PROCESSED_DIR / 'stabilization_policy_quarterly_panel.csv'}")
    print(f"  {PROCESSED_DIR / 'stabilization_policy.sqlite'}")


if __name__ == "__main__":
    main()
