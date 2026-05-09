# Stabilization Policy Julia Workflow
#
# Purpose:
# Estimate a simple output-gap persistence model and simulate recovery under
# weak and strong stabilization responses.

using CSV
using DataFrames
using GLM
using Statistics

base_dir = normpath(joinpath(@__DIR__, ".."))
panel_path = joinpath(base_dir, "data", "processed", "stabilization_policy_quarterly_panel.csv")
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
model_df = dropmissing(df[:, [:output_gap_pct, :output_gap_lag, :recession_indicator, :federal_funds_rate, :gov_spending_growth_yoy_pct]])

model = lm(@formula(output_gap_pct ~ output_gap_lag + recession_indicator + federal_funds_rate + gov_spending_growth_yoy_pct), model_df)

coef_df = DataFrame(
    term = coefnames(model),
    estimate = coef(model),
    stderr = stderror(model)
)

CSV.write(joinpath(table_dir, "julia_output_gap_policy_model.csv"), coef_df)

function simulate_stabilization(initial_gap::Float64; persistence::Float64, shock::Float64, fiscal_response::Float64, monetary_response::Float64, periods::Int = 20)
    gaps = Vector{Float64}(undef, periods)
    gaps[1] = initial_gap
    for t in 2:periods
        crisis_shock = t == 3 ? shock : 0.0
        stabilization = fiscal_response + monetary_response
        gaps[t] = persistence * gaps[t-1] + crisis_shock + stabilization
    end
    return gaps
end

simulation = DataFrame(
    quarter = 1:20,
    weak_stabilization = simulate_stabilization(
        0.5,
        persistence = 0.84,
        shock = -5.0,
        fiscal_response = 0.10,
        monetary_response = 0.10,
        periods = 20
    ),
    stronger_stabilization = simulate_stabilization(
        0.5,
        persistence = 0.70,
        shock = -5.0,
        fiscal_response = 0.35,
        monetary_response = 0.25,
        periods = 20
    )
)

CSV.write(joinpath(table_dir, "julia_stabilization_simulation.csv"), simulation)

println(coef_df)
println(simulation)
