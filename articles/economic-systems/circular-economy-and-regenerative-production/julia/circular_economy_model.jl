# Circular Economy and Regenerative Production
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

material = CSV.read(joinpath(processed_dir, "material_flow_scenarios.csv"), DataFrame)
design = CSV.read(joinpath(processed_dir, "product_life_design.csv"), DataFrame)
pathways = CSV.read(joinpath(processed_dir, "value_retention_pathways.csv"), DataFrame)
regeneration = CSV.read(joinpath(processed_dir, "regenerative_production.csv"), DataFrame)
rebound = CSV.read(joinpath(processed_dir, "rebound_scale_scenarios.csv"), DataFrame)
justice = CSV.read(joinpath(processed_dir, "circular_justice.csv"), DataFrame)

material.circularity_ratio = material.recovered_material ./ material.total_material_input
material.virgin_material_input = material.total_material_input .- material.recovered_material
material.waste_reduction_ratio = 1 .- (material.residual_waste ./ material.total_throughput)

design.product_life_extension = design.actual_product_life ./ design.baseline_product_life
design.design_for_circularity_score =
    0.18 .* design.durability .+
    0.18 .* design.repairability .+
    0.16 .* design.modularity .+
    0.16 .* design.disassembly_score .+
    0.14 .* design.material_separability .+
    0.10 .* (1 .- design.proprietary_lock_in) .+
    0.08 .* design.product_life_extension ./ maximum(design.product_life_extension)

pathways.value_retention_score =
    0.22 .* pathways.material_retention .+
    0.18 .* pathways.energy_retention .+
    0.18 .* pathways.labor_value_retention .+
    0.20 .* pathways.functional_retention .+
    0.10 .* (1 .- pathways.processing_intensity) .+
    0.12 .* (1 .- pathways.quality_loss)

regeneration.regenerative_balance = regeneration.ecological_restoration .- regeneration.ecological_degradation
regeneration.regenerative_production_score =
    0.16 .* regeneration.soil_health .+
    0.16 .* regeneration.water_retention .+
    0.16 .* regeneration.biodiversity .+
    0.16 .* regeneration.local_capability .+
    0.16 .* regeneration.stewardship_labor .+
    0.20 .* ((regeneration.regenerative_balance .- minimum(regeneration.regenerative_balance)) ./ (maximum(regeneration.regenerative_balance) - minimum(regeneration.regenerative_balance)))

rebound.net_efficiency_gain = rebound.efficiency_gain .- rebound.induced_additional_use

justice.circular_justice_score =
    0.18 .* justice.pollution_reduction .+
    0.18 .* justice.job_quality .+
    0.16 .* justice.local_value_capture .+
    0.16 .* justice.decision_voice .+
    0.16 .* (1 .- justice.hazard_exposure) .+
    0.16 .* justice.access_to_repair

CSV.write(joinpath(table_dir, "julia_material_flow_results.csv"), material)
CSV.write(joinpath(table_dir, "julia_product_life_design_results.csv"), design)
CSV.write(joinpath(table_dir, "julia_value_retention_results.csv"), pathways)
CSV.write(joinpath(table_dir, "julia_regenerative_production_results.csv"), regeneration)
CSV.write(joinpath(table_dir, "julia_rebound_results.csv"), rebound)
CSV.write(joinpath(table_dir, "julia_circular_justice_results.csv"), justice)

println(material[:, [:scenario, :circularity_ratio, :waste_reduction_ratio]])
println(design[:, [:product, :product_life_extension, :design_for_circularity_score]])
println(pathways[:, [:pathway, :value_retention_score]])
println(regeneration[:, [:scenario, :regenerative_balance, :regenerative_production_score]])
println(rebound[:, [:scenario, :net_efficiency_gain, :absolute_throughput_change]])
println(justice[:, [:group, :circular_justice_score]])
