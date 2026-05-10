# Capitalism and Its Varieties
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

regimes = CSV.read(joinpath(processed_dir, "regime_scenarios.csv"), DataFrame)
finance = CSV.read(joinpath(processed_dir, "financialization_scenarios.csv"), DataFrame)
labor = CSV.read(joinpath(processed_dir, "labor_skill_systems.csv"), DataFrame)
housing = CSV.read(joinpath(processed_dir, "housing_household_vulnerability.csv"), DataFrame)
crisis = CSV.read(joinpath(processed_dir, "crisis_sustainability.csv"), DataFrame)

regimes.profit = regimes.revenue .- regimes.cost
regimes.wage_share = regimes.wages ./ regimes.output
regimes.profit_share = regimes.profit ./ regimes.output
regimes.institutional_advantage_score =
    0.20 .* regimes.finance_patience .+
    0.20 .* regimes.labor_coordination .+
    0.18 .* regimes.welfare_buffer .+
    0.18 .* regimes.state_coordination .+
    0.12 .* regimes.innovation_radical .+
    0.12 .* regimes.innovation_incremental

finance.financialization_score =
    0.20 .* finance.asset_price_intensity .+
    0.18 .* finance.household_debt .+
    0.18 .* finance.corporate_leverage .+
    0.18 .* finance.shareholder_payout_pressure .+
    0.14 .* finance.buyback_intensity .+
    0.12 .* finance.speculative_pressure

labor.labor_coordination_score =
    0.18 .* labor.employment_protection .+
    0.20 .* labor.collective_bargaining .+
    0.16 .* labor.union_density .+
    0.14 .* labor.vocational_training .+
    0.14 .* labor.firm_specific_skills .+
    0.10 .* labor.wage_compression .+
    0.08 .* labor.general_skills

housing.housing_vulnerability_score =
    0.20 .* housing.rent_burden .+
    0.18 .* housing.mortgage_debt .+
    0.18 .* housing.asset_price_volatility .+
    0.14 .* (1 .- housing.tenant_protection) .+
    0.12 .* (1 .- housing.public_housing_capacity) .+
    0.10 .* (1 .- housing.household_resilience) .+
    0.08 .* housing.wealth_concentration_pressure

crisis.sustainable_capitalism_score =
    0.18 .* crisis.public_investment_capacity .+
    0.16 .* crisis.household_buffer .+
    0.14 .* crisis.financial_regulation .+
    0.18 .* crisis.industrial_adaptation .+
    0.18 .* crisis.ecological_constraint .+
    0.16 .* crisis.democratic_legitimacy

CSV.write(joinpath(table_dir, "julia_regime_results.csv"), regimes)
CSV.write(joinpath(table_dir, "julia_financialization_results.csv"), finance)
CSV.write(joinpath(table_dir, "julia_labor_results.csv"), labor)
CSV.write(joinpath(table_dir, "julia_housing_results.csv"), housing)
CSV.write(joinpath(table_dir, "julia_crisis_sustainability_results.csv"), crisis)

println(regimes[:, [:regime, :profit, :wage_share, :profit_share, :institutional_advantage_score]])
println(finance[:, [:scenario, :financialization_score]])
println(labor[:, [:system, :labor_coordination_score]])
println(housing[:, [:housing_regime, :housing_vulnerability_score]])
println(crisis[:, [:scenario, :sustainable_capitalism_score]])
