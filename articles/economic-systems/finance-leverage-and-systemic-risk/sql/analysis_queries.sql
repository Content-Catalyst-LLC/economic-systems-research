.headers on
.mode column

.print "Institution leverage indicators"
SELECT
    institution,
    assets,
    debt,
    assets - debt AS equity,
    ROUND(assets / (assets - debt), 3) AS leverage,
    ROUND(debt / (assets - debt), 3) AS debt_to_equity,
    ROUND((assets - debt) / assets, 3) AS capital_ratio,
    ROUND(short_term_liabilities - liquid_assets, 3) AS raw_funding_gap
FROM institution_balance_sheets
ORDER BY leverage DESC;

.print ""
.print "Collateral haircut stress"
SELECT
    scenario,
    collateral_value,
    haircut_before,
    haircut_after,
    outstanding_borrowing,
    ROUND((1 - haircut_before) * collateral_value, 3) AS borrowing_capacity_before,
    ROUND((1 - haircut_after) * collateral_value, 3) AS borrowing_capacity_after,
    ROUND(outstanding_borrowing - ((1 - haircut_after) * collateral_value), 3) AS haircut_funding_gap
FROM collateral_haircut_scenarios
ORDER BY haircut_funding_gap DESC;

.print ""
.print "Funding gap stress"
SELECT
    institution,
    short_term_liabilities,
    liquid_assets,
    rollover_rate,
    emergency_liquidity_access,
    ROUND(short_term_liabilities - liquid_assets, 3) AS raw_funding_gap,
    ROUND((short_term_liabilities * (1 - rollover_rate) - liquid_assets) * (1 - emergency_liquidity_access), 3) AS backstop_adjusted_gap
FROM funding_gap_scenarios
ORDER BY backstop_adjusted_gap DESC;

.print ""
.print "Network incoming exposure"
SELECT
    to_institution AS institution,
    SUM(exposure) AS total_incoming_exposure
FROM network_exposure_matrix
GROUP BY to_institution
ORDER BY total_incoming_exposure DESC;

.print ""
.print "Household leverage stress"
SELECT
    household_group,
    housing_value,
    mortgage_debt,
    income,
    debt_service,
    CASE WHEN housing_value > 0 THEN ROUND(mortgage_debt / housing_value, 3) ELSE 0 END AS loan_to_value,
    ROUND(debt_service / income, 3) AS debt_service_ratio
FROM household_leverage_scenarios
ORDER BY debt_service_ratio DESC;
