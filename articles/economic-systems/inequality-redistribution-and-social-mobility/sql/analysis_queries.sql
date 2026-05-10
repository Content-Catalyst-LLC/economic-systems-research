.headers on
.mode column

.print "Income, redistribution, and service-adjusted income"
SELECT
    "group" AS group_name,
    market_income,
    taxes,
    transfers,
    public_service_value,
    ROUND(market_income - taxes + transfers, 2) AS disposable_income,
    ROUND(market_income - taxes + transfers + public_service_value, 2) AS service_adjusted_income,
    ROUND(housing_cost / (market_income - taxes + transfers), 3) AS housing_cost_burden
FROM income_distribution
ORDER BY market_income;

.print ""
.print "Income shares"
SELECT
    "group" AS group_name,
    ROUND(market_income / (SELECT SUM(market_income) FROM income_distribution), 3) AS market_income_share,
    ROUND((market_income - taxes + transfers) / (SELECT SUM(market_income - taxes + transfers) FROM income_distribution), 3) AS disposable_income_share
FROM income_distribution
ORDER BY market_income;

.print ""
.print "Wealth concentration"
SELECT
    "group" AS group_name,
    wealth,
    debt,
    ROUND(wealth - debt, 2) AS net_wealth,
    ROUND(wealth / (SELECT SUM(wealth) FROM wealth_distribution), 3) AS wealth_share,
    ROUND((wealth * (1 + asset_return) + inheritance_receipts), 2) AS next_period_wealth
FROM wealth_distribution
ORDER BY wealth DESC;

.print ""
.print "Mobility and opportunity"
SELECT
    scenario,
    persistence_b,
    ROUND(baseline_a + persistence_b * parent_outcome, 2) AS predicted_child_outcome,
    ROUND(
      0.22 * education_access +
      0.20 * health_access +
      0.20 * place_advantage +
      0.18 * network_access +
      0.20 * family_wealth_buffer,
      3
    ) AS opportunity_score
FROM mobility_scenarios
ORDER BY persistence_b ASC;

.print ""
.print "Labor-market security"
SELECT
    sector,
    ROUND(top_wage / bottom_wage, 3) AS wage_dispersion_ratio,
    ROUND(
      0.22 * bargaining_power +
      0.20 * union_strength +
      0.20 * employment_security +
      0.18 * schedule_stability +
      0.20 * benefit_access,
      3
    ) AS labor_security_score
FROM labor_market_scenarios
ORDER BY labor_security_score DESC;

.print ""
.print "Place-based opportunity"
SELECT
    place,
    ROUND(housing_cost / median_income, 3) AS housing_cost_burden,
    ROUND(
      0.20 * school_quality +
      0.18 * transit_access +
      0.18 * environmental_quality +
      0.20 * job_access +
      0.14 * homeownership_rate,
      3
    ) AS place_opportunity_score
FROM housing_place_scenarios
ORDER BY place_opportunity_score DESC;
