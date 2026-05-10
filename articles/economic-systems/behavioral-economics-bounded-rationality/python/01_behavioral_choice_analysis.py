"""
Behavioral choice analysis: satisficing, cognitive costs, present bias, loss aversion, and probability weighting.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"
FIGURE_DIR = BASE_DIR / "outputs" / "figures"
TABLE_DIR = BASE_DIR / "outputs" / "tables"

for directory in [FIGURE_DIR, TABLE_DIR]:
    directory.mkdir(parents=True, exist_ok=True)


def value_function(x: np.ndarray, lambda_loss: float = 2.0, alpha_gain: float = 0.88, beta_loss: float = 0.88) -> np.ndarray:
    return np.where(x >= 0, x ** alpha_gain, -lambda_loss * ((-x) ** beta_loss))


def probability_weight(p: np.ndarray, gamma: float = 0.72) -> np.ndarray:
    # Prelec-style one-parameter weighting
    return np.exp(-((-np.log(p)) ** gamma))


def main() -> None:
    options = pd.read_csv(PROCESSED_DIR / "choice_options.csv")
    present = pd.read_csv(PROCESSED_DIR / "present_bias_scenarios.csv")
    risk = pd.read_csv(PROCESSED_DIR / "risk_probability_scenarios.csv")

    kappa = 5.0
    options["effective_utility"] = options["utility"] - kappa * options["complexity"] + 10 * options["salience"]

    optimizer_choice = options.loc[options["utility"].idxmax()].copy()
    effective_optimizer_choice = options.loc[options["effective_utility"].idxmax()].copy()

    ordered = options.sort_values("search_order")
    satisfice_candidates = ordered[ordered["utility"] >= ordered["satisficing_threshold"]]
    satisficing_choice = satisfice_candidates.iloc[0].copy()

    choice_summary = pd.DataFrame([
        {"choice_rule": "global_utility_maximization", "chosen_option": optimizer_choice["option_label"], "utility": optimizer_choice["utility"], "effective_utility": optimizer_choice["effective_utility"]},
        {"choice_rule": "cognitive_cost_adjusted", "chosen_option": effective_optimizer_choice["option_label"], "utility": effective_optimizer_choice["utility"], "effective_utility": effective_optimizer_choice["effective_utility"]},
        {"choice_rule": "satisficing", "chosen_option": satisficing_choice["option_label"], "utility": satisficing_choice["utility"], "effective_utility": satisficing_choice["effective_utility"]},
    ])
    options.to_csv(TABLE_DIR / "satisficing_choice_results_python.csv", index=False)
    choice_summary.to_csv(TABLE_DIR / "choice_rule_summary_python.csv", index=False)

    present_records = []
    for scenario, group in present.groupby("scenario"):
        beta = group["beta"].iloc[0]
        delta = group["delta"].iloc[0]
        discounted_value = np.sum([
            beta * (delta ** period) * value
            for period, value in zip(group["period"], group["future_value"])
            if period > 0
        ])
        exponential_value = np.sum([
            (delta ** period) * value
            for period, value in zip(group["period"], group["future_value"])
            if period > 0
        ])
        present_records.append({
            "scenario": scenario,
            "beta": beta,
            "delta": delta,
            "present_biased_value": discounted_value,
            "exponential_discount_value": exponential_value,
            "present_bias_gap": exponential_value - discounted_value,
        })
    present_results = pd.DataFrame(present_records)
    present_results.to_csv(TABLE_DIR / "present_bias_results_python.csv", index=False)

    x = np.arange(-100, 101, 2)
    loss_df = pd.DataFrame({
        "outcome": x,
        "value_lambda_1": value_function(x, lambda_loss=1.0),
        "value_lambda_2": value_function(x, lambda_loss=2.0),
        "value_lambda_3": value_function(x, lambda_loss=3.0),
    })
    loss_df.to_csv(TABLE_DIR / "loss_aversion_results_python.csv", index=False)

    risk["weighted_probability"] = probability_weight(risk["probability"].clip(lower=0.001, upper=0.999))
    risk["objective_expected_value"] = risk["probability"] * risk["outcome_value"]
    risk["behavioral_expected_value"] = risk["weighted_probability"] * risk["outcome_value"] * (1 + 0.4 * risk["salience"])
    risk.to_csv(TABLE_DIR / "probability_weighting_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(loss_df["outcome"], loss_df["value_lambda_1"], label="lambda=1")
    ax.plot(loss_df["outcome"], loss_df["value_lambda_2"], label="lambda=2")
    ax.plot(loss_df["outcome"], loss_df["value_lambda_3"], label="lambda=3")
    ax.axhline(0, linestyle="--")
    ax.axvline(0, linestyle="--")
    ax.set_title("Loss Aversion Value Function")
    ax.set_xlabel("Outcome relative to reference point")
    ax.set_ylabel("Behavioral value")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "loss_aversion_value_function_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(present_results["scenario"], present_results["present_bias_gap"])
    ax.set_title("Gap Between Exponential and Present-Biased Valuation")
    ax.set_ylabel("Valuation gap")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "present_bias_discounting_python.png", dpi=300)
    plt.close(fig)

    print(choice_summary)
    print(present_results)


if __name__ == "__main__":
    main()
