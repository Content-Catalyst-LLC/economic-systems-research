.headers on
.mode column

.print "Mixed economy structure"
SELECT
    scenario,
    market_allocation,
    public_planning,
    public_provision,
    regulation_rights,
    public_ownership_share,
    ROUND(
      0.20 * public_planning +
      0.20 * public_provision +
      0.16 * regulation_rights +
      0.16 * public_ownership_share +
      0.14 * social_rights_strength +
      0.14 * social_need_weight,
      3
    ) AS public_purpose_score
FROM mixed_economy_scenarios
ORDER BY public_purpose_score DESC;

.print ""
.print "Planning capacity"
SELECT
    scenario,
    ROUND(
      0.18 * state_capacity +
      0.16 * data_quality +
      0.16 * institutional_reach +
      0.16 * feedback_quality +
      0.16 * democratic_accountability +
      0.10 * coordination_authority +
      0.08 * implementation_speed,
      3
    ) AS planning_capacity_score
FROM planning_capacity
ORDER BY planning_capacity_score DESC;

.print ""
.print "Decommodification"
SELECT
    scenario,
    ROUND(
      0.18 * healthcare_access +
      0.16 * education_access +
      0.16 * housing_security +
      0.14 * childcare_support +
      0.12 * public_transport +
      0.12 * social_insurance +
      0.12 * guaranteed_access,
      3
    ) AS decommodification_score
FROM decommodification_scenarios
ORDER BY decommodification_score DESC;

.print ""
.print "Sectoral fit: market coordination versus public coordination"
SELECT
    sector,
    ROUND(
      0.18 * planning_fit +
      0.16 * public_ownership_fit +
      0.18 * regulation_need +
      0.16 * social_rights_need +
      0.16 * network_interdependence +
      0.16 * public_good_character,
      3
    ) AS public_coordination_need,
    ROUND(
      0.70 * market_fit +
      0.15 * (1 - network_interdependence) +
      0.15 * (1 - public_good_character),
      3
    ) AS market_coordination_usefulness
FROM sector_coordination
ORDER BY public_coordination_need DESC;

.print ""
.print "Public utilities"
SELECT
    utility,
    ROUND(
      0.18 * universal_access +
      0.18 * affordability +
      0.16 * maintenance_investment +
      0.14 * democratic_accountability +
      0.14 * service_reliability +
      0.10 * (1 - profit_extraction_pressure) +
      0.10 * regional_equity,
      3
    ) AS utility_public_purpose_score
FROM public_utilities
ORDER BY utility_public_purpose_score DESC;

.print ""
.print "Industrial policy"
SELECT
    scenario,
    ROUND(
      0.18 * public_investment +
      0.14 * sector_targeting +
      0.16 * learning_policy +
      0.14 * supplier_development +
      0.14 * public_procurement +
      0.12 * performance_discipline +
      0.12 * green_transition_alignment,
      3
    ) AS industrial_policy_score
FROM industrial_policy
ORDER BY industrial_policy_score DESC;

.print ""
.print "Crisis coordination and sustainable transition"
SELECT
    scenario,
    ROUND(
      0.20 * public_planning +
      0.18 * infrastructure_depth +
      0.18 * fiscal_capacity +
      0.16 * administrative_speed +
      0.14 * social_protection +
      0.14 * democratic_legitimacy,
      3
    ) AS crisis_coordination_score,
    ROUND(
      0.18 * public_planning +
      0.18 * infrastructure_depth +
      0.14 * fiscal_capacity +
      0.16 * social_protection +
      0.20 * ecological_targets +
      0.14 * democratic_legitimacy,
      3
    ) AS sustainable_transition_score
FROM crisis_transition_globalization
ORDER BY sustainable_transition_score DESC;
