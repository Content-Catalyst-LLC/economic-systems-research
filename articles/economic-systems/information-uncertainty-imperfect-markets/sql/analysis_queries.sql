.headers on
.mode column

.print "Market quality types and pooled expected value components"
SELECT
    type,
    share,
    value,
    reservation_value,
    quality_verifiability
FROM market_quality_types
ORDER BY value DESC;

.print ""
.print "Credit risk expected loss"
SELECT
    borrower_type,
    share,
    default_probability,
    loss_given_default,
    ROUND(default_probability * loss_given_default, 3) AS expected_loss,
    productive_return,
    screening_cost,
    ROUND(productive_return - default_probability * loss_given_default - screening_cost, 3) AS net_expected_return
FROM credit_risk_types
ORDER BY net_expected_return DESC;

.print ""
.print "Signal credibility"
SELECT
    signal,
    signal_strength,
    signal_cost_high_type,
    signal_cost_low_type,
    signal_cost_low_type - signal_cost_high_type AS credibility_gap,
    verification_strength
FROM signaling_scenarios
ORDER BY credibility_gap DESC;

.print ""
.print "Information search net value"
SELECT
    information_level,
    ROUND(benefit_information, 3) AS benefit_information,
    ROUND(cost_information + time_cost + processing_cost, 3) AS total_information_cost,
    ROUND(benefit_information - cost_information - time_cost - processing_cost, 3) AS net_information_value
FROM information_search_scenarios
ORDER BY net_information_value DESC;

.print ""
.print "Robustness under deep uncertainty"
SELECT
    action,
    ROUND((good_case + moderate_case + bad_case + transition_case + systemic_crisis_case) / 5.0, 3) AS expected_equal_weight_payoff,
    MIN(good_case, moderate_case, bad_case, transition_case, systemic_crisis_case) AS worst_case
FROM uncertainty_scenarios
ORDER BY worst_case DESC;
