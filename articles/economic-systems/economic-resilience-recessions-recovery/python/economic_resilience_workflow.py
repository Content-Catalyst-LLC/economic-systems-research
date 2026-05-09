from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"

DATA_DIR.mkdir(parents=True, exist_ok=True)
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SERIES = {
    "UNRATE": "unemployment_rate",
    "GDPC1": "real_gdp",
    "FEDFUNDS": "federal_funds_rate",
    "USREC": "recession_indicator",
}

def read_fred_csv(series_id: str, value_name: str) -> pd.DataFrame:
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
    df = pd.read_csv(url)
    df.columns = ["date", value_name]
    df["date"] = pd.to_datetime(df["date"])
    df[value_name] = pd.to_numeric(df[value_name], errors="coerce")
    return df

def main() -> None:
    frames = [
        read_fred_csv(series_id, value_name)
        for series_id, value_name in SERIES.items()
    ]

    combined = frames[0]
    for frame in frames[1:]:
        combined = combined.merge(frame, on="date", how="outer")

    combined = combined.sort_values("date")

    combined["real_gdp_growth_annualized"] = combined["real_gdp"].pct_change() * 400

    combined["unemployment_12m_low"] = (
        combined["unemployment_rate"].rolling(window=12, min_periods=3).min()
    )

    combined["unemployment_gap_from_12m_low"] = (
        combined["unemployment_rate"] - combined["unemployment_12m_low"]
    )

    output_file = OUTPUT_DIR / "economic_resilience_indicators.csv"
    combined.to_csv(output_file, index=False)

    recent = combined.dropna(subset=["unemployment_rate"]).tail(24)
    recent.to_csv(OUTPUT_DIR / "recent_resilience_snapshot.csv", index=False)

    print(f"Saved: {output_file}")

if __name__ == "__main__":
    main()
