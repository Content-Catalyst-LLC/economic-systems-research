"""
Defaults, administrative burden, social norms, framing, and take-up behavior.
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


def logistic(z):
    return 1 / (1 + np.exp(-z))


def main() -> None:
    framing = pd.read_csv(PROCESSED_DIR / "framing_default_scenarios.csv")
    norms = pd.read_csv(PROCESSED_DIR / "social_norm_scenarios.csv")
    burden = pd.read_csv(PROCESSED_DIR / "admin_burden_scenarios.csv")

    frame_effect = {"neutral": 0.00, "gain": 0.18, "loss": 0.28, "social": 0.22}
    framing["frame_effect"] = framing["frame"].map(frame_effect).fillna(0)
    framing["take_up_probability"] = logistic(
        -1.6
        + 0.020 * framing["benefit_value"]
        - 0.025 * framing["admin_burden"]
        + 1.15 * framing["default_status"]
        + 1.10 * framing["trust_index"]
        + 0.85 * framing["salience"]
        + framing["frame_effect"]
    )
    framing.to_csv(TABLE_DIR / "default_take_up_results_python.csv", index=False)

    burden["take_up_probability"] = logistic(
        -1.4
        + 0.022 * burden["benefit_value"]
        - 0.030 * burden["admin_burden"]
        + 1.25 * burden["default_support"]
        + 1.15 * burden["trust_index"]
    )
    burden["expected_take_up"] = burden["eligible_population"] * burden["take_up_probability"]
    burden["non_take_up"] = burden["eligible_population"] - burden["expected_take_up"]
    burden.to_csv(TABLE_DIR / "admin_burden_results_python.csv", index=False)

    norms["compliance_probability"] = logistic(
        -1.2
        + 1.65 * norms["peer_cooperation_rate"]
        + 1.20 * norms["institutional_trust"]
        + 1.15 * norms["fairness_perception"]
        - 0.020 * norms["private_cost"]
        + 0.006 * norms["collective_benefit"]
    )
    norms["expected_collective_contribution_index"] = norms["compliance_probability"] * norms["collective_benefit"]
    norms.to_csv(TABLE_DIR / "social_norm_results_python.csv", index=False)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(framing["scenario"], framing["take_up_probability"])
    ax.set_title("Default, Framing, and Take-Up Probability")
    ax.set_ylabel("Modeled take-up probability")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "default_take_up_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(burden["program"], burden["take_up_probability"])
    ax.set_title("Administrative Burden and Program Take-Up")
    ax.set_ylabel("Modeled take-up probability")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "admin_burden_take_up_python.png", dpi=300)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(norms["scenario"], norms["compliance_probability"])
    ax.set_title("Social Norms, Trust, Fairness, and Compliance")
    ax.set_ylabel("Modeled compliance probability")
    ax.tick_params(axis="x", rotation=35)
    fig.tight_layout()
    fig.savefig(FIGURE_DIR / "social_norm_compliance_python.png", dpi=300)
    plt.close(fig)

    print(framing[["scenario", "take_up_probability"]])
    print(burden[["program", "take_up_probability", "expected_take_up"]])
    print(norms[["scenario", "compliance_probability"]])


if __name__ == "__main__":
    main()
