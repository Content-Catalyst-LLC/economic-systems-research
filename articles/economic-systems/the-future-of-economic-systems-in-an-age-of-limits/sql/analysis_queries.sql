.headers on
.mode column

.print "Future viability"
SELECT
    scenario,
    ROUND(
      0.22 * (1 - ecological_pressure) +
      0.20 * institutional_capacity +
      0.18 * social_inclusion +
      0.16 * resilience +
      0.12 * public_trust +
      0.12 * adaptive_learning,
      3
    ) AS future_viability_score
FROM future_viability
ORDER BY future_viability_score DESC;

.print ""
.print "Throughput pressure"
SELECT
    scenario,
    population,
    affluence,
    material_intensity,
    ROUND(population * affluence * material_intensity, 2) AS throughput_pressure,
    wellbeing,
    inclusion
FROM throughput_pressure
ORDER BY throughput_pressure DESC;

.print ""
.print "Transition capacity"
SELECT
    scenario,
    ROUND(
      0.18 * public_investment +
      0.18 * policy_credibility +
      0.16 * technology +
      0.16 * social_trust +
      0.16 * implementation_capacity +
      0.16 * coordination,
      3
    ) AS transition_capacity_score
FROM transition_capacity
ORDER BY transition_capacity_score DESC;

.print ""
.print "Well-being beyond output"
SELECT
    scenario,
    ROUND(
      (health + security + inclusion + ecological_quality + public_goods + care + time_balance) / 7.0,
      3
    ) AS wellbeing_score
FROM wellbeing_measurement
ORDER BY wellbeing_score DESC;

.print ""
.print "Finance direction"
SELECT
    portfolio,
    ROUND(
      0.18 * (1 - fossil_exposure) +
      0.20 * resilience_investment +
      0.18 * restoration +
      0.18 * public_goods_alignment +
      0.12 * (1 - short_termism) +
      0.14 * adaptation_finance,
      3
    ) AS finance_direction_score
FROM finance_direction
ORDER BY finance_direction_score DESC;

.print ""
.print "Circularity, repair, and regeneration"
SELECT
    system,
    ROUND(
      0.18 * repairability +
      0.16 * reuse +
      0.16 * remanufacturing +
      0.16 * material_recovery +
      0.16 * maintenance_culture +
      0.18 * regeneration,
      3
    ) AS circular_repair_score
FROM circular_repair_systems
ORDER BY circular_repair_score DESC;

.print ""
.print "Technology governance"
SELECT
    scenario,
    ROUND(
      0.16 * productivity +
      0.18 * distribution +
      0.20 * public_purpose +
      0.16 * energy_demand_control +
      0.14 * labor_transition_support +
      0.16 * capability_expansion,
      3
    ) AS technology_governance_score
FROM technology_governance
ORDER BY technology_governance_score DESC;

.print ""
.print "Global asymmetry"
SELECT
    country_group,
    ROUND(
      0.30 * material_footprint +
      0.28 * historic_responsibility +
      0.16 * adaptive_capacity +
      0.18 * finance_obligation +
      0.08 * (1 - basic_needs_gap),
      3
    ) AS excess_reduction_obligation,
    ROUND(
      0.34 * development_need +
      0.28 * basic_needs_gap +
      0.14 * (1 - adaptive_capacity) +
      0.12 * (1 - historic_responsibility) +
      0.12 * (1 - material_footprint),
      3
    ) AS development_priority_score
FROM global_asymmetry
ORDER BY development_priority_score DESC;

.print ""
.print "Democratic legitimacy"
SELECT
    scenario,
    ROUND(
      0.18 * fairness +
      0.18 * affordability +
      0.16 * voice +
      0.16 * trust +
      0.18 * visible_benefit +
      0.14 * policy_stability,
      3
    ) AS democratic_legitimacy_score
FROM democratic_legitimacy
ORDER BY democratic_legitimacy_score DESC;
