.headers on
.mode column

.print "Regime distribution and institutional advantage"
SELECT
    regime,
    ROUND(revenue - cost, 2) AS profit,
    ROUND(wages / output, 3) AS wage_share,
    ROUND((revenue - cost) / output, 3) AS profit_share,
    ROUND(
      0.20 * finance_patience +
      0.20 * labor_coordination +
      0.18 * welfare_buffer +
      0.18 * state_coordination +
      0.12 * innovation_radical +
      0.12 * innovation_incremental,
      3
    ) AS institutional_advantage_score
FROM regime_scenarios
ORDER BY institutional_advantage_score DESC;

.print ""
.print "Financialization"
SELECT
    scenario,
    ROUND(
      0.20 * asset_price_intensity +
      0.18 * household_debt +
      0.18 * corporate_leverage +
      0.18 * shareholder_payout_pressure +
      0.14 * buyback_intensity +
      0.12 * speculative_pressure,
      3
    ) AS financialization_score,
    ROUND(
      0.44 * productive_investment +
      0.20 * (1 - speculative_pressure) +
      0.18 * (1 - shareholder_payout_pressure) +
      0.18 * (1 - asset_price_intensity),
      3
    ) AS productive_finance_score
FROM financialization_scenarios
ORDER BY financialization_score DESC;

.print ""
.print "Labor coordination and skill formation"
SELECT
    system,
    ROUND(
      0.18 * employment_protection +
      0.20 * collective_bargaining +
      0.16 * union_density +
      0.14 * vocational_training +
      0.14 * firm_specific_skills +
      0.10 * wage_compression +
      0.08 * general_skills,
      3
    ) AS labor_coordination_score
FROM labor_skill_systems
ORDER BY labor_coordination_score DESC;

.print ""
.print "Housing and household vulnerability"
SELECT
    housing_regime,
    ROUND(
      0.20 * rent_burden +
      0.18 * mortgage_debt +
      0.18 * asset_price_volatility +
      0.14 * (1 - tenant_protection) +
      0.12 * (1 - public_housing_capacity) +
      0.10 * (1 - household_resilience) +
      0.08 * wealth_concentration_pressure,
      3
    ) AS housing_vulnerability_score
FROM housing_household_vulnerability
ORDER BY housing_vulnerability_score DESC;

.print ""
.print "Globalized hybrid capitalism"
SELECT
    scenario,
    ROUND(
      0.18 * value_chain_dependence +
      0.18 * (1 - domestic_supplier_depth) +
      0.18 * foreign_currency_exposure +
      0.16 * (1 - technology_sovereignty) +
      0.12 * (1 - labor_standards) +
      0.08 * (1 - industrial_policy_capacity) +
      0.10 * external_vulnerability,
      3
    ) AS dependent_hybridization_score
FROM globalization_hybrids
ORDER BY dependent_hybridization_score DESC;

.print ""
.print "Crisis response and sustainability"
SELECT
    scenario,
    ROUND(
      0.18 * automatic_stabilizers +
      0.16 * public_investment_capacity +
      0.18 * household_buffer +
      0.14 * financial_regulation +
      0.14 * industrial_adaptation +
      0.10 * ecological_constraint +
      0.10 * democratic_legitimacy,
      3
    ) AS crisis_response_score,
    ROUND(
      0.18 * public_investment_capacity +
      0.16 * household_buffer +
      0.14 * financial_regulation +
      0.18 * industrial_adaptation +
      0.18 * ecological_constraint +
      0.16 * democratic_legitimacy,
      3
    ) AS sustainable_capitalism_score
FROM crisis_sustainability
ORDER BY sustainable_capitalism_score DESC;
