# The Welfare State and Social Protection
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

household = CSV.read(joinpath(processed_dir, "household_tax_transfer.csv"), DataFrame)
spending = CSV.read(joinpath(processed_dir, "social_spending_scenarios.csv"), DataFrame)
coverage = CSV.read(joinpath(processed_dir, "program_coverage.csv"), DataFrame)
life = CSV.read(joinpath(processed_dir, "life_course_risk.csv"), DataFrame)
adaptive = CSV.read(joinpath(processed_dir, "adaptive_protection.csv"), DataFrame)

household.disposable_income = household.market_income .- household.taxes .+ household.transfers
household.service_adjusted_income = household.disposable_income .+ household.service_value
household.post_cost_security_income = household.service_adjusted_income .- household.housing_cost .- household.care_cost

spending.social_spending_ratio = spending.social_spending ./ spending.output
spending.protection_strength_score =
    0.24 .* spending.social_spending_ratio ./ maximum(spending.social_spending_ratio) .+
    0.18 .* spending.healthcare_spending ./ maximum(spending.healthcare_spending) .+
    0.18 .* spending.pensions ./ maximum(spending.pensions) .+
    0.14 .* spending.unemployment ./ maximum(spending.unemployment) .+
    0.14 .* spending.family_policy ./ maximum(spending.family_policy) .+
    0.12 .* spending.administration_quality

coverage.coverage_rate = coverage.covered_population ./ coverage.target_population
coverage.replacement_rate = coverage.benefit ./ coverage.previous_earnings
coverage.effective_protection_score =
    0.28 .* coverage.coverage_rate .+
    0.24 .* coverage.replacement_rate .+
    0.18 .* coverage.take_up_rate .+
    0.16 .* (1 .- coverage.administrative_burden) .+
    0.14 .* (1 .- coverage.stigma_cost)

life.vulnerability_reduction = life.baseline_vulnerability .- life.protected_vulnerability
life.life_course_protection_score =
    0.24 .* life.vulnerability_reduction .+
    0.20 .* life.coverage .+
    0.20 .* life.adequacy .+
    0.18 .* life.duration_support .+
    0.18 .* life.service_integration

adaptive.shock_vulnerability_reduction = adaptive.baseline_exposure .- adaptive.post_shock_vulnerability
adaptive.adaptive_capacity_score =
    0.18 .* adaptive.scale_up_capacity .+
    0.18 .* adaptive.payment_speed .+
    0.16 .* adaptive.registry_quality .+
    0.16 .* adaptive.local_delivery_capacity .+
    0.16 .* adaptive.benefit_adequacy .+
    0.16 .* (1 .- adaptive.post_shock_vulnerability)

CSV.write(joinpath(table_dir, "julia_household_tax_transfer_results.csv"), household)
CSV.write(joinpath(table_dir, "julia_social_spending_results.csv"), spending)
CSV.write(joinpath(table_dir, "julia_program_coverage_results.csv"), coverage)
CSV.write(joinpath(table_dir, "julia_life_course_risk_results.csv"), life)
CSV.write(joinpath(table_dir, "julia_adaptive_protection_results.csv"), adaptive)

println(household[:, [:household, :market_income, :disposable_income, :service_adjusted_income, :post_cost_security_income]])
println(spending[:, [:scenario, :social_spending_ratio, :protection_strength_score]])
println(coverage[:, [:program, :coverage_rate, :replacement_rate, :effective_protection_score]])
println(life[:, [:risk, :vulnerability_reduction, :life_course_protection_score]])
println(adaptive[:, [:shock, :shock_vulnerability_reduction, :adaptive_capacity_score]])
