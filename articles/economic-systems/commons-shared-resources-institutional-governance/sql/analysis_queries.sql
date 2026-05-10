.headers on
.mode column

.print "Resource scenarios"
SELECT
    resource,
    initial_stock,
    carrying_capacity,
    regeneration_rate,
    critical_stock_threshold
FROM resource_scenarios
ORDER BY regeneration_rate DESC;

.print ""
.print "User extraction and access"
SELECT
    user_group,
    baseline_extraction,
    governed_extraction,
    baseline_extraction - governed_extraction AS extraction_reduction,
    access_rights_index,
    compliance_tendency
FROM user_extraction_profiles
ORDER BY baseline_extraction DESC;

.print ""
.print "Governance compliance indicators"
SELECT
    scenario,
    ROUND(
      0.28 * monitoring_capacity +
      0.22 * rule_clarity +
      0.25 * legitimacy +
      0.15 * sanction_capacity +
      0.10 * (1 - capture_risk),
      3
    ) AS compliance_score,
    ROUND(
      0.35 * local_knowledge_use +
      0.35 * polycentric_coordination +
      0.20 * legitimacy +
      0.10 * monitoring_capacity,
      3
    ) AS adaptive_governance_score,
    capture_risk
FROM governance_scenarios
ORDER BY compliance_score DESC;

.print ""
.print "Access, justice, and enclosure risk"
SELECT
    regime,
    ROUND(
      0.30 * preservation_score +
      0.25 * access_score +
      0.25 * justice_score +
      0.20 * maintenance_score,
      3
    ) AS commons_welfare_score,
    ROUND(
      0.25 * preservation_score +
      0.35 * (1 - access_score) +
      0.30 * (1 - justice_score) +
      0.10 * (1 - maintenance_score),
      3
    ) AS enclosure_risk_score
FROM access_justice_scenarios
ORDER BY commons_welfare_score DESC;
