"""
Life-course risk, care systems, fiscal capacity, digital administration, and adaptive social protection.
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


def main() -> None:
    life = pd.read_csv(PROCESSED_DIR / "life_course_risk.csv")
    care = pd.read_csv(PROCESSED_DIR / "care_family_policy.csv")
    fiscal = pd.read_csv(PROCESSED_DIR / "fiscal_capacity.csv")
    digital = pd.read_csv(PROCESSED_DIR / "digital_administration.csv")
    adaptive = pd.read_csv(PROCESSED_DIR / "adaptive_protection.csv")

    life["vulnerability_reduction"] = life["baseline_vulnerability"] - life["protected_vulnerability"]
    life["life_course_protection_score"] = (
        0.24 * life["vulnerability_reduction"]
        + 0.20 * life["coverage"]
        + 0.20 * life["adequacy"]
        + 0.18 * life["duration_support"]
        + 0.18 * life["service_integration"]
    )
    life.to_csv(TABLE_DIR / "life_course_risk_results_python.csv", index=False)

    care["care_system_strength"] = (
        0.18 * care["childcare_support"]
        + 0.16 * care["paid_leave"]
        + 0.14 * care["eldercare_support"]
        + 0.14 * care["disability_care_support"]
        + 0.14 * care["care_worker_protection"]
        + 0.12 * care["female_labor_participation_support"]
        + 0.12 * care["child_development_support"]
    )
    care.to_csv(TABLE_DIR / "care_family_policy_results_python.csv", index=False)

    fiscal["tax_ratio"] = fiscal["tax_revenue"] / fiscal["output"]
    fiscal["fiscal_capacity_score"] = (
        0.22 * fiscal["tax_ratio"] / fiscal["tax_ratio"].max()
        + 0.18 * fiscal["administrative_capacity"]
        + 0.16 * fiscal["compliance_strength"]
        + 0.16 * fiscal["progressivity"]
        + 0.14 * fiscal["benefit_delivery_quality"]
        + 0.14 * fiscal["automatic_stabilizer_strength"]
    )
    fiscal.to_csv(TABLE_DIR / "fiscal_capacity_results_python.csv", index=False)

    digital["digital_access_quality"] = (
        0.16 * digital["digital_access"]
        + 0.16 * digital["identity_coverage"]
        + 0.16 * digital["application_simplicity"]
        + 0.16 * digital["appeal_access"]
        + 0.14 * (1 - digital["automation_error_risk"])
        + 0.12 * digital["data_protection"]
        + 0.10 * digital["human_support"]
    )
    digital.to_csv(TABLE_DIR / "digital_administration_results_python.csv", index=False)

    adaptive["adaptive_capacity_score"] = (
        0.18 * adaptive["scale_up_capacity"]
        + 0.18 * adaptive["payment_speed"]
        + 0.16 * adaptive["registry_quality"]
        + 0.16 * adaptive["local_delivery_capacity"]
        + 0.16 * adaptive["benefit_adequacy"]
        + 0.16 * (1 - adaptive["post_shock_vulnerability"])
    )
    adaptive["shock_vulnerability_reduction"] = adaptive["baseline_exposure"] - adaptive["post_shock_vulnerability"]
    adaptive.to_csv(TABLE_DIR / "adaptive_protection_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(life["risk"], life["life_course_protection_score"])
    ax.set_title("Life-Course Protection")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "life_course_protection_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(care["scenario"], care["care_system_strength"])
    ax.set_title("Care-System Strength")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "care_system_strength_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(fiscal["scenario"], fiscal["fiscal_capacity_score"])
    ax.set_title("Fiscal Capacity for Social Protection")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "fiscal_capacity_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(digital["scenario"], digital["digital_access_quality"])
    ax.set_title("Digital Administration Access Quality")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "digital_administration_quality_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(adaptive["shock"], adaptive["adaptive_capacity_score"])
    ax.set_title("Adaptive Social Protection Capacity")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "adaptive_social_protection_python.png", dpi=300)
    plt.close(fig)

    print(life[["risk", "vulnerability_reduction", "life_course_protection_score"]])
    print(care[["scenario", "care_system_strength"]])
    print(fiscal[["scenario", "tax_ratio", "fiscal_capacity_score"]])
    print(digital[["scenario", "digital_access_quality"]])
    print(adaptive[["shock", "shock_vulnerability_reduction", "adaptive_capacity_score"]])


if __name__ == "__main__":
    main()
