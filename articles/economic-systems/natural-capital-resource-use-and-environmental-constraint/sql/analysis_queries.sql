.headers on
.mode column

.print "Natural capital stock-flow results"
SELECT
    system,
    natural_capital_t,
    regeneration,
    degradation,
    ROUND(natural_capital_t + regeneration - degradation, 2) AS natural_capital_next,
    ROUND(degradation - regeneration, 2) AS regeneration_gap,
    ROUND((natural_capital_t + regeneration - degradation) - threshold, 2) AS threshold_distance
FROM stock_flow_scenarios
ORDER BY threshold_distance ASC;

.print ""
.print "Resource-use and waste constraints"
SELECT
    resource,
    resource_use,
    regenerative_capacity,
    CASE
      WHEN regenerative_capacity > 0 THEN ROUND(resource_use / regenerative_capacity, 3)
      ELSE NULL
    END AS resource_use_ratio,
    ROUND(emissions / absorptive_capacity, 3) AS waste_constraint_ratio,
    social_necessity,
    substitutability
FROM resource_use_constraints
ORDER BY waste_constraint_ratio DESC;

.print ""
.print "Sector resource pressure"
SELECT
    sector,
    ROUND(
      0.18 * material_intensity +
      0.18 * energy_intensity +
      0.16 * water_intensity +
      0.14 * land_intensity +
      0.14 * waste_intensity +
      0.12 * import_dependence +
      0.08 * social_necessity,
      3
    ) AS sector_pressure_score
FROM sector_resource_pressure
ORDER BY sector_pressure_score DESC;

.print ""
.print "Ecosystem function scores"
SELECT
    ecosystem,
    ROUND(
      0.18 * water_filtration +
      0.18 * flood_buffering +
      0.18 * carbon_storage +
      0.16 * habitat_support +
      0.14 * soil_protection +
      0.10 * pollination_support +
      0.06 * (1 - market_visibility),
      3
    ) AS ecosystem_function_score
FROM ecosystem_functions
ORDER BY ecosystem_function_score DESC;

.print ""
.print "Resource governance regimes"
SELECT
    regime,
    ROUND(
      0.14 * secure_tenure +
      0.16 * monitoring +
      0.16 * participation +
      0.14 * enforcement +
      0.16 * adaptive_rules +
      0.12 * equity +
      0.12 * regeneration_alignment,
      3
    ) AS resource_governance_score
FROM governance_regimes
ORDER BY resource_governance_score DESC;

.print ""
.print "Resource justice burdens"
SELECT
    "group",
    ROUND(
      0.24 * exposure +
      0.18 * (1 - income_buffer) +
      0.18 * (1 - public_infrastructure) +
      0.16 * (1 - adaptive_capacity) +
      0.14 * (1 - political_voice) +
      0.10 * (1 - benefit_capture),
      3
    ) AS justice_burden_score
FROM justice_burdens
ORDER BY justice_burden_score DESC;

.print ""
.print "Resilience and strategic dependence"
SELECT
    system,
    ROUND(
      0.18 * diversity +
      0.18 * regeneration +
      0.16 * redundancy +
      0.16 * governance +
      0.12 * strategic_reserve +
      0.10 * (1 - import_dependence) +
      0.10 * (1 - shock_exposure),
      3
    ) AS ecological_resilience_score,
    ROUND(
      0.30 * import_dependence +
      0.24 * shock_exposure +
      0.16 * (1 - diversity) +
      0.16 * (1 - redundancy) +
      0.14 * (1 - strategic_reserve),
      3
    ) AS strategic_dependency_score
FROM resilience_dependency
ORDER BY strategic_dependency_score DESC;

.print ""
.print "Substitution, efficiency, and rebound"
SELECT
    scenario,
    efficiency_gain,
    rebound_effect,
    substitution_feasibility,
    ecological_irreplaceability,
    absolute_reduction,
    innovation_quality
FROM substitution_efficiency
ORDER BY absolute_reduction DESC;
