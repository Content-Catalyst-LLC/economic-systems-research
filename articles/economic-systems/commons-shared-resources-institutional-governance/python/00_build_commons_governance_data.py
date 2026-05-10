"""
Build stylized datasets for commons, shared resources, and institutional governance.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_resource_scenarios() -> pd.DataFrame:
    rows = [
        {"resource": "fishery", "initial_stock": 100.0, "carrying_capacity": 150.0, "regeneration_rate": 0.12, "critical_stock_threshold": 45.0},
        {"resource": "forest", "initial_stock": 120.0, "carrying_capacity": 180.0, "regeneration_rate": 0.08, "critical_stock_threshold": 70.0},
        {"resource": "groundwater_basin", "initial_stock": 90.0, "carrying_capacity": 110.0, "regeneration_rate": 0.045, "critical_stock_threshold": 55.0},
        {"resource": "urban_public_space", "initial_stock": 80.0, "carrying_capacity": 100.0, "regeneration_rate": 0.06, "critical_stock_threshold": 50.0},
        {"resource": "knowledge_commons", "initial_stock": 130.0, "carrying_capacity": 220.0, "regeneration_rate": 0.10, "critical_stock_threshold": 85.0},
        {"resource": "atmospheric_sink", "initial_stock": 75.0, "carrying_capacity": 100.0, "regeneration_rate": 0.025, "critical_stock_threshold": 60.0},
    ]
    return pd.DataFrame(rows)


def build_user_extraction_profiles() -> pd.DataFrame:
    rows = [
        {"user_group": "small_local_users", "baseline_extraction": 3.2, "governed_extraction": 2.4, "access_rights_index": 0.78, "compliance_tendency": 0.80, "population_weight": 0.28},
        {"user_group": "large_commercial_users", "baseline_extraction": 7.5, "governed_extraction": 4.6, "access_rights_index": 0.62, "compliance_tendency": 0.52, "population_weight": 0.18},
        {"user_group": "subsistence_users", "baseline_extraction": 2.4, "governed_extraction": 2.0, "access_rights_index": 0.58, "compliance_tendency": 0.72, "population_weight": 0.20},
        {"user_group": "public_institutions", "baseline_extraction": 1.5, "governed_extraction": 1.2, "access_rights_index": 0.70, "compliance_tendency": 0.78, "population_weight": 0.14},
        {"user_group": "informal_or_unrecognized_users", "baseline_extraction": 2.8, "governed_extraction": 2.2, "access_rights_index": 0.30, "compliance_tendency": 0.48, "population_weight": 0.12},
        {"user_group": "future_users", "baseline_extraction": 0.0, "governed_extraction": 0.0, "access_rights_index": 0.10, "compliance_tendency": 1.00, "population_weight": 0.08},
    ]
    return pd.DataFrame(rows)


def build_governance_scenarios() -> pd.DataFrame:
    rows = [
        {
            "scenario": "open_access_weak_governance",
            "monitoring_capacity": 0.20,
            "rule_clarity": 0.25,
            "legitimacy": 0.28,
            "sanction_capacity": 0.15,
            "capture_risk": 0.45,
            "local_knowledge_use": 0.30,
            "polycentric_coordination": 0.18,
            "institutional_upkeep": 1.2,
            "institutional_erosion": 3.8,
            "extraction_multiplier": 1.15,
        },
        {
            "scenario": "community_governance",
            "monitoring_capacity": 0.72,
            "rule_clarity": 0.76,
            "legitimacy": 0.82,
            "sanction_capacity": 0.58,
            "capture_risk": 0.22,
            "local_knowledge_use": 0.86,
            "polycentric_coordination": 0.42,
            "institutional_upkeep": 3.4,
            "institutional_erosion": 1.8,
            "extraction_multiplier": 0.82,
        },
        {
            "scenario": "state_regulation",
            "monitoring_capacity": 0.76,
            "rule_clarity": 0.80,
            "legitimacy": 0.60,
            "sanction_capacity": 0.74,
            "capture_risk": 0.32,
            "local_knowledge_use": 0.42,
            "polycentric_coordination": 0.55,
            "institutional_upkeep": 3.1,
            "institutional_erosion": 2.2,
            "extraction_multiplier": 0.78,
        },
        {
            "scenario": "polycentric_governance",
            "monitoring_capacity": 0.84,
            "rule_clarity": 0.78,
            "legitimacy": 0.80,
            "sanction_capacity": 0.70,
            "capture_risk": 0.18,
            "local_knowledge_use": 0.82,
            "polycentric_coordination": 0.88,
            "institutional_upkeep": 4.0,
            "institutional_erosion": 1.4,
            "extraction_multiplier": 0.70,
        },
        {
            "scenario": "enclosure_private_control",
            "monitoring_capacity": 0.78,
            "rule_clarity": 0.72,
            "legitimacy": 0.36,
            "sanction_capacity": 0.82,
            "capture_risk": 0.68,
            "local_knowledge_use": 0.28,
            "polycentric_coordination": 0.22,
            "institutional_upkeep": 2.6,
            "institutional_erosion": 2.8,
            "extraction_multiplier": 0.64,
        },
        {
            "scenario": "captured_governance",
            "monitoring_capacity": 0.56,
            "rule_clarity": 0.48,
            "legitimacy": 0.26,
            "sanction_capacity": 0.36,
            "capture_risk": 0.86,
            "local_knowledge_use": 0.20,
            "polycentric_coordination": 0.28,
            "institutional_upkeep": 1.8,
            "institutional_erosion": 4.4,
            "extraction_multiplier": 1.05,
        },
    ]
    return pd.DataFrame(rows)


def build_access_justice_scenarios() -> pd.DataFrame:
    rows = [
        {"regime": "open_access", "preservation_score": 0.34, "access_score": 0.72, "justice_score": 0.42, "maintenance_score": 0.28},
        {"regime": "community_commons", "preservation_score": 0.76, "access_score": 0.74, "justice_score": 0.78, "maintenance_score": 0.80},
        {"regime": "state_managed", "preservation_score": 0.72, "access_score": 0.62, "justice_score": 0.58, "maintenance_score": 0.70},
        {"regime": "polycentric", "preservation_score": 0.84, "access_score": 0.76, "justice_score": 0.82, "maintenance_score": 0.86},
        {"regime": "private_enclosure", "preservation_score": 0.70, "access_score": 0.32, "justice_score": 0.28, "maintenance_score": 0.64},
        {"regime": "captured_institution", "preservation_score": 0.42, "access_score": 0.38, "justice_score": 0.20, "maintenance_score": 0.34},
    ]
    return pd.DataFrame(rows)


def save_sqlite(resources, users, governance, justice) -> None:
    db_path = PROCESSED_DIR / "commons_governance.sqlite"
    with sqlite3.connect(db_path) as conn:
        resources.to_sql("resource_scenarios", conn, if_exists="replace", index=False)
        users.to_sql("user_extraction_profiles", conn, if_exists="replace", index=False)
        governance.to_sql("governance_scenarios", conn, if_exists="replace", index=False)
        justice.to_sql("access_justice_scenarios", conn, if_exists="replace", index=False)


def main() -> None:
    resources = build_resource_scenarios()
    users = build_user_extraction_profiles()
    governance = build_governance_scenarios()
    justice = build_access_justice_scenarios()

    resources.to_csv(PROCESSED_DIR / "resource_scenarios.csv", index=False)
    users.to_csv(PROCESSED_DIR / "user_extraction_profiles.csv", index=False)
    governance.to_csv(PROCESSED_DIR / "governance_scenarios.csv", index=False)
    justice.to_csv(PROCESSED_DIR / "access_justice_scenarios.csv", index=False)

    save_sqlite(resources, users, governance, justice)
    print("Created commons governance base data.")


if __name__ == "__main__":
    main()
