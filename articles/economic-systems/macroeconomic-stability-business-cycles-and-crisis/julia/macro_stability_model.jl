# Macroeconomic Stability, Business Cycles, and Crisis
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

demand = CSV.read(joinpath(processed_dir, "aggregate_demand_scenarios.csv"), DataFrame)
households = CSV.read(joinpath(processed_dir, "household_balance_sheet_scenarios.csv"), DataFrame)
credit = CSV.read(joinpath(processed_dir, "credit_contraction_scenarios.csv"), DataFrame)
fiscal = CSV.read(joinpath(processed_dir, "fiscal_stabilization_scenarios.csv"), DataFrame)
open_economy = CSV.read(joinpath(processed_dir, "open_economy_shock_scenarios.csv"), DataFrame)
recovery = CSV.read(joinpath(processed_dir, "crisis_recovery_path_scenarios.csv"), DataFrame)

demand.output = demand.consumption .+ demand.investment .+ demand.government_spending .+ demand.net_exports
demand.output_gap = (demand.output .- demand.potential_output) ./ demand.potential_output

households.debt_burden_ratio = households.debt_service ./ households.income
households.savings_buffer_months = households.liquid_savings ./ (households.income ./ 12)
households.post_shock_income = households.income .* (1 .- households.job_loss_income_shock)
households.post_shock_debt_burden_ratio = households.debt_service ./ households.post_shock_income

credit.real_debt_burden = credit.nominal_debt ./ credit.price_level
credit.real_debt_burden_change = credit.real_debt_burden ./ credit.nominal_debt .- 1

fiscal.delta_y = fiscal.fiscal_multiplier .* fiscal.delta_g
fiscal.stabilized_gap = fiscal.initial_output_gap .+ (fiscal.delta_y ./ 1000) .+ (0.04 .* fiscal.automatic_stabilizer_strength)

open_economy.transmission_score = open_economy.shock_intensity .* (
    0.28 .* open_economy.export_exposure .+
    0.28 .* open_economy.import_price_exposure .+
    0.24 .* open_economy.capital_flow_exposure .+
    0.20 .* open_economy.fx_debt_exposure
)

recovery.output_shortfall = 100 .- recovery.output_index
recovery.employment_shortfall = 100 .- recovery.employment_index

CSV.write(joinpath(table_dir, "julia_macro_stability_results.csv"), demand)
CSV.write(joinpath(table_dir, "julia_household_balance_sheet_results.csv"), households)
CSV.write(joinpath(table_dir, "julia_credit_contraction_results.csv"), credit)
CSV.write(joinpath(table_dir, "julia_fiscal_stabilization_results.csv"), fiscal)
CSV.write(joinpath(table_dir, "julia_open_economy_shock_results.csv"), open_economy)
CSV.write(joinpath(table_dir, "julia_crisis_recovery_results.csv"), recovery)

println(demand[:, [:scenario, :output, :output_gap]])
println(households[:, [:household_group, :debt_burden_ratio, :post_shock_debt_burden_ratio]])
println(fiscal[:, [:scenario, :delta_y, :stabilized_gap]])
