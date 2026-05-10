.headers on
.mode column

.print "Material-flow circularity"
SELECT
    scenario,
    recovered_material,
    total_material_input,
    ROUND(recovered_material / total_material_input, 3) AS circularity_ratio,
    ROUND(total_material_input - recovered_material, 2) AS virgin_material_input,
    ROUND(1 - (residual_waste / total_throughput), 3) AS waste_reduction_ratio
FROM material_flow_scenarios
ORDER BY circularity_ratio DESC;

.print ""
.print "Product life and design for circularity"
SELECT
    product,
    actual_product_life,
    baseline_product_life,
    ROUND(actual_product_life / baseline_product_life, 3) AS product_life_extension,
    ROUND(
      0.18 * durability +
      0.18 * repairability +
      0.16 * modularity +
      0.16 * disassembly_score +
      0.14 * material_separability +
      0.10 * (1 - proprietary_lock_in),
      3
    ) AS design_for_circularity_score
FROM product_life_design
ORDER BY design_for_circularity_score DESC;

.print ""
.print "Value-retention hierarchy"
SELECT
    pathway,
    ROUND(
      0.22 * material_retention +
      0.18 * energy_retention +
      0.18 * labor_value_retention +
      0.20 * functional_retention +
      0.10 * (1 - processing_intensity) +
      0.12 * (1 - quality_loss),
      3
    ) AS value_retention_score
FROM value_retention_pathways
ORDER BY value_retention_score DESC;

.print ""
.print "Regenerative production"
SELECT
    scenario,
    ecological_restoration,
    ecological_degradation,
    ROUND(ecological_restoration - ecological_degradation, 2) AS regenerative_balance,
    soil_health,
    water_retention,
    biodiversity,
    local_capability
FROM regenerative_production
ORDER BY regenerative_balance DESC;

.print ""
.print "Circular infrastructure and policy"
SELECT
    policy_system,
    ROUND(
      0.12 * collection_systems +
      0.12 * sorting_capacity +
      0.16 * repair_hubs +
      0.14 * reverse_logistics +
      0.16 * product_standards +
      0.12 * public_procurement +
      0.10 * digital_product_passports +
      0.08 * right_to_repair,
      3
    ) AS circular_infrastructure_score
FROM infrastructure_policy
ORDER BY circular_infrastructure_score DESC;

.print ""
.print "Labor and business models"
SELECT
    model,
    ROUND(
      0.16 * repair_jobs +
      0.16 * remanufacturing_jobs +
      0.16 * maintenance_capacity +
      0.16 * worker_skill_depth +
      0.14 * producer_responsibility +
      0.12 * durability_incentive +
      0.10 * local_value_capture,
      3
    ) AS circular_labor_model_score
FROM labor_business_models
ORDER BY circular_labor_model_score DESC;

.print ""
.print "Rebound and scale discipline"
SELECT
    scenario,
    efficiency_gain,
    induced_additional_use,
    ROUND(efficiency_gain - induced_additional_use, 3) AS net_efficiency_gain,
    absolute_throughput_change,
    scale_discipline,
    circularity_ratio,
    wellbeing_gain
FROM rebound_scale_scenarios
ORDER BY absolute_throughput_change ASC;

.print ""
.print "Circular justice"
SELECT
    "group",
    ROUND(
      0.18 * pollution_reduction +
      0.18 * job_quality +
      0.16 * local_value_capture +
      0.16 * decision_voice +
      0.16 * (1 - hazard_exposure) +
      0.16 * access_to_repair,
      3
    ) AS circular_justice_score
FROM circular_justice
ORDER BY circular_justice_score DESC;
