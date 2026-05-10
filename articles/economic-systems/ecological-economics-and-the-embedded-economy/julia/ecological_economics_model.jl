# Ecological Economics and the Embedded Economy
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

throughput = CSV.read(joinpath(processed_dir, "throughput_scenarios.csv"), DataFrame)
sectors = CSV.read(joinpath(processed_dir, "sector_footprints.csv"), DataFrame)
burdens = CSV.read(joinpath(processed_dir, "ecological_burdens.csv"), DataFrame)
embedded = CSV.read(joinpath(processed_dir, "embeddedness_scenarios.csv"), DataFrame)
resilience = CSV.read(joinpath(processed_dir, "resilience_commons.csv"), DataFrame)

throughput.throughput = throughput.energy_input .+ throughput.material_input
throughput.waste_residual = throughput.throughput .- throughput.recovered_throughput
throughput.recovery_rate = throughput.recovered_throughput ./ throughput.throughput
throughput.scale_ratio = throughput.economic_scale ./ throughput.ecological_capacity

sectors.material_footprint = sectors.domestic_extraction .+ sectors.imports .- sectors.exports
sectors.ecological_pressure_score =
    0.20 .* sectors.material_footprint ./ maximum(sectors.material_footprint) .+
    0.18 .* sectors.energy_intensity .+
    0.18 .* sectors.water_pressure .+
    0.18 .* sectors.land_pressure .+
    0.16 .* sectors.waste_intensity .+
    0.10 .* sectors.social_necessity

burdens.ecological_burden_score =
    0.24 .* burdens.exposure .+
    0.18 .* (1 .- burdens.income_buffer) .+
    0.18 .* (1 .- burdens.infrastructure) .+
    0.18 .* (1 .- burdens.adaptive_capacity) .+
    0.10 .* (1 .- burdens.political_voice) .+
    0.12 .* (1 .- burdens.historical_responsibility)

embedded.embeddedness_score =
    0.18 .* embedded.ecology_integrity .+
    0.18 .* embedded.care_capacity .+
    0.16 .* embedded.public_institutions .+
    0.14 .* embedded.infrastructure_maintenance .+
    0.14 .* embedded.cultural_reciprocity .+
    0.10 .* (1 .- embedded.market_dependence) .+
    0.10 .* embedded.community_resilience

resilience.resilience_score =
    0.16 .* resilience.diversity .+
    0.14 .* resilience.redundancy .+
    0.16 .* resilience.regeneration .+
    0.16 .* resilience.governance .+
    0.12 .* resilience.maintenance .+
    0.12 .* resilience.learning .+
    0.08 .* resilience.monitoring .+
    0.06 .* resilience.participation

CSV.write(joinpath(table_dir, "julia_throughput_results.csv"), throughput)
CSV.write(joinpath(table_dir, "julia_sector_results.csv"), sectors)
CSV.write(joinpath(table_dir, "julia_burden_results.csv"), burdens)
CSV.write(joinpath(table_dir, "julia_embeddedness_results.csv"), embedded)
CSV.write(joinpath(table_dir, "julia_resilience_results.csv"), resilience)

println(throughput[:, [:scenario, :throughput, :waste_residual, :scale_ratio, :wellbeing_index]])
println(sectors[:, [:sector, :material_footprint, :ecological_pressure_score]])
println(burdens[:, [:group, :ecological_burden_score]])
println(embedded[:, [:scenario, :embeddedness_score]])
println(resilience[:, [:system, :resilience_score]])
