# Economic Resilience Julia Workflow
#
# Purpose:
# Estimate a simple dynamic output-gap model and simulate recovery paths.
# This is a lightweight modeling companion, not a full structural macro model.

using CSV
using DataFrames
using GLM
using Statistics

base_dir = normpath(joinpath(@__DIR__, ".."))
panel_path = joinpath(base_dir, "data", "processed", "economic_resilience_quarterly_panel.csv")
table_dir = joinpath(base_dir, "outputs", "tables")

if !isdir(table_dir)
    mkpath(table_dir)
end

if !isfile(panel_path)
    error("Panel file not found. Run `make python` first.")
end

df = CSV.read(panel_path, DataFrame)

# Prepare lagged output gap.
sort!(df, :date)
df.output_gap_lag = [missing; df.output_gap_pct[1:end-1]]

model_df = dropmissing(df[:, [:output_gap_pct, :output_gap_lag, :recession_indicator, :federal_funds_rate]])

# Simple dynamic model:
# output_gap_t = alpha + beta * output_gap_{t-1} + gamma * recession + delta * fed_funds + error
model = lm(@formula(output_gap_pct ~ output_gap_lag + recession_indicator + federal_funds_rate), model_df)

coef_table = coeftable(model)
coef_df = DataFrame(
    term = coefnames(model),
    estimate = coef(model),
    stderr = stderror(model)
)

CSV.write(joinpath(table_dir, "julia_dynamic_output_gap_model.csv"), coef_df)

# Simple illustrative recovery simulation.
# A negative output gap gradually closes depending on persistence and policy support.
function simulate_recovery(initial_gap::Float64; persistence::Float64 = 0.75, policy_support::Float64 = 0.35, periods::Int = 16)
    gaps = Vector{Float64}(undef, periods)
    gaps[1] = initial_gap
    for t in 2:periods
        gaps[t] = persistence * gaps[t-1] + policy_support
    end
    return gaps
end

simulation = DataFrame(
    quarter = 1:16,
    weak_support_gap = simulate_recovery(-6.0, persistence = 0.85, policy_support = 0.15, periods = 16),
    stronger_support_gap = simulate_recovery(-6.0, persistence = 0.70, policy_support = 0.45, periods = 16)
)

CSV.write(joinpath(table_dir, "julia_recovery_simulation.csv"), simulation)

println(coef_df)
println(simulation)
