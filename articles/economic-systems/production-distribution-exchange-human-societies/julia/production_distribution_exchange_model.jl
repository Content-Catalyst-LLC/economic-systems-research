# Production, Distribution, and Exchange in Human Societies
# Julia Workflow

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

sectors = CSV.read(joinpath(processed_dir, "production_sectors.csv"), DataFrame)
demand = CSV.read(joinpath(processed_dir, "final_demand_exchange_scenarios.csv"), DataFrame)

I_mat = Matrix{Float64}(I, size(A, 1), size(A, 2))
L_inv = inv(I_mat - A)

records = DataFrame(
    scenario = String[],
    sector_code = String[],
    final_demand = Float64[],
    total_output = Float64[],
    labor_income = Float64[],
    non_labor_income = Float64[],
    ecological_throughput = Float64[],
    exchange_dependency = Float64[]
)

for row in eachrow(demand)
    f = [Float64(row[Symbol(sector)]) for sector in sector_codes]
    x = L_inv * f

    for i in eachindex(sector_codes)
        sector_row = sectors[sectors.sector_code .== sector_codes[i], :][1, :]
        push!(
            records,
            (
                String(row.scenario),
                sector_codes[i],
                f[i],
                x[i],
                x[i] * sector_row.labor_share,
                x[i] * sector_row.non_labor_share,
                x[i] * sector_row.ecological_intensity,
                x[i] * sector_row.trade_exposure
            )
        )
    end
end

summary = combine(groupby(records, :scenario),
    :total_output => sum => :total_output,
    :labor_income => sum => :labor_income,
    :non_labor_income => sum => :non_labor_income,
    :ecological_throughput => sum => :ecological_throughput,
    :exchange_dependency => sum => :exchange_dependency
)

summary.labor_share = summary.labor_income ./ summary.total_output
summary.non_labor_share = summary.non_labor_income ./ summary.total_output
summary.exchange_dependency_ratio = summary.exchange_dependency ./ summary.total_output

CSV.write(joinpath(table_dir, "julia_pde_input_output_results.csv"), records)
CSV.write(joinpath(table_dir, "julia_pde_scenario_summary.csv"), summary)

println(summary)
