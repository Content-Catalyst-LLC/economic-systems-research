"""
Adverse selection, moral hazard, and signal credibility.
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


def main() -> None:
    quality = pd.read_csv(PROCESSED_DIR / "market_quality_types.csv")
    credit = pd.read_csv(PROCESSED_DIR / "credit_risk_types.csv")
    signals = pd.read_csv(PROCESSED_DIR / "signaling_scenarios.csv")

    q_values = np.linspace(0, 1, 101)
    V_H = 100
    V_L = 38
    pooled_value = q_values * V_H + (1 - q_values) * V_L
    adverse = pd.DataFrame({
        "share_high_quality": q_values,
        "pooled_expected_value": pooled_value,
        "high_quality_remains": pooled_value >= 82,
    })
    adverse.to_csv(TABLE_DIR / "adverse_selection_results_python.csv", index=False)

    credit["expected_loss"] = credit["default_probability"] * credit["loss_given_default"]
    credit["net_expected_return"] = credit["productive_return"] - credit["expected_loss"] - credit["screening_cost"]
    credit["pooled_expected_loss"] = (credit["expected_loss"] * credit["share"]).sum()
    credit.to_csv(TABLE_DIR / "credit_risk_pooling_results_python.csv", index=False)

    effort = np.arange(0, 11)
    output = 6.0 * effort
    effort_cost = 0.82 * effort ** 2
    records = []
    for insured_share in [0.0, 0.25, 0.50, 0.75]:
        retained_output = output * (1 - insured_share)
        agent_payoff = retained_output - effort_cost
        best_idx = int(np.argmax(agent_payoff))
        records.append({
            "insured_share": insured_share,
            "chosen_effort": effort[best_idx],
            "agent_payoff": agent_payoff[best_idx],
            "system_output": output[best_idx],
        })
    moral = pd.DataFrame(records)
    moral.to_csv(TABLE_DIR / "moral_hazard_results_python.csv", index=False)

    signals["credibility_gap"] = signals["signal_cost_low_type"] - signals["signal_cost_high_type"]
    signals["credible_signal_score"] = (
        0.45 * signals["verification_strength"]
        + 0.35 * (signals["credibility_gap"] / signals["credibility_gap"].max())
        + 0.20 * signals["signal_strength"]
    )
    signals["credible_signal_flag"] = signals["credible_signal_score"] >= 0.60
    signals.to_csv(TABLE_DIR / "signal_credibility_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(adverse["share_high_quality"], adverse["pooled_expected_value"])
    ax.axhline(82, linestyle="--", label="high-quality reservation value")
    ax.set_title("Adverse Selection and Pooled Market Value")
    ax.set_xlabel("Share high quality")
    ax.set_ylabel("Pooled expected value")
    ax.legend()
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "adverse_selection_pooled_value_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(moral["insured_share"].astype(str), moral["chosen_effort"])
    ax.set_title("Hidden Action and Effort Under Risk Shifting")
    ax.set_xlabel("Insured / shifted risk share")
    ax.set_ylabel("Chosen effort")
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "moral_hazard_effort_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(signals["signal"], signals["credible_signal_score"])
    ax.set_title("Signal Credibility by Verification and Imitation Cost")
    ax.set_ylabel("Credibility score")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "signal_credibility_python.png", dpi=300)
    plt.close(fig)

    print(adverse.head())
    print(moral)
    print(signals[["signal", "credibility_gap", "credible_signal_score"]])


if __name__ == "__main__":
    main()
