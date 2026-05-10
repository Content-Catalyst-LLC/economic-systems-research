.headers on
.mode column

.print "Aggregate demand and output gaps"
SELECT
    scenario,
    consumption + investment + government_spending + net_exports AS output,
    potential_output,
    ROUND(((consumption + investment + government_spending + net_exports) - potential_output) / potential_output, 3) AS output_gap,
    ROUND(consumption / (consumption + investment + government_spending + net_exports), 3) AS consumption_share,
    ROUND(investment / (consumption + investment + government_spending + net_exports), 3) AS investment_share
FROM aggregate_demand_scenarios
ORDER BY output_gap ASC;

.print ""
.print "Household balance-sheet fragility"
SELECT
    household_group,
    income,
    debt_service,
    liquid_savings,
    ROUND(debt_service / income, 3) AS debt_burden_ratio,
    ROUND(liquid_savings / (income / 12), 3) AS savings_buffer_months,
    ROUND(debt_service / (income * (1 - job_loss_income_shock)), 3) AS post_shock_debt_burden_ratio
FROM household_balance_sheet_scenarios
ORDER BY post_shock_debt_burden_ratio DESC;

.print ""
.print "Credit contraction and real debt burden"
SELECT
    scenario,
    credit_growth,
    nominal_debt,
    price_level,
    ROUND(nominal_debt / price_level, 3) AS real_debt_burden,
    asset_price_change,
    default_pressure
FROM credit_contraction_scenarios
ORDER BY real_debt_burden DESC;

.print ""
.print "Fiscal stabilization"
SELECT
    scenario,
    delta_g,
    fiscal_multiplier,
    ROUND(fiscal_multiplier * delta_g, 3) AS delta_y,
    automatic_stabilizer_strength,
    public_capacity_score
FROM fiscal_stabilization_scenarios
ORDER BY delta_y DESC;

.print ""
.print "Open economy shock transmission"
SELECT
    external_shock,
    shock_intensity,
    ROUND(shock_intensity * (
      0.28 * export_exposure +
      0.28 * import_price_exposure +
      0.24 * capital_flow_exposure +
      0.20 * fx_debt_exposure
    ), 3) AS transmission_score
FROM open_economy_shock_scenarios
ORDER BY transmission_score DESC;
