"""
Build stylized datasets for externalities, public goods, and collective provision.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_externality_scenarios() -> pd.DataFrame:
    rows = [
        {
            "scenario": "baseline_pollution_externality",
            "mpc_intercept": 10.0,
            "mpc_slope": 0.20,
            "mec_intercept": 2.0,
            "mec_slope": 0.05,
            "mpb_intercept": 40.0,
            "mpb_slope": -0.25,
            "meb_intercept": 0.0,
            "meb_slope": 0.00,
            "critical_threshold": 35.0,
        },
        {
            "scenario": "high_external_damage",
            "mpc_intercept": 9.0,
            "mpc_slope": 0.18,
            "mec_intercept": 4.0,
            "mec_slope": 0.09,
            "mpb_intercept": 42.0,
            "mpb_slope": -0.24,
            "meb_intercept": 0.0,
            "meb_slope": 0.00,
            "critical_threshold": 30.0,
        },
        {
            "scenario": "knowledge_spillover",
            "mpc_intercept": 14.0,
            "mpc_slope": 0.10,
            "mec_intercept": 0.0,
            "mec_slope": 0.00,
            "mpb_intercept": 30.0,
            "mpb_slope": -0.18,
            "meb_intercept": 8.0,
            "meb_slope": -0.02,
            "critical_threshold": 999.0,
        },
        {
            "scenario": "public_health_preparedness",
            "mpc_intercept": 16.0,
            "mpc_slope": 0.08,
            "mec_intercept": 0.0,
            "mec_slope": 0.00,
            "mpb_intercept": 26.0,
            "mpb_slope": -0.12,
            "meb_intercept": 12.0,
            "meb_slope": -0.03,
            "critical_threshold": 999.0,
        },
        {
            "scenario": "ecological_threshold_risk",
            "mpc_intercept": 8.0,
            "mpc_slope": 0.16,
            "mec_intercept": 3.5,
            "mec_slope": 0.12,
            "mpb_intercept": 38.0,
            "mpb_slope": -0.22,
            "meb_intercept": 0.0,
            "meb_slope": 0.00,
            "critical_threshold": 24.0,
        },
    ]
    return pd.DataFrame(rows)


def build_public_good_scenarios() -> pd.DataFrame:
    rows = [
        {"public_good": "basic_research", "private_benefit": 18, "external_benefit": 42, "private_cost": 36, "social_need": 85, "voluntary_provision": 34},
        {"public_good": "public_health_surveillance", "private_benefit": 22, "external_benefit": 50, "private_cost": 38, "social_need": 90, "voluntary_provision": 30},
        {"public_good": "flood_control", "private_benefit": 26, "external_benefit": 44, "private_cost": 41, "social_need": 88, "voluntary_provision": 42},
        {"public_good": "clean_air_monitoring", "private_benefit": 15, "external_benefit": 58, "private_cost": 35, "social_need": 92, "voluntary_provision": 28},
        {"public_good": "public_transit_resilience", "private_benefit": 30, "external_benefit": 36, "private_cost": 44, "social_need": 80, "voluntary_provision": 46},
        {"public_good": "ecological_restoration", "private_benefit": 12, "external_benefit": 64, "private_cost": 40, "social_need": 95, "voluntary_provision": 24},
    ]
    return pd.DataFrame(rows)


def build_contribution_scenarios() -> pd.DataFrame:
    rows = [
        {"scenario": "voluntary_fragmented", "contributor_group": "large_firms", "contribution": 16, "benefit_share": 0.28},
        {"scenario": "voluntary_fragmented", "contributor_group": "small_firms", "contribution": 5, "benefit_share": 0.18},
        {"scenario": "voluntary_fragmented", "contributor_group": "high_income_households", "contribution": 9, "benefit_share": 0.16},
        {"scenario": "voluntary_fragmented", "contributor_group": "low_income_households", "contribution": 0, "benefit_share": 0.14},
        {"scenario": "voluntary_fragmented", "contributor_group": "local_government", "contribution": 8, "benefit_share": 0.14},
        {"scenario": "voluntary_fragmented", "contributor_group": "future_generations", "contribution": 0, "benefit_share": 0.10},

        {"scenario": "mandated_contribution", "contributor_group": "large_firms", "contribution": 30, "benefit_share": 0.28},
        {"scenario": "mandated_contribution", "contributor_group": "small_firms", "contribution": 12, "benefit_share": 0.18},
        {"scenario": "mandated_contribution", "contributor_group": "high_income_households", "contribution": 16, "benefit_share": 0.16},
        {"scenario": "mandated_contribution", "contributor_group": "low_income_households", "contribution": 4, "benefit_share": 0.14},
        {"scenario": "mandated_contribution", "contributor_group": "local_government", "contribution": 22, "benefit_share": 0.14},
        {"scenario": "mandated_contribution", "contributor_group": "future_generations", "contribution": 0, "benefit_share": 0.10},

        {"scenario": "progressive_public_finance", "contributor_group": "large_firms", "contribution": 38, "benefit_share": 0.28},
        {"scenario": "progressive_public_finance", "contributor_group": "small_firms", "contribution": 10, "benefit_share": 0.18},
        {"scenario": "progressive_public_finance", "contributor_group": "high_income_households", "contribution": 26, "benefit_share": 0.16},
        {"scenario": "progressive_public_finance", "contributor_group": "low_income_households", "contribution": 2, "benefit_share": 0.14},
        {"scenario": "progressive_public_finance", "contributor_group": "local_government", "contribution": 26, "benefit_share": 0.14},
        {"scenario": "progressive_public_finance", "contributor_group": "future_generations", "contribution": 0, "benefit_share": 0.10},
    ]
    return pd.DataFrame(rows)


def build_collective_finance_scenarios() -> pd.DataFrame:
    rows = [
        {"scenario": "austerity_low_capacity", "tax_revenue": 45, "borrowing_capacity": 10, "pooled_funds": 8, "maintenance_need": 90, "preparedness_need": 80},
        {"scenario": "baseline_mixed_finance", "tax_revenue": 70, "borrowing_capacity": 25, "pooled_funds": 12, "maintenance_need": 90, "preparedness_need": 80},
        {"scenario": "high_capacity_public_finance", "tax_revenue": 95, "borrowing_capacity": 45, "pooled_funds": 18, "maintenance_need": 90, "preparedness_need": 80},
        {"scenario": "pooled_resilience_fund", "tax_revenue": 78, "borrowing_capacity": 30, "pooled_funds": 36, "maintenance_need": 90, "preparedness_need": 80},
        {"scenario": "crisis_after_underinvestment", "tax_revenue": 62, "borrowing_capacity": 60, "pooled_funds": 10, "maintenance_need": 125, "preparedness_need": 115},
    ]
    return pd.DataFrame(rows)


def build_burden_distribution_groups() -> pd.DataFrame:
    rows = [
        {"group": "high_income_low_exposure", "income_index": 0.92, "exposure_index": 0.28, "political_voice_index": 0.82, "population_weight": 0.18},
        {"group": "middle_income_suburban", "income_index": 0.62, "exposure_index": 0.42, "political_voice_index": 0.60, "population_weight": 0.26},
        {"group": "low_income_pollution_exposed", "income_index": 0.34, "exposure_index": 0.86, "political_voice_index": 0.32, "population_weight": 0.22},
        {"group": "infrastructure_fragile_region", "income_index": 0.42, "exposure_index": 0.78, "political_voice_index": 0.38, "population_weight": 0.16},
        {"group": "climate_exposed_coastal_or_rural", "income_index": 0.46, "exposure_index": 0.82, "political_voice_index": 0.42, "population_weight": 0.12},
        {"group": "future_generations", "income_index": 0.50, "exposure_index": 0.90, "political_voice_index": 0.05, "population_weight": 0.06},
    ]
    return pd.DataFrame(rows)


def save_sqlite(externalities, public_goods, contributions, finance, burden) -> None:
    db_path = PROCESSED_DIR / "externalities_public_goods_collective_provision.sqlite"
    with sqlite3.connect(db_path) as conn:
        externalities.to_sql("externality_scenarios", conn, if_exists="replace", index=False)
        public_goods.to_sql("public_good_scenarios", conn, if_exists="replace", index=False)
        contributions.to_sql("contribution_scenarios", conn, if_exists="replace", index=False)
        finance.to_sql("collective_finance_scenarios", conn, if_exists="replace", index=False)
        burden.to_sql("burden_distribution_groups", conn, if_exists="replace", index=False)


def main() -> None:
    externalities = build_externality_scenarios()
    public_goods = build_public_good_scenarios()
    contributions = build_contribution_scenarios()
    finance = build_collective_finance_scenarios()
    burden = build_burden_distribution_groups()

    externalities.to_csv(PROCESSED_DIR / "externality_scenarios.csv", index=False)
    public_goods.to_csv(PROCESSED_DIR / "public_good_scenarios.csv", index=False)
    contributions.to_csv(PROCESSED_DIR / "contribution_scenarios.csv", index=False)
    finance.to_csv(PROCESSED_DIR / "collective_finance_scenarios.csv", index=False)
    burden.to_csv(PROCESSED_DIR / "burden_distribution_groups.csv", index=False)

    save_sqlite(externalities, public_goods, contributions, finance, burden)
    print("Created externalities, public goods, and collective provision base data.")


if __name__ == "__main__":
    main()
