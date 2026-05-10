# Finance, Leverage, and Systemic Risk
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

institutions = CSV.read(joinpath(processed_dir, "institution_balance_sheets.csv"), DataFrame)
collateral = CSV.read(joinpath(processed_dir, "collateral_haircut_scenarios.csv"), DataFrame)
funding = CSV.read(joinpath(processed_dir, "funding_gap_scenarios.csv"), DataFrame)
households = CSV.read(joinpath(processed_dir, "household_leverage_scenarios.csv"), DataFrame)
buffers = CSV.read(joinpath(processed_dir, "macroprudential_buffer_scenarios.csv"), DataFrame)
sustainability = CSV.read(joinpath(processed_dir, "sustainability_shock_scenarios.csv"), DataFrame)

institutions.equity = institutions.assets .- institutions.debt
institutions.leverage = institutions.assets ./ institutions.equity
institutions.debt_to_equity = institutions.debt ./ institutions.equity
institutions.capital_ratio = institutions.equity ./ institutions.assets
institutions.raw_funding_gap = institutions.short_term_liabilities .- institutions.liquid_assets

collateral.borrowing_capacity_before = (1 .- collateral.haircut_before) .* collateral.collateral_value
collateral.borrowing_capacity_after = (1 .- collateral.haircut_after) .* collateral.collateral_value
collateral.haircut_funding_gap = collateral.outstanding_borrowing .- collateral.borrowing_capacity_after

funding.raw_funding_gap = funding.short_term_liabilities .- funding.liquid_assets
funding.rollover_adjusted_gap = funding.short_term_liabilities .* (1 .- funding.rollover_rate) .- funding.liquid_assets
funding.backstop_adjusted_gap = funding.rollover_adjusted_gap .* (1 .- funding.emergency_liquidity_access)

households.loan_to_value = [row.housing_value > 0 ? row.mortgage_debt / row.housing_value : 0.0 for row in eachrow(households)]
households.debt_service_ratio = households.debt_service ./ households.income
households.housing_value_after_15pct_shock = households.housing_value .* 0.85
households.ltv_after_housing_shock = [row.housing_value_after_15pct_shock > 0 ? row.mortgage_debt / row.housing_value_after_15pct_shock : 0.0 for row in eachrow(households)]

buffers.macroprudential_resilience_score =
    0.24 .* (buffers.capital_buffer ./ maximum(buffers.capital_buffer)) .+
    0.24 .* (buffers.liquidity_buffer ./ maximum(buffers.liquidity_buffer)) .+
    0.20 .* (buffers.countercyclical_buffer ./ maximum(buffers.countercyclical_buffer)) .+
    0.16 .* (1 .- buffers.loan_to_value_limit) .+
    0.16 .* buffers.stress_test_strength

sustainability.expected_loss = sustainability.portfolio_exposure .* sustainability.loss_given_shock
sustainability.systemic_sustainability_risk_score =
    0.36 .* sustainability.expected_loss .+
    0.28 .* sustainability.liquidity_impact .+
    0.22 .* sustainability.public_backstop_need .+
    0.14 .* sustainability.portfolio_exposure

CSV.write(joinpath(table_dir, "julia_finance_leverage_results.csv"), institutions)
CSV.write(joinpath(table_dir, "julia_collateral_haircut_results.csv"), collateral)
CSV.write(joinpath(table_dir, "julia_funding_gap_results.csv"), funding)
CSV.write(joinpath(table_dir, "julia_household_leverage_results.csv"), households)
CSV.write(joinpath(table_dir, "julia_macroprudential_buffer_results.csv"), buffers)
CSV.write(joinpath(table_dir, "julia_sustainability_shock_results.csv"), sustainability)

println(institutions[:, [:institution, :leverage, :capital_ratio, :raw_funding_gap]])
println(collateral[:, [:scenario, :haircut_funding_gap]])
println(buffers[:, [:scenario, :macroprudential_resilience_score]])
