"""
Build stylized datasets for behavioral economics and bounded rationality.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[1]
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def build_choice_options() -> pd.DataFrame:
    rows = [
        {"option_id": 1, "option_label": "simple_default_low_return", "utility": 62, "complexity": 1.0, "salience": 0.82, "search_order": 1, "satisficing_threshold": 70},
        {"option_id": 2, "option_label": "moderate_return_moderate_complexity", "utility": 74, "complexity": 2.3, "salience": 0.62, "search_order": 2, "satisficing_threshold": 70},
        {"option_id": 3, "option_label": "high_return_high_complexity", "utility": 90, "complexity": 5.2, "salience": 0.44, "search_order": 3, "satisficing_threshold": 70},
        {"option_id": 4, "option_label": "trusted_socially_recommended", "utility": 79, "complexity": 2.0, "salience": 0.78, "search_order": 4, "satisficing_threshold": 70},
        {"option_id": 5, "option_label": "low_visibility_high_value", "utility": 88, "complexity": 3.8, "salience": 0.25, "search_order": 5, "satisficing_threshold": 70},
        {"option_id": 6, "option_label": "familiar_habitual_option", "utility": 68, "complexity": 0.8, "salience": 0.86, "search_order": 6, "satisficing_threshold": 70},
    ]
    return pd.DataFrame(rows)


def build_present_bias_scenarios() -> pd.DataFrame:
    rows = []
    for scenario, beta, delta in [
        ("high_present_bias", 0.55, 0.94),
        ("moderate_present_bias", 0.75, 0.95),
        ("low_present_bias", 0.92, 0.96),
        ("near_exponential_discounting", 1.00, 0.96),
    ]:
        for period in range(0, 13):
            future_value = 100 if period > 0 else 0
            rows.append({
                "scenario": scenario,
                "beta": beta,
                "delta": delta,
                "period": period,
                "future_value": future_value,
            })
    return pd.DataFrame(rows)


def build_framing_default_scenarios() -> pd.DataFrame:
    rows = [
        {"scenario": "neutral_active_choice", "frame": "neutral", "default_status": 0, "benefit_value": 100, "admin_burden": 38, "trust_index": 0.60, "salience": 0.55},
        {"scenario": "gain_frame_active_choice", "frame": "gain", "default_status": 0, "benefit_value": 100, "admin_burden": 38, "trust_index": 0.60, "salience": 0.68},
        {"scenario": "loss_frame_active_choice", "frame": "loss", "default_status": 0, "benefit_value": 100, "admin_burden": 38, "trust_index": 0.60, "salience": 0.74},
        {"scenario": "beneficial_default", "frame": "neutral", "default_status": 1, "benefit_value": 100, "admin_burden": 22, "trust_index": 0.66, "salience": 0.76},
        {"scenario": "complex_menu_low_trust", "frame": "neutral", "default_status": 0, "benefit_value": 100, "admin_burden": 68, "trust_index": 0.38, "salience": 0.42},
        {"scenario": "simple_public_service", "frame": "gain", "default_status": 1, "benefit_value": 100, "admin_burden": 14, "trust_index": 0.78, "salience": 0.82},
    ]
    return pd.DataFrame(rows)


def build_risk_probability_scenarios() -> pd.DataFrame:
    rows = [
        {"risk_case": "rare_salient_disaster", "probability": 0.02, "outcome_value": -500, "salience": 0.95, "ambiguity": 0.65},
        {"risk_case": "slow_chronic_environmental_risk", "probability": 0.35, "outcome_value": -180, "salience": 0.35, "ambiguity": 0.70},
        {"risk_case": "moderate_health_risk", "probability": 0.18, "outcome_value": -220, "salience": 0.60, "ambiguity": 0.40},
        {"risk_case": "financial_penalty_risk", "probability": 0.10, "outcome_value": -160, "salience": 0.72, "ambiguity": 0.30},
        {"risk_case": "preventive_benefit_uncertain", "probability": 0.45, "outcome_value": 120, "salience": 0.38, "ambiguity": 0.55},
    ]
    return pd.DataFrame(rows)


def build_social_norm_scenarios() -> pd.DataFrame:
    rows = [
        {"scenario": "low_peer_cooperation", "peer_cooperation_rate": 0.25, "institutional_trust": 0.42, "fairness_perception": 0.38, "private_cost": 28, "collective_benefit": 90},
        {"scenario": "mixed_peer_cooperation", "peer_cooperation_rate": 0.52, "institutional_trust": 0.56, "fairness_perception": 0.52, "private_cost": 28, "collective_benefit": 90},
        {"scenario": "high_peer_cooperation", "peer_cooperation_rate": 0.78, "institutional_trust": 0.70, "fairness_perception": 0.68, "private_cost": 28, "collective_benefit": 90},
        {"scenario": "high_trust_reciprocal", "peer_cooperation_rate": 0.74, "institutional_trust": 0.84, "fairness_perception": 0.82, "private_cost": 28, "collective_benefit": 90},
        {"scenario": "unfair_burden_low_legitimacy", "peer_cooperation_rate": 0.48, "institutional_trust": 0.30, "fairness_perception": 0.22, "private_cost": 36, "collective_benefit": 90},
    ]
    return pd.DataFrame(rows)


def build_admin_burden_scenarios() -> pd.DataFrame:
    rows = [
        {"program": "retirement_auto_enrollment", "eligible_population": 10000, "benefit_value": 85, "admin_burden": 12, "default_support": 1, "trust_index": 0.72},
        {"program": "manual_retirement_enrollment", "eligible_population": 10000, "benefit_value": 85, "admin_burden": 48, "default_support": 0, "trust_index": 0.62},
        {"program": "energy_rebate_complex_application", "eligible_population": 8000, "benefit_value": 70, "admin_burden": 66, "default_support": 0, "trust_index": 0.48},
        {"program": "energy_rebate_simple_application", "eligible_population": 8000, "benefit_value": 70, "admin_burden": 24, "default_support": 0, "trust_index": 0.64},
        {"program": "public_health_default_appointment", "eligible_population": 12000, "benefit_value": 60, "admin_burden": 16, "default_support": 1, "trust_index": 0.68},
        {"program": "disaster_preparedness_opt_in", "eligible_population": 6500, "benefit_value": 55, "admin_burden": 52, "default_support": 0, "trust_index": 0.50},
    ]
    return pd.DataFrame(rows)


def save_sqlite(choice, present, framing, risk, norms, burden) -> None:
    db_path = PROCESSED_DIR / "behavioral_economics_bounded_rationality.sqlite"
    with sqlite3.connect(db_path) as conn:
        choice.to_sql("choice_options", conn, if_exists="replace", index=False)
        present.to_sql("present_bias_scenarios", conn, if_exists="replace", index=False)
        framing.to_sql("framing_default_scenarios", conn, if_exists="replace", index=False)
        risk.to_sql("risk_probability_scenarios", conn, if_exists="replace", index=False)
        norms.to_sql("social_norm_scenarios", conn, if_exists="replace", index=False)
        burden.to_sql("admin_burden_scenarios", conn, if_exists="replace", index=False)


def main() -> None:
    choice = build_choice_options()
    present = build_present_bias_scenarios()
    framing = build_framing_default_scenarios()
    risk = build_risk_probability_scenarios()
    norms = build_social_norm_scenarios()
    burden = build_admin_burden_scenarios()

    choice.to_csv(PROCESSED_DIR / "choice_options.csv", index=False)
    present.to_csv(PROCESSED_DIR / "present_bias_scenarios.csv", index=False)
    framing.to_csv(PROCESSED_DIR / "framing_default_scenarios.csv", index=False)
    risk.to_csv(PROCESSED_DIR / "risk_probability_scenarios.csv", index=False)
    norms.to_csv(PROCESSED_DIR / "social_norm_scenarios.csv", index=False)
    burden.to_csv(PROCESSED_DIR / "admin_burden_scenarios.csv", index=False)

    save_sqlite(choice, present, framing, risk, norms, burden)
    print("Created behavioral economics and bounded rationality base data.")


if __name__ == "__main__":
    main()
