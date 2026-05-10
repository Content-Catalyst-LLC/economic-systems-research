"""
Compliance, access justice, enclosure risk, and institutional integrity.
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


def simulate_integrity(row: pd.Series, periods: int = 40) -> pd.DataFrame:
    integrity = 70.0
    rows = []

    for period in range(periods + 1):
        rows.append({
            "governance_scenario": row["scenario"],
            "period": period,
            "institutional_integrity": max(0, min(100, integrity)),
            "institutional_upkeep": row["institutional_upkeep"],
            "institutional_erosion": row["institutional_erosion"],
        })

        integrity = integrity + row["institutional_upkeep"] - row["institutional_erosion"]

    return pd.DataFrame(rows)


def main() -> None:
    governance = pd.read_csv(PROCESSED_DIR / "governance_scenarios.csv")
    users = pd.read_csv(PROCESSED_DIR / "user_extraction_profiles.csv")
    justice = pd.read_csv(PROCESSED_DIR / "access_justice_scenarios.csv")

    governance["compliance_score"] = (
        0.28 * governance["monitoring_capacity"]
        + 0.22 * governance["rule_clarity"]
        + 0.25 * governance["legitimacy"]
        + 0.15 * governance["sanction_capacity"]
        + 0.10 * (1 - governance["capture_risk"])
    )
    governance["adaptive_governance_score"] = (
        0.35 * governance["local_knowledge_use"]
        + 0.35 * governance["polycentric_coordination"]
        + 0.20 * governance["legitimacy"]
        + 0.10 * governance["monitoring_capacity"]
    )
    governance["governance_failure_risk"] = 1 - (
        0.30 * governance["compliance_score"]
        + 0.25 * governance["adaptive_governance_score"]
        + 0.20 * (1 - governance["capture_risk"])
        + 0.25 * governance["legitimacy"]
    )

    governance.to_csv(TABLE_DIR / "governance_compliance_results_python.csv", index=False)

    users["extraction_reduction"] = users["baseline_extraction"] - users["governed_extraction"]
    users["access_vulnerability_score"] = (1 - users["access_rights_index"]) * users["population_weight"]
    users.to_csv(TABLE_DIR / "user_extraction_access_results_python.csv", index=False)

    justice["commons_welfare_score"] = (
        0.30 * justice["preservation_score"]
        + 0.25 * justice["access_score"]
        + 0.25 * justice["justice_score"]
        + 0.20 * justice["maintenance_score"]
    )
    justice["enclosure_risk_score"] = (
        justice["preservation_score"] * 0.25
        + (1 - justice["access_score"]) * 0.35
        + (1 - justice["justice_score"]) * 0.30
        + (1 - justice["maintenance_score"]) * 0.10
    )
    justice.to_csv(TABLE_DIR / "access_justice_results_python.csv", index=False)

    integrity = pd.concat([simulate_integrity(row, 40) for _, row in governance.iterrows()], ignore_index=True)
    integrity.to_csv(TABLE_DIR / "institutional_integrity_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(governance["scenario"], governance["compliance_score"])
    ax.set_title("Compliance Score by Governance Scenario")
    ax.set_ylabel("Compliance score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "compliance_by_governance_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(justice["regime"], justice["commons_welfare_score"], label="Commons welfare")
    ax.plot(justice["regime"], justice["enclosure_risk_score"], marker="o", label="Enclosure risk")
    ax.set_title("Access, Justice, Preservation, and Enclosure Risk")
    ax.set_ylabel("Index")
    ax.tick_params(axis="x", rotation=35)
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "access_justice_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    for scenario, group in integrity.groupby("governance_scenario"):
        ax.plot(group["period"], group["institutional_integrity"], label=scenario)
    ax.set_title("Institutional Integrity Over Time")
    ax.set_xlabel("Period")
    ax.set_ylabel("Institutional integrity")
    ax.legend(fontsize=7)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "institutional_integrity_python.png", dpi=300)
    plt.close(fig)

    print(governance[["scenario", "compliance_score", "adaptive_governance_score", "governance_failure_risk"]])
    print(justice[["regime", "commons_welfare_score", "enclosure_risk_score"]])


if __name__ == "__main__":
    main()
