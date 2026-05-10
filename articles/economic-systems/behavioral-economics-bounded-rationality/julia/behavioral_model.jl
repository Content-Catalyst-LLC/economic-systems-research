# Behavioral Economics and Bounded Rationality
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

choice = CSV.read(joinpath(processed_dir, "choice_options.csv"), DataFrame)
present = CSV.read(joinpath(processed_dir, "present_bias_scenarios.csv"), DataFrame)
framing = CSV.read(joinpath(processed_dir, "framing_default_scenarios.csv"), DataFrame)

logistic(z) = 1 / (1 + exp(-z))

choice.effective_utility = choice.utility .- 5.0 .* choice.complexity .+ 10.0 .* choice.salience

choice_summary = DataFrame(
    rule = ["global_utility_maximization", "cognitive_cost_adjusted", "satisficing"],
    chosen_option = [
        choice[argmax(choice.utility), :option_label],
        choice[argmax(choice.effective_utility), :option_label],
        sort(choice[choice.utility .>= choice.satisficing_threshold, :], :search_order)[1, :option_label]
    ]
)

present_summary = combine(groupby(present[present.period .> 0, :], [:scenario, :beta, :delta]),
    [:period, :future_value, :beta, :delta] => ((period, future_value, beta, delta) ->
        sum(beta[1] .* (delta[1] .^ period) .* future_value)
    ) => :present_biased_value,
    [:period, :future_value, :delta] => ((period, future_value, delta) ->
        sum((delta[1] .^ period) .* future_value)
    ) => :exponential_discount_value
)

framing.frame_effect = [f == "gain" ? 0.18 : f == "loss" ? 0.28 : 0.0 for f in framing.frame]
framing.take_up_probability = logistic.(
    -1.6 .+
    0.020 .* framing.benefit_value .-
    0.025 .* framing.admin_burden .+
    1.15 .* framing.default_status .+
    1.10 .* framing.trust_index .+
    0.85 .* framing.salience .+
    framing.frame_effect
)

CSV.write(joinpath(table_dir, "julia_behavioral_results.csv"), choice)
CSV.write(joinpath(table_dir, "julia_behavioral_choice_summary.csv"), choice_summary)
CSV.write(joinpath(table_dir, "julia_present_bias_results.csv"), present_summary)
CSV.write(joinpath(table_dir, "julia_default_take_up_results.csv"), framing)

println(choice_summary)
println(present_summary)
println(framing[:, [:scenario, :take_up_probability]])
