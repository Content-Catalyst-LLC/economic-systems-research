"""
Build stylized datasets for information, uncertainty, and imperfect markets.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_market_quality_types() -> pd.DataFrame:
    return pd.DataFrame([
        {"type": "high_quality", "share": 0.55, "value": 100, "reservation_value": 82, "quality_verifiability": 0.35},
        {"type": "medium_quality", "share": 0.30, "value": 72, "reservation_value": 58, "quality_verifiability": 0.45},
        {"type": "low_quality", "share": 0.15, "value": 38, "reservation_value": 24, "quality_verifiability": 0.25},
    ])


def build_credit_risk_types() -> pd.DataFrame:
    return pd.DataFrame([
        {"borrower_type": "safe_borrower", "share": 0.48, "default_probability": 0.03, "loss_given_default": 55, "productive_return": 12, "screening_cost": 4},
        {"borrower_type": "moderate_borrower", "share": 0.34, "default_probability": 0.09, "loss_given_default": 65, "productive_return": 16, "screening_cost": 6},
        {"borrower_type": "risky_borrower", "share": 0.18, "default_probability": 0.23, "loss_given_default": 85, "productive_return": 22, "screening_cost": 8},
    ])


def build_signaling_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"signal": "basic_warranty", "signal_strength": 0.42, "signal_cost_high_type": 6, "signal_cost_low_type": 9, "verification_strength": 0.45},
        {"signal": "third_party_certification", "signal_strength": 0.70, "signal_cost_high_type": 10, "signal_cost_low_type": 24, "verification_strength": 0.78},
        {"signal": "audited_disclosure", "signal_strength": 0.74, "signal_cost_high_type": 12, "signal_cost_low_type": 28, "verification_strength": 0.84},
        {"signal": "brand_reputation", "signal_strength": 0.62, "signal_cost_high_type": 18, "signal_cost_low_type": 26, "verification_strength": 0.55},
        {"signal": "cheap_green_claim", "signal_strength": 0.30, "signal_cost_high_type": 4, "signal_cost_low_type": 5, "verification_strength": 0.18},
        {"signal": "collateral_requirement", "signal_strength": 0.68, "signal_cost_high_type": 8, "signal_cost_low_type": 22, "verification_strength": 0.72},
    ])


def build_information_search_scenarios() -> pd.DataFrame:
    rows = []
    for info_level in range(0, 13):
        rows.append({
            "information_level": info_level,
            "benefit_information": 24 * __import__("math").log(info_level + 1),
            "cost_information": 1.65 * (info_level ** 2),
            "time_cost": 1.1 * info_level,
            "processing_cost": 0.75 * (info_level ** 1.6),
        })
    return pd.DataFrame(rows)


def build_uncertainty_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"action": "conservative_buffered", "good_case": 68, "moderate_case": 66, "bad_case": 58, "transition_case": 62, "systemic_crisis_case": 52},
        {"action": "balanced_resilient", "good_case": 78, "moderate_case": 72, "bad_case": 60, "transition_case": 68, "systemic_crisis_case": 56},
        {"action": "aggressive_optimized", "good_case": 98, "moderate_case": 74, "bad_case": 36, "transition_case": 46, "systemic_crisis_case": 22},
        {"action": "precautionary_redundant", "good_case": 72, "moderate_case": 70, "bad_case": 64, "transition_case": 70, "systemic_crisis_case": 60},
        {"action": "delayed_wait_and_see", "good_case": 82, "moderate_case": 60, "bad_case": 34, "transition_case": 38, "systemic_crisis_case": 26},
    ])


def build_consumer_complexity_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"market": "plain_language_savings_account", "complexity_index": 0.18, "hidden_fee_index": 0.08, "switching_cost_index": 0.12, "trust_index": 0.78, "disclosure_quality": 0.82},
        {"market": "credit_card_contract", "complexity_index": 0.68, "hidden_fee_index": 0.72, "switching_cost_index": 0.46, "trust_index": 0.44, "disclosure_quality": 0.40},
        {"market": "health_insurance_plan", "complexity_index": 0.86, "hidden_fee_index": 0.58, "switching_cost_index": 0.70, "trust_index": 0.46, "disclosure_quality": 0.38},
        {"market": "used_vehicle_market", "complexity_index": 0.62, "hidden_fee_index": 0.42, "switching_cost_index": 0.34, "trust_index": 0.48, "disclosure_quality": 0.44},
        {"market": "green_investment_product", "complexity_index": 0.74, "hidden_fee_index": 0.36, "switching_cost_index": 0.38, "trust_index": 0.50, "disclosure_quality": 0.42},
        {"market": "certified_energy_retrofit", "complexity_index": 0.46, "hidden_fee_index": 0.22, "switching_cost_index": 0.30, "trust_index": 0.66, "disclosure_quality": 0.70},
    ])


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "information_uncertainty_imperfect_markets.sqlite"
    names = [
        "market_quality_types",
        "credit_risk_types",
        "signaling_scenarios",
        "information_search_scenarios",
        "uncertainty_scenarios",
        "consumer_complexity_scenarios",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_market_quality_types(),
        build_credit_risk_types(),
        build_signaling_scenarios(),
        build_information_search_scenarios(),
        build_uncertainty_scenarios(),
        build_consumer_complexity_scenarios(),
    ]

    filenames = [
        "market_quality_types.csv",
        "credit_risk_types.csv",
        "signaling_scenarios.csv",
        "information_search_scenarios.csv",
        "uncertainty_scenarios.csv",
        "consumer_complexity_scenarios.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created information, uncertainty, and imperfect markets base data.")


if __name__ == "__main__":
    main()
