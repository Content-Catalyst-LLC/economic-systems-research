# What Is an Economic System? Julia Workflow
#
# Purpose:
# Solve the input-output system using linear algebra and simulate reproduction paths.

using CSV
using DataFrames
using LinearAlgebra

base_dir = normpath(joinpath(@__DIR__, ".."))
processed_dir = joinpath(base_dir, "data", "processed")
table_dir = joinpath(base_dir, "outputs", "tables")

if !isdir(table_dir)
    mkpath(table_dir)
end

A_df = CSV.read(joinpath(processed_dir, "input_output_matrix.csv"), DataFrame)
sector_codes = String.(A_df[:, 1])
A = Matrix(select(A_df, Not(names(A_df)[1])))

demand = CSV.read(joinpath(processed_dir, "final_demand_scenarios.csv"), DataFrame)

I_mat = Matrix{Float64}(I, size(A, 1), size(A, 2))
L_inv = inv(I_mat - A)

records = DataFrame(
    scenario = String[],
    sector_code = String[],
    final_demand = Float64[],
    total_output = Float64[],
    indirect_output_requirement = Float64[]
)

for row in eachrow(demand)
    f = [Float64(row[Symbol(sector)]) for sector in sector_codes]
    x = L_inv * f
    for i in eachindex(sector_codes)
        push!(records, (String(row.scenario), sector_codes[i], f[i], x[i], x[i] - f[i]))
    end
end

CSV.write(joinpath(table_dir, "julia_input_output_results.csv"), records)

reproduction = CSV.read(joinpath(processed_dir, "reproduction_parameters.csv"), DataFrame)
sim = DataFrame(
    scenario = String[],
    period = Int[],
    produced_capital = Float64[],
    natural_capital = Float64[]
)

for row in eachrow(reproduction)
    produced = Float64(row.initial_produced_capital)
    natural = Float64(row.initial_natural_capital)
    for period in 0:(Int(row.periods)-1)
        push!(sim, (String(row.scenario), period, produced, natural))
        produced = produced + row.investment - row.depreciation_rate * produced
        natural = natural + row.regeneration - row.depletion
    end
end

CSV.write(joinpath(table_dir, "julia_reproduction_results.csv"), sim)

println(records)
println(sim)
