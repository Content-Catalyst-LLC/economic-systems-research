"""
Build stylized economic-system data for the article companion.

This script creates:
1. Sector metadata
2. Input-output requirements matrix
3. Final-demand scenarios
4. Allocation profiles
5. Distribution metrics
6. Reproduction parameters
7. SQLite database
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
TABLE_DIR = BASE_DIR / "outputs" / "tables"

for directory in [PROCESSED_DIR, TABLE_DIR]:
    directory.mkdir(parents=True, exist_ok=True)


SECTORS = [
    {
        "sector_code": "energy",
        "sector": "Energy",
        "institutional_role": "Material and energetic foundation of production",
        "wage_share": 0.42,
        "profit_share": 0.28,
        "public_or_mixed_share": 0.30,
        "ecological_intensity": 0.85,
        "employment_intensity": 0.18,
    },
    {
        "sector_code": "manufacturing",
        "sector": "Manufacturing",
        "institutional_role": "Transformation of materials into goods and capital equipment",
        "wage_share": 0.50,
        "profit_share": 0.32,
        "public_or_mixed_share": 0.18,
        "ecological_intensity": 0.65,
        "employment_intensity": 0.32,
    },
    {
        "sector_code": "services",
        "sector": "Services",
        "institutional_role": "Market and non-market services supporting everyday life",
        "wage_share": 0.62,
        "profit_share": 0.25,
        "public_or_mixed_share": 0.13,
        "ecological_intensity": 0.30,
        "employment_intensity": 0.56,
    },
    {
        "sector_code": "public_care",
        "sector": "Public Care and Social Reproduction",
        "institutional_role": "Health, education, care, household support, and social capability",
        "wage_share": 0.70,
        "profit_share": 0.05,
        "public_or_mixed_share": 0.25,
        "ecological_intensity": 0.20,
        "employment_intensity": 0.72,
    },
    {
        "sector_code": "restoration",
        "sector": "Ecological Restoration and Maintenance",
        "institutional_role": "Repair, maintenance, climate adaptation, and ecological reproduction",
        "wage_share": 0.58,
        "profit_share": 0.12,
        "public_or_mixed_share": 0.30,
        "ecological_intensity": -0.25,
        "employment_intensity": 0.44,
    },
]


def build_input_output_matrix() -> pd.DataFrame:
    sector_codes = [item["sector_code"] for item in SECTORS]

    # Rows are supplying sectors; columns are purchasing sectors.
    matrix = np.array([
        [0.18, 0.16, 0.08, 0.07, 0.10],
        [0.12, 0.22, 0.10, 0.08, 0.12],
        [0.08, 0.12, 0.20, 0.14, 0.10],
        [0.05, 0.05, 0.10, 0.18, 0.08],
        [0.04, 0.06, 0.05, 0.06, 0.16],
    ])

    return pd.DataFrame(matrix, index=sector_codes, columns=sector_codes)


def build_final_demand() -> pd.DataFrame:
    rows = [
        {"scenario": "baseline", "energy": 80, "manufacturing": 130, "services": 170, "public_care": 110, "restoration": 50},
        {"scenario": "manufacturing_expansion", "energy": 85, "manufacturing": 170, "services": 175, "public_care": 110, "restoration": 55},
        {"scenario": "public_care_expansion", "energy": 82, "manufacturing": 130, "services": 175, "public_care": 155, "restoration": 60},
        {"scenario": "green_restoration_expansion", "energy": 78, "manufacturing": 140, "services": 175, "public_care": 120, "restoration": 100},
        {"scenario": "austerity_and_undermaintenance", "energy": 75, "manufacturing": 120, "services": 160, "public_care": 80, "restoration": 30},
    ]
    return pd.DataFrame(rows)


def build_allocation_profiles() -> pd.DataFrame:
    rows = [
        {
            "scenario": "baseline",
            "consumption_share": 0.55,
            "investment_share": 0.20,
            "public_provision_share": 0.17,
            "restoration_share": 0.08,
        },
        {
            "scenario": "consumption_heavy",
            "consumption_share": 0.68,
            "investment_share": 0.14,
            "public_provision_share": 0.13,
            "restoration_share": 0.05,
        },
        {
            "scenario": "developmental_investment",
            "consumption_share": 0.48,
            "investment_share": 0.28,
            "public_provision_share": 0.16,
            "restoration_share": 0.08,
        },
        {
            "scenario": "social_ecological_repair",
            "consumption_share": 0.48,
            "investment_share": 0.20,
            "public_provision_share": 0.20,
            "restoration_share": 0.12,
        },
    ]

    return pd.DataFrame(rows)


def build_reproduction_parameters() -> pd.DataFrame:
    rows = [
        {
            "scenario": "baseline",
            "initial_produced_capital": 1000.0,
            "initial_natural_capital": 1000.0,
            "investment": 65.0,
            "depreciation_rate": 0.05,
            "regeneration": 25.0,
            "depletion": 30.0,
            "periods": 25,
        },
        {
            "scenario": "underinvestment_and_depletion",
            "initial_produced_capital": 1000.0,
            "initial_natural_capital": 1000.0,
            "investment": 40.0,
            "depreciation_rate": 0.06,
            "regeneration": 15.0,
            "depletion": 40.0,
            "periods": 25,
        },
        {
            "scenario": "repair_and_maintenance",
            "initial_produced_capital": 1000.0,
            "initial_natural_capital": 1000.0,
            "investment": 75.0,
            "depreciation_rate": 0.045,
            "regeneration": 45.0,
            "depletion": 25.0,
            "periods": 25,
        },
    ]

    return pd.DataFrame(rows)


def save_sqlite(
    sectors: pd.DataFrame,
    io_matrix_long: pd.DataFrame,
    final_demand: pd.DataFrame,
    allocation: pd.DataFrame,
    reproduction: pd.DataFrame,
) -> None:
    db_path = PROCESSED_DIR / "economic_system.sqlite"
    with sqlite3.connect(db_path) as conn:
        sectors.to_sql("sectors", conn, if_exists="replace", index=False)
        io_matrix_long.to_sql("input_output_requirements", conn, if_exists="replace", index=False)
        final_demand.to_sql("final_demand_scenarios", conn, if_exists="replace", index=False)
        allocation.to_sql("allocation_profiles", conn, if_exists="replace", index=False)
        reproduction.to_sql("reproduction_parameters", conn, if_exists="replace", index=False)


def main() -> None:
    sectors = pd.DataFrame(SECTORS)
    io_matrix = build_input_output_matrix()
    final_demand = build_final_demand()
    allocation = build_allocation_profiles()
    reproduction = build_reproduction_parameters()

    io_long = (
        io_matrix.reset_index(names="supplying_sector")
        .melt(id_vars="supplying_sector", var_name="purchasing_sector", value_name="input_requirement")
    )

    sectors.to_csv(PROCESSED_DIR / "economic_system_sectors.csv", index=False)
    io_matrix.to_csv(PROCESSED_DIR / "input_output_matrix.csv")
    io_long.to_csv(PROCESSED_DIR / "input_output_matrix_long.csv", index=False)
    final_demand.to_csv(PROCESSED_DIR / "final_demand_scenarios.csv", index=False)
    allocation.to_csv(PROCESSED_DIR / "allocation_profiles.csv", index=False)
    reproduction.to_csv(PROCESSED_DIR / "reproduction_parameters.csv", index=False)

    save_sqlite(sectors, io_long, final_demand, allocation, reproduction)

    print("Created economic-system base data.")


if __name__ == "__main__":
    main()
