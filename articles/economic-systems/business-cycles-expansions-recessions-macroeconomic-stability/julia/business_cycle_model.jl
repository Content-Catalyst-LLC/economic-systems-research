# Business Cycles Julia Workflow
#
# Purpose:
# Estimate a simple output-gap persistence model and simulate expansion/recession
# dynamics under different stabilization assumptions.

using CSV
using DataFrames
using GLM
using Statistics

base_dir = normpath(joinpath(@__DIR__, ".."))
panel_path = joinpath(base_dir, "data", "processed", "business_cycles_quarterly_panel.csv")
table_dir = joinpath(base_dir, "outputs", "tables")

if !isdir(table_dir)
    mkpath(table_dir)
end

if !isfile(panel_path)
    error("Panel file not found. Run `make python` first.")
end

df = CSV.read(panel_path, DataFrame)
sort!(df, :date)

df.output_gap_lag = [missing; df.output_gap_pct[1:end-1]]
model_df = dropmissing(df[:, [:output_gap_pct, :output_gap_lag, :recession_indicator, :federal_funds_rate]])

model = lm(@formula(output_gap_pct ~ output_gap_lag + recession_indicator + federal_funds_rate), model_df)

coef_df = DataFrame(
    term = coefnames(model),
    estimate = coef(model),
    stderr = stderror(model)
)

CSV.write(joinpath(table_dir, "julia_output_gap_persistence_model.csv"), coef_df)

function simulate_cycle(initial_gap::Float64; persistence::Float64, shock::Float64, stabilization::Float64, periods::Int = 24)
    gaps = Vector{Float64}(undef, periods)
    gaps[1] = initial_gap
    for t in 2:periods
        current_shock = t == 4 ? shock : 0.0
        gaps[t] = persistence * gaps[t-1] + current_shock + stabilization
    end
    return gaps
end

simulation = DataFrame(
    quarter = 1:24,
    weak_stabilization = simulate_cycle(1.0, persistence = 0.82, shock = -5.0, stabilization = 0.10, periods = 24),
    stronger_stabilization = simulate_cycle(1.0, persistence = 0.70, shock = -5.0, stabilization = 0.35, periods = 24)
)

CSV.write(joinpath(table_dir, "julia_cycle_simulation.csv"), simulation)

println(coef_df)
println(simulation)
