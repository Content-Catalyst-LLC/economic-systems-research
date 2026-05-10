# Capital, Investment, and the Dynamics of Accumulation
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

capital = CSV.read(joinpath(processed_dir, "capital_stock_scenarios.csv"), DataFrame)
projects = CSV.read(joinpath(processed_dir, "investment_project_scenarios.csv"), DataFrame)
ownership = CSV.read(joinpath(processed_dir, "ownership_distribution_scenarios.csv"), DataFrame)
sustainable = CSV.read(joinpath(processed_dir, "sustainable_investment_scenarios.csv"), DataFrame)

paths = DataFrame(
    scenario = String[],
    period = Int[],
    capital_stock = Float64[],
    capital_intensity = Float64[],
    investment_rate = Float64[]
)

for row in eachrow(capital)
    K = Float64(row.initial_capital)

    for period in 0:15
        push!(paths, (
            String(row.scenario),
            period,
            K,
            K / row.labor,
            row.annual_investment / row.output
        ))

        K = K + row.annual_investment - row.depreciation_rate * K
    end
end

function npv(cashflows, r)
    periods = collect(0:(length(cashflows)-1))
    return sum(cashflows ./ ((1 + r) .^ periods))
end

project_results = DataFrame(project = String[], npv_private = Float64[], npv_public = Float64[], public_private_npv_gap = Float64[])

for row in eachrow(projects)
    cashflows = [
        row.cashflow_year_0,
        row.cashflow_year_1,
        row.cashflow_year_2,
        row.cashflow_year_3,
        row.cashflow_year_4,
        row.cashflow_year_5,
    ]

    private = npv(cashflows, row.private_discount_rate)
    public = npv(cashflows, row.public_discount_rate)

    push!(project_results, (String(row.project), private, public, public - private))
end

ownership.capital_income_share = ownership.profit_share .+ ownership.rent_share
ownership.public_capacity_share = ownership.tax_public_share .+ ownership.public_reinvestment_share
ownership.labor_to_capital_claim_ratio = ownership.wage_share ./ ownership.capital_income_share

sustainable.sustainable_investment_score =
    0.18 .* sustainable.financial_return_score .+
    0.26 .* sustainable.resilience_score .+
    0.24 .* sustainable.ecological_alignment_score .+
    0.22 .* sustainable.public_value_score .+
    0.10 .* sustainable.maintenance_score

CSV.write(joinpath(table_dir, "julia_capital_results.csv"), paths)
CSV.write(joinpath(table_dir, "julia_npv_project_results.csv"), project_results)
CSV.write(joinpath(table_dir, "julia_ownership_claims_results.csv"), ownership)
CSV.write(joinpath(table_dir, "julia_sustainable_investment_results.csv"), sustainable)

println(first(paths, 10))
println(project_results)
println(sustainable[:, [:project, :sustainable_investment_score]])
