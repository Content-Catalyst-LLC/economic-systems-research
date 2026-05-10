# Inequality, Redistribution, and Social Mobility
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

income = CSV.read(joinpath(processed_dir, "income_distribution.csv"), DataFrame)
wealth = CSV.read(joinpath(processed_dir, "wealth_distribution.csv"), DataFrame)
mobility = CSV.read(joinpath(processed_dir, "mobility_scenarios.csv"), DataFrame)
labor = CSV.read(joinpath(processed_dir, "labor_market_scenarios.csv"), DataFrame)
place = CSV.read(joinpath(processed_dir, "housing_place_scenarios.csv"), DataFrame)

income.disposable_income = income.market_income .- income.taxes .+ income.transfers
income.service_adjusted_income = income.disposable_income .+ income.public_service_value
income.housing_adjusted_income = income.service_adjusted_income .- income.housing_cost .- income.debt_service
income.market_income_share = income.market_income ./ sum(income.market_income)
income.disposable_income_share = income.disposable_income ./ sum(income.disposable_income)
income.housing_cost_burden = income.housing_cost ./ income.disposable_income

wealth.net_wealth = wealth.wealth .- wealth.debt
wealth.wealth_share = wealth.wealth ./ sum(wealth.wealth)
wealth.next_period_wealth = wealth.wealth .* (1 .+ wealth.asset_return) .+ wealth.inheritance_receipts
wealth.next_period_wealth_share = wealth.next_period_wealth ./ sum(wealth.next_period_wealth)

mobility.predicted_child_outcome = mobility.baseline_a .+ mobility.persistence_b .* mobility.parent_outcome
mobility.opportunity_score =
    0.22 .* mobility.education_access .+
    0.20 .* mobility.health_access .+
    0.20 .* mobility.place_advantage .+
    0.18 .* mobility.network_access .+
    0.20 .* mobility.family_wealth_buffer
mobility.mobility_openness_score = (1 .- mobility.persistence_b) .* 0.55 .+ mobility.opportunity_score .* 0.45

labor.wage_dispersion_ratio = labor.top_wage ./ labor.bottom_wage
labor.labor_security_score =
    0.22 .* labor.bargaining_power .+
    0.20 .* labor.union_strength .+
    0.20 .* labor.employment_security .+
    0.18 .* labor.schedule_stability .+
    0.20 .* labor.benefit_access

place.housing_cost_burden = place.housing_cost ./ place.median_income
place.place_opportunity_score =
    0.20 .* place.school_quality .+
    0.18 .* place.transit_access .+
    0.18 .* place.environmental_quality .+
    0.20 .* place.job_access .+
    0.14 .* place.homeownership_rate .+
    0.10 .* (1 .- place.housing_cost_burden ./ maximum(place.housing_cost_burden))

CSV.write(joinpath(table_dir, "julia_income_distribution_results.csv"), income)
CSV.write(joinpath(table_dir, "julia_wealth_distribution_results.csv"), wealth)
CSV.write(joinpath(table_dir, "julia_mobility_results.csv"), mobility)
CSV.write(joinpath(table_dir, "julia_labor_market_results.csv"), labor)
CSV.write(joinpath(table_dir, "julia_housing_place_results.csv"), place)

println(income[:, [:group, :market_income, :disposable_income, :service_adjusted_income, :housing_adjusted_income]])
println(wealth[:, [:group, :wealth_share, :next_period_wealth_share]])
println(mobility[:, [:scenario, :persistence_b, :predicted_child_outcome, :opportunity_score, :mobility_openness_score]])
println(labor[:, [:sector, :wage_dispersion_ratio, :labor_security_score]])
println(place[:, [:place, :housing_cost_burden, :place_opportunity_score]])
