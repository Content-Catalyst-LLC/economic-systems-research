# Socialism, Planning, and the Mixed Economy
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

mixed = CSV.read(joinpath(processed_dir, "mixed_economy_scenarios.csv"), DataFrame)
planning = CSV.read(joinpath(processed_dir, "planning_capacity.csv"), DataFrame)
decommodification = CSV.read(joinpath(processed_dir, "decommodification_scenarios.csv"), DataFrame)
sectors = CSV.read(joinpath(processed_dir, "sector_coordination.csv"), DataFrame)
crisis = CSV.read(joinpath(processed_dir, "crisis_transition_globalization.csv"), DataFrame)

mixed.public_purpose_score =
    0.20 .* mixed.public_planning .+
    0.20 .* mixed.public_provision .+
    0.16 .* mixed.regulation_rights .+
    0.16 .* mixed.public_ownership_share .+
    0.14 .* mixed.social_rights_strength .+
    0.14 .* mixed.social_need_weight

planning.planning_capacity_score =
    0.18 .* planning.state_capacity .+
    0.16 .* planning.data_quality .+
    0.16 .* planning.institutional_reach .+
    0.16 .* planning.feedback_quality .+
    0.16 .* planning.democratic_accountability .+
    0.10 .* planning.coordination_authority .+
    0.08 .* planning.implementation_speed

decommodification.decommodification_score =
    0.18 .* decommodification.healthcare_access .+
    0.16 .* decommodification.education_access .+
    0.16 .* decommodification.housing_security .+
    0.14 .* decommodification.childcare_support .+
    0.12 .* decommodification.public_transport .+
    0.12 .* decommodification.social_insurance .+
    0.12 .* decommodification.guaranteed_access

sectors.public_coordination_need =
    0.18 .* sectors.planning_fit .+
    0.16 .* sectors.public_ownership_fit .+
    0.18 .* sectors.regulation_need .+
    0.16 .* sectors.social_rights_need .+
    0.16 .* sectors.network_interdependence .+
    0.16 .* sectors.public_good_character

crisis.crisis_coordination_score =
    0.20 .* crisis.public_planning .+
    0.18 .* crisis.infrastructure_depth .+
    0.18 .* crisis.fiscal_capacity .+
    0.16 .* crisis.administrative_speed .+
    0.14 .* crisis.social_protection .+
    0.14 .* crisis.democratic_legitimacy

crisis.sustainable_transition_score =
    0.18 .* crisis.public_planning .+
    0.18 .* crisis.infrastructure_depth .+
    0.14 .* crisis.fiscal_capacity .+
    0.16 .* crisis.social_protection .+
    0.20 .* crisis.ecological_targets .+
    0.14 .* crisis.democratic_legitimacy

CSV.write(joinpath(table_dir, "julia_mixed_economy_results.csv"), mixed)
CSV.write(joinpath(table_dir, "julia_planning_capacity_results.csv"), planning)
CSV.write(joinpath(table_dir, "julia_decommodification_results.csv"), decommodification)
CSV.write(joinpath(table_dir, "julia_sector_coordination_results.csv"), sectors)
CSV.write(joinpath(table_dir, "julia_crisis_transition_results.csv"), crisis)

println(mixed[:, [:scenario, :public_purpose_score]])
println(planning[:, [:scenario, :planning_capacity_score]])
println(decommodification[:, [:scenario, :decommodification_score]])
println(sectors[:, [:sector, :public_coordination_need]])
println(crisis[:, [:scenario, :crisis_coordination_score, :sustainable_transition_score]])
