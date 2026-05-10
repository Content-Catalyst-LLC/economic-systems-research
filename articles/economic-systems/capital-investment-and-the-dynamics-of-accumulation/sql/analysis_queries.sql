.headers on
.mode column

.print "Capital stock scenario indicators"
SELECT
    scenario,
    initial_capital,
    annual_investment,
    depreciation_rate,
    ROUND(annual_investment / output, 3) AS investment_rate,
    ROUND(initial_capital / labor, 3) AS initial_capital_intensity
FROM capital_stock_scenarios
ORDER BY investment_rate DESC;

.print ""
.print "Ownership and claims on output"
SELECT
    scenario,
    wage_share,
    profit_share,
    rent_share,
    tax_public_share,
    public_reinvestment_share,
    ROUND(profit_share + rent_share, 3) AS capital_income_share,
    ROUND(wage_share / (profit_share + rent_share), 3) AS labor_to_capital_claim_ratio
FROM ownership_distribution_scenarios
ORDER BY labor_to_capital_claim_ratio DESC;

.print ""
.print "Finance direction and developmental allocation"
SELECT
    finance_channel,
    flow_share,
    productive_capacity_score,
    resilience_score,
    speculation_score,
    extraction_score,
    ROUND(
      0.35 * productive_capacity_score +
      0.35 * resilience_score +
      0.15 * (1 - speculation_score) +
      0.15 * (1 - extraction_score),
      3
    ) AS developmental_allocation_score
FROM finance_direction_scenarios
ORDER BY developmental_allocation_score DESC;

.print ""
.print "Sustainable investment score"
SELECT
    project,
    financial_return_score,
    resilience_score,
    ecological_alignment_score,
    public_value_score,
    maintenance_score,
    ROUND(
      0.18 * financial_return_score +
      0.26 * resilience_score +
      0.24 * ecological_alignment_score +
      0.22 * public_value_score +
      0.10 * maintenance_score,
      3
    ) AS sustainable_investment_score
FROM sustainable_investment_scenarios
ORDER BY sustainable_investment_score DESC;

.print ""
.print "Maintenance gap by scenario"
SELECT
    scenario,
    SUM(new_maintenance_need) AS total_new_maintenance_need,
    SUM(actual_maintenance) AS total_actual_maintenance,
    SUM(new_maintenance_need - actual_maintenance) AS cumulative_backlog_change
FROM maintenance_scenarios
GROUP BY scenario
ORDER BY cumulative_backlog_change DESC;
