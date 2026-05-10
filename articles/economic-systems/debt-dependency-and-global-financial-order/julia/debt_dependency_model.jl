# Debt, Dependency, and Global Financial Order
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

debt = CSV.read(joinpath(processed_dir, "debt_position_scenarios.csv"), DataFrame)
external = CSV.read(joinpath(processed_dir, "external_account_scenarios.csv"), DataFrame)
capital = CSV.read(joinpath(processed_dir, "capital_flow_scenarios.csv"), DataFrame)
restructuring = CSV.read(joinpath(processed_dir, "restructuring_scenarios.csv"), DataFrame)
sustainable = CSV.read(joinpath(processed_dir, "sustainable_finance_scenarios.csv"), DataFrame)

debt.debt_ratio = debt.debt_stock ./ debt.output
debt.external_debt_service_ratio = debt.external_debt_service ./ debt.export_earnings
debt.domestic_currency_fx_burden = debt.foreign_currency_debt .* debt.exchange_rate
debt.reserve_adequacy = debt.reserves ./ debt.short_term_external_obligations
debt.interest_growth_pressure = (debt.effective_interest_rate .- debt.growth_rate) .* debt.debt_stock .+ debt.primary_deficit

external.dependency_score =
    0.22 .* external.export_concentration .+
    0.20 .* external.import_dependence .+
    0.20 .* external.external_finance_reliance .+
    0.16 .* external.capital_flow_volatility .+
    0.12 .* (1 .- external.reserve_buffer) .+
    0.10 .* (1 .- external.domestic_capability)

capital.sudden_stop_risk_score =
    0.18 .* capital.portfolio_share .+
    0.14 .* (1 .- capital.fdi_share) .+
    0.20 .* capital.short_term_debt_share .+
    0.18 .* capital.capital_flow_reversal .+
    0.14 .* capital.reserve_loss .+
    0.16 .* capital.currency_depreciation

restructuring.post_restructuring_debt = restructuring.initial_debt .* (1 .- restructuring.restructuring_haircut)
restructuring.resolution_quality_score =
    0.22 .* restructuring.restructuring_haircut .+
    0.18 .* restructuring.maturity_extension .+
    0.18 .* restructuring.interest_relief .+
    0.18 .* restructuring.social_spending_floor .+
    0.16 .* restructuring.growth_recovery .+
    0.08 .* restructuring.creditor_acceptance

sustainable.sustainable_finance_score =
    0.22 .* sustainable.productive_investment .+
    0.18 .* sustainable.domestic_capability .+
    0.18 .* sustainable.export_resilience .+
    0.14 .* sustainable.social_protection .+
    0.14 .* sustainable.ecological_resilience .+
    0.14 .* sustainable.debt_manageability

CSV.write(joinpath(table_dir, "julia_debt_position_results.csv"), debt)
CSV.write(joinpath(table_dir, "julia_external_account_results.csv"), external)
CSV.write(joinpath(table_dir, "julia_capital_flow_results.csv"), capital)
CSV.write(joinpath(table_dir, "julia_restructuring_results.csv"), restructuring)
CSV.write(joinpath(table_dir, "julia_sustainable_finance_results.csv"), sustainable)

println(debt[:, [:scenario, :debt_ratio, :external_debt_service_ratio, :reserve_adequacy, :interest_growth_pressure]])
println(external[:, [:scenario, :dependency_score]])
println(capital[:, [:scenario, :sudden_stop_risk_score]])
println(restructuring[:, [:scenario, :post_restructuring_debt, :resolution_quality_score]])
println(sustainable[:, [:scenario, :sustainable_finance_score]])
