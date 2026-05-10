# Commons, Shared Resources, and Institutional Governance
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

resources = CSV.read(joinpath(processed_dir, "resource_scenarios.csv"), DataFrame)
users = CSV.read(joinpath(processed_dir, "user_extraction_profiles.csv"), DataFrame)
governance = CSV.read(joinpath(processed_dir, "governance_scenarios.csv"), DataFrame)

fishery = resources[resources.resource .== "fishery", :][1, :]

function regen(stock, r, K)
    return r * stock * (1 - stock / K)
end

paths = DataFrame(
    governance_scenario = String[],
    period = Int[],
    stock = Float64[],
    regeneration = Float64[],
    harvest = Float64[],
    depletion_risk_flag = Int[]
)

baseline_harvest = sum(users.baseline_extraction)
governed_harvest = sum(users.governed_extraction)

for gov in eachrow(governance)
    stock = Float64(fishery.initial_stock)

    for period in 0:40
        rgen = regen(stock, fishery.regeneration_rate, fishery.carrying_capacity)

        harvest = if String(gov.scenario) in ["open_access_weak_governance", "captured_governance"]
            baseline_harvest * gov.extraction_multiplier
        else
            governed_harvest * gov.extraction_multiplier
        end

        flag = stock < fishery.critical_stock_threshold ? 1 : 0

        push!(paths, (String(gov.scenario), period, stock, rgen, harvest, flag))

        stock = max(0.0, stock + rgen - harvest)
    end
end

summary = combine(groupby(paths, :governance_scenario),
    :stock => last => :final_stock,
    :stock => minimum => :minimum_stock,
    :harvest => mean => :average_harvest,
    :regeneration => mean => :average_regeneration,
    :depletion_risk_flag => sum => :periods_in_depletion_risk
)

governance.compliance_score =
    0.28 .* governance.monitoring_capacity .+
    0.22 .* governance.rule_clarity .+
    0.25 .* governance.legitimacy .+
    0.15 .* governance.sanction_capacity .+
    0.10 .* (1 .- governance.capture_risk)

governance.adaptive_governance_score =
    0.35 .* governance.local_knowledge_use .+
    0.35 .* governance.polycentric_coordination .+
    0.20 .* governance.legitimacy .+
    0.10 .* governance.monitoring_capacity

CSV.write(joinpath(table_dir, "julia_commons_results.csv"), summary)
CSV.write(joinpath(table_dir, "julia_commons_stock_paths.csv"), paths)
CSV.write(joinpath(table_dir, "julia_commons_governance_scores.csv"), governance)

println(summary)
println(governance[:, [:scenario, :compliance_score, :adaptive_governance_score]])
