# Scarcity, Allocation, and the Organization of Material Life
# Julia Workflow

using CSV
using DataFrames
using LinearAlgebra

base_dir = normpath(joinpath(@__DIR__, ".."))
processed_dir = joinpath(base_dir, "data", "processed")
table_dir = joinpath(base_dir, "outputs", "tables")

if !isdir(table_dir)
    mkpath(table_dir)
end

scenarios = CSV.read(joinpath(processed_dir, "allocation_scenarios.csv"), DataFrame)
priorities = CSV.read(joinpath(processed_dir, "allocation_priorities.csv"), DataFrame)
reproduction = CSV.read(joinpath(processed_dir, "reproduction_constraints.csv"), DataFrame)

total_resources = 1000.0

allocation = leftjoin(scenarios, priorities, on=:priority)
allocation.allocation_units = allocation.share .* total_resources
allocation.essentiality_weighted_allocation = allocation.allocation_units .* allocation.essentiality
allocation.resilience_weighted_allocation = allocation.allocation_units .* allocation.resilience_value

summary = combine(groupby(allocation, :scenario),
    :allocation_units => sum => :total_allocation,
    :essentiality_weighted_allocation => sum => :essentiality_weighted_total,
    :resilience_weighted_allocation => sum => :resilience_weighted_total
)

CSV.write(joinpath(table_dir, "julia_allocation_results.csv"), summary)

sim = DataFrame(
    scenario = String[],
    period = Int[],
    produced_capacity = Float64[],
    ecological_capacity = Float64[]
)

for row in eachrow(reproduction)
    produced = Float64(row.initial_produced_capacity)
    ecological = Float64(row.initial_ecological_capacity)
    for period in 0:(Int(row.periods)-1)
        push!(sim, (String(row.scenario), period, produced, ecological))
        produced = produced + row.investment + row.maintenance - row.depreciation_rate * produced
        ecological = ecological + row.ecological_restoration + row.regenerative_capacity - row.resource_use
    end
end

CSV.write(joinpath(table_dir, "julia_reproduction_constraints.csv"), sim)

println(summary)
println(sim)
