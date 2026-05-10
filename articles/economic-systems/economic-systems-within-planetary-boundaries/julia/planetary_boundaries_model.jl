# Economic Systems Within Planetary Boundaries
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

boundaries = CSV.read(joinpath(processed_dir, "boundary_pressure.csv"), DataFrame)
resources = CSV.read(joinpath(processed_dir, "resource_use_identity.csv"), DataFrame)
transition = CSV.read(joinpath(processed_dir, "transition_capacity.csv"), DataFrame)
finance = CSV.read(joinpath(processed_dir, "finance_direction.csv"), DataFrame)
accounting = CSV.read(joinpath(processed_dir, "boundary_accounting.csv"), DataFrame)

boundaries.boundary_pressure_ratio = boundaries.economic_pressure ./ boundaries.earth_system_capacity
boundaries.overshoot_gap = max.(boundaries.boundary_pressure_ratio .- 1, 0)

resources.resource_use = resources.population .* resources.affluence .* resources.resource_intensity
resources.resource_wellbeing_efficiency = resources.wellbeing_index ./ resources.resource_use

transition.transition_capacity_score =
    0.20 .* transition.state_capacity .+
    0.18 .* transition.public_investment .+
    0.18 .* transition.social_legitimacy .+
    0.16 .* transition.technological_capability .+
    0.14 .* transition.coordination .+
    0.14 .* transition.adaptive_governance

finance.finance_direction_score =
    0.18 .* (1 .- finance.fossil_exposure) .+
    0.20 .* finance.restoration_investment .+
    0.20 .* finance.resilience_investment .+
    0.16 .* finance.circular_materials .+
    0.16 .* finance.public_goods_alignment .+
    0.10 .* (1 .- finance.short_term_return_pressure)

accounting.boundary_aware_progress =
    0.30 .* accounting.wellbeing .+
    0.22 .* accounting.inclusion .+
    0.20 .* accounting.natural_capital .+
    0.12 .* (1 .- accounting.material_throughput) .+
    0.12 .* (1 .- accounting.ecological_pressure)

CSV.write(joinpath(table_dir, "julia_boundary_pressure_results.csv"), boundaries)
CSV.write(joinpath(table_dir, "julia_resource_use_results.csv"), resources)
CSV.write(joinpath(table_dir, "julia_transition_capacity_results.csv"), transition)
CSV.write(joinpath(table_dir, "julia_finance_direction_results.csv"), finance)
CSV.write(joinpath(table_dir, "julia_boundary_accounting_results.csv"), accounting)

println(boundaries[:, [:boundary, :boundary_pressure_ratio, :overshoot_gap]])
println(resources[:, [:scenario, :resource_use, :resource_wellbeing_efficiency]])
println(transition[:, [:scenario, :transition_capacity_score]])
println(finance[:, [:portfolio, :finance_direction_score]])
println(accounting[:, [:scenario, :boundary_aware_progress]])
