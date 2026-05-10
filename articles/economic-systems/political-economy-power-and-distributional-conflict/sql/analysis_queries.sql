.headers on
.mode column

.print "Income shares"
SELECT
    scenario,
    ROUND(wages + profits + rents, 2) AS total_income,
    ROUND(wages / (wages + profits + rents), 3) AS wage_share,
    ROUND(profits / (wages + profits + rents), 3) AS profit_share,
    ROUND(rents / (wages + profits + rents), 3) AS rent_share,
    ROUND(benefits_received + public_goods_value - taxes_paid, 2) AS net_fiscal_position
FROM income_distribution
ORDER BY wage_share DESC;

.print ""
.print "Power asymmetry"
SELECT
    "group",
    ROUND(
      0.20 * ownership_power +
      0.16 * organization_power +
      0.16 * access_power +
      0.14 * mobility_power +
      0.14 * voice_power +
      0.10 * media_influence +
      0.10 * legal_position,
      3
    ) AS power_asymmetry_score
FROM power_groups
ORDER BY power_asymmetry_score DESC;

.print ""
.print "Fiscal incidence"
SELECT
    "group",
    market_income,
    taxes_paid,
    cash_transfers,
    services_received,
    ROUND(market_income - taxes_paid + cash_transfers, 2) AS disposable_income,
    ROUND(market_income - taxes_paid + cash_transfers + services_received - debt_service - housing_cost, 2) AS post_burden_income
FROM fiscal_incidence
ORDER BY market_income;

.print ""
.print "Inflation and labor conflict"
SELECT
    scenario,
    ROUND(nominal_wage_growth - price_inflation, 3) AS real_wage_change,
    price_inflation,
    interest_rate_shock,
    unemployment_pressure,
    bargaining_strength
FROM inflation_labor_conflict
ORDER BY real_wage_change ASC;

.print ""
.print "Debt and rent pressure"
SELECT
    scenario,
    ROUND(debt_stock / income, 3) AS debt_to_income,
    ROUND((debt_stock * interest_rate) / income, 3) AS interest_burden,
    rent_burden,
    asset_owner_gain,
    debtor_relief_access
FROM debt_rent_conflict
ORDER BY interest_burden DESC;

.print ""
.print "Social compromise and globalization constraints"
SELECT
    scenario,
    ROUND(
      0.22 * welfare_buffer +
      0.18 * tax_progressivity +
      0.18 * labor_voice +
      0.14 * (1 - capital_mobility) +
      0.10 * (1 - austerity_pressure) +
      0.18 * public_trust,
      3
    ) AS social_compromise_score,
    ROUND(
      0.32 * capital_mobility +
      0.24 * trade_exposure +
      0.22 * austerity_pressure +
      0.12 * (1 - labor_voice) +
      0.10 * (1 - tax_progressivity),
      3
    ) AS globalization_constraint_score
FROM welfare_globalization_crisis
ORDER BY social_compromise_score DESC;

.print ""
.print "Conflict intensity and legitimacy"
SELECT
    scenario,
    ROUND(
      0.22 * inequality_pressure +
      0.18 * inflation_pressure +
      0.18 * unemployment_pressure +
      0.20 * representation_gap +
      0.22 * shock_exposure,
      3
    ) AS conflict_intensity_score,
    ROUND(
      0.26 * fairness +
      0.24 * security +
      0.24 * voice +
      0.26 * institutional_trust,
      3
    ) AS legitimacy_score
FROM legitimacy_conflict
ORDER BY legitimacy_score DESC;
