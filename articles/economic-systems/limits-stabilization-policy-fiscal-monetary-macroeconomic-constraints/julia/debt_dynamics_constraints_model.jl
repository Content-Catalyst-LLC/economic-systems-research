# Limits of Stabilization Policy Julia Workflow
#
# Purpose:
# Estimate a simple constraint model and simulate debt dynamics under
# different interest-growth and primary-balance assumptions.

using CSV
using DataFrames
using GLM
using Statistics

base_dir = normpath(joinpath(@__DIR__, ".."))
panel_path = joinpath(base_dir, "data", "processed", "stabilization_constraints_quarterly_panel.csv")
table_dir = joinpath(base_dir, "outputs", "tables")

if !isdir(table_dir)
    mkpath(table_dir)
end

if !isfile(panel_path)
    error("Panel file not found. Run `make python` first.")
end

df = CSV.read(panel_path, DataFrame)
sort!(df, :date)

model_df = dropmissing(df[:, [:federal_funds_rate, :cpi_inflation_yoy_pct, :output_gap_pct, :recession_indicator, :lower_bound_constraint_flag, :inflation_constraint_flag]])

model = lm(@formula(federal_funds_rate ~ cpi_inflation_yoy_pct + output_gap_pct + recession_indicator + lower_bound_constraint_flag + inflation_constraint_flag), model_df)

coef_df = DataFrame(
    term = coefnames(model),
    estimate = coef(model),
    stderr = stderror(model)
)

CSV.write(joinpath(table_dir, "julia_monetary_constraint_model.csv"), coef_df)

function simulate_debt_path(initial_debt::Float64; interest_rate::Float64, growth_rate::Float64, primary_balance::Float64, periods::Int = 30)
    # Debt dynamics approximation:
    # d_t = ((1 + r) / (1 + g)) * d_{t-1} - primary_balance
    debt = Vector{Float64}(undef, periods)
    debt[1] = initial_debt
    r = interest_rate / 100.0
    g = growth_rate / 100.0
    for t in 2:periods
        debt[t] = ((1 + r) / (1 + g)) * debt[t-1] - primary_balance
    end
    return debt
end

simulation = DataFrame(
    year = 1:30,
    favorable_r_less_than_g = simulate_debt_path(100.0, interest_rate = 2.0, growth_rate = 4.0, primary_balance = -1.0, periods = 30),
    neutral_r_equals_g = simulate_debt_path(100.0, interest_rate = 3.0, growth_rate = 3.0, primary_balance = 0.0, periods = 30),
    adverse_r_greater_than_g = simulate_debt_path(100.0, interest_rate = 5.0, growth_rate = 2.0, primary_balance = 1.0, periods = 30)
)

CSV.write(joinpath(table_dir, "julia_debt_dynamics_simulation.csv"), simulation)

println(coef_df)
println(simulation)
