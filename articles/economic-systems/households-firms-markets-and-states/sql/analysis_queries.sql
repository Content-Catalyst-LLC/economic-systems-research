.headers on
.mode column

.print "Institutional flow balances"
SELECT
    scenario,
    household_wages + household_transfers + asset_income - taxes_paid - debt_service - household_consumption AS household_saving,
    firm_revenue - labor_cost - capital_cost - input_cost AS firm_profit,
    public_spending + public_transfers + public_debt_interest - tax_revenue AS public_borrowing
FROM institutional_flow_scenarios
ORDER BY scenario;

.print ""
.print "Effective access"
SELECT
    group_name,
    ROUND(need_index, 2) AS need_index,
    ROUND(income_command, 2) AS income_command,
    ROUND(price_burden, 2) AS price_burden,
    ROUND(institutional_access, 2) AS institutional_access,
    ROUND(
      0.34 * income_command +
      0.30 * institutional_access +
      0.22 * (1 - price_burden) +
      0.14 * need_index,
      3
    ) AS effective_access
FROM market_access_scenarios
ORDER BY effective_access ASC;

.print ""
.print "Risk distribution scenarios"
SELECT
    scenario,
    household_risk,
    firm_risk,
    market_risk,
    state_risk,
    ROUND(state_risk - household_risk, 3) AS state_minus_household_risk
FROM risk_distribution_scenarios
ORDER BY state_minus_household_risk DESC;
