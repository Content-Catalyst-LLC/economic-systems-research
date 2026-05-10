# Monetary Policy, Central Banking, and Financial Conditions
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

policy = CSV.read(joinpath(processed_dir, "policy_rate_scenarios.csv"), DataFrame)
debt = CSV.read(joinpath(processed_dir, "debt_service_scenarios.csv"), DataFrame)
conditions = CSV.read(joinpath(processed_dir, "financial_conditions_scenarios.csv"), DataFrame)
liquidity = CSV.read(joinpath(processed_dir, "bank_liquidity_scenarios.csv"), DataFrame)
public_debt = CSV.read(joinpath(processed_dir, "public_debt_interaction_scenarios.csv"), DataFrame)
investment = CSV.read(joinpath(processed_dir, "sustainable_investment_scenarios.csv"), DataFrame)

policy.real_rate = policy.nominal_rate .- policy.expected_inflation
policy.policy_rate_rule = policy.neutral_rate .+ policy.a_inflation .* policy.inflation_gap .+ policy.b_output .* policy.output_gap
policy.stance_gap = policy.nominal_rate .- policy.policy_rate_rule

debt.debt_service_ratio = debt.debt_service ./ debt.income
debt.additional_debt_service = debt.debt_stock .* debt.repricing_share .* debt.rate_shock ./ 12
debt.post_shock_dsr = (debt.debt_service .+ debt.additional_debt_service) ./ debt.income

conditions.financial_conditions_index =
    conditions.policy_rate .+
    conditions.credit_spread .+
    conditions.exchange_rate_pressure .+
    conditions.lending_tightness .* 0.08 .+
    conditions.market_liquidity_stress .* 0.08 .-
    conditions.equity_price_change .* 0.18

liquidity.liquidity_coverage_ratio = liquidity.liquid_assets ./ liquidity.short_term_outflows
liquidity.stressed_lcr = liquidity.liquid_assets ./ (liquidity.short_term_outflows .* (1 .+ liquidity.deposit_outflow_shock))

public_debt.current_debt_service = public_debt.public_debt .* public_debt.average_interest_rate
public_debt.shock_adjusted_interest_rate = public_debt.average_interest_rate .+ public_debt.share_rolling_over .* public_debt.rate_shock
public_debt.shock_adjusted_debt_service = public_debt.public_debt .* public_debt.shock_adjusted_interest_rate
public_debt.debt_service_to_output = public_debt.shock_adjusted_debt_service ./ public_debt.output

investment.post_shock_financing_cost = investment.financing_cost .+ investment.rate_shock
investment.investment_affordability_gap = investment.expected_social_return .- investment.post_shock_financing_cost

CSV.write(joinpath(table_dir, "julia_monetary_policy_results.csv"), policy)
CSV.write(joinpath(table_dir, "julia_debt_service_results.csv"), debt)
CSV.write(joinpath(table_dir, "julia_financial_conditions_results.csv"), conditions)
CSV.write(joinpath(table_dir, "julia_bank_liquidity_results.csv"), liquidity)
CSV.write(joinpath(table_dir, "julia_public_debt_interaction_results.csv"), public_debt)
CSV.write(joinpath(table_dir, "julia_sustainable_investment_results.csv"), investment)

println(policy[:, [:scenario, :real_rate, :policy_rate_rule, :stance_gap]])
println(debt[:, [:borrower_group, :post_shock_dsr]])
println(conditions[:, [:scenario, :financial_conditions_index]])
println(investment[:, [:investment_area, :investment_affordability_gap]])
