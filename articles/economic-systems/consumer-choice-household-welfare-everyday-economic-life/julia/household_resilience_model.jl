# Consumer Choice, Household Welfare, and Everyday Economic Life
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

households = CSV.read(joinpath(processed_dir, "household_profiles.csv"), DataFrame)

households.total_consumption = households.rent .+ households.food .+ households.transport .+ households.utilities .+ households.health .+ households.other
households.essentials_spending = households.rent .+ households.food .+ households.transport .+ households.utilities .+ households.health
households.saving = households.income .+ households.transfers .+ households.liquid_assets .- households.debt_service .- households.other_fixed_burdens .- households.total_consumption
households.essentials_ratio = households.essentials_spending ./ (households.income .+ households.transfers)
households.fragility_ratio = (households.essentials_spending .+ households.debt_service .+ households.other_fixed_burdens) ./ (households.income .+ households.transfers .+ households.liquid_assets)
households.rest_discretionary_hours = 24 .- households.paid_labor_hours .- households.care_hours .- households.commute_hours .- households.household_admin_hours

sim = DataFrame(
    household_group = String[],
    month = Int[],
    liquid_assets_remaining = Float64[],
    resilience_status = String[]
)

for row in eachrow(households)
    assets = Float64(row.liquid_assets)
    monthly_shock = 450.0

    for month in 0:24
        status = assets > 0 ? "buffer_remaining" : "buffer_depleted"
        push!(sim, (String(row.household_group), month, max(assets, 0.0), status))
        assets -= monthly_shock
    end
end

summary = DataFrame(
    weighted_essentials_ratio = [sum(households.essentials_ratio .* households.population_weight) / sum(households.population_weight)],
    weighted_fragility_ratio = [sum(households.fragility_ratio .* households.population_weight) / sum(households.population_weight)],
    weighted_rest_hours = [sum(households.rest_discretionary_hours .* households.population_weight) / sum(households.population_weight)]
)

CSV.write(joinpath(table_dir, "julia_household_resilience_results.csv"), households)
CSV.write(joinpath(table_dir, "julia_asset_depletion_paths.csv"), sim)
CSV.write(joinpath(table_dir, "julia_household_welfare_summary.csv"), summary)

println(summary)
