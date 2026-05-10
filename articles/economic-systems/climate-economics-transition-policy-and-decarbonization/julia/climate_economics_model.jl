# Climate Economics, Transition Policy, and Decarbonization
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

sectors = CSV.read(joinpath(processed_dir, "sector_emissions.csv"), DataFrame)
policies = CSV.read(joinpath(processed_dir, "policy_packages.csv"), DataFrame)
investment = CSV.read(joinpath(processed_dir, "transition_investment.csv"), DataFrame)
damage = CSV.read(joinpath(processed_dir, "damage_adaptation.csv"), DataFrame)
justice = CSV.read(joinpath(processed_dir, "just_transition.csv"), DataFrame)

sectors.emissions = sectors.output .* sectors.energy_intensity .* sectors.carbon_intensity
sectors.decarbonization_rate = (sectors.old_emissions_intensity .- sectors.new_emissions_intensity) ./ sectors.years

policies.policy_mix_score =
    0.18 .* policies.carbon_price_strength .+
    0.20 .* policies.regulatory_strength .+
    0.22 .* policies.public_investment .+
    0.18 .* policies.industrial_policy .+
    0.12 .* policies.social_protection .+
    0.10 .* policies.implementation_capacity

investment.transition_investment_score =
    0.22 .* investment.public_investment .+
    0.20 .* investment.private_capital .+
    0.22 .* investment.policy_credibility .+
    0.16 .* investment.cost_of_capital_support .+
    0.10 .* investment.permitting_capacity .+
    0.10 .* investment.grid_readiness

damage.damage_risk_score =
    0.18 .* damage.temperature_stress .+
    0.18 .* damage.flood_exposure .+
    0.12 .* damage.wildfire_smoke .+
    0.18 .* damage.economic_exposure .+
    0.18 .* damage.vulnerability .+
    0.10 .* (1 .- damage.adaptation_capacity) .+
    0.06 .* (1 .- damage.public_health_capacity)

justice.just_transition_score =
    0.16 .* (1 .- justice.worker_exposure) .+
    0.16 .* justice.retraining .+
    0.18 .* justice.regional_investment .+
    0.14 .* justice.income_support .+
    0.14 .* justice.public_services .+
    0.12 .* justice.new_industry_pipeline .+
    0.10 .* justice.labor_standards

CSV.write(joinpath(table_dir, "julia_sector_emissions_results.csv"), sectors)
CSV.write(joinpath(table_dir, "julia_policy_package_results.csv"), policies)
CSV.write(joinpath(table_dir, "julia_transition_investment_results.csv"), investment)
CSV.write(joinpath(table_dir, "julia_damage_adaptation_results.csv"), damage)
CSV.write(joinpath(table_dir, "julia_just_transition_results.csv"), justice)

println(sectors[:, [:sector, :emissions, :decarbonization_rate]])
println(policies[:, [:package, :policy_mix_score]])
println(investment[:, [:scenario, :transition_investment_score]])
println(damage[:, [:region, :damage_risk_score]])
println(justice[:, [:community, :just_transition_score]])
