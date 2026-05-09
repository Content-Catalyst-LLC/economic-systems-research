.headers on
.mode column

.print "Stabilization-policy phase summary"
SELECT
    policy_phase,
    COUNT(*) AS observations,
    ROUND(AVG(real_gdp_growth_annualized), 2) AS avg_real_gdp_growth,
    ROUND(AVG(unemployment_rate), 2) AS avg_unemployment,
    ROUND(AVG(output_gap_pct), 2) AS avg_output_gap,
    ROUND(AVG(cpi_inflation_yoy_pct), 2) AS avg_inflation,
    ROUND(AVG(federal_funds_rate), 2) AS avg_federal_funds_rate,
    ROUND(AVG(gov_spending_growth_yoy_pct), 2) AS avg_gov_spending_growth,
    ROUND(AVG(policy_rate_gap), 2) AS avg_policy_rate_gap
FROM quarterly_policy_indicators
GROUP BY policy_phase;

.print ""
.print "Most negative output-gap quarters"
SELECT
    date,
    ROUND(output_gap_pct, 2) AS output_gap_pct,
    ROUND(unemployment_rate, 2) AS unemployment_rate,
    ROUND(federal_funds_rate, 2) AS federal_funds_rate,
    ROUND(gov_spending_growth_yoy_pct, 2) AS gov_spending_growth,
    policy_phase
FROM quarterly_policy_indicators
WHERE output_gap_pct IS NOT NULL
ORDER BY output_gap_pct ASC
LIMIT 12;

.print ""
.print "Largest federal funds rate cuts by quarter"
SELECT
    date,
    ROUND(delta_federal_funds_rate, 2) AS delta_federal_funds_rate,
    ROUND(output_gap_pct, 2) AS output_gap_pct,
    ROUND(unemployment_rate, 2) AS unemployment_rate,
    policy_phase
FROM quarterly_policy_indicators
WHERE delta_federal_funds_rate IS NOT NULL
ORDER BY delta_federal_funds_rate ASC
LIMIT 12;

.print ""
.print "Illustrative Taylor-rule benchmark comparison"
SELECT
    date,
    ROUND(federal_funds_rate, 2) AS federal_funds_rate,
    ROUND(taylor_rule_rate, 2) AS taylor_rule_rate,
    ROUND(policy_rate_gap, 2) AS policy_rate_gap,
    ROUND(cpi_inflation_yoy_pct, 2) AS inflation,
    ROUND(output_gap_pct, 2) AS output_gap
FROM quarterly_policy_indicators
WHERE taylor_rule_rate IS NOT NULL
ORDER BY date DESC
LIMIT 12;
