"""
Social reproduction, time poverty, bargaining power, institutional support, and automation shocks.
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
    households = pd.read_csv(PROCESSED_DIR / "household_reproduction_scenarios.csv")
    time_use = pd.read_csv(PROCESSED_DIR / "time_use_scenarios.csv")
    bargaining = pd.read_csv(PROCESSED_DIR / "bargaining_institution_scenarios.csv")
    automation = pd.read_csv(PROCESSED_DIR / "automation_shock_scenarios.csv")

    households["total_supporting_income"] = households["wage_income"] + households["social_support"]
    households["total_reproduction_cost"] = households["household_cost"] + households["care_reproduction_cost"]
    households["adequacy_gap"] = households["total_supporting_income"] - households["total_reproduction_cost"]
    households["adequacy_ratio"] = households["total_supporting_income"] / households["total_reproduction_cost"]
    households["reproduction_stress_flag"] = (households["adequacy_gap"] < 0).astype(int)
    households.to_csv(TABLE_DIR / "social_reproduction_adequacy_python.csv", index=False)

    time_use["rest_recovery_time"] = (
        24
        - time_use["paid_work_time"]
        - time_use["care_time"]
        - time_use["household_time"]
        - time_use["commute_time"]
    )
    time_use["time_poverty_flag"] = (time_use["rest_recovery_time"] < 8).astype(int)
    time_use["total_work_burden"] = (
        time_use["paid_work_time"]
        + time_use["care_time"]
        + time_use["household_time"]
        + time_use["commute_time"]
    )
    time_use.to_csv(TABLE_DIR / "time_poverty_results_python.csv", index=False)

    bargaining["modeled_wage"] = (
        1.15
        + 0.52 * bargaining["labor_productivity"]
        + 1.15 * bargaining["bargaining_power"]
        + 0.95 * bargaining["institutional_support"]
        + 0.70 * bargaining["outside_option"]
    )
    bargaining["labor_capture_index"] = bargaining["modeled_wage"] / bargaining["labor_productivity"]
    bargaining.to_csv(TABLE_DIR / "bargaining_wage_results_python.csv", index=False)

    automation["post_automation_output_index"] = 100 * (1 + automation["productivity_gain"])
    automation["post_automation_employment_index"] = 100 * (1 + automation["employment_effect"])
    automation["post_automation_wage_share_index"] = 100 * (1 + automation["wage_share_effect"])
    automation["post_automation_quality_index"] = 100 * (1 + automation["quality_effect"])
    automation["worker_welfare_index"] = (
        0.35 * automation["post_automation_wage_share_index"]
        + 0.35 * automation["post_automation_employment_index"]
        + 0.30 * automation["post_automation_quality_index"]
    )
    automation.to_csv(TABLE_DIR / "automation_shock_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(households["household_type"], households["adequacy_gap"])
    ax.axhline(0, linestyle="--")
    ax.set_title("Social Reproduction Adequacy Gap")
    ax.set_ylabel("Income + support minus household + care cost")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "social_reproduction_gap_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(time_use["worker_group"], time_use["rest_recovery_time"])
    ax.axhline(8, linestyle="--", label="rest/recovery threshold")
    ax.set_title("Rest and Recovery Time by Worker Group")
    ax.set_ylabel("Hours per day")
    ax.tick_params(axis="x", rotation=35)
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "time_poverty_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(bargaining["scenario"], bargaining["modeled_wage"])
    ax.set_title("Modeled Wage Under Bargaining and Institutional Scenarios")
    ax.set_ylabel("Modeled wage")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "bargaining_wage_scenarios_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(automation["scenario"], automation["worker_welfare_index"])
    ax.set_title("Automation Shock: Worker Welfare Index")
    ax.set_ylabel("Index")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "automation_shock_python.png", dpi=300)
    plt.close(fig)

    print(households[["household_type", "adequacy_gap", "adequacy_ratio"]])
    print(time_use[["worker_group", "rest_recovery_time", "time_poverty_flag"]])
    print(bargaining[["scenario", "modeled_wage", "labor_capture_index"]])


if __name__ == "__main__":
    main()
