# IS-LM Julia Workflow
#
# Purpose:
# Solve IS-LM systems using linear algebra and export scenario results.

using CSV
using DataFrames
using LinearAlgebra

base_dir = normpath(joinpath(@__DIR__, ".."))
scenario_path = joinpath(base_dir, "data", "processed", "is_lm_scenario_results.csv")
table_dir = joinpath(base_dir, "outputs", "tables")

if !isdir(table_dir)
    mkpath(table_dir)
end

if !isfile(scenario_path)
    error("Scenario file not found. Run `make python` first.")
end

scenarios = CSV.read(scenario_path, DataFrame)

function solve_linear_is_lm(alpha, beta, gamma, fiscal_shift, money_shift)
    # IS rearranged: Y + beta*r = alpha + fiscal_shift
    # LM rearranged: -gamma*Y + r = -money_shift
    A = [1.0 beta; -gamma 1.0]
    b = [alpha + fiscal_shift, -money_shift]
    solution = A \ b
    return solution[1], solution[2]
end

outputs = DataFrame(
    scenario = String[],
    output_linear_solve = Float64[],
    interest_linear_solve = Float64[],
    fiscal_multiplier = Float64[],
    monetary_multiplier = Float64[]
)

for row in eachrow(scenarios)
    y, r = solve_linear_is_lm(row.alpha, row.beta, row.gamma, row.fiscal_shift, row.money_shift)
    push!(
        outputs,
        (
            row.scenario,
            y,
            r,
            1 / (1 + row.beta * row.gamma),
            row.beta / (1 + row.beta * row.gamma)
        )
    )
end

CSV.write(joinpath(table_dir, "julia_is_lm_policy_results.csv"), outputs)

println(outputs)
