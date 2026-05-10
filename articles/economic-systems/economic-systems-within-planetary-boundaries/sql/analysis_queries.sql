.headers on
.mode column

.print "Boundary pressure ratios"
SELECT
    boundary,
    ROUND(economic_pressure / earth_system_capacity, 3) AS boundary_pressure_ratio,
    ROUND(MAX((economic_pressure / earth_system_capacity) - 1, 0), 3) AS overshoot_gap,
    irreversibility,
    system_connectivity,
    policy_response
FROM boundary_pressure
ORDER BY boundary_pressure_ratio DESC;

.print ""
.print "Resource-use identity"
SELECT
    scenario,
    population,
    affluence,
    resource_intensity,
    ROUND(population * affluence * resource_intensity, 2) AS resource_use,
    wellbeing_index,
    distribution_quality
FROM resource_use_identity
ORDER BY resource_use DESC;

.print ""
.print "Sector boundary pressure"
SELECT
    sector,
    ROUND(
      0.20 * climate +
      0.18 * biosphere +
      0.16 * land +
      0.14 * freshwater +
      0.14 * nutrients +
      0.10 * novel_entities +
      0.08 * social_necessity,
      3
    ) AS sector_pressure_score
FROM sector_pressure
ORDER BY sector_pressure_score DESC;

.print ""
.print "Coupled system pressure"
SELECT
    system,
    ROUND(
      0.25 * energy_pressure +
      0.25 * food_pressure +
      0.20 * land_pressure +
      0.18 * water_pressure +
      0.07 * (1 - governance_integration) +
      0.05 * (1 - adaptation_capacity),
      3
    ) AS coupled_pressure_score
FROM coupled_systems
ORDER BY coupled_pressure_score DESC;

.print ""
.print "Ecological space and justice"
SELECT
    "group",
    ROUND(
      0.28 * resource_claim +
      0.22 * historic_pressure +
      0.20 * harm_exposure +
      0.12 * (1 - adaptive_capacity) +
      0.10 * (1 - voice) +
      0.08 * development_need,
      3
    ) AS ecological_space_stress
FROM ecological_space_justice
ORDER BY ecological_space_stress DESC;

.print ""
.print "Transition capacity"
SELECT
    scenario,
    ROUND(
      0.20 * state_capacity +
      0.18 * public_investment +
      0.18 * social_legitimacy +
      0.16 * technological_capability +
      0.14 * coordination +
      0.14 * adaptive_governance,
      3
    ) AS transition_capacity_score
FROM transition_capacity
ORDER BY transition_capacity_score DESC;

.print ""
.print "Finance direction"
SELECT
    portfolio,
    ROUND(
      0.18 * (1 - fossil_exposure) +
      0.20 * restoration_investment +
      0.20 * resilience_investment +
      0.16 * circular_materials +
      0.16 * public_goods_alignment +
      0.10 * (1 - short_term_return_pressure),
      3
    ) AS finance_direction_score
FROM finance_direction
ORDER BY finance_direction_score DESC;

.print ""
.print "Boundary-aware progress"
SELECT
    scenario,
    gdp_growth,
    ROUND(
      0.30 * wellbeing +
      0.22 * inclusion +
      0.20 * natural_capital +
      0.12 * (1 - material_throughput) +
      0.12 * (1 - ecological_pressure),
      3
    ) AS boundary_aware_progress
FROM boundary_accounting
ORDER BY boundary_aware_progress DESC;
