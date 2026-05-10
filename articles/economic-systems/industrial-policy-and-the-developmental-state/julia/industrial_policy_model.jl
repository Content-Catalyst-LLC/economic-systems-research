# Industrial Policy and the Developmental State
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

sectors = CSV.read(joinpath(processed_dir, "strategic_sector_scenarios.csv"), DataFrame)
support = CSV.read(joinpath(processed_dir, "support_conditionality_scenarios.csv"), DataFrame)
finance = CSV.read(joinpath(processed_dir, "development_finance_scenarios.csv"), DataFrame)
capture = CSV.read(joinpath(processed_dir, "capture_risk_scenarios.csv"), DataFrame)
green = CSV.read(joinpath(processed_dir, "green_industrial_policy_scenarios.csv"), DataFrame)

sectors.sector_output_share = sectors.sector_output ./ sectors.total_output
sectors.sector_productivity = sectors.sector_output ./ sectors.sector_labor
sectors.export_ratio = sectors.sector_exports ./ sectors.sector_output
sectors.strategic_priority_score =
    0.22 .* sectors.sector_output_share ./ maximum(sectors.sector_output_share) .+
    0.22 .* sectors.export_ratio .+
    0.22 .* sectors.technology_depth .+
    0.18 .* sectors.learning_potential .+
    0.16 .* sectors.domestic_linkage_potential

sector_output_map = Dict(row.sector => row.sector_output for row in eachrow(sectors))
support.sector_output = [sector_output_map[row.sector] for row in eachrow(support)]
support.support_intensity = support.public_support ./ support.sector_output
support.performance_score =
    0.22 .* support.productivity_gain ./ maximum(support.productivity_gain) .+
    0.18 .* support.export_growth ./ maximum(support.export_growth) .+
    0.18 .* support.employment_gain ./ maximum(support.employment_gain) .+
    0.18 .* support.local_supplier_share .+
    0.16 .* support.emissions_reduction ./ maximum(support.emissions_reduction) .+
    0.08 .* (1 .- support.support_duration_years ./ maximum(support.support_duration_years))

finance.development_finance_alignment_score =
    0.26 .* finance.patient_credit_share .+
    0.24 .* finance.industrial_credit_share .+
    0.20 .* (1 .- finance.speculative_credit_share) .+
    0.12 .* (1 .- finance.fx_debt_exposure) .+
    0.10 .* finance.development_bank_capacity .+
    0.08 .* finance.credit_monitoring_quality

capture.capture_risk_score =
    0.20 .* capture.market_concentration .+
    0.20 .* capture.lobbying_intensity .+
    0.20 .* (1 .- capture.evaluation_strength) .+
    0.16 .* capture.open_ended_support .+
    0.16 .* capture.performance_shortfall .+
    0.08 .* (1 .- capture.public_disclosure)

green.green_industrial_score =
    0.18 .* green.productivity_gain ./ maximum(green.productivity_gain) .+
    0.22 .* green.emissions_reduction ./ maximum(green.emissions_reduction) .+
    0.18 .* green.domestic_linkage .+
    0.16 .* green.employment_quality .+
    0.18 .* green.resilience_value .+
    0.08 .* (1 .- green.material_risk)

CSV.write(joinpath(table_dir, "julia_industrial_policy_results.csv"), sectors)
CSV.write(joinpath(table_dir, "julia_support_conditionality_results.csv"), support)
CSV.write(joinpath(table_dir, "julia_development_finance_results.csv"), finance)
CSV.write(joinpath(table_dir, "julia_capture_risk_results.csv"), capture)
CSV.write(joinpath(table_dir, "julia_green_industrial_policy_results.csv"), green)

println(sectors[:, [:sector, :sector_output_share, :sector_productivity, :export_ratio, :strategic_priority_score]])
println(support[:, [:sector, :support_intensity, :performance_score]])
println(finance[:, [:scenario, :development_finance_alignment_score]])
println(capture[:, [:program, :capture_risk_score]])
println(green[:, [:sector, :green_industrial_score]])
