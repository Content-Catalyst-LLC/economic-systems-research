# Economic Resilience Julia Model
# Purpose: Minimal dynamic demand-recovery starting point for future extension.

using CSV
using DataFrames
using Statistics

base_dir = normpath(joinpath(@__DIR__, ".."))
input_file = joinpath(base_dir, "outputs", "economic_resilience_indicators.csv")
output_file = joinpath(base_dir, "outputs", "julia_resilience_summary.csv")

if !isfile(input_file)
    error("Input file not found. Run the Python workflow first.")
end

df = CSV.read(input_file, DataFrame)

summary = combine(groupby(df, :recession_indicator),
    :unemployment_rate => mean => :avg_unemployment_rate,
    :real_gdp_growth_annualized => mean => :avg_real_gdp_growth_annualized,
    :federal_funds_rate => mean => :avg_federal_funds_rate
)

CSV.write(output_file, summary)

println(summary)
