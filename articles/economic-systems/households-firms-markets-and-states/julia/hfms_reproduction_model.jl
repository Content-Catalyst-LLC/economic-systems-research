# Households, Firms, Markets, and States
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

flows = CSV.read(joinpath(processed_dir, "institutional_flow_scenarios.csv"), DataFrame)

flows.household_saving = flows.household_wages .+ flows.household_transfers .+ flows.asset_income .-
    flows.taxes_paid .- flows.debt_service .- flows.household_consumption

flows.firm_profit = flows.firm_revenue .- flows.labor_cost .- flows.capital_cost .- flows.input_cost

flows.public_borrowing = flows.public_spending .+ flows.public_transfers .+ flows.public_debt_interest .- flows.tax_revenue

sim = DataFrame(
    scenario = String[],
    period = Int[],
    household_capacity = Float64[],
    productive_capacity = Float64[],
    institutional_capacity = Float64[],
    system_capacity = Float64[]
)

for row in eachrow(flows)
    household = 100.0
    productive = 100.0
    institutional = 100.0

    for period in 0:24
        system = mean([household, productive, institutional])
        push!(sim, (String(row.scenario), period, household, productive, institutional, system))

        household = household + 0.05 * row.household_saving - 0.03 * row.debt_service
        productive = productive + 0.04 * row.firm_profit + 0.01 * row.public_spending - 0.02 * row.input_cost
        institutional = institutional + 0.02 * row.tax_revenue - 0.015 * row.public_borrowing + 0.01 * row.public_spending
    end
end

CSV.write(joinpath(table_dir, "julia_reproduction_dynamics.csv"), sim)
CSV.write(joinpath(table_dir, "julia_institutional_flow_results.csv"), flows)

println(flows)
println(sim)
