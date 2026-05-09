.headers on
.mode column

.print "IS-LM scenario results"
SELECT
    scenario,
    lm_slope_type,
    ROUND(equilibrium_output, 2) AS equilibrium_output,
    ROUND(equilibrium_interest_rate, 2) AS equilibrium_interest_rate,
    ROUND(delta_output_from_baseline, 2) AS delta_output,
    ROUND(delta_interest_from_baseline, 2) AS delta_interest
FROM is_lm_scenario_results
ORDER BY scenario;

.print ""
.print "Policy multiplier summary by LM slope"
SELECT
    lm_slope_type,
    COUNT(*) AS scenarios,
    ROUND(AVG(fiscal_multiplier_model), 3) AS avg_fiscal_multiplier,
    ROUND(AVG(monetary_multiplier_model), 3) AS avg_monetary_multiplier,
    ROUND(AVG(crowding_out_indicator), 3) AS avg_crowding_out_indicator
FROM is_lm_scenario_results
GROUP BY lm_slope_type;

.print ""
.print "Scenarios with strongest output gains"
SELECT
    scenario,
    ROUND(delta_output_from_baseline, 2) AS delta_output,
    ROUND(delta_interest_from_baseline, 2) AS delta_interest,
    ROUND(crowding_out_indicator, 2) AS crowding_out_indicator
FROM is_lm_scenario_results
ORDER BY delta_output_from_baseline DESC
LIMIT 6;
