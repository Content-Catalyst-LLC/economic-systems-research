.headers on
.mode column

.print "Real rates and policy-rule comparison"
SELECT
    scenario,
    nominal_rate,
    expected_inflation,
    ROUND(nominal_rate - expected_inflation, 3) AS real_rate,
    ROUND(neutral_rate + a_inflation * inflation_gap + b_output * output_gap, 3) AS policy_rate_rule
FROM policy_rate_scenarios
ORDER BY real_rate DESC;

.print ""
.print "Debt-service stress"
SELECT
    borrower_group,
    income,
    debt_service,
    ROUND(debt_service / income, 3) AS debt_service_ratio,
    repricing_share,
    ROUND((debt_service + debt_stock * repricing_share * rate_shock / 12) / income, 3) AS post_shock_dsr
FROM debt_service_scenarios
ORDER BY post_shock_dsr DESC;

.print ""
.print "Financial conditions"
SELECT
    scenario,
    policy_rate,
    credit_spread,
    equity_price_change,
    exchange_rate_pressure,
    lending_tightness,
    market_liquidity_stress,
    ROUND(policy_rate + credit_spread + exchange_rate_pressure + lending_tightness * 0.08 + market_liquidity_stress * 0.08 - equity_price_change * 0.18, 3) AS financial_conditions_index
FROM financial_conditions_scenarios
ORDER BY financial_conditions_index DESC;

.print ""
.print "Bank liquidity stress"
SELECT
    institution,
    liquid_assets,
    short_term_outflows,
    ROUND(liquid_assets / short_term_outflows, 3) AS liquidity_coverage_ratio,
    ROUND(liquid_assets / (short_term_outflows * (1 + deposit_outflow_shock)), 3) AS stressed_lcr,
    collateral_quality,
    central_bank_access
FROM bank_liquidity_scenarios
ORDER BY stressed_lcr ASC;

.print ""
.print "Public debt service under monetary tightening"
SELECT
    scenario,
    public_debt,
    average_interest_rate,
    share_rolling_over,
    rate_shock,
    ROUND(public_debt * (average_interest_rate + share_rolling_over * rate_shock), 3) AS shock_adjusted_debt_service,
    ROUND((public_debt * (average_interest_rate + share_rolling_over * rate_shock)) / output, 3) AS debt_service_to_output
FROM public_debt_interaction_scenarios
ORDER BY debt_service_to_output DESC;

.print ""
.print "Sustainable investment affordability"
SELECT
    investment_area,
    expected_social_return,
    financing_cost,
    rate_shock,
    ROUND(expected_social_return - (financing_cost + rate_shock), 3) AS investment_affordability_gap,
    strategic_priority
FROM sustainable_investment_scenarios
ORDER BY investment_affordability_gap DESC;
