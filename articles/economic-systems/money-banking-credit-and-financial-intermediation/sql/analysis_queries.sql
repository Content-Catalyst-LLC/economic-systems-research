.headers on
.mode column

.print "Money aggregate indicators"
SELECT
    scenario,
    currency,
    deposits,
    currency + deposits AS money_supply,
    ROUND(deposits / (currency + deposits), 3) AS deposit_share_of_money,
    near_money_claims,
    central_bank_reserves
FROM money_aggregate_scenarios
ORDER BY money_supply DESC;

.print ""
.print "Bank balance-sheet indicators"
SELECT
    bank,
    assets,
    equity,
    loans,
    bank_deposits,
    ROUND(assets / equity, 3) AS leverage,
    ROUND(equity / assets, 3) AS capital_ratio,
    ROUND(loans / bank_deposits, 3) AS loan_to_deposit_ratio,
    ROUND(liquid_assets / assets, 3) AS liquid_asset_ratio
FROM bank_balance_sheet_scenarios
ORDER BY leverage DESC;

.print ""
.print "Debt-service stress"
SELECT
    borrower_group,
    income_or_ebit,
    interest_payment,
    principal_payment,
    ROUND(income_or_ebit / interest_payment, 3) AS interest_coverage_ratio,
    ROUND((interest_payment + principal_payment) / income_or_ebit, 3) AS debt_service_ratio
FROM debt_service_scenarios
ORDER BY debt_service_ratio DESC;

.print ""
.print "Liquidity stress"
SELECT
    institution,
    hqla,
    net_cash_outflows,
    ROUND(hqla / net_cash_outflows, 3) AS liquidity_coverage_ratio,
    deposit_outflow_rate,
    market_funding_rollover_rate
FROM liquidity_stress_scenarios
ORDER BY liquidity_coverage_ratio ASC;

.print ""
.print "Credit allocation and developmental score"
SELECT
    credit_channel,
    flow_share,
    productive_score,
    speculation_score,
    resilience_score,
    inclusion_score,
    ROUND(
      0.34 * productive_score +
      0.28 * resilience_score +
      0.22 * inclusion_score +
      0.16 * (1 - speculation_score),
      3
    ) AS developmental_credit_score
FROM credit_allocation_scenarios
ORDER BY developmental_credit_score DESC;
