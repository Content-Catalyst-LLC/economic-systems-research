# Natural Capital, Resource Use, and Environmental Constraint
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

stock = CSV.read(joinpath(processed_dir, "stock_flow_scenarios.csv"), DataFrame)
resources = CSV.read(joinpath(processed_dir, "resource_use_constraints.csv"), DataFrame)
sectors = CSV.read(joinpath(processed_dir, "sector_resource_pressure.csv"), DataFrame)
governance = CSV.read(joinpath(processed_dir, "governance_regimes.csv"), DataFrame)
burdens = CSV.read(joinpath(processed_dir, "justice_burdens.csv"), DataFrame)
resilience = CSV.read(joinpath(processed_dir, "resilience_dependency.csv"), DataFrame)

stock.natural_capital_next = stock.natural_capital_t .+ stock.regeneration .- stock.degradation
stock.regeneration_gap = stock.degradation .- stock.regeneration
stock.threshold_distance = stock.natural_capital_next .- stock.threshold

resources.resource_use_ratio = [
    row.regenerative_capacity > 0 ? row.resource_use / row.regenerative_capacity : Inf
    for row in eachrow(resources)
]
resources.waste_constraint_ratio = resources.emissions ./ resources.absorptive_capacity

sectors.sector_pressure_score =
    0.18 .* sectors.material_intensity .+
    0.18 .* sectors.energy_intensity .+
    0.16 .* sectors.water_intensity .+
    0.14 .* sectors.land_intensity .+
    0.14 .* sectors.waste_intensity .+
    0.12 .* sectors.import_dependence .+
    0.08 .* sectors.social_necessity

governance.resource_governance_score =
    0.14 .* governance.secure_tenure .+
    0.16 .* governance.monitoring .+
    0.16 .* governance.participation .+
    0.14 .* governance.enforcement .+
    0.16 .* governance.adaptive_rules .+
    0.12 .* governance.equity .+
    0.12 .* governance.regeneration_alignment

burdens.justice_burden_score =
    0.24 .* burdens.exposure .+
    0.18 .* (1 .- burdens.income_buffer) .+
    0.18 .* (1 .- burdens.public_infrastructure) .+
    0.16 .* (1 .- burdens.adaptive_capacity) .+
    0.14 .* (1 .- burdens.political_voice) .+
    0.10 .* (1 .- burdens.benefit_capture)

resilience.ecological_resilience_score =
    0.18 .* resilience.diversity .+
    0.18 .* resilience.regeneration .+
    0.16 .* resilience.redundancy .+
    0.16 .* resilience.governance .+
    0.12 .* resilience.strategic_reserve .+
    0.10 .* (1 .- resilience.import_dependence) .+
    0.10 .* (1 .- resilience.shock_exposure)

CSV.write(joinpath(table_dir, "julia_stock_flow_results.csv"), stock)
CSV.write(joinpath(table_dir, "julia_resource_constraint_results.csv"), resources)
CSV.write(joinpath(table_dir, "julia_sector_pressure_results.csv"), sectors)
CSV.write(joinpath(table_dir, "julia_governance_results.csv"), governance)
CSV.write(joinpath(table_dir, "julia_justice_burden_results.csv"), burdens)
CSV.write(joinpath(table_dir, "julia_resilience_results.csv"), resilience)

println(stock[:, [:system, :natural_capital_next, :regeneration_gap, :threshold_distance]])
println(resources[:, [:resource, :resource_use_ratio, :waste_constraint_ratio]])
println(sectors[:, [:sector, :sector_pressure_score]])
println(governance[:, [:regime, :resource_governance_score]])
println(burdens[:, [:group, :justice_burden_score]])
println(resilience[:, [:system, :ecological_resilience_score]])
