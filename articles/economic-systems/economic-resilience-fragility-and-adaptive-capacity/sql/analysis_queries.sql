.headers on
.mode column

.print "Resilience"
SELECT
    scenario,
    ROUND(
      0.18 * buffers +
      0.18 * redundancy +
      0.18 * coordination +
      0.14 * trust +
      0.16 * learning +
      0.16 * recovery_capacity,
      3
    ) AS resilience_score
FROM resilience_scenarios
ORDER BY resilience_score DESC;

.print ""
.print "Fragility"
SELECT
    scenario,
    ROUND(
      0.20 * leverage +
      0.18 * concentration +
      0.20 * exposure +
      0.18 * underinvestment +
      0.14 * inequality +
      0.10 * political_fragmentation,
      3
    ) AS fragility_score
FROM fragility_scenarios
ORDER BY fragility_score DESC;

.print ""
.print "Adaptive capacity"
SELECT
    scenario,
    ROUND(
      0.18 * information +
      0.18 * fiscal_space +
      0.16 * skills +
      0.16 * flexibility +
      0.16 * legitimacy +
      0.16 * implementation_capacity,
      3
    ) AS adaptive_capacity_score
FROM adaptive_capacity
ORDER BY adaptive_capacity_score DESC;

.print ""
.print "Shock impact"
SELECT
    shock,
    shock_magnitude,
    ROUND(
      0.26 * household_vulnerability +
      0.22 * firm_vulnerability +
      0.18 * (1 - public_capacity) +
      0.18 * (1 - infrastructure_integrity) +
      0.16 * (1 - recovery_speed),
      3
    ) AS vulnerability,
    ROUND(
      shock_magnitude *
      (
        0.26 * household_vulnerability +
        0.22 * firm_vulnerability +
        0.18 * (1 - public_capacity) +
        0.18 * (1 - infrastructure_integrity) +
        0.16 * (1 - recovery_speed)
      ),
      3
    ) AS shock_impact
FROM shock_scenarios
ORDER BY shock_impact DESC;

.print ""
.print "Household resilience"
SELECT
    household_group,
    ROUND(
      0.22 * income_security +
      0.18 * savings +
      0.18 * care_access +
      0.18 * housing_stability +
      0.14 * social_protection +
      0.10 * mobility,
      3
    ) AS distributional_resilience_score
FROM household_resilience
ORDER BY distributional_resilience_score DESC;

.print ""
.print "Firm and supply chain resilience"
SELECT
    firm_type,
    ROUND(
      0.22 * (1 - supplier_concentration) +
      0.20 * inventory_buffer +
      0.16 * credit_access +
      0.16 * demand_diversification +
      0.12 * digital_continuity +
      0.14 * adaptation_capability,
      3
    ) AS supply_chain_resilience_score
FROM firm_supply_chain
ORDER BY supply_chain_resilience_score DESC;

.print ""
.print "Financial fragility"
SELECT
    system,
    ROUND(
      0.20 * leverage +
      0.20 * refinancing_risk +
      0.16 * asset_price_dependence +
      0.16 * (1 - liquidity_buffer) +
      0.12 * (1 - regulatory_capacity) +
      0.16 * contagion_channels,
      3
    ) AS financial_fragility_score
FROM financial_fragility
ORDER BY financial_fragility_score DESC;

.print ""
.print "Labor adaptive capacity"
SELECT
    region,
    ROUND(
      0.18 * skill_transferability +
      0.18 * training_capacity +
      0.18 * income_support +
      0.14 * mobility_support +
      0.18 * place_based_investment +
      0.14 * employer_diversity,
      3
    ) AS labor_adaptive_capacity_score
FROM labor_adaptation
ORDER BY labor_adaptive_capacity_score DESC;

.print ""
.print "Ecological and energy vulnerability"
SELECT
    system,
    ROUND(
      0.20 * energy_volatility +
      0.18 * water_stress +
      0.22 * climate_hazard +
      0.14 * material_dependency +
      0.14 * (1 - adaptation_investment) +
      0.12 * (1 - ecosystem_integrity),
      3
    ) AS ecological_energy_vulnerability_score
FROM ecological_energy_risk
ORDER BY ecological_energy_vulnerability_score DESC;

.print ""
.print "Recovery and learning"
SELECT
    scenario,
    ROUND(
      0.16 * response_speed +
      0.18 * public_capacity +
      0.16 * household_stability +
      0.16 * infrastructure_integrity +
      0.18 * institutional_learning +
      0.16 * transformational_adaptation,
      3
    ) AS recovery_learning_score
FROM recovery_learning
ORDER BY recovery_learning_score DESC;
