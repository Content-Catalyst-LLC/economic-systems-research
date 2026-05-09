"""
Create IS-LM diagrams for baseline, fiscal shift, and monetary shift scenarios.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
FIGURE_DIR = BASE_DIR / "outputs" / "figures"

FIGURE_DIR.mkdir(parents=True, exist_ok=True)


def is_rate(y: np.ndarray, alpha: float, beta: float, fiscal_shift: float) -> np.ndarray:
    return (alpha + fiscal_shift - y) / beta


def lm_rate(y: np.ndarray, gamma: float, money_shift: float) -> np.ndarray:
    return gamma * y - money_shift


def plot_scenario_pair(
    baseline: pd.Series,
    scenario: pd.Series,
    title: str,
    filename: str,
    shift_type: str,
) -> None:
    y_min = 550
    y_max = 950
    y_grid = np.linspace(y_min, y_max, 250)

    fig, ax = plt.subplots(figsize=(8, 5))

    ax.plot(
        y_grid,
        is_rate(y_grid, baseline["alpha"], baseline["beta"], baseline["fiscal_shift"]),
        label="IS baseline",
        linewidth=1.4,
    )
    ax.plot(
        y_grid,
        lm_rate(y_grid, baseline["gamma"], baseline["money_shift"]),
        label="LM baseline",
        linewidth=1.4,
    )

    if shift_type == "fiscal":
        ax.plot(
            y_grid,
            is_rate(y_grid, scenario["alpha"], scenario["beta"], scenario["fiscal_shift"]),
            label="IS after fiscal shift",
            linewidth=1.4,
            linestyle="--",
        )
    elif shift_type == "monetary":
        ax.plot(
            y_grid,
            lm_rate(y_grid, scenario["gamma"], scenario["money_shift"]),
            label="LM after monetary shift",
            linewidth=1.4,
            linestyle="--",
        )
    else:
        ax.plot(
            y_grid,
            is_rate(y_grid, scenario["alpha"], scenario["beta"], scenario["fiscal_shift"]),
            label="IS scenario",
            linewidth=1.4,
            linestyle="--",
        )
        ax.plot(
            y_grid,
            lm_rate(y_grid, scenario["gamma"], scenario["money_shift"]),
            label="LM scenario",
            linewidth=1.4,
            linestyle="--",
        )

    ax.scatter(
        baseline["equilibrium_output"],
        baseline["equilibrium_interest_rate"],
        label="Baseline equilibrium",
        zorder=5,
    )
    ax.scatter(
        scenario["equilibrium_output"],
        scenario["equilibrium_interest_rate"],
        label="Scenario equilibrium",
        zorder=5,
    )

    ax.set_title(title)
    ax.set_xlabel("Output (Y)")
    ax.set_ylabel("Interest rate (r)")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / filename, dpi=300)
    plt.close(fig)


def main() -> None:
    df = pd.read_csv(PROCESSED_DIR / "is_lm_scenario_results.csv")
    baseline = df.loc[df["scenario"] == "baseline"].iloc[0]
    fiscal = df.loc[df["scenario"] == "expansionary_fiscal_policy"].iloc[0]
    monetary = df.loc[df["scenario"] == "expansionary_monetary_policy"].iloc[0]
    coordinated = df.loc[df["scenario"] == "coordinated_expansion"].iloc[0]

    plot_scenario_pair(
        baseline,
        baseline,
        "Baseline IS-LM Equilibrium",
        "is_lm_baseline_python.png",
        shift_type="baseline",
    )

    plot_scenario_pair(
        baseline,
        fiscal,
        "Expansionary Fiscal Policy in the IS-LM Model",
        "is_lm_fiscal_shift_python.png",
        shift_type="fiscal",
    )

    plot_scenario_pair(
        baseline,
        monetary,
        "Expansionary Monetary Policy in the IS-LM Model",
        "is_lm_monetary_shift_python.png",
        shift_type="monetary",
    )

    plot_scenario_pair(
        baseline,
        coordinated,
        "Coordinated Fiscal and Monetary Expansion",
        "is_lm_coordinated_policy_python.png",
        shift_type="both",
    )

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.bar(df["scenario"], df["delta_output_from_baseline"])
    ax.set_title("Output Change Relative to Baseline")
    ax.set_ylabel("Change in output")
    ax.set_xticklabels(df["scenario"], rotation=45, ha="right")
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "is_lm_policy_multipliers_python.png", dpi=300)
    plt.close(fig)


if __name__ == "__main__":
    main()
