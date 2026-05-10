# Political Economy, Power, and Distributional Conflict
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

income = CSV.read(joinpath(processed_dir, "income_distribution.csv"), DataFrame)
power = CSV.read(joinpath(processed_dir, "power_groups.csv"), DataFrame)
fiscal = CSV.read(joinpath(processed_dir, "fiscal_incidence.csv"), DataFrame)
debt = CSV.read(joinpath(processed_dir, "debt_rent_conflict.csv"), DataFrame)
legitimacy = CSV.read(joinpath(processed_dir, "legitimacy_conflict.csv"), DataFrame)

income.total_income = income.wages .+ income.profits .+ income.rents
income.wage_share = income.wages ./ income.total_income
income.profit_share = income.profits ./ income.total_income
income.rent_share = income.rents ./ income.total_income
income.net_fiscal_position = income.benefits_received .+ income.public_goods_value .- income.taxes_paid

power.power_asymmetry_score =
    0.20 .* power.ownership_power .+
    0.16 .* power.organization_power .+
    0.16 .* power.access_power .+
    0.14 .* power.mobility_power .+
    0.14 .* power.voice_power .+
    0.10 .* power.media_influence .+
    0.10 .* power.legal_position

fiscal.disposable_income = fiscal.market_income .- fiscal.taxes_paid .+ fiscal.cash_transfers
fiscal.service_adjusted_income = fiscal.disposable_income .+ fiscal.services_received
fiscal.post_burden_income = fiscal.service_adjusted_income .- fiscal.debt_service .- fiscal.housing_cost

debt.debt_to_income = debt.debt_stock ./ debt.income
debt.interest_burden = debt.debt_stock .* debt.interest_rate ./ debt.income
debt.debt_rent_pressure_score =
    0.22 .* debt.debt_to_income ./ maximum(debt.debt_to_income) .+
    0.18 .* debt.interest_burden ./ maximum(debt.interest_burden) .+
    0.18 .* debt.rent_burden .+
    0.16 .* debt.asset_owner_gain .+
    0.14 .* (1 .- debt.debtor_relief_access) .+
    0.12 .* debt.legal_enforcement_strength

legitimacy.conflict_intensity_score =
    0.22 .* legitimacy.inequality_pressure .+
    0.18 .* legitimacy.inflation_pressure .+
    0.18 .* legitimacy.unemployment_pressure .+
    0.20 .* legitimacy.representation_gap .+
    0.22 .* legitimacy.shock_exposure

legitimacy.legitimacy_score =
    0.26 .* legitimacy.fairness .+
    0.24 .* legitimacy.security .+
    0.24 .* legitimacy.voice .+
    0.26 .* legitimacy.institutional_trust

CSV.write(joinpath(table_dir, "julia_income_distribution_results.csv"), income)
CSV.write(joinpath(table_dir, "julia_power_asymmetry_results.csv"), power)
CSV.write(joinpath(table_dir, "julia_fiscal_incidence_results.csv"), fiscal)
CSV.write(joinpath(table_dir, "julia_debt_rent_results.csv"), debt)
CSV.write(joinpath(table_dir, "julia_legitimacy_results.csv"), legitimacy)

println(income[:, [:scenario, :wage_share, :profit_share, :rent_share, :net_fiscal_position]])
println(power[:, [:group, :power_asymmetry_score]])
println(fiscal[:, [:group, :disposable_income, :post_burden_income]])
println(debt[:, [:scenario, :debt_to_income, :interest_burden, :debt_rent_pressure_score]])
println(legitimacy[:, [:scenario, :conflict_intensity_score, :legitimacy_score]])
