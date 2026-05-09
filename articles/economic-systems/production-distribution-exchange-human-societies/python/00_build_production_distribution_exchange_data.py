"""
Build stylized production, distribution, and exchange datasets.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


SECTORS = [
    {
        "sector_code": "agriculture",
        "sector": "Agriculture and Food Systems",
        "institutional_role": "Food production, land use, rural livelihoods, and ecological dependence",
        "labor_share": 0.45,
        "non_labor_share": 0.35,
        "public_or_mixed_share": 0.20,
        "public_goods_dependence": 0.70,
        "ecological_intensity": 0.82,
        "employment_intensity": 0.48,
        "trade_exposure": 0.46,
    },
    {
        "sector_code": "manufacturing",
        "sector": "Manufacturing",
        "institutional_role": "Transformation of materials into goods, machinery, and capital equipment",
        "labor_share": 0.38,
        "non_labor_share": 0.42,
        "public_or_mixed_share": 0.20,
        "public_goods_dependence": 0.66,
        "ecological_intensity": 0.74,
        "employment_intensity": 0.36,
        "trade_exposure": 0.72,
    },
    {
        "sector_code": "services",
        "sector": "Market Services",
        "institutional_role": "Commercial services, logistics, information, retail, and professional coordination",
        "labor_share": 0.58,
        "non_labor_share": 0.30,
        "public_or_mixed_share": 0.12,
        "public_goods_dependence": 0.58,
        "ecological_intensity": 0.28,
        "employment_intensity": 0.62,
        "trade_exposure": 0.34,
    },
    {
        "sector_code": "public_goods",
        "sector": "Public Goods and Social Provision",
        "institutional_role": "Education, health, public administration, law, science, and infrastructure support",
        "labor_share": 0.68,
        "non_labor_share": 0.07,
        "public_or_mixed_share": 0.25,
        "public_goods_dependence": 0.95,
        "ecological_intensity": 0.22,
        "employment_intensity": 0.70,
        "trade_exposure": 0.18,
    },
    {
        "sector_code": "care_reproduction",
        "sector": "Care and Social Reproduction",
        "institutional_role": "Household support, elder care, child care, disability support, and reproductive labor",
        "labor_share": 0.76,
        "non_labor_share": 0.08,
        "public_or_mixed_share": 0.16,
        "public_goods_dependence": 0.80,
        "ecological_intensity": 0.16,
        "employment_intensity": 0.84,
        "trade_exposure": 0.08,
    },
    {
        "sector_code": "ecological_repair",
        "sector": "Ecological Repair and Maintenance",
        "institutional_role": "Restoration, adaptation, pollution control, maintenance, and environmental protection",
        "labor_share": 0.60,
        "non_labor_share": 0.12,
        "public_or_mixed_share": 0.28,
        "public_goods_dependence": 0.88,
        "ecological_intensity": -0.30,
        "employment_intensity": 0.52,
        "trade_exposure": 0.20,
    },
]


def build_input_output_matrix() -> pd.DataFrame:
    sector_codes = [item["sector_code"] for item in SECTORS]

    # Rows are supplying sectors; columns are purchasing sectors.
    matrix = np.array([
        [0.18, 0.08, 0.05, 0.06, 0.08, 0.04],
        [0.12, 0.20, 0.10, 0.08, 0.06, 0.14],
        [0.08, 0.12, 0.22, 0.14, 0.12, 0.10],
        [0.06, 0.06, 0.10, 0.18, 0.12, 0.10],
        [0.04, 0.04, 0.08, 0.10, 0.18, 0.06],
        [0.05, 0.05, 0.04, 0.06, 0.06, 0.16],
    ])

    return pd.DataFrame(matrix, index=sector_codes, columns=sector_codes)


def build_final_demand_scenarios() -> pd.DataFrame:
    rows = [
        {"scenario": "baseline", "agriculture": 90, "manufacturing": 150, "services": 190, "public_goods": 120, "care_reproduction": 90, "ecological_repair": 45},
        {"scenario": "export_manufacturing_expansion", "agriculture": 92, "manufacturing": 210, "services": 200, "public_goods": 120, "care_reproduction": 90, "ecological_repair": 45},
        {"scenario": "public_goods_expansion", "agriculture": 92, "manufacturing": 155, "services": 195, "public_goods": 170, "care_reproduction": 105, "ecological_repair": 60},
        {"scenario": "care_centered_economy", "agriculture": 95, "manufacturing": 145, "services": 185, "public_goods": 145, "care_reproduction": 145, "ecological_repair": 65},
        {"scenario": "ecological_transition", "agriculture": 88, "manufacturing": 155, "services": 190, "public_goods": 145, "care_reproduction": 105, "ecological_repair": 115},
        {"scenario": "austerity_fragility", "agriculture": 88, "manufacturing": 145, "services": 180, "public_goods": 85, "care_reproduction": 70, "ecological_repair": 25},
    ]
    return pd.DataFrame(rows)


def save_sqlite(sectors: pd.DataFrame, io_long: pd.DataFrame, scenarios: pd.DataFrame) -> None:
    db_path = PROCESSED_DIR / "production_distribution_exchange.sqlite"
    with sqlite3.connect(db_path) as conn:
        sectors.to_sql("production_sectors", conn, if_exists="replace", index=False)
        io_long.to_sql("input_output_requirements", conn, if_exists="replace", index=False)
        scenarios.to_sql("final_demand_exchange_scenarios", conn, if_exists="replace", index=False)


def main() -> None:
    sectors = pd.DataFrame(SECTORS)
    io_matrix = build_input_output_matrix()
    scenarios = build_final_demand_scenarios()

    io_long = (
        io_matrix.reset_index(names="supplying_sector")
        .melt(id_vars="supplying_sector", var_name="purchasing_sector", value_name="input_requirement")
    )

    sectors.to_csv(PROCESSED_DIR / "production_sectors.csv", index=False)
    io_matrix.to_csv(PROCESSED_DIR / "input_output_matrix.csv")
    io_long.to_csv(PROCESSED_DIR / "input_output_matrix_long.csv", index=False)
    scenarios.to_csv(PROCESSED_DIR / "final_demand_exchange_scenarios.csv", index=False)

    save_sqlite(sectors, io_long, scenarios)
    print("Created production, distribution, and exchange base data.")


if __name__ == "__main__":
    main()
