.headers on
.mode column

.print "Disposable income and service-adjusted security"
SELECT
    household,
    market_income,
    taxes,
    transfers,
    ROUND(market_income - taxes + transfers, 2) AS disposable_income,
    ROUND(market_income - taxes + transfers + service_value, 2) AS service_adjusted_income,
    ROUND(market_income - taxes + transfers + service_value - housing_cost - care_cost, 2) AS post_cost_security_income
FROM household_tax_transfer
ORDER BY market_income;

.print ""
.print "Social spending ratios"
SELECT
    scenario,
    ROUND(social_spending / output, 3) AS social_spending_ratio,
    healthcare_spending,
    pensions,
    unemployment,
    family_policy,
    administration_quality
FROM social_spending_scenarios
ORDER BY social_spending_ratio DESC;

.print ""
.print "Coverage and replacement rates"
SELECT
    program,
    ROUND(covered_population / target_population, 3) AS coverage_rate,
    ROUND(benefit / previous_earnings, 3) AS replacement_rate,
    take_up_rate,
    administrative_burden,
    stigma_cost
FROM program_coverage
ORDER BY coverage_rate DESC;

.print ""
.print "Welfare regime strength"
SELECT
    regime,
    ROUND(
      0.18 * universalism +
      0.12 * targeting_precision +
      0.18 * benefit_adequacy +
      0.18 * service_quality +
      0.14 * labor_market_security +
      0.10 * dignity_score +
      0.10 * political_durability,
      3
    ) AS regime_strength_score
FROM welfare_regime_scenarios
ORDER BY regime_strength_score DESC;

.print ""
.print "Life-course vulnerability reduction"
SELECT
    risk,
    baseline_vulnerability,
    protected_vulnerability,
    ROUND(baseline_vulnerability - protected_vulnerability, 3) AS vulnerability_reduction,
    coverage,
    adequacy,
    duration_support
FROM life_course_risk
ORDER BY vulnerability_reduction DESC;

.print ""
.print "Adaptive social protection"
SELECT
    shock,
    baseline_exposure,
    post_shock_vulnerability,
    ROUND(baseline_exposure - post_shock_vulnerability, 3) AS shock_vulnerability_reduction,
    ROUND(
      0.18 * scale_up_capacity +
      0.18 * payment_speed +
      0.16 * registry_quality +
      0.16 * local_delivery_capacity +
      0.16 * benefit_adequacy +
      0.16 * (1 - post_shock_vulnerability),
      3
    ) AS adaptive_capacity_score
FROM adaptive_protection
ORDER BY adaptive_capacity_score DESC;
