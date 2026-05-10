.headers on
.mode column

.print "Choice options with cognitive-cost adjustment"
SELECT
    option_label,
    utility,
    complexity,
    salience,
    ROUND(utility - 5.0 * complexity + 10.0 * salience, 3) AS effective_utility,
    search_order,
    satisficing_threshold
FROM choice_options
ORDER BY search_order;

.print ""
.print "Present-bias scenario values"
SELECT
    scenario,
    beta,
    delta,
    ROUND(SUM(CASE WHEN period > 0 THEN beta * POWER(delta, period) * future_value ELSE 0 END), 3) AS present_biased_value,
    ROUND(SUM(CASE WHEN period > 0 THEN POWER(delta, period) * future_value ELSE 0 END), 3) AS exponential_discount_value
FROM present_bias_scenarios
GROUP BY scenario, beta, delta
ORDER BY present_biased_value ASC;

.print ""
.print "Defaults and administrative burden"
SELECT
    scenario,
    frame,
    default_status,
    benefit_value,
    admin_burden,
    trust_index,
    salience
FROM framing_default_scenarios
ORDER BY admin_burden DESC;

.print ""
.print "Social norms and compliance inputs"
SELECT
    scenario,
    peer_cooperation_rate,
    institutional_trust,
    fairness_perception,
    private_cost,
    collective_benefit
FROM social_norm_scenarios
ORDER BY fairness_perception DESC;
