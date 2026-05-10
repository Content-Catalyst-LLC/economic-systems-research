# Beyond GDP: Measuring Well-Being, Inclusion, and Sustainability
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

dashboard = CSV.read(joinpath(processed_dir, "gdp_dashboard_scenarios.csv"), DataFrame)
inclusion = CSV.read(joinpath(processed_dir, "inclusion_scenarios.csv"), DataFrame)
stocks = CSV.read(joinpath(processed_dir, "sustainability_stocks.csv"), DataFrame)
adjusted = CSV.read(joinpath(processed_dir, "adjusted_progress.csv"), DataFrame)
capability = CSV.read(joinpath(processed_dir, "capability_conversion.csv"), DataFrame)

dashboard.gdp = dashboard.consumption .+ dashboard.investment .+ dashboard.government .+ dashboard.net_exports
dashboard.wellbeing_score = [
    mean([
        row.health,
        row.education,
        row.income_security,
        row.housing,
        row.safety,
        row.social_connection,
        row.environment,
        row.time_balance,
    ])
    for row in eachrow(dashboard)
]

inclusion.inclusion_score =
    0.22 .* inclusion.distribution .+
    0.18 .* inclusion.mobility .+
    0.20 .* inclusion.access .+
    0.18 .* inclusion.voice .+
    0.12 .* inclusion.regional_equity .+
    0.10 .* inclusion.service_reach

stocks.sustainability_score =
    0.26 .* stocks.natural_capital .+
    0.22 .* stocks.human_capital .+
    0.20 .* stocks.institutional_trust .+
    0.16 .* stocks.produced_capital .+
    0.08 .* (1 .- stocks.maintenance_gap) .+
    0.08 .* (1 .- stocks.ecological_pressure)

adjusted.adjusted_progress =
    adjusted.current_benefits .-
    adjusted.social_costs .-
    adjusted.ecological_costs .-
    adjusted.defensive_expenditure .+
    adjusted.unpaid_care_value .+
    adjusted.public_goods_value

adjusted.adjusted_progress_ratio = adjusted.adjusted_progress ./ adjusted.current_benefits

capability.capability_score =
    0.18 .* capability.resources .+
    0.20 .* capability.public_goods .+
    0.16 .* capability.health_conversion .+
    0.16 .* capability.education_conversion .+
    0.12 .* capability.transport_access .+
    0.12 .* capability.care_support .+
    0.06 .* (1 .- capability.discrimination_barrier)

CSV.write(joinpath(table_dir, "julia_gdp_dashboard_results.csv"), dashboard)
CSV.write(joinpath(table_dir, "julia_inclusion_results.csv"), inclusion)
CSV.write(joinpath(table_dir, "julia_sustainability_results.csv"), stocks)
CSV.write(joinpath(table_dir, "julia_adjusted_progress_results.csv"), adjusted)
CSV.write(joinpath(table_dir, "julia_capability_results.csv"), capability)

println(dashboard[:, [:scenario, :gdp, :wellbeing_score]])
println(inclusion[:, [:group, :inclusion_score]])
println(stocks[:, [:scenario, :sustainability_score]])
println(adjusted[:, [:scenario, :adjusted_progress, :adjusted_progress_ratio]])
println(capability[:, [:household_type, :capability_score]])
