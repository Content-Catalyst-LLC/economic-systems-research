# Inflation, Energy Shocks, and Supply Constraints
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

prices = CSV.read(joinpath(processed_dir, "price_index_scenarios.csv"), DataFrame)
pass_through = CSV.read(joinpath(processed_dir, "sector_energy_pass_through_scenarios.csv"), DataFrame)
households = CSV.read(joinpath(processed_dir, "household_energy_burden_scenarios.csv"), DataFrame)
imports = CSV.read(joinpath(processed_dir, "import_price_transmission_scenarios.csv"), DataFrame)
bottlenecks = CSV.read(joinpath(processed_dir, "supply_bottleneck_scenarios.csv"), DataFrame)
market_power = CSV.read(joinpath(processed_dir, "market_power_price_amplification_scenarios.csv"), DataFrame)
resilience = CSV.read(joinpath(processed_dir, "resilience_policy_scenarios.csv"), DataFrame)

sort!(prices, [:scenario, :period])
prices.inflation_rate = zeros(nrow(prices))
for scenario in unique(prices.scenario)
    idx = findall(prices.scenario .== scenario)
    for j in 2:length(idx)
        prices.inflation_rate[idx[j]] = prices.price_level[idx[j]] / prices.price_level[idx[j - 1]] - 1
    end
end

pass_through.estimated_price_change =
    pass_through.alpha_energy .* pass_through.energy_cost_change .+
    pass_through.beta_wage .* pass_through.wage_cost_change .+
    pass_through.gamma_materials .* pass_through.materials_cost_change

households.household_energy_burden = households.energy_spending ./ households.income
households.transport_fuel_burden = households.transport_fuel_spending ./ households.income
households.combined_energy_transport_burden = (households.energy_spending .+ households.transport_fuel_spending) ./ households.income
households.real_wage = [row.nominal_wage > 0 ? row.nominal_wage / row.price_level_relative : 0.0 for row in eachrow(households)]

imports.import_price_change = imports.world_price_change .+ imports.exchange_rate_effect
imports.weighted_import_inflation_pressure = imports.import_price_change .* imports.import_dependence .* (0.5 .+ imports.energy_share_of_imports)

bottlenecks.effective_output_capacity = [
    minimum([row.capital_capacity, row.labor_capacity, row.energy_capacity, row.logistics_capacity, row.supply_availability])
    for row in eachrow(bottlenecks)
]
bottlenecks.bottleneck_gap = 1 .- bottlenecks.effective_output_capacity

market_power.amplified_price_change =
    market_power.cost_shock .+
    0.45 .* market_power.market_concentration_index .* market_power.margin_expansion .+
    0.25 .* market_power.demand_necessity_score .* market_power.margin_expansion

market_power.price_amplification_score = market_power.amplified_price_change .- market_power.cost_shock

resilience.long_run_resilience_score =
    0.24 .* resilience.energy_resilience .+
    0.22 .* resilience.supply_diversification .+
    0.18 .* resilience.household_protection .+
    0.18 .* resilience.infrastructure_capacity .+
    0.18 .* resilience.public_buffer_capacity

resilience.balanced_policy_score = 0.70 .* resilience.long_run_resilience_score .+ 0.30 .* resilience.near_term_disinflation

CSV.write(joinpath(table_dir, "julia_inflation_energy_results.csv"), prices)
CSV.write(joinpath(table_dir, "julia_energy_pass_through_results.csv"), pass_through)
CSV.write(joinpath(table_dir, "julia_household_energy_burden_results.csv"), households)
CSV.write(joinpath(table_dir, "julia_import_price_transmission_results.csv"), imports)
CSV.write(joinpath(table_dir, "julia_supply_bottleneck_results.csv"), bottlenecks)
CSV.write(joinpath(table_dir, "julia_market_power_results.csv"), market_power)
CSV.write(joinpath(table_dir, "julia_resilience_policy_results.csv"), resilience)

println(pass_through[:, [:sector, :estimated_price_change]])
println(households[:, [:household_group, :combined_energy_transport_burden, :real_wage]])
println(resilience[:, [:policy, :balanced_policy_score]])
