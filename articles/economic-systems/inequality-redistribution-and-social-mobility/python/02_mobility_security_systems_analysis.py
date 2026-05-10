"""
Mobility, labor markets, housing/place, public services, and economic security.
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
    mobility = pd.read_csv(PROCESSED_DIR / "mobility_scenarios.csv")
    labor = pd.read_csv(PROCESSED_DIR / "labor_market_scenarios.csv")
    place = pd.read_csv(PROCESSED_DIR / "housing_place_scenarios.csv")
    services = pd.read_csv(PROCESSED_DIR / "public_services_scenarios.csv")

    mobility["predicted_child_outcome"] = mobility["baseline_a"] + mobility["persistence_b"] * mobility["parent_outcome"]
    mobility["opportunity_score"] = (
        0.22 * mobility["education_access"]
        + 0.20 * mobility["health_access"]
        + 0.20 * mobility["place_advantage"]
        + 0.18 * mobility["network_access"]
        + 0.20 * mobility["family_wealth_buffer"]
    )
    mobility["mobility_openness_score"] = (1 - mobility["persistence_b"]) * 0.55 + mobility["opportunity_score"] * 0.45
    mobility.to_csv(TABLE_DIR / "mobility_results_python.csv", index=False)

    labor["wage_dispersion_ratio"] = labor["top_wage"] / labor["bottom_wage"]
    labor["labor_security_score"] = (
        0.22 * labor["bargaining_power"]
        + 0.20 * labor["union_strength"]
        + 0.20 * labor["employment_security"]
        + 0.18 * labor["schedule_stability"]
        + 0.20 * labor["benefit_access"]
    )
    labor.to_csv(TABLE_DIR / "labor_market_results_python.csv", index=False)

    place["housing_cost_burden"] = place["housing_cost"] / place["median_income"]
    place["place_opportunity_score"] = (
        0.20 * place["school_quality"]
        + 0.18 * place["transit_access"]
        + 0.18 * place["environmental_quality"]
        + 0.20 * place["job_access"]
        + 0.14 * place["homeownership_rate"]
        + 0.10 * (1 - place["housing_cost_burden"] / place["housing_cost_burden"].max())
    )
    place.to_csv(TABLE_DIR / "housing_place_results_python.csv", index=False)

    services["public_security_score"] = (
        0.18 * services["healthcare_access"]
        + 0.18 * services["education_quality"]
        + 0.14 * services["childcare_support"]
        + 0.12 * services["transit_quality"]
        + 0.14 * services["income_support"]
        + 0.12 * services["unemployment_insurance"]
        + 0.12 * services["pension_security"]
    )
    services.to_csv(TABLE_DIR / "public_services_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(mobility["scenario"], mobility["mobility_openness_score"])
    ax.set_title("Mobility Openness by Institutional Scenario")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "mobility_openness_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(labor["sector"], labor["wage_dispersion_ratio"])
    ax.set_title("Wage Dispersion by Labor-Market Segment")
    ax.set_ylabel("Top wage / bottom wage")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "labor_wage_dispersion_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(place["place"], place["place_opportunity_score"])
    ax.set_title("Place-Based Opportunity")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "place_opportunity_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(services["scenario"], services["public_security_score"])
    ax.set_title("Public Services and Social Insurance Security")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "public_security_score_python.png", dpi=300)
    plt.close(fig)

    print(mobility[["scenario", "persistence_b", "predicted_child_outcome", "opportunity_score", "mobility_openness_score"]])
    print(labor[["sector", "wage_dispersion_ratio", "labor_security_score"]])
    print(place[["place", "housing_cost_burden", "place_opportunity_score"]])
    print(services[["scenario", "public_security_score"]])


if __name__ == "__main__":
    main()
