"""
Build stylized datasets for labor, wages, productivity, and the social organization of work.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_sector_labor_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"sector": "manufacturing", "output": 1250, "hours_worked": 210, "total_wages": 520, "employment_quality_index": 0.68, "care_intensity": 0.18},
        {"sector": "logistics", "output": 980, "hours_worked": 230, "total_wages": 410, "employment_quality_index": 0.52, "care_intensity": 0.12},
        {"sector": "health_care", "output": 1120, "hours_worked": 260, "total_wages": 560, "employment_quality_index": 0.60, "care_intensity": 0.86},
        {"sector": "education", "output": 900, "hours_worked": 245, "total_wages": 500, "employment_quality_index": 0.62, "care_intensity": 0.72},
        {"sector": "digital_platform_services", "output": 1450, "hours_worked": 180, "total_wages": 460, "employment_quality_index": 0.48, "care_intensity": 0.10},
        {"sector": "public_infrastructure_maintenance", "output": 1020, "hours_worked": 240, "total_wages": 540, "employment_quality_index": 0.74, "care_intensity": 0.30},
        {"sector": "retail_and_food_service", "output": 760, "hours_worked": 260, "total_wages": 330, "employment_quality_index": 0.38, "care_intensity": 0.42},
    ])


def build_wage_productivity_time_series() -> pd.DataFrame:
    rows = []
    years = list(range(2000, 2026))
    for idx, year in enumerate(years):
        productivity_index = 100 * (1.022 ** idx)
        wage_index = 100 * (1.012 ** idx)
        compensation_with_strong_bargaining = 100 * (1.020 ** idx)
        rows.append({
            "year": year,
            "productivity_index": productivity_index,
            "wage_index": wage_index,
            "compensation_with_strong_bargaining": compensation_with_strong_bargaining,
            "union_density_index": max(45, 100 - 1.7 * idx),
            "labor_market_tightness": 0.48 + 0.18 * (idx % 8) / 7,
        })
    return pd.DataFrame(rows)


def build_household_reproduction_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"household_type": "single_worker_low_wage", "wage_income": 2300, "social_support": 250, "household_cost": 2200, "care_reproduction_cost": 460, "dependents": 0},
        {"household_type": "single_parent_service_worker", "wage_income": 2800, "social_support": 550, "household_cost": 2600, "care_reproduction_cost": 1050, "dependents": 2},
        {"household_type": "dual_worker_median_income", "wage_income": 6200, "social_support": 150, "household_cost": 4300, "care_reproduction_cost": 1400, "dependents": 2},
        {"household_type": "care_worker_multigenerational", "wage_income": 3400, "social_support": 450, "household_cost": 3000, "care_reproduction_cost": 1650, "dependents": 3},
        {"household_type": "professional_high_income", "wage_income": 9800, "social_support": 0, "household_cost": 6100, "care_reproduction_cost": 1100, "dependents": 1},
        {"household_type": "precarious_platform_worker", "wage_income": 2600, "social_support": 200, "household_cost": 2450, "care_reproduction_cost": 720, "dependents": 1},
    ])


def build_time_use_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"worker_group": "standard_full_time", "paid_work_time": 8.5, "care_time": 1.5, "household_time": 2.0, "commute_time": 1.0},
        {"worker_group": "single_parent_service_worker", "paid_work_time": 8.0, "care_time": 4.5, "household_time": 2.5, "commute_time": 1.5},
        {"worker_group": "long_commute_worker", "paid_work_time": 9.0, "care_time": 1.5, "household_time": 2.0, "commute_time": 2.5},
        {"worker_group": "gig_worker_fragmented_schedule", "paid_work_time": 9.5, "care_time": 2.5, "household_time": 2.2, "commute_time": 1.3},
        {"worker_group": "care_worker_double_shift", "paid_work_time": 8.0, "care_time": 5.0, "household_time": 2.4, "commute_time": 1.0},
        {"worker_group": "remote_professional", "paid_work_time": 8.8, "care_time": 1.8, "household_time": 1.6, "commute_time": 0.2},
    ])


def build_bargaining_institution_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "weak_bargaining_low_support", "labor_productivity": 6.2, "bargaining_power": 0.22, "institutional_support": 0.25, "outside_option": 0.30},
        {"scenario": "tight_labor_market", "labor_productivity": 6.2, "bargaining_power": 0.48, "institutional_support": 0.38, "outside_option": 0.58},
        {"scenario": "union_sectoral_bargaining", "labor_productivity": 6.2, "bargaining_power": 0.76, "institutional_support": 0.78, "outside_option": 0.62},
        {"scenario": "strong_social_wage", "labor_productivity": 6.2, "bargaining_power": 0.58, "institutional_support": 0.84, "outside_option": 0.74},
        {"scenario": "monopsony_local_labor_market", "labor_productivity": 6.2, "bargaining_power": 0.18, "institutional_support": 0.32, "outside_option": 0.20},
        {"scenario": "high_skill_high_mobility", "labor_productivity": 8.4, "bargaining_power": 0.70, "institutional_support": 0.52, "outside_option": 0.80},
    ])


def build_automation_shock_scenarios() -> pd.DataFrame:
    return pd.DataFrame([
        {"scenario": "worker_augmenting_automation", "automation_intensity": 0.62, "productivity_gain": 0.28, "employment_effect": -0.02, "wage_share_effect": 0.04, "quality_effect": 0.08},
        {"scenario": "labor_displacing_automation", "automation_intensity": 0.74, "productivity_gain": 0.34, "employment_effect": -0.18, "wage_share_effect": -0.10, "quality_effect": -0.06},
        {"scenario": "surveillance_intensification", "automation_intensity": 0.58, "productivity_gain": 0.18, "employment_effect": -0.05, "wage_share_effect": -0.06, "quality_effect": -0.18},
        {"scenario": "public_transition_support", "automation_intensity": 0.65, "productivity_gain": 0.30, "employment_effect": -0.04, "wage_share_effect": 0.02, "quality_effect": 0.10},
        {"scenario": "platform_fragmentation", "automation_intensity": 0.54, "productivity_gain": 0.16, "employment_effect": 0.05, "wage_share_effect": -0.12, "quality_effect": -0.22},
        {"scenario": "care_technology_support", "automation_intensity": 0.36, "productivity_gain": 0.12, "employment_effect": 0.02, "wage_share_effect": 0.03, "quality_effect": 0.15},
    ])


def save_sqlite(*tables) -> None:
    db_path = PROCESSED_DIR / "labor_wages_productivity_work.sqlite"
    names = [
        "sector_labor_scenarios",
        "wage_productivity_time_series",
        "household_reproduction_scenarios",
        "time_use_scenarios",
        "bargaining_institution_scenarios",
        "automation_shock_scenarios",
    ]
    with sqlite3.connect(db_path) as conn:
        for name, table in zip(names, tables):
            table.to_sql(name, conn, if_exists="replace", index=False)


def main() -> None:
    tables = [
        build_sector_labor_scenarios(),
        build_wage_productivity_time_series(),
        build_household_reproduction_scenarios(),
        build_time_use_scenarios(),
        build_bargaining_institution_scenarios(),
        build_automation_shock_scenarios(),
    ]

    filenames = [
        "sector_labor_scenarios.csv",
        "wage_productivity_time_series.csv",
        "household_reproduction_scenarios.csv",
        "time_use_scenarios.csv",
        "bargaining_institution_scenarios.csv",
        "automation_shock_scenarios.csv",
    ]

    for table, filename in zip(tables, filenames):
        table.to_csv(PROCESSED_DIR / filename, index=False)

    save_sqlite(*tables)
    print("Created labor, wages, productivity, and work organization base data.")


if __name__ == "__main__":
    main()
