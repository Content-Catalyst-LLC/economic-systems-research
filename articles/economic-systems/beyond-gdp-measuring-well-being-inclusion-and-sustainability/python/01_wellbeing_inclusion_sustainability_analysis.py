"""
GDP, well-being, inclusion, sustainability, and adjusted progress analysis.
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
    dashboard = pd.read_csv(PROCESSED_DIR / "gdp_dashboard_scenarios.csv")
    inclusion = pd.read_csv(PROCESSED_DIR / "inclusion_scenarios.csv")
    stocks = pd.read_csv(PROCESSED_DIR / "sustainability_stocks.csv")
    adjusted = pd.read_csv(PROCESSED_DIR / "adjusted_progress.csv")

    dashboard["gdp"] = dashboard["consumption"] + dashboard["investment"] + dashboard["government"] + dashboard["net_exports"]
    wellbeing_columns = ["health", "education", "income_security", "housing", "safety", "social_connection", "environment", "time_balance"]
    dashboard["wellbeing_score"] = dashboard[wellbeing_columns].mean(axis=1)
    dashboard["gdp_wellbeing_gap"] = (dashboard["gdp"] / dashboard["gdp"].max()) - dashboard["wellbeing_score"]
    dashboard.to_csv(TABLE_DIR / "gdp_wellbeing_dashboard_results_python.csv", index=False)

    inclusion["inclusion_score"] = (
        0.22 * inclusion["distribution"]
        + 0.18 * inclusion["mobility"]
        + 0.20 * inclusion["access"]
        + 0.18 * inclusion["voice"]
        + 0.12 * inclusion["regional_equity"]
        + 0.10 * inclusion["service_reach"]
    )
    inclusion.to_csv(TABLE_DIR / "inclusion_results_python.csv", index=False)

    stocks["sustainability_score"] = (
        0.26 * stocks["natural_capital"]
        + 0.22 * stocks["human_capital"]
        + 0.20 * stocks["institutional_trust"]
        + 0.16 * stocks["produced_capital"]
        + 0.08 * (1 - stocks["maintenance_gap"])
        + 0.08 * (1 - stocks["ecological_pressure"])
    )
    stocks.to_csv(TABLE_DIR / "sustainability_stock_results_python.csv", index=False)

    adjusted["adjusted_progress"] = (
        adjusted["current_benefits"]
        - adjusted["social_costs"]
        - adjusted["ecological_costs"]
        - adjusted["defensive_expenditure"]
        + adjusted["unpaid_care_value"]
        + adjusted["public_goods_value"]
    )
    adjusted["adjusted_progress_ratio"] = adjusted["adjusted_progress"] / adjusted["current_benefits"]
    adjusted.to_csv(TABLE_DIR / "adjusted_progress_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(dashboard["scenario"], dashboard["gdp"])
    ax.set_title("GDP by Scenario")
    ax.set_ylabel("GDP index")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "gdp_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(dashboard["scenario"], dashboard["wellbeing_score"])
    ax.set_title("Well-Being Score")
    ax.set_ylabel("Composite score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "wellbeing_score_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(inclusion["group"], inclusion["inclusion_score"])
    ax.set_title("Inclusion Score")
    ax.set_ylabel("Composite inclusion score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "inclusion_score_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(stocks["scenario"], stocks["sustainability_score"])
    ax.set_title("Sustainability Stock Score")
    ax.set_ylabel("Composite sustainability score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "sustainability_score_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(adjusted["scenario"], adjusted["adjusted_progress_ratio"])
    ax.set_title("Adjusted Progress Ratio")
    ax.set_ylabel("Adjusted progress / current benefits")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "adjusted_progress_python.png", dpi=300)
    plt.close(fig)

    print(dashboard[["scenario", "gdp", "wellbeing_score", "gdp_wellbeing_gap"]])
    print(inclusion[["group", "inclusion_score"]])
    print(stocks[["scenario", "sustainability_score"]])
    print(adjusted[["scenario", "adjusted_progress", "adjusted_progress_ratio"]])


if __name__ == "__main__":
    main()
