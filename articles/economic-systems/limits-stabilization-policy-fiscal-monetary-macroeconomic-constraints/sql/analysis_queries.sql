.headers on
.mode column

.print "Constraint phase summary"
SELECT
    constraint_phase,
    COUNT(*) AS observations,
    ROUND(AVG(output_gap_pct), 2) AS avg_output_gap,
    ROUND(AVG(cpi_inflation_yoy_pct), 2) AS avg_inflation,
    ROUND(AVG(federal_funds_rate), 2) AS avg_fed_funds,
    ROUND(AVG(debt_to_gdp), 2) AS avg_debt_to_gdp,
    ROUND(AVG(interest_growth_gap), 2) AS avg_interest_growth_gap,
    ROUND(AVG(debt_stabilizing_primary_balance_pct_gdp), 2) AS avg_debt_stabilizing_balance
FROM quarterly_constraint_indicators
GROUP BY constraint_phase;

.print ""
.print "Elevated inflation constraint quarters"
SELECT
    date,
    ROUND(cpi_inflation_yoy_pct, 2) AS inflation,
    ROUND(output_gap_pct, 2) AS output_gap,
    ROUND(federal_funds_rate, 2) AS fed_funds,
    constraint_phase
FROM quarterly_constraint_indicators
WHERE inflation_constraint_flag = 1
ORDER BY date DESC
LIMIT 12;

.print ""
.print "Potential fiscal-space constraint quarters"
SELECT
    date,
    ROUND(debt_to_gdp, 2) AS debt_to_gdp,
    ROUND(interest_growth_gap, 2) AS interest_growth_gap,
    ROUND(debt_stabilizing_primary_balance_pct_gdp, 2) AS debt_stabilizing_primary_balance,
    constraint_phase
FROM quarterly_constraint_indicators
WHERE fiscal_space_constraint_flag = 1
ORDER BY date DESC
LIMIT 12;

.print ""
.print "Lower-bound monetary constraint quarters"
SELECT
    date,
    ROUND(federal_funds_rate, 2) AS fed_funds,
    ROUND(output_gap_pct, 2) AS output_gap,
    ROUND(unemployment_rate, 2) AS unemployment_rate,
    constraint_phase
FROM quarterly_constraint_indicators
WHERE lower_bound_constraint_flag = 1
ORDER BY date DESC
LIMIT 12;
