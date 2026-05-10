.headers on
.mode column

.print "Debt position metrics"
SELECT
    scenario,
    ROUND(debt_stock / output, 3) AS debt_ratio,
    ROUND(external_debt_service / export_earnings, 3) AS external_debt_service_ratio,
    ROUND(foreign_currency_debt * exchange_rate, 2) AS domestic_currency_fx_burden,
    ROUND(reserves / short_term_external_obligations, 3) AS reserve_adequacy,
    ROUND((effective_interest_rate - growth_rate) * debt_stock + primary_deficit, 2) AS interest_growth_pressure
FROM debt_position_scenarios
ORDER BY external_debt_service_ratio DESC;

.print ""
.print "Currency hierarchy constraint"
SELECT
    scenario,
    ROUND(
      0.24 * foreign_currency_debt_share +
      0.18 * (1 - own_currency_borrowing_share) +
      0.16 * (1 - market_depth) +
      0.16 * (1 - safe_asset_status) +
      0.14 * (1 - policy_space) +
      0.12 * external_discipline,
      3
    ) AS currency_hierarchy_constraint_score
FROM currency_hierarchy_scenarios
ORDER BY currency_hierarchy_constraint_score DESC;

.print ""
.print "External dependency score"
SELECT
    scenario,
    ROUND(
      0.22 * export_concentration +
      0.20 * import_dependence +
      0.20 * external_finance_reliance +
      0.16 * capital_flow_volatility +
      0.12 * (1 - reserve_buffer) +
      0.10 * (1 - domestic_capability),
      3
    ) AS dependency_score
FROM external_account_scenarios
ORDER BY dependency_score DESC;

.print ""
.print "Policy-space pressure from conditionality"
SELECT
    program,
    ROUND(
      0.22 * fiscal_compression +
      0.18 * (1 - social_spending_protection) +
      0.18 * (1 - public_investment_protection) +
      0.16 * privatization_pressure +
      0.14 * (1 - policy_space) +
      0.12 * (1 - developmental_alignment),
      3
    ) AS policy_space_pressure
FROM conditionality_scenarios
ORDER BY policy_space_pressure DESC;

.print ""
.print "Debt restructuring options"
SELECT
    scenario,
    ROUND(initial_debt * (1 - restructuring_haircut), 2) AS post_restructuring_debt,
    restructuring_haircut,
    maturity_extension,
    interest_relief,
    social_spending_floor,
    growth_recovery,
    creditor_acceptance
FROM restructuring_scenarios
ORDER BY post_restructuring_debt ASC;

.print ""
.print "Sustainable development finance"
SELECT
    scenario,
    ROUND(
      0.22 * productive_investment +
      0.18 * domestic_capability +
      0.18 * export_resilience +
      0.14 * social_protection +
      0.14 * ecological_resilience +
      0.14 * debt_manageability,
      3
    ) AS sustainable_finance_score
FROM sustainable_finance_scenarios
ORDER BY sustainable_finance_score DESC;
