# Post-Growth, Degrowth, and the Critique of Endless Expansion
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

growth = CSV.read(joinpath(processed_dir, "growth_dependence.csv"), DataFrame)
throughput = CSV.read(joinpath(processed_dir, "throughput_scenarios.csv"), DataFrame)
wellbeing = CSV.read(joinpath(processed_dir, "wellbeing_dashboard.csv"), DataFrame)
sufficiency = CSV.read(joinpath(processed_dir, "sufficiency.csv"), DataFrame)
transition = CSV.read(joinpath(processed_dir, "degrowth_transition.csv"), DataFrame)

growth.growth_dependence_score = [
    mean([
        row.employment_dependency,
        row.debt_service_dependency,
        row.fiscal_dependency,
        row.asset_dependency,
        row.pension_dependency,
        row.housing_market_dependency,
        row.political_legitimacy_dependency,
    ])
    for row in eachrow(growth)
]

throughput.throughput_index = throughput.population .* throughput.affluence .* throughput.intensity
throughput.wellbeing_per_throughput = throughput.wellbeing_index ./ throughput.throughput_index

wellbeing.wellbeing_score = [
    mean([
        row.health,
        row.time_balance,
        row.security,
        row.equality,
        row.public_goods,
        row.ecological_quality,
        row.care_support,
        row.social_trust,
    ])
    for row in eachrow(wellbeing)
]

sufficiency.sufficiency_ratio = sufficiency.needs_met ./ sufficiency.throughput_required
sufficiency.social_sufficiency_score =
    0.28 .* sufficiency.needs_met .+
    0.22 .* (1 .- sufficiency.throughput_required) .+
    0.16 .* sufficiency.time_security .+
    0.14 .* sufficiency.public_access .+
    0.10 .* sufficiency.care_capacity .+
    0.10 .* sufficiency.dignity

transition.degrowth_transition_score =
    0.18 .* transition.throughput_reduction .+
    0.20 .* transition.redistribution .+
    0.20 .* transition.public_services .+
    0.16 .* transition.democratic_legitimacy .+
    0.14 .* transition.macro_stabilization .+
    0.12 .* transition.employment_security

CSV.write(joinpath(table_dir, "julia_growth_dependence_results.csv"), growth)
CSV.write(joinpath(table_dir, "julia_throughput_results.csv"), throughput)
CSV.write(joinpath(table_dir, "julia_wellbeing_results.csv"), wellbeing)
CSV.write(joinpath(table_dir, "julia_sufficiency_results.csv"), sufficiency)
CSV.write(joinpath(table_dir, "julia_degrowth_transition_results.csv"), transition)

println(growth[:, [:scenario, :growth_dependence_score]])
println(throughput[:, [:scenario, :throughput_index, :wellbeing_per_throughput]])
println(wellbeing[:, [:scenario, :wellbeing_score]])
println(sufficiency[:, [:system, :sufficiency_ratio, :social_sufficiency_score]])
println(transition[:, [:scenario, :degrowth_transition_score]])
