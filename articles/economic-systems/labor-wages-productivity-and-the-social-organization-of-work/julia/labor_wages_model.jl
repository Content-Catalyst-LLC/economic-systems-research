# Labor, Wages, Productivity, and the Social Organization of Work
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

sectors = CSV.read(joinpath(processed_dir, "sector_labor_scenarios.csv"), DataFrame)
series = CSV.read(joinpath(processed_dir, "wage_productivity_time_series.csv"), DataFrame)
households = CSV.read(joinpath(processed_dir, "household_reproduction_scenarios.csv"), DataFrame)
bargaining = CSV.read(joinpath(processed_dir, "bargaining_institution_scenarios.csv"), DataFrame)
automation = CSV.read(joinpath(processed_dir, "automation_shock_scenarios.csv"), DataFrame)

sectors.labor_productivity = sectors.output ./ sectors.hours_worked
sectors.wage_share = sectors.total_wages ./ sectors.output
sectors.average_wage = sectors.total_wages ./ sectors.hours_worked
sectors.unit_labor_cost = sectors.average_wage ./ sectors.labor_productivity

series.productivity_wage_divergence = series.productivity_index .- series.wage_index
series.wage_productivity_ratio = series.wage_index ./ series.productivity_index

households.total_supporting_income = households.wage_income .+ households.social_support
households.total_reproduction_cost = households.household_cost .+ households.care_reproduction_cost
households.adequacy_gap = households.total_supporting_income .- households.total_reproduction_cost
households.adequacy_ratio = households.total_supporting_income ./ households.total_reproduction_cost

bargaining.modeled_wage =
    1.15 .+
    0.52 .* bargaining.labor_productivity .+
    1.15 .* bargaining.bargaining_power .+
    0.95 .* bargaining.institutional_support .+
    0.70 .* bargaining.outside_option

bargaining.labor_capture_index = bargaining.modeled_wage ./ bargaining.labor_productivity

automation.post_automation_output_index = 100 .* (1 .+ automation.productivity_gain)
automation.post_automation_employment_index = 100 .* (1 .+ automation.employment_effect)
automation.post_automation_wage_share_index = 100 .* (1 .+ automation.wage_share_effect)
automation.post_automation_quality_index = 100 .* (1 .+ automation.quality_effect)

automation.worker_welfare_index =
    0.35 .* automation.post_automation_wage_share_index .+
    0.35 .* automation.post_automation_employment_index .+
    0.30 .* automation.post_automation_quality_index

CSV.write(joinpath(table_dir, "julia_labor_results.csv"), sectors)
CSV.write(joinpath(table_dir, "julia_wage_productivity_divergence.csv"), series)
CSV.write(joinpath(table_dir, "julia_social_reproduction.csv"), households)
CSV.write(joinpath(table_dir, "julia_bargaining_wage_results.csv"), bargaining)
CSV.write(joinpath(table_dir, "julia_automation_shock_results.csv"), automation)

println(sectors[:, [:sector, :labor_productivity, :wage_share, :unit_labor_cost]])
println(households[:, [:household_type, :adequacy_gap, :adequacy_ratio]])
println(bargaining[:, [:scenario, :modeled_wage, :labor_capture_index]])
