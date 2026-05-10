# Trade, Globalization, and Uneven Development
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

trade = CSV.read(joinpath(processed_dir, "trade_position_scenarios.csv"), DataFrame)
basket = CSV.read(joinpath(processed_dir, "export_basket_scenarios.csv"), DataFrame)
value_chain = CSV.read(joinpath(processed_dir, "value_chain_scenarios.csv"), DataFrame)
finance = CSV.read(joinpath(processed_dir, "finance_currency_scenarios.csv"), DataFrame)
regions = CSV.read(joinpath(processed_dir, "regional_inequality_scenarios.csv"), DataFrame)
resilience = CSV.read(joinpath(processed_dir, "strategic_resilience_scenarios.csv"), DataFrame)

trade.trade_openness = (trade.exports .+ trade.imports) ./ trade.output
trade.trade_balance = trade.exports .- trade.imports
trade.import_dependence_score =
    0.40 .* trade.strategic_import_dependence .+
    0.30 .* trade.intermediate_import_share .+
    0.30 .* trade.energy_import_share

export_results = DataFrame()
for scenario in unique(basket.scenario)
    group = basket[basket.scenario .== scenario, :]
    total_exports = sum(group.export_value)
    group.export_share = group.export_value ./ total_exports
    concentration = sum(group.export_share .^ 2)
    push!(export_results, (scenario=scenario, export_concentration_index=concentration, diversification_score=1 - concentration))
end

value_chain.domestic_value_capture = value_chain.domestic_value_added ./ value_chain.gross_exports
value_chain.command_position_score =
    0.24 .* value_chain.domestic_value_capture .+
    0.20 .* value_chain.lead_firm_control .+
    0.20 .* value_chain.technology_control .+
    0.16 .* value_chain.branding_control .+
    0.12 .* (1 .- value_chain.assembly_dependence) .+
    0.08 .* value_chain.upgrading_potential

finance.external_vulnerability_score =
    0.22 .* finance.foreign_currency_debt .+
    0.20 .* finance.capital_flow_volatility .+
    0.18 .* (1 .- finance.reserve_buffer) .+
    0.16 .* finance.current_account_pressure .+
    0.14 .* finance.external_financing_need .+
    0.10 .* (1 .- finance.policy_space)

regions.globalization_advantage_score =
    0.20 .* regions.export_linkage .+
    0.20 .* regions.productivity .+
    0.18 .* regions.infrastructure_depth .+
    0.16 .* regions.capital_access .+
    0.14 .* regions.market_access .+
    0.12 .* regions.institutional_capacity

resilience.sustainable_trade_resilience_score =
    0.20 .* resilience.supplier_diversification .+
    0.22 .* resilience.domestic_capability .+
    0.16 .* resilience.strategic_stock_buffer .+
    0.16 .* resilience.regional_redundancy .+
    0.12 .* resilience.import_substitution_capacity .+
    0.14 .* resilience.cooperative_trade_access

CSV.write(joinpath(table_dir, "julia_trade_position_results.csv"), trade)
CSV.write(joinpath(table_dir, "julia_export_concentration_results.csv"), export_results)
CSV.write(joinpath(table_dir, "julia_value_chain_results.csv"), value_chain)
CSV.write(joinpath(table_dir, "julia_finance_currency_results.csv"), finance)
CSV.write(joinpath(table_dir, "julia_regional_inequality_results.csv"), regions)
CSV.write(joinpath(table_dir, "julia_strategic_resilience_results.csv"), resilience)

println(trade[:, [:scenario, :trade_openness, :trade_balance, :import_dependence_score]])
println(export_results)
println(value_chain[:, [:scenario, :domestic_value_capture, :command_position_score]])
println(finance[:, [:scenario, :external_vulnerability_score]])
println(regions[:, [:region, :globalization_advantage_score]])
println(resilience[:, [:scenario, :sustainable_trade_resilience_score]])
