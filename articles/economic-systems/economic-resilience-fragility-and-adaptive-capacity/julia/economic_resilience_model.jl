# Economic Resilience, Fragility, and Adaptive Capacity
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

resilience = CSV.read(joinpath(processed_dir, "resilience_scenarios.csv"), DataFrame)
fragility = CSV.read(joinpath(processed_dir, "fragility_scenarios.csv"), DataFrame)
adaptive = CSV.read(joinpath(processed_dir, "adaptive_capacity.csv"), DataFrame)
shocks = CSV.read(joinpath(processed_dir, "shock_scenarios.csv"), DataFrame)
households = CSV.read(joinpath(processed_dir, "household_resilience.csv"), DataFrame)

resilience.resilience_score =
    0.18 .* resilience.buffers .+
    0.18 .* resilience.redundancy .+
    0.18 .* resilience.coordination .+
    0.14 .* resilience.trust .+
    0.16 .* resilience.learning .+
    0.16 .* resilience.recovery_capacity

fragility.fragility_score =
    0.20 .* fragility.leverage .+
    0.18 .* fragility.concentration .+
    0.20 .* fragility.exposure .+
    0.18 .* fragility.underinvestment .+
    0.14 .* fragility.inequality .+
    0.10 .* fragility.political_fragmentation

adaptive.adaptive_capacity_score =
    0.18 .* adaptive.information .+
    0.18 .* adaptive.fiscal_space .+
    0.16 .* adaptive.skills .+
    0.16 .* adaptive.flexibility .+
    0.16 .* adaptive.legitimacy .+
    0.16 .* adaptive.implementation_capacity

shocks.vulnerability =
    0.26 .* shocks.household_vulnerability .+
    0.22 .* shocks.firm_vulnerability .+
    0.18 .* (1 .- shocks.public_capacity) .+
    0.18 .* (1 .- shocks.infrastructure_integrity) .+
    0.16 .* (1 .- shocks.recovery_speed)

shocks.shock_impact = shocks.shock_magnitude .* shocks.vulnerability

households.distributional_resilience_score =
    0.22 .* households.income_security .+
    0.18 .* households.savings .+
    0.18 .* households.care_access .+
    0.18 .* households.housing_stability .+
    0.14 .* households.social_protection .+
    0.10 .* households.mobility

CSV.write(joinpath(table_dir, "julia_resilience_results.csv"), resilience)
CSV.write(joinpath(table_dir, "julia_fragility_results.csv"), fragility)
CSV.write(joinpath(table_dir, "julia_adaptive_capacity_results.csv"), adaptive)
CSV.write(joinpath(table_dir, "julia_shock_results.csv"), shocks)
CSV.write(joinpath(table_dir, "julia_household_resilience_results.csv"), households)

println(resilience[:, [:scenario, :resilience_score]])
println(fragility[:, [:scenario, :fragility_score]])
println(adaptive[:, [:scenario, :adaptive_capacity_score]])
println(shocks[:, [:shock, :vulnerability, :shock_impact]])
println(households[:, [:household_group, :distributional_resilience_score]])
