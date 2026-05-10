# Information, Uncertainty, and Imperfect Markets
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

signals = CSV.read(joinpath(processed_dir, "signaling_scenarios.csv"), DataFrame)
search = CSV.read(joinpath(processed_dir, "information_search_scenarios.csv"), DataFrame)
uncertainty = CSV.read(joinpath(processed_dir, "uncertainty_scenarios.csv"), DataFrame)
consumers = CSV.read(joinpath(processed_dir, "consumer_complexity_scenarios.csv"), DataFrame)

signals.credibility_gap = signals.signal_cost_low_type .- signals.signal_cost_high_type
signals.credible_signal_score =
    0.45 .* signals.verification_strength .+
    0.35 .* (signals.credibility_gap ./ maximum(signals.credibility_gap)) .+
    0.20 .* signals.signal_strength

search.total_information_cost = search.cost_information .+ search.time_cost .+ search.processing_cost
search.net_information_value = search.benefit_information .- search.total_information_cost

scenario_cols = [:good_case, :moderate_case, :bad_case, :transition_case, :systemic_crisis_case]

expected_payoff = Float64[]
worst_case = Float64[]
payoff_range = Float64[]

for row in eachrow(uncertainty)
    vals = [row[col] for col in scenario_cols]
    push!(expected_payoff, mean(vals))
    push!(worst_case, minimum(vals))
    push!(payoff_range, maximum(vals) - minimum(vals))
end

uncertainty.expected_equal_weight_payoff = expected_payoff
uncertainty.worst_case = worst_case
uncertainty.payoff_range = payoff_range

consumers.effective_intelligibility =
    0.35 .* consumers.disclosure_quality .+
    0.25 .* consumers.trust_index .+
    0.20 .* (1 .- consumers.complexity_index) .+
    0.12 .* (1 .- consumers.hidden_fee_index) .+
    0.08 .* (1 .- consumers.switching_cost_index)

consumers.opacity_risk = 1 .- consumers.effective_intelligibility

CSV.write(joinpath(table_dir, "julia_information_uncertainty_results.csv"), uncertainty)
CSV.write(joinpath(table_dir, "julia_signal_credibility_results.csv"), signals)
CSV.write(joinpath(table_dir, "julia_information_search_results.csv"), search)
CSV.write(joinpath(table_dir, "julia_consumer_opacity_results.csv"), consumers)

println(uncertainty[:, [:action, :expected_equal_weight_payoff, :worst_case]])
println(signals[:, [:signal, :credible_signal_score]])
println(consumers[:, [:market, :opacity_risk]])
