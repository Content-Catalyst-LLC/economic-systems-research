# Growth, Development, and Structural Transformation
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

growth = CSV.read(joinpath(processed_dir, "growth_path_scenarios.csv"), DataFrame)
sectors = CSV.read(joinpath(processed_dir, "sector_transformation_scenarios.csv"), DataFrame)
capability = CSV.read(joinpath(processed_dir, "development_capability_scenarios.csv"), DataFrame)
energy = CSV.read(joinpath(processed_dir, "energy_ecology_scenarios.csv"), DataFrame)
debt = CSV.read(joinpath(processed_dir, "debt_fragility_scenarios.csv"), DataFrame)

sort!(growth, [:scenario, :period])
growth.growth_rate = zeros(nrow(growth))
for scenario in unique(growth.scenario)
    idx = findall(growth.scenario .== scenario)
    for j in 2:length(idx)
        growth.growth_rate[idx[j]] = growth.output[idx[j]] / growth.output[idx[j - 1]] - 1
    end
end
growth.labor_productivity = growth.output ./ growth.labor

sector_results = DataFrame()
for scenario in unique(sectors.scenario)
    group = sectors[sectors.scenario .== scenario, :]
    total_output = sum(group.sector_output)
    total_labor = sum(group.sector_labor)
    group.output_share = group.sector_output ./ total_output
    group.labor_share = group.sector_labor ./ total_labor
    group.sector_productivity = group.sector_output ./ group.sector_labor
    append!(sector_results, group)
end

capability.capability_index =
    0.22 .* capability.income_index .+
    0.20 .* capability.health_index .+
    0.20 .* capability.education_index .+
    0.22 .* capability.infrastructure_index .+
    0.16 .* capability.security_index

energy.energy_intensity = energy.energy_use ./ energy.output
energy.emissions_intensity = energy.emissions ./ energy.output
energy.sustainable_growth_score =
    0.30 .* (1 .- energy.energy_intensity ./ maximum(energy.energy_intensity)) .+
    0.30 .* (1 .- energy.emissions_intensity ./ maximum(energy.emissions_intensity)) .+
    0.25 .* energy.renewable_share .+
    0.15 .* (1 .- energy.resource_stress)

debt.middle_income_fragility_score =
    0.22 .* debt.external_debt_ratio .+
    0.20 .* debt.fx_debt_share .+
    0.16 .* debt.short_term_debt_share .+
    0.18 .* debt.export_concentration .+
    0.14 .* (1 .- debt.reserve_buffer) .+
    0.10 .* (1 .- debt.productivity_momentum)

CSV.write(joinpath(table_dir, "julia_development_results.csv"), growth)
CSV.write(joinpath(table_dir, "julia_sector_transformation_results.csv"), sector_results)
CSV.write(joinpath(table_dir, "julia_development_capability_results.csv"), capability)
CSV.write(joinpath(table_dir, "julia_energy_ecology_results.csv"), energy)
CSV.write(joinpath(table_dir, "julia_debt_fragility_results.csv"), debt)

println(growth[:, [:scenario, :period, :growth_rate, :labor_productivity]])
println(sector_results[:, [:scenario, :sector, :output_share, :labor_share, :sector_productivity]])
println(capability[:, [:scenario, :capability_index]])
println(debt[:, [:scenario, :middle_income_fragility_score]])
