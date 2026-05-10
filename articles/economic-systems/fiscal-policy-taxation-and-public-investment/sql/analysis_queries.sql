.headers on
.mode column

.print "Fiscal position and debt dynamics"
SELECT
    scenario,
    tax_revenue,
    public_spending,
    ROUND(tax_revenue - public_spending, 3) AS budget_balance,
    ROUND(tax_revenue / output, 3) AS tax_ratio,
    ROUND(debt_stock / output, 3) AS debt_to_output,
    ROUND(debt_stock + (public_spending - tax_revenue) + interest_rate * debt_stock, 3) AS next_period_debt
FROM fiscal_position_scenarios
ORDER BY budget_balance ASC;

.print ""
.print "Tax distribution and effective tax rates"
SELECT
    income_group,
    income,
    tax_paid,
    transfer_received,
    ROUND(tax_paid / income, 3) AS effective_tax_rate,
    ROUND((tax_paid + consumption_tax_paid + wealth_tax_paid) / income, 3) AS broad_effective_tax_rate,
    ROUND(transfer_received - (tax_paid + consumption_tax_paid + wealth_tax_paid), 3) AS net_transfer_position
FROM tax_distribution_scenarios
ORDER BY income ASC;

.print ""
.print "Public spending composition"
SELECT
    spending_category,
    spending_amount,
    public_investment_component,
    current_service_component,
    ROUND(public_investment_component / spending_amount, 3) AS public_investment_share,
    resilience_score
FROM spending_composition_scenarios
ORDER BY public_investment_share DESC;

.print ""
.print "Fiscal multiplier effects"
SELECT
    instrument,
    delta_g,
    fiscal_multiplier,
    ROUND(delta_g * fiscal_multiplier, 3) AS delta_y,
    slack_index,
    long_run_capacity_score
FROM fiscal_multiplier_scenarios
ORDER BY delta_y DESC;

.print ""
.print "Infrastructure maintenance gaps"
SELECT
    asset_class,
    maintenance_needed,
    maintenance_actual,
    ROUND(maintenance_needed - maintenance_actual, 3) AS maintenance_gap,
    ROUND((maintenance_needed - maintenance_actual) / maintenance_needed, 3) AS maintenance_gap_ratio,
    replacement_cost_if_deferred
FROM infrastructure_maintenance_scenarios
ORDER BY maintenance_gap DESC;

.print ""
.print "Public investment resilience returns"
SELECT
    investment_area,
    public_investment,
    avoided_future_losses,
    ROUND(avoided_future_losses / public_investment, 3) AS avoided_loss_return,
    productivity_gain,
    equity_score,
    climate_resilience_score
FROM public_investment_resilience_scenarios
ORDER BY avoided_loss_return DESC;
