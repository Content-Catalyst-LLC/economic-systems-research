-- IS-LM SQL Schema
-- Designed for SQLite-compatible scenario analysis.

DROP TABLE IF EXISTS is_lm_scenario_results;

CREATE TABLE is_lm_scenario_results (
    scenario TEXT PRIMARY KEY,
    alpha REAL,
    beta REAL,
    gamma REAL,
    fiscal_shift REAL,
    money_shift REAL,
    lm_slope_type TEXT,
    description TEXT,
    equilibrium_output REAL,
    equilibrium_interest_rate REAL,
    delta_output_from_baseline REAL,
    delta_interest_from_baseline REAL,
    fiscal_multiplier_model REAL,
    monetary_multiplier_model REAL,
    crowding_out_indicator REAL
);
