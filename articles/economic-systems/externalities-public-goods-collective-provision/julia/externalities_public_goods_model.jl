# Externalities, Public Goods, and Collective Provision
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

externalities = CSV.read(joinpath(processed_dir, "externality_scenarios.csv"), DataFrame)
public_goods = CSV.read(joinpath(processed_dir, "public_good_scenarios.csv"), DataFrame)
contributions = CSV.read(joinpath(processed_dir, "contribution_scenarios.csv"), DataFrame)

optimum = DataFrame(
    scenario = String[],
    private_output = Int[],
    social_output = Int[],
    private_minus_social_output = Int[],
    threshold_crossing_output = Union{Missing, Int}[]
)

for row in eachrow(externalities)
    outputs = collect(1:120)
    MPC = row.mpc_intercept .+ row.mpc_slope .* outputs
    MEC = row.mec_intercept .+ row.mec_slope .* outputs
    MSC = MPC .+ MEC
    MPB = row.mpb_intercept .+ row.mpb_slope .* outputs
    MEB = row.meb_intercept .+ row.meb_slope .* outputs
    MSB = MPB .+ MEB
    damage = cumsum(max.(MEC, 0.0)) ./ 10

    private_index = argmin(abs.(MPB .- MPC))
    social_index = argmin(abs.(MSB .- MSC))
    crossed = findfirst(damage .> row.critical_threshold)

    push!(
        optimum,
        (
            String(row.scenario),
            outputs[private_index],
            outputs[social_index],
            outputs[private_index] - outputs[social_index],
            isnothing(crossed) ? missing : outputs[crossed]
        )
    )
end

public_goods.social_benefit = public_goods.private_benefit .+ public_goods.external_benefit
public_goods.underprovision_gap = public_goods.social_need .- public_goods.voluntary_provision
public_goods.social_return_ratio = public_goods.social_benefit ./ public_goods.private_cost

contribution_summary = combine(groupby(contributions, :scenario),
    :contribution => sum => :total_contribution,
    :benefit_share => sum => :benefit_coverage
)

CSV.write(joinpath(table_dir, "julia_externality_public_good_results.csv"), optimum)
CSV.write(joinpath(table_dir, "julia_public_good_underprovision.csv"), public_goods)
CSV.write(joinpath(table_dir, "julia_contribution_summary.csv"), contribution_summary)

println(optimum)
println(public_goods)
println(contribution_summary)
