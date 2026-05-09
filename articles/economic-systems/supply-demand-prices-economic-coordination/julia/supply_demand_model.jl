# Supply, Demand, Prices, and Economic Coordination
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

scenarios = CSV.read(joinpath(processed_dir, "market_parameter_scenarios.csv"), DataFrame)

function solve_equilibrium(a, b, c, d, markup_rate)
    competitive_price = (a - c) / (b + d)
    price = competitive_price * (1 + markup_rate)
    quantity = a - b * price
    return price, quantity
end

results = DataFrame(
    market = String[],
    scenario = String[],
    equilibrium_price = Float64[],
    equilibrium_quantity = Float64[],
    demand_elasticity = Float64[],
    supply_elasticity = Float64[],
    marginal_social_cost_price = Float64[],
    social_cost_gap = Float64[]
)

for row in eachrow(scenarios)
    price, quantity = solve_equilibrium(row.a, row.b, row.c, row.d, row.markup_rate)
    demand_elasticity = -row.b * (price / quantity)
    supply_elasticity = row.d * (price / quantity)
    social_price = price + row.external_cost

    push!(
        results,
        (
            String(row.market),
            String(row.scenario),
            price,
            quantity,
            demand_elasticity,
            supply_elasticity,
            social_price,
            social_price - price
        )
    )
end

CSV.write(joinpath(table_dir, "julia_equilibrium_results.csv"), results)
println(results)
