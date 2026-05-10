# Poverty, Capability, and Economic Inclusion
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

household = CSV.read(joinpath(processed_dir, "household_poverty_scenarios.csv"), DataFrame)
capability = CSV.read(joinpath(processed_dir, "capability_scenarios.csv"), DataFrame)
inclusion = CSV.read(joinpath(processed_dir, "inclusion_scenarios.csv"), DataFrame)
work = CSV.read(joinpath(processed_dir, "work_informality_scenarios.csv"), DataFrame)
services = CSV.read(joinpath(processed_dir, "public_service_vulnerability_scenarios.csv"), DataFrame)

household.poverty_status = household.income .< household.poverty_line
household.poverty_gap = max.(household.poverty_line .- household.income, 0)
household.normalized_poverty_gap = household.poverty_gap ./ household.poverty_line
household.post_cost_income = household.income .- household.housing_cost .- household.debt_service .- household.health_cost
household.vulnerability_score =
    0.24 .* (1 .- household.savings ./ maximum(household.savings)) .+
    0.22 .* (household.debt_service ./ household.income) .+
    0.22 .* (household.housing_cost ./ household.income) .+
    0.14 .* (household.health_cost ./ household.income) .+
    0.18 .* household.shock_exposure

capability.capability_score =
    0.18 .* capability.income_score .+
    0.17 .* capability.health_score .+
    0.17 .* capability.education_score .+
    0.14 .* capability.mobility_score .+
    0.12 .* capability.safety_score .+
    0.10 .* capability.time_score .+
    0.12 .* capability.institutional_access
capability.conversion_condition_score =
    (capability.health_score .+ capability.education_score .+ capability.mobility_score .+
     capability.safety_score .+ capability.time_score .+ capability.institutional_access) ./ 6
capability.real_freedom_proxy = capability.income_score .* capability.conversion_condition_score

inclusion.inclusion_score =
    0.16 .* inclusion.work_access .+
    0.14 .* inclusion.finance_access .+
    0.18 .* inclusion.service_access .+
    0.16 .* inclusion.infrastructure_access .+
    0.12 .* inclusion.digital_access .+
    0.10 .* inclusion.legal_recognition .+
    0.14 .* inclusion.participation_security

work.work_inclusion_score =
    0.20 .* work.wage_adequacy .+
    0.16 .* work.hours_stability .+
    0.16 .* work.legal_protection .+
    0.16 .* work.benefit_access .+
    0.14 .* work.skill_progression .+
    0.10 .* work.workplace_safety .+
    0.08 .* work.recognition

services.public_service_score =
    0.18 .* services.healthcare_access .+
    0.16 .* services.education_quality .+
    0.14 .* services.childcare_support .+
    0.12 .* services.food_support .+
    0.14 .* services.unemployment_protection .+
    0.12 .* services.disability_support
services.raw_vulnerability_score =
    0.24 .* services.low_savings .+
    0.20 .* services.high_debt .+
    0.22 .* services.insecure_work .+
    0.16 .* (1 .- services.public_service_score) .+
    0.18 .* services.shock_exposure
services.service_adjusted_vulnerability = services.raw_vulnerability_score .* (1 .- 0.45 .* services.public_service_score)

CSV.write(joinpath(table_dir, "julia_household_poverty_results.csv"), household)
CSV.write(joinpath(table_dir, "julia_capability_results.csv"), capability)
CSV.write(joinpath(table_dir, "julia_inclusion_results.csv"), inclusion)
CSV.write(joinpath(table_dir, "julia_work_inclusion_results.csv"), work)
CSV.write(joinpath(table_dir, "julia_public_service_vulnerability_results.csv"), services)

println(household[:, [:household, :income, :poverty_status, :normalized_poverty_gap, :vulnerability_score]])
println(capability[:, [:scenario, :capability_score, :conversion_condition_score, :real_freedom_proxy]])
println(inclusion[:, [:scenario, :inclusion_score]])
println(work[:, [:sector, :work_inclusion_score]])
println(services[:, [:scenario, :public_service_score, :service_adjusted_vulnerability]])
