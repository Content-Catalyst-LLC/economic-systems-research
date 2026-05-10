# Fiscal Policy, Taxation, and Public Investment
# Julia Workflow

using CSV
using DataFrames
using Statistics

base_dir = normpath(joinpath(@__DIR__, ".."))
processed_dir = joinpath(base_dir, "data", "processed")
table_dir = joinpath(base_dir, "outputs", "tables")

if !isdir(table_dir)
    mkpath(table_dir)
end

fiscal = CSV.read(joinpath(processed_dir, "fiscal_position_scenarios.csv"), DataFrame)
taxes = CSV.read(joinpath(processed_dir, "tax_distribution_scenarios.csv"), DataFrame)
spending = CSV.read(joinpath(processed_dir, "spending_composition_scenarios.csv"), DataFrame)
multipliers = CSV.read(joinpath(processed_dir, "fiscal_multiplier_scenarios.csv"), DataFrame)
maintenance = CSV.read(joinpath(processed_dir, "infrastructure_maintenance_scenarios.csv"), DataFrame)
resilience = CSV.read(joinpath(processed_dir, "public_investment_resilience_scenarios.csv"), DataFrame)

fiscal.budget_balance = fiscal.tax_revenue .- fiscal.public_spending
fiscal.primary_balance = fiscal.tax_revenue .- fiscal.primary_spending
fiscal.tax_ratio = fiscal.tax_revenue ./ fiscal.output
fiscal.debt_to_output = fiscal.debt_stock ./ fiscal.output
fiscal.interest_cost = fiscal.interest_rate .* fiscal.debt_stock
fiscal.next_period_debt = fiscal.debt_stock .+ (fiscal.public_spending .- fiscal.tax_revenue) .+ fiscal.interest_cost

taxes.effective_tax_rate = taxes.tax_paid ./ taxes.income
taxes.total_tax_with_consumption_and_wealth = taxes.tax_paid .+ taxes.consumption_tax_paid .+ taxes.wealth_tax_paid
taxes.broad_effective_tax_rate = taxes.total_tax_with_consumption_and_wealth ./ taxes.income
taxes.net_transfer_position = taxes.transfer_received .- taxes.total_tax_with_consumption_and_wealth

spending.public_investment_share = spending.public_investment_component ./ spending.spending_amount
spending.weighted_resilience_contribution = spending.spending_amount .* spending.resilience_score

multipliers.delta_y = multipliers.fiscal_multiplier .* multipliers.delta_g

maintenance.maintenance_gap = maintenance.maintenance_needed .- maintenance.maintenance_actual
maintenance.maintenance_gap_ratio = maintenance.maintenance_gap ./ maintenance.maintenance_needed

resilience.avoided_loss_return = resilience.avoided_future_losses ./ resilience.public_investment
resilience.resilience_investment_score =
    0.32 .* (resilience.avoided_loss_return ./ maximum(resilience.avoided_loss_return)) .+
    0.22 .* (resilience.productivity_gain ./ maximum(resilience.productivity_gain)) .+
    0.23 .* resilience.equity_score .+
    0.23 .* resilience.climate_resilience_score

CSV.write(joinpath(table_dir, "julia_fiscal_policy_results.csv"), fiscal)
CSV.write(joinpath(table_dir, "julia_tax_distribution_results.csv"), taxes)
CSV.write(joinpath(table_dir, "julia_spending_composition_results.csv"), spending)
CSV.write(joinpath(table_dir, "julia_fiscal_multiplier_results.csv"), multipliers)
CSV.write(joinpath(table_dir, "julia_infrastructure_maintenance_results.csv"), maintenance)
CSV.write(joinpath(table_dir, "julia_public_investment_resilience_results.csv"), resilience)

println(fiscal[:, [:scenario, :budget_balance, :tax_ratio, :next_period_debt]])
println(taxes[:, [:income_group, :effective_tax_rate, :broad_effective_tax_rate]])
println(resilience[:, [:investment_area, :avoided_loss_return, :resilience_investment_score]])
