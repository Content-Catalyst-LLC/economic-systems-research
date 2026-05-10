# The Future of Economic Systems in an Age of Limits
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

viability = CSV.read(joinpath(processed_dir, "future_viability.csv"), DataFrame)
throughput = CSV.read(joinpath(processed_dir, "throughput_pressure.csv"), DataFrame)
transition = CSV.read(joinpath(processed_dir, "transition_capacity.csv"), DataFrame)
wellbeing = CSV.read(joinpath(processed_dir, "wellbeing_measurement.csv"), DataFrame)
legitimacy = CSV.read(joinpath(processed_dir, "democratic_legitimacy.csv"), DataFrame)

viability.future_viability_score =
    0.22 .* (1 .- viability.ecological_pressure) .+
    0.20 .* viability.institutional_capacity .+
    0.18 .* viability.social_inclusion .+
    0.16 .* viability.resilience .+
    0.12 .* viability.public_trust .+
    0.12 .* viability.adaptive_learning

throughput.throughput_pressure = throughput.population .* throughput.affluence .* throughput.material_intensity
throughput.wellbeing_per_throughput = throughput.wellbeing ./ throughput.throughput_pressure

transition.transition_capacity_score =
    0.18 .* transition.public_investment .+
    0.18 .* transition.policy_credibility .+
    0.16 .* transition.technology .+
    0.16 .* transition.social_trust .+
    0.16 .* transition.implementation_capacity .+
    0.16 .* transition.coordination

wellbeing.wellbeing_score = [
    mean([
        row.health,
        row.security,
        row.inclusion,
        row.ecological_quality,
        row.public_goods,
        row.care,
        row.time_balance,
    ])
    for row in eachrow(wellbeing)
]

legitimacy.democratic_legitimacy_score =
    0.18 .* legitimacy.fairness .+
    0.18 .* legitimacy.affordability .+
    0.16 .* legitimacy.voice .+
    0.16 .* legitimacy.trust .+
    0.18 .* legitimacy.visible_benefit .+
    0.14 .* legitimacy.policy_stability

CSV.write(joinpath(table_dir, "julia_future_viability_results.csv"), viability)
CSV.write(joinpath(table_dir, "julia_throughput_pressure_results.csv"), throughput)
CSV.write(joinpath(table_dir, "julia_transition_capacity_results.csv"), transition)
CSV.write(joinpath(table_dir, "julia_wellbeing_results.csv"), wellbeing)
CSV.write(joinpath(table_dir, "julia_democratic_legitimacy_results.csv"), legitimacy)

println(viability[:, [:scenario, :future_viability_score]])
println(throughput[:, [:scenario, :throughput_pressure, :wellbeing_per_throughput]])
println(transition[:, [:scenario, :transition_capacity_score]])
println(wellbeing[:, [:scenario, :wellbeing_score]])
println(legitimacy[:, [:scenario, :democratic_legitimacy_score]])
