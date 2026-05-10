# Money, Banking, Credit, and Financial Intermediation
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

money = CSV.read(joinpath(processed_dir, "money_aggregate_scenarios.csv"), DataFrame)
banks = CSV.read(joinpath(processed_dir, "bank_balance_sheet_scenarios.csv"), DataFrame)
liquidity = CSV.read(joinpath(processed_dir, "liquidity_stress_scenarios.csv"), DataFrame)
credit = CSV.read(joinpath(processed_dir, "credit_allocation_scenarios.csv"), DataFrame)
sustainable = CSV.read(joinpath(processed_dir, "sustainable_finance_scenarios.csv"), DataFrame)

money.money_supply = money.currency .+ money.deposits
money.broad_liquidity_proxy = money.money_supply .+ money.near_money_claims
money.deposit_share_of_money = money.deposits ./ money.money_supply

banks.leverage = banks.assets ./ banks.equity
banks.capital_ratio = banks.equity ./ banks.assets
banks.loan_to_deposit_ratio = banks.loans ./ banks.bank_deposits
banks.liquid_asset_ratio = banks.liquid_assets ./ banks.assets

liquidity.liquidity_coverage_ratio = liquidity.hqla ./ liquidity.net_cash_outflows
liquidity.liquidity_stress_flag = liquidity.liquidity_coverage_ratio .< 1.0

credit.developmental_credit_score =
    0.34 .* credit.productive_score .+
    0.28 .* credit.resilience_score .+
    0.22 .* credit.inclusion_score .+
    0.16 .* (1 .- credit.speculation_score)

credit.weighted_developmental_contribution = credit.flow_share .* credit.developmental_credit_score

sustainable.sustainable_finance_score =
    0.16 .* sustainable.financial_return_score .+
    0.27 .* sustainable.resilience_score .+
    0.27 .* sustainable.ecological_alignment_score .+
    0.20 .* sustainable.inclusion_score .+
    0.10 .* (1 .- sustainable.systemic_risk_score)

CSV.write(joinpath(table_dir, "julia_money_banking_results.csv"), banks)
CSV.write(joinpath(table_dir, "julia_money_aggregate_results.csv"), money)
CSV.write(joinpath(table_dir, "julia_liquidity_stress_results.csv"), liquidity)
CSV.write(joinpath(table_dir, "julia_credit_allocation_results.csv"), credit)
CSV.write(joinpath(table_dir, "julia_sustainable_finance_results.csv"), sustainable)

println(banks[:, [:bank, :leverage, :loan_to_deposit_ratio, :liquid_asset_ratio]])
println(liquidity[:, [:institution, :liquidity_coverage_ratio, :liquidity_stress_flag]])
println(sustainable[:, [:finance_use, :sustainable_finance_score]])
